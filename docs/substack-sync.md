# Substack sync

The blog list at <https://trustial.org/blog/> includes posts from <https://trustial.substack.com> as redirect stubs. One post is already linked by hand at `content/english/blog/gpt-opus-wearable-pcb/`. `scripts/sync_substack.py` creates the same kind of leaf bundle for every newer item in the public feed <https://trustial.substack.com/feed>.

The blog card links straight to Substack (external-link icon) because `layouts/partials/components/blog-card.html` reads `external_url`. The stub page itself is the redirect in `layouts/blog/single.html`. `noindex` and `canonical` are rendered by `layouts/partials/basic-seo.html`.

## What a new bundle looks like

For a feed item whose link is not already an `external_url` or `canonical` anywhere under `content/english/blog/`, the script creates:

```text
content/english/blog/<substack-slug>/
  index.md
  featured.jpg    # or .png / .webp / .gif, when the download succeeds
```

`index.md` follows the wearable-PCB stub:

- `title`, `description`, and `summary` come from the feed title and subtitle (HTML stripped). `description` and `summary` are the same text.
- `author` comes from the feed's `dc:creator`.
- `date` and `lastmod` are the feed `pubDate`, converted to `America/Los_Angeles` (the site timezone in `hugo.toml`).
- `external_url` and `canonical` are the Substack post URL.
- `noindex: true`, `featured: false`, `draft: false`.
- `image` is the local featured file when one was downloaded.

The body is empty. The article stays on Substack; the stub only redirects.

The slug is the `/p/<slug>` segment of the Substack URL. That is why the hand-written wearable-PCB bundle (`gpt-opus-wearable-pcb`) is not duplicated: matching is on `external_url` / `canonical`, not on the directory name.

## Images

Featured images are downloaded into the bundle on a real run. That matches `image: featured.png` on the existing stub, so the theme image partial keeps using a local page resource. The feed's enclosure URL is a Substack image-proxy link (the filename and the `Content-Type` header do not always agree), so the script trusts the file's magic bytes and names it `featured.jpg`, `featured.png`, `featured.webp`, or `featured.gif`.

Downloads are HTTPS only, limited to `substackcdn.com` and `substack-post-media.s3.amazonaws.com`, capped at 8 MiB, and retried three times. `--dry-run` does not download them.

If the download still fails, the stub is created without an `image` field and a warning is printed. The post URL is then already linked, so a later run will not try the image again. One broken enclosure cannot block the rest of the feed.

## What the script will not do

- It does not modify or delete an existing file or directory.
- If `content/english/blog/<slug>/` or `<slug>.md` already exists, that item is skipped even when the URL is new.
- It only accepts `https://trustial.substack.com/p/<slug>` links, so a different feed cannot add posts.
- It does not copy the article HTML from `content:encoded`.

## Run it locally

Python 3.9 or newer, from the repository root:

```bash
python3 scripts/sync_substack.py --dry-run
python3 scripts/sync_substack.py
```

`--dry-run` fetches the feed and prints the bundles it would create. It writes nothing.

| Flag            | Meaning                                                                   |
| --------------- | ------------------------------------------------------------------------- |
| `--feed`        | `https` feed URL, or a local RSS file. Default: the public Substack feed. |
| `--content-dir` | Blog directory to scan and update. Default: `content/english/blog`.       |
| `--timezone`    | IANA timezone for `date` and `lastmod`. Default: `America/Los_Angeles`.   |
| `--timeout`     | Network timeout in seconds. Default: 30.                                  |

Run it a second time after a real run. The second run should create nothing.

Then build the site:

```bash
npm ci
npm run build
```

## GitHub Actions

`.github/workflows/sync-substack.yml` runs every day at 15:17 UTC and from the Actions tab (`workflow_dispatch`). It uses the default `GITHUB_TOKEN` only. There are no repository secrets.

When the script creates files, the workflow builds with Hugo Extended 0.149.0 and opens or updates a **draft** pull request on the branch `substack-sync` (`peter-evans/create-pull-request` v8.1.3, pinned to a commit SHA). The workflow does not merge and does not mark the pull request ready. A later run updates the same open pull request and leaves its draft state alone.

The job permissions are `contents: write` (push `substack-sync`) and `pull-requests: write` (open the draft). Checkout does not persist credentials. Only paths under `content/english/blog/` are committed, so a Hugo build cannot sneak `hugo_stats.json` or `public/` into the pull request.

Events caused by `GITHUB_TOKEN` do not start other workflows. `.github/workflows/deploy.yml` listens for a push to `main`, so the site updates when a person marks the draft ready and merges it. The deploy does not run on the sync pull request itself.

Scheduled runs can be delayed by GitHub, and the workflow file has to be on the default branch before the schedule starts.

## Rollback

- Close the sync pull request without merging to discard a batch of stubs.
- Delete `.github/workflows/sync-substack.yml` to stop the daily run. Bundles that are already on `main` stay until they are removed by hand. The script never deletes content.
