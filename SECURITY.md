# SECURITY.md

Known security issues and open risks for this repository. Maintained by Claude Code per instructions in CLAUDE.md.

---

### GitHub Actions: actions pinned to full commit SHAs

- **File**: `.github/workflows/deploy.yml`
- **Status**: Resolved (2026-04-13, 21799a1)
- **Risk**: Tag-pinned actions can be silently overwritten by a compromised upstream; a supply chain attack could execute arbitrary code in the build environment.
- **Fix**: Commit `21799a1` pinned every `uses:` entry to a full commit SHA with a version comment and scoped workflow permissions by job.
