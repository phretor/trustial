#!/usr/bin/env python3
"""Create Hugo redirect bundles for Substack posts not already in the blog."""

from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ElementTree
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from pathlib import Path

FEED_URL = "https://trustial.substack.com/feed"
POST_HOST = "trustial.substack.com"
USER_AGENT = "trustial-substack-sync/1.0 (+https://trustial.org/)"
MAX_RESPONSE_BYTES = 10 * 1024 * 1024
URL_FIELD = re.compile(
    r"^(?:external_url|canonical):\s*(?:\"([^\"]+)\"|'([^']+)'|(\S+))\s*$",
    re.MULTILINE,
)
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
POST_PATH = re.compile(r"^/p/([a-z0-9]+(?:-[a-z0-9]+)*)$")
IMAGE_HOSTS = {"substackcdn.com", "substack-post-media.s3.amazonaws.com"}


@dataclass(frozen=True)
class Post:
    slug: str
    title: str
    description: str
    url: str
    date: str
    image_url: str | None


def normalized_url(value: str) -> str:
    parts = urllib.parse.urlsplit(value.strip())
    return urllib.parse.urlunsplit(
        (parts.scheme.lower(), parts.netloc.lower(), parts.path.rstrip("/"), "", "")
    )


def yaml_string(value: str) -> str:
    escaped = (
        value.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\r", "\\r")
        .replace("\n", "\\n")
    )
    return f'"{escaped}"'


def read_limited(response, limit: int = MAX_RESPONSE_BYTES) -> bytes:
    data = response.read(limit + 1)
    if len(data) > limit:
        raise ValueError(f"response exceeds {limit} bytes")
    return data


def fetch_feed(source: str, timeout: float) -> ElementTree.Element:
    path = Path(source)
    if path.is_file():
        return ElementTree.fromstring(path.read_bytes())

    parts = urllib.parse.urlsplit(source)
    if parts.scheme != "https" or parts.hostname != POST_HOST:
        raise ValueError(f"source must be an HTTPS endpoint on {POST_HOST}")
    request = urllib.request.Request(
        source,
        headers={
            "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.1",
            "User-Agent": USER_AGENT,
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        final = urllib.parse.urlsplit(response.geturl())
        if final.scheme != "https" or final.hostname != POST_HOST:
            raise ValueError("source redirected to an untrusted host")
        return ElementTree.fromstring(read_limited(response))


def parse_posts(root: ElementTree.Element) -> list[Post]:
    channel = root.find("channel")
    if channel is None:
        return []
    posts: list[Post] = []
    for item in channel.findall("item"):
        link = (item.findtext("link") or "").strip()
        url = normalized_url(link)
        parts = urllib.parse.urlsplit(url)
        slug_match = POST_PATH.fullmatch(parts.path or "")
        if parts.scheme != "https" or parts.hostname != POST_HOST or slug_match is None:
            print(f"skip invalid post link: {link or '(missing)'}", file=sys.stderr)
            continue
        slug = slug_match.group(1)
        title = html.unescape((item.findtext("title") or "").strip())
        if not title:
            print(f"skip post without title: {url}", file=sys.stderr)
            continue
        description = html.unescape((item.findtext("description") or "").strip()) or title
        raw_date = (item.findtext("pubDate") or "").strip()
        try:
            published = parsedate_to_datetime(raw_date)
        except (TypeError, ValueError):
            published = None
        if published is None:
            print(f"skip post with invalid date: {url}", file=sys.stderr)
            continue
        image_url: str | None = None
        enclosure = item.find("enclosure")
        if enclosure is not None:
            enclosure_url = enclosure.get("url")
            enclosure_type = (enclosure.get("type") or "").lower()
            if enclosure_url and enclosure_type.startswith("image/"):
                image_url = enclosure_url
        posts.append(
            Post(
                slug=slug,
                title=title,
                description=description,
                url=url,
                date=published.isoformat(timespec="seconds"),
                image_url=image_url,
            )
        )
    return posts


def existing_links(content_dir: Path) -> set[str]:
    links: set[str] = set()
    for markdown in content_dir.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        frontmatter = text.split("---", 2)[1]
        for match in URL_FIELD.finditer(frontmatter):
            links.add(normalized_url(next(value for value in match.groups() if value)))
    return links


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


def download_image(url: str, timeout: float) -> tuple[bytes, str]:
    parts = urllib.parse.urlsplit(url)
    host = (parts.hostname or "").lower()
    if parts.scheme != "https" or not (
        host in IMAGE_HOSTS or host.endswith(".substackcdn.com")
    ):
        raise ValueError("untrusted image URL")
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        final = urllib.parse.urlsplit(response.geturl())
        final_host = (final.hostname or "").lower()
        if final.scheme != "https" or not (
            final_host in IMAGE_HOSTS or final_host.endswith(".substackcdn.com")
        ):
            raise ValueError("image redirected to an untrusted host")
        data = read_limited(response)
    extension = image_extension(data)
    if extension is None:
        raise ValueError("unsupported image format")
    return data, extension


def render(post: Post, image_name: str | None) -> str:
    fields = [
        "---",
        f"title: {yaml_string(post.title)}",
        f"description: {yaml_string(post.description)}",
        f"summary: {yaml_string(post.description)}",
        'author: "Federico Maggi"',
        f"date: {post.date}",
        f"lastmod: {post.date}",
        "featured: false",
        "draft: false",
    ]
    if image_name:
        fields.append(f"image: {image_name}")
    fields.extend(
        [
            f"external_url: {yaml_string(post.url)}",
            f"canonical: {yaml_string(post.url)}",
            "noindex: true",
            "---",
            "",
        ]
    )
    return "\n".join(fields)


def sync(source: str, content_dir: Path, timeout: float, dry_run: bool) -> int:
    posts = parse_posts(fetch_feed(source, timeout))
    linked = existing_links(content_dir)
    created = 0

    for post in posts:
        if post.url in linked:
            print(f"skip linked: {post.url}")
            continue
        target = content_dir / post.slug
        if target.exists() or (content_dir / f"{post.slug}.md").exists():
            print(f"skip occupied path: {target}", file=sys.stderr)
            continue
        if dry_run:
            print(f"would create: {target / 'index.md'}")
            created += 1
            continue

        image_data: bytes | None = None
        image_name: str | None = None
        if post.image_url:
            try:
                image_data, extension = download_image(post.image_url, timeout)
                image_name = f"featured{extension}"
            except Exception as error:  # The redirect stub remains useful without an image.
                print(f"warning: image unavailable for {post.url}: {error}", file=sys.stderr)

        target.mkdir()
        try:
            if image_data is not None and image_name is not None:
                (target / image_name).write_bytes(image_data)
            (target / "index.md").write_text(render(post, image_name), encoding="utf-8")
        except Exception:
            shutil.rmtree(target)
            raise
        linked.add(post.url)
        created += 1
        print(f"created: {target / 'index.md'}")

    print(f"created {created} bundle(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        default=FEED_URL,
        help="HTTPS RSS feed URL or local XML file",
    )
    parser.add_argument(
        "--content-dir",
        type=Path,
        default=Path("content/english/blog"),
        help="Hugo blog content directory",
    )
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not args.content_dir.is_dir():
        parser.error(f"content directory does not exist: {args.content_dir}")
    try:
        return sync(args.source, args.content_dir.resolve(), args.timeout, args.dry_run)
    except (OSError, ValueError, ElementTree.ParseError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
