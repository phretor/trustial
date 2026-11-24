#!/usr/bin/env python3
"""Create Hugo redirect bundles for Substack posts not already in the blog."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

API_URL = "https://trustial.substack.com/api/v1/posts"
POST_HOST = "trustial.substack.com"
USER_AGENT = "trustial-substack-sync/1.0 (+https://trustial.org/)"
MAX_RESPONSE_BYTES = 10 * 1024 * 1024
URL_FIELD = re.compile(
    r"^(?:external_url|canonical):\s*(?:\"([^\"]+)\"|'([^']+)'|(\S+))\s*$",
    re.MULTILINE,
)
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
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


def fetch_json(source: str, timeout: float) -> dict:
    path = Path(source)
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))

    parts = urllib.parse.urlsplit(source)
    if parts.scheme != "https" or parts.hostname != POST_HOST:
        raise ValueError(f"source must be an HTTPS endpoint on {POST_HOST}")
    request = urllib.request.Request(
        source,
        headers={"Accept": "application/json", "User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        final = urllib.parse.urlsplit(response.geturl())
        if final.scheme != "https" or final.hostname != POST_HOST:
            raise ValueError("source redirected to an untrusted host")
        return json.loads(read_limited(response))


def parse_posts(payload: dict) -> list[Post]:
    posts: list[Post] = []
    for item in payload.get("posts", []):
        slug = item.get("slug", "")
        url = normalized_url(item.get("canonical_url", ""))
        parts = urllib.parse.urlsplit(url)
        if (
            not SLUG.fullmatch(slug)
            or parts.scheme != "https"
            or parts.hostname != POST_HOST
            or parts.path != f"/p/{slug}"
        ):
            print(f"skip invalid post metadata: {slug or '(missing slug)'}", file=sys.stderr)
            continue
        title = str(item.get("title", "")).strip()
        if not title:
            print(f"skip post without title: {url}", file=sys.stderr)
            continue
        description = str(item.get("subtitle") or title).strip()
        raw_date = str(item.get("post_date", ""))
        try:
            published = datetime.fromisoformat(raw_date.replace("Z", "+00:00"))
        except ValueError:
            print(f"skip post with invalid date: {url}", file=sys.stderr)
            continue
        posts.append(
            Post(
                slug=slug,
                title=title,
                description=description,
                url=url,
                date=published.isoformat(timespec="seconds"),
                image_url=item.get("cover_image"),
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
    posts = parse_posts(fetch_json(source, timeout))
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
    parser.add_argument("--source", default=API_URL, help="HTTPS API URL or local JSON file")
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
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
