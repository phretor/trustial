# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Federico Maggi's personal professional website ([trustial.org](https://trustial.org)) — a static site built with Hugo + Hugoplate theme + TailwindCSS 4. Deployed to GitHub Pages via Actions on push to `main`.

## Commands

```bash
npm run dev          # Hugo dev server at localhost:1313 (live reload)
npm run build        # Production build → public/
npm run preview      # Production build + local preview
npm run format       # Prettier (HTML + Go templates)
```

No test suite — this is a static site. Validate visually with `npm run dev`.

After adding Hugo modules: `npm run update-modules` to refresh `go.sum`.

**After every change, run `npm run build` and confirm it exits cleanly before considering the task done. If the build passes, ask whether to commit and push.**

## Architecture

```
content/english/          ← all Markdown content (blog, publications, talks, advisories)
layouts/                  ← Hugo templates overriding the Hugoplate theme
  publications/           ← list.html + single.html
  talks/                  ← list.html + single.html
  partials/components/    ← reusable partials (publication-card, blog-card, citation-content, etc.)
assets/css/               ← TailwindCSS entry point (custom.css)
config/_default/          ← params.toml, languages.toml, menus.en.toml, module.toml
data/                     ← theme.json (colors, fonts)
```

### Content structure

All content lives under `content/english/` (single-language site). Each section maps to a content type:

| Section         | URL pattern                        | Template                   |
| --------------- | ---------------------------------- | -------------------------- |
| `blog/`         | `/blog/slug/`                      | `layouts/blog/single.html` |
| `publications/` | `/publications/author_title_year/` | `layouts/publications/`    |
| `talks/`        | `/talks/event_talk_year/`          | `layouts/talks/`           |
| `advisories/`   | `/advisories/slug/`                | theme default              |

### Template override model

This project overrides Hugoplate theme templates by placing files in `layouts/`. Hugo picks local templates over module templates. The theme itself is loaded as a Hugo module (see `config/_default/module.toml`).

### Key params

`config/_default/params.toml` controls: dark mode default, Google Analytics (`G-2QG24QF490`), search (indexes `blog` only via `searchindex.json`), and social links.

### Search

Client-side search. Indexes only `mainSections = ["blog"]`. The index is built at `public/searchindex.json` during Hugo build.

### Deployment

Push to `main` → GitHub Actions (`.github/workflows/deploy.yml`) → Hugo Extended 0.149.0 build → GitHub Pages. No staging environment.

## Security tracking

A `SECURITY.md` file at the repo root tracks known security issues and open risks. Keep it current:

- When you spot a new security issue (supply chain, config, dependency, workflow), add it.
- When an issue is fixed, mark it resolved with the fix date and commit reference.
- Do not remove resolved entries — they serve as a record.
- Any change in remediation status (Open → Resolved, or regression back to Open) must be committed atomically with the code change that caused it — same commit, not a follow-up.

Format for each entry:

```
### <short title>
- **File**: path/to/file (line N if relevant)
- **Status**: Open | Resolved (YYYY-MM-DD, <commit>)
- **Risk**: one-line description
- **Fix**: what needs to be done (or was done)
```
