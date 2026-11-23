#!/usr/bin/env python3
"""Create Hugo leaf bundles for new posts on trustial.substack.com.

Reads the public Substack feed and, for each post that is not already
referenced by ``external_url`` or ``canonical`` under the blog content
directory, creates ``content/english/blog/<slug>/index.md`` using the same
frontmatter shape as ``content/english/blog/gpt-opus-wearable-pcb/``.

The script is idempotent. It never modifies or deletes an existing file.
``--dry-run`` prints the plan and does not download images or write files.
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from zoneinfo import ZoneInfo

DEFAULT_FEED = "https://trustial.substack.com/feed"
POST_HOST = "trustial.substack.com"
USER_AGENT = "trustial-substack-sync/1.0 (+https://trustial.org/blog/)"
MAX_FEED_BYTES = 5 * 1024 * 1024
MAX_IMAGE_BYTES = 8 * 1024 * 1024
IMAGE_ATTEMPTS = 3

DC_CREATOR = "{http://purl.org/dc/elements/1.1/}creator"
SLUG_RE = re.compile(r"^/p/([a-z0-9]+(?:-[a-z0-9]+)*)$")
FRONTMATTER_URL_RE = re.compile(
    r"^(?:external_url|canonical):\s*(?:\"([^\"]*)\"|'([^']*)'|(\S+))\s*$",
    re.MULTILINE,
)
TAG_RE = re.compile(r"<[^>]+>")


@dataclass(frozen=True)
class FeedPost:
    title: str
    link: str
    slug: str
    description: str
    author: str
    published: datetime
    image_url: str | None


@dataclass(frozen=True)
class ExistingLink:
    url: str
    path: Path


def repo_root() -> Path:
    here = Path(__file__).resolve().parent
    for candidate in (here, *here.parents):
        if (candidate / "hugo.toml").is_file():
            return candidate
    raise SystemExit("error: hugo.toml not found above the script; pass --content-dir")


def display_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(Path.cwd().resolve()))
    except ValueError:
        return str(resolved)


def yaml_quote(value: str) -> str:
    escaped = (
        value.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\r", "\\r")
        .replace("\n", "\\n")
        .replace("\t", "\\t")
    )
    return f'"{escaped}"'


def plain_text(value: str) -> str:
    text = TAG_RE.sub(" ", value or "")
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def normalize_url(url: str) -> str:
    parts = urllib.parse.urlsplit(url.strip())
    if parts.scheme not in {"http", "https"} or not parts.netloc:
        return url.strip().rstrip("/")
    path = parts.path.rstrip("/") or "/"
    return urllib.parse.urlunsplit(
        (parts.scheme.lower(), parts.netloc.lower(), path, "", "")
    )


def format_hugo_date(moment: datetime, zone: ZoneInfo) -> str:
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=timezone.utc)
    local = moment.astimezone(zone)
    stamped = local.strftime("%Y-%m-%dT%H:%M:%S%z")
    return f"{stamped[:-2]}:{stamped[-2:]}"


def frontmatter_block(text: str) -> str:
    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return ""
    return parts[1]


def linked_posts(blog_dir: Path) -> dict[str, ExistingLink]:
    found: dict[str, ExistingLink] = {}
    if not blog_dir.is_dir():
        return found
    for path in sorted(blog_dir.rglob("*.md")):
        if not path.is_file():
            continue
        block = frontmatter_block(path.read_text(encoding="utf-8"))
        for match in FRONTMATTER_URL_RE.finditer(block):
            raw = next(group for group in match.groups() if group is not None)
            url = normalize_url(raw)
            if url and url not in found:
                found[url] = ExistingLink(url=url, path=path)
    return found


def host_allowed(hostname: str | None) -> bool:
    if not hostname:
        return False
    host = hostname.lower().rstrip(".")
    if host == "substackcdn.com" or host.endswith(".substackcdn.com"):
        return True
    return host == "substack-post-media.s3.amazonaws.com"


def image_extension(data: bytes) -> str | None:
    if data.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if data.startswith((b"GIF87a", b"GIF89a")):
        return ".gif"
    if len(data) >= 12 and data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        return ".webp"
    return None


class _RedirectGuard(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or not host_allowed(parts.hostname):
            raise urllib.error.URLError(f"refusing redirect to {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _read_limited(response, limit: int) -> bytes:
    chunks: list[bytes] = []
    total = 0
    while True:
        chunk = response.read(64 * 1024)
        if not chunk:
            break
        total += len(chunk)
        if total > limit:
            raise ValueError(f"response exceeds {limit} bytes")
        chunks.append(chunk)
    return b"".join(chunks)


def fetch_bytes(url: str, limit: int, timeout: float) -> bytes:
    parts = urllib.parse.urlsplit(url)
    if parts.scheme != "https" or not host_allowed(parts.hostname):
        raise ValueError(f"refusing image URL {url}")
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "image/jpeg,image/png,image/webp,image/gif",
        },
    )
    opener = urllib.request.build_opener(_RedirectGuard)
    with opener.open(request, timeout=timeout) as response:
        final = urllib.parse.urlsplit(response.geturl())
        if final.scheme != "https" or not host_allowed(final.hostname):
            raise ValueError(f"refusing final image URL {response.geturl()}")
        return _read_limited(response, limit)


def download_image(url: str, timeout: float) -> tuple[bytes, str]:
    last_error: Exception | None = None
    for attempt in range(1, IMAGE_ATTEMPTS + 1):
        try:
            data = fetch_bytes(url, MAX_IMAGE_BYTES, timeout)
            extension = image_extension(data)
            if extension is None:
                raise ValueError("response is not a jpeg, png, gif, or webp image")
            return data, extension
        except Exception as exc:  # noqa: BLE001 - retry any transport or format error
            last_error = exc
            if attempt < IMAGE_ATTEMPTS:
                time.sleep(attempt)
    assert last_error is not None
    raise last_error


def load_feed(source: str, timeout: float) -> bytes:
    candidate = Path(source)
    if candidate.is_file():
        data = candidate.read_bytes()
        if len(data) > MAX_FEED_BYTES:
            raise SystemExit(f"error: feed file exceeds {MAX_FEED_BYTES} bytes")
        return data
    parts = urllib.parse.urlsplit(source)
    if parts.scheme != "https":
        raise SystemExit("error: --feed must be an https URL or a local XML file")
    request = urllib.request.Request(source, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = _read_limited(response, MAX_FEED_BYTES)
    except (urllib.error.URLError, ValueError, TimeoutError) as exc:
        raise SystemExit(f"error: failed to fetch feed: {exc}") from exc
    return data


def parse_feed(xml_bytes: bytes, zone: ZoneInfo) -> list[FeedPost]:
    text = xml_bytes.decode("utf-8", errors="replace")
    lowered = text.lstrip().lower()
    if lowered.startswith("<!doctype") or "<!entity" in lowered:
        raise SystemExit("error: refusing a feed that declares a doctype or entity")
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError as exc:
        raise SystemExit(f"error: feed XML is not valid: {exc}") from exc
    channel = root.find("channel") if root.tag == "rss" else None
    if channel is None:
        raise SystemExit("error: feed is not RSS 2.0")

    posts: list[FeedPost] = []
    seen: set[str] = set()
    for item in channel.findall("item"):
        title = plain_text(item.findtext("title") or "")
        link = normalize_url(item.findtext("link") or "")
        description = plain_text(item.findtext("description") or "")
        author = plain_text(item.findtext(DC_CREATOR) or "") or "Federico Maggi"
        published_raw = (item.findtext("pubDate") or "").strip()
        enclosure = item.find("enclosure")
        image_url = None
        if enclosure is not None:
            image_url = (enclosure.attrib.get("url") or "").strip() or None
            enclosure_type = (enclosure.attrib.get("type") or "").lower()
            if image_url and enclosure_type and not enclosure_type.startswith("image/"):
                image_url = None

        if not title or not link or not published_raw:
            print(f"SKIP  {link or '(missing link)'}\n      missing title, link, or pubDate", file=sys.stderr)
            continue
        parts = urllib.parse.urlsplit(link)
        if parts.scheme != "https" or parts.netloc.lower() != POST_HOST:
            print(f"SKIP  {link}\n      not a {POST_HOST} post")
            continue
        slug_match = SLUG_RE.match(parts.path)
        if not slug_match:
            print(f"SKIP  {link}\n      post URL is not /p/<slug>")
            continue
        if link in seen:
            print(f"SKIP  {link}\n      duplicate item in the feed")
            continue
        try:
            published = parsedate_to_datetime(published_raw)
        except (TypeError, ValueError):
            print(f"SKIP  {link}\n      unreadable pubDate {published_raw!r}", file=sys.stderr)
            continue
        if published is None:
            print(f"SKIP  {link}\n      unreadable pubDate {published_raw!r}", file=sys.stderr)
            continue
        if published.tzinfo is None:
            published = published.replace(tzinfo=timezone.utc)
        # Touch the zone here so a bad timezone fails before any writes.
        format_hugo_date(published, zone)
        seen.add(link)
        posts.append(
            FeedPost(
                title=title,
                link=link,
                slug=slug_match.group(1),
                description=description or title,
                author=author,
                published=published,
                image_url=image_url,
            )
        )
    return posts


def render_post(post: FeedPost, zone: ZoneInfo, image_name: str | None) -> str:
    date = format_hugo_date(post.published, zone)
    lines = [
        "---",
        f"title: {yaml_quote(post.title)}",
        f"description: {yaml_quote(post.description)}",
        f"summary: {yaml_quote(post.description)}",
        f"author: {yaml_quote(post.author)}",
        f"date: {date}",
        f"lastmod: {date}",
        "featured: false",
        "draft: false",
    ]
    if image_name:
        lines.append(f"image: {image_name}")
    lines.extend(
        [
            f"external_url: {yaml_quote(post.link)}",
            f"canonical: {yaml_quote(post.link)}",
            "noindex: true",
            "---",
            "",
        ]
    )
    return "\n".join(lines)


def occupied_slug(blog_dir: Path, slug: str) -> Path | None:
    directory = blog_dir / slug
    page = blog_dir / f"{slug}.md"
    if directory.exists():
        return directory
    if page.exists():
        return page
    return None


def create_bundle(
    blog_dir: Path,
    post: FeedPost,
    zone: ZoneInfo,
    timeout: float,
    dry_run: bool,
) -> str:
    """Write one new bundle. Returns ``created``, ``skipped``, or ``warn``."""
    target = (blog_dir / post.slug).resolve()
    if target.parent != blog_dir.resolve():
        raise SystemExit(f"error: refusing to write outside {blog_dir}")
    date = format_hugo_date(post.published, zone)
    print(f"{'PLAN' if dry_run else 'CREATE'}  {display_path(target / 'index.md')}")
    print(f"      title: {post.title}")
    print(f"      date: {date}")
    print(f"      url: {post.link}")
    if post.image_url:
        print(f"      image: {post.image_url}")
    else:
        print("      image: (none in the feed)")
    if dry_run:
        return "created"

    taken = occupied_slug(blog_dir, post.slug)
    if taken is not None:
        print(f"SKIP  {post.link}")
        print(f"      path exists and was not modified: {display_path(taken)}")
        return "skipped"

    image_bytes: bytes | None = None
    image_name: str | None = None
    warned = False
    if post.image_url:
        try:
            image_bytes, extension = download_image(post.image_url, timeout)
            image_name = f"featured{extension}"
        except Exception as exc:  # noqa: BLE001 - a bad enclosure must not block the stub
            warned = True
            print(
                f"WARN  {post.link}\n      image download failed ({exc}); creating the stub without an image",
                file=sys.stderr,
            )

    markdown = render_post(post, zone, image_name)
    target.mkdir()
    try:
        if image_bytes is not None and image_name is not None:
            (target / image_name).write_bytes(image_bytes)
            print(f"      wrote {image_name} ({len(image_bytes)} bytes)")
        (target / "index.md").write_text(markdown, encoding="utf-8")
    except Exception:
        shutil.rmtree(target)
        raise
    return "warn" if warned else "created"


def sync(args: argparse.Namespace) -> int:
    zone = ZoneInfo(args.timezone)
    blog_dir = (args.content_dir or (repo_root() / "content" / "english" / "blog")).resolve()
    if not blog_dir.is_dir():
        raise SystemExit(f"error: blog directory does not exist: {blog_dir}")

    print("Substack sync")
    print(f"  feed: {args.feed}")
    print(f"  content: {display_path(blog_dir)}")
    print(f"  mode: {'dry-run' if args.dry_run else 'write'}")

    posts = parse_feed(load_feed(args.feed, args.timeout), zone)
    existing = linked_posts(blog_dir)
    print(f"  items: {len(posts)}")
    print(f"  already linked: {sum(1 for post in posts if post.link in existing)}")

    created = 0
    skipped = 0
    warned = 0
    failed = 0
    for post in posts:
        prior = existing.get(post.link)
        if prior is not None:
            print(f"SKIP  {post.link}")
            print(f"      already linked from {display_path(prior.path)}")
            skipped += 1
            continue
        taken = occupied_slug(blog_dir, post.slug)
        if taken is not None:
            print(f"SKIP  {post.link}")
            print(f"      path exists and was not modified: {display_path(taken)}")
            skipped += 1
            continue
        try:
            status = create_bundle(blog_dir, post, zone, args.timeout, args.dry_run)
        except Exception as exc:  # noqa: BLE001 - one bad item must not hide the rest
            failed += 1
            print(f"ERROR {post.link}\n      {exc}", file=sys.stderr)
            continue
        if status == "skipped":
            skipped += 1
        elif status == "warn":
            warned += 1
            created += 1
        else:
            created += 1

    action = "would be created" if args.dry_run else "created"
    print(
        f"done: {created} bundle(s) {action}, {skipped} skipped, {warned} image warning(s), {failed} failed"
    )
    if args.dry_run:
        print("dry-run: no files written")
    return 1 if failed else 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="fetch the feed and print the plan; do not download images or write files",
    )
    parser.add_argument(
        "--feed",
        default=DEFAULT_FEED,
        help=f"https feed URL or a local XML file (default: {DEFAULT_FEED})",
    )
    parser.add_argument(
        "--content-dir",
        type=Path,
        help="blog directory to scan and update (default: content/english/blog)",
    )
    parser.add_argument(
        "--timezone",
        default="America/Los_Angeles",
        help="IANA timezone used for date and lastmod (default: America/Los_Angeles)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="network timeout in seconds (default: 30)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    return sync(args)


if __name__ == "__main__":
    raise SystemExit(main())
