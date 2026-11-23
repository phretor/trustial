# SECURITY.md

Known security issues and open risks for this repository. Maintained by Claude Code per instructions in CLAUDE.md.

---

### GitHub Actions: actions pinned to tags, not SHA hashes

- **File**: `.github/workflows/deploy.yml` (lines 31, 37, 44, 56, 70)
- **Status**: Resolved (2026-04-13, pending commit)
- **Risk**: Tag-pinned actions can be silently overwritten by a compromised upstream; a supply chain attack could execute arbitrary code in the build environment.
- **Fix**: Pin every `uses:` entry to a full commit SHA with a version comment, e.g. `actions/checkout@<sha>  # v4.2.2`. Use `zizmor .github/workflows/` to audit.

### Build-tool dependency vulnerabilities

- **File**: `package-lock.json`
- **Status**: Resolved (2026-11-23, pending commit)
- **Risk**: Vulnerable transitive npm dependencies could expose local and CI builds to denial-of-service or arbitrary file-write attacks.
- **Fix**: Refresh the npm lockfile so `tar`, `picomatch` and `source-map-js` resolve to patched versions within their existing ranges, and override `postcss-selector-parser` to `^6.1.6` under `@tailwindcss/typography` (which pins `6.0.10`), without changing direct dependency versions.
