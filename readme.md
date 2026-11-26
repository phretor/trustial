# Trustial

> Federico Maggi's professional digital space - cybersecurity engineering, research, and strategic insights.

## Overview

**Trustial** is the personal website and professional digital space of **Federico Maggi**, a cybersecurity engineer, researcher, and advisor leading security for hyperscale AI & infrastructure technology platforms. The site serves as a central hub for:

- **Technical Leadership**: Platform & enterprise infrastructure security insights
- **Research Excellence**: Academic and industry security research publications
- **Professional Network**: Talks, advisories, and industry engagement
- **Knowledge Sharing**: Blog posts on cybersecurity engineering and business strategy

### Target Audience

- Cybersecurity professionals and researchers
- Industry leaders and enterprise decision-makers
- Academic collaborators and students
- Technology platform stakeholders

## Technical Stack

### Core Technologies

- **[Hugo](https://gohugo.io/)** - Static site generator
- **[Hugoplate](https://github.com/zeon-studio/hugoplate)** - Modern Hugo theme
- **[TailwindCSS](https://tailwindcss.com/)** - Utility-first CSS framework
- **Node.js** - Build toolchain and asset processing

### Development Dependencies

- Hugo Extended 0.149.0
- Node.js 18+
- NPM for package management
- Git for version control

## Deployment

The site is built and published from this public repository by
`.github/workflows/deploy.yml`.

- A push to `main` starts the workflow.
- The build job installs Hugo Extended 0.149.0, checks out this repository,
  installs the npm dependencies, and runs `npm run build`.
- The generated `public/` directory is uploaded as a GitHub Pages artifact.
- The deploy job publishes that artifact with `actions/deploy-pages`, using
  GitHub's Pages and OpenID Connect permissions. No personal access token or
  separate deployment repository is required.
- GitHub Pages serves the site at the custom domain
  [trustial.org](https://trustial.org), which is declared in `static/CNAME`.

For local development, install Hugo Extended 0.149.0 and Node.js, then follow
the development workflow below.

## Development Workflow

### Local Development Setup

1. **Clone the repository**:

   ```bash
   git clone git@github.com:phretor/trustial.git
   cd trustial
   ```

2. **Install dependencies**:

   ```bash
   npm ci
   ```

3. **Start development server**:

   ```bash
   npm run dev
   # Site available at http://localhost:1313
   ```

### Available Commands

```bash
# Development
npm run dev              # Start development server
npm run preview          # Production preview mode

# Building
npm run build           # Build for production
npm run format          # Format code with Prettier

# Theme Management
npm run update-theme    # Update Hugoplate theme
npm run update-modules  # Update Hugo modules
```

### Content Management

#### Directory Structure

```text
content/english/
├── _index.md          # Homepage content
├── about/             # About section
├── blog/              # Blog posts
├── publications/      # Research publications
├── talks/             # Conference talks & presentations
├── advisories/        # Security advisories
└── contact/           # Contact information
```

#### Adding Content

- **Blog Posts**: Create `.md` files in `content/english/blog/`
- **Publications**: Add entries to `content/english/publications/`
- **Talks**: Include presentations in `content/english/talks/`
- **Static Assets**: Place images and files in `static/` directory

#### Substack sync

`.github/workflows/sync-substack.yml` checks the public Substack RSS feed
once a day. `scripts/sync_substack.py` creates an empty-body Hugo leaf bundle
for each post whose canonical URL is not already present in blog frontmatter,
downloads its featured image when available, and leaves all existing content
unchanged. The workflow proposes new bundles on
`automated/substack-sync` through a pull request; it never pushes to `main`.

Run the workflow by hand from **Actions → Sync Substack posts → Run workflow**.
Select **Dry run** to fetch posts and report the plan without writing files or
opening a pull request.
For local inspection only, use:

```bash
python3 scripts/sync_substack.py --dry-run
```

The workflow uses only `GITHUB_TOKEN`, with `contents: write` and
`pull-requests: write`. Pull requests created by `GITHUB_TOKEN` do not trigger
other workflows, so the normal site build runs after the sync pull request is
merged to `main`.

### Theme Customization

- **Layouts**: Custom layouts in `layouts/` directory
- **Styles**: TailwindCSS customizations in `assets/css/`
- **Components**: Reusable components in `layouts/partials/`
- **Configuration**: Site settings in `hugo.toml`

## Site Sections

### Core Content Areas

- **Homepage**: Professional overview and key capabilities
- **About**: Detailed background and expertise
- **Blog**: Technical insights and industry analysis
- **Publications**: Academic and industry research papers
- **Talks**: Conference presentations and speaking engagements
- **Advisories**: Security vulnerability disclosures
- **Contact**: Professional contact information

### Content Features

- **Responsive Design**: Mobile-first approach with TailwindCSS
- **Search Functionality**: Built-in search across all content
- **Social Sharing**: Integrated social media sharing
- **Analytics**: Google Analytics integration
- **SEO Optimized**: Meta tags, structured data, and performance optimization

## Maintaining the site with Claude Code

This site is maintained via [Claude Code](https://claude.ai/code). The `CLAUDE.md` file at the repo root gives Claude the context it needs to work autonomously.

### Common tasks you can ask Claude to do

| Task                  | Example prompt                                                     |
| --------------------- | ------------------------------------------------------------------ |
| Add a blog post       | "Add a blog post titled '…' with this content: …"                  |
| Add a publication     | "Add publication: title, authors, venue, year, abstract, PDF link" |
| Add a talk            | "Add talk: title, event, year, slides/video link"                  |
| Update review service | "I'm also reviewing for XYZ 2026"                                  |
| Update the about page | "Update the about section with …"                                  |
| Fix content           | "The link on the '…' post is broken, update it to …"               |

### Workflow

Claude will:

1. Make the requested changes
2. Run `npm run build` to verify no errors
3. Ask whether to commit and push

If the build fails, Claude will diagnose and fix before asking to commit.

### Pre-commit hooks

[prek](https://github.com/your-repo/prek) is installed and runs on every commit:

- **prettier** — formats HTML, JSON, Markdown, and YAML
- **zizmor** — audits GitHub Actions workflows for security issues

If a hook fails on commit, Claude will fix the issue before retrying.

## Maintenance & Updates

### Regular Maintenance

- **Theme Updates**: Use `npm run update-theme` for Hugoplate updates
- **Dependency Updates**: Regular `npm update` for security patches
- **Content Review**: Periodic review of publications and talks
- **Performance Monitoring**: Check site performance and loading times

### Troubleshooting

#### Common Issues

- **Build Failures**: Check the Hugo Extended and Node.js versions
- **Deployment Errors**: Inspect the GitHub Pages workflow run
- **Theme Issues**: Ensure theme version compatibility
- **Content Rendering**: Validate Markdown syntax and frontmatter

#### Debug Commands

```bash
# Verbose build for debugging
hugo --debug --verbose

# Check Hugo version
hugo version

# Validate configuration
hugo config
```

## Contributing

### Guidelines

- Follow existing content structure and naming conventions
- Test locally before pushing changes
- Use descriptive commit messages
- Maintain consistent formatting with Prettier

### Security Considerations

- Keep dependencies updated for security patches
- Review external links and references
- Validate content for professional standards
- Monitor for broken links and outdated information

## License

The repository's theme and code are covered by the MIT `LICENSE`. Unless
otherwise stated, original site content is licensed under
[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/), as
noted in the site's footer.

---

**Trustial** - Bridging complex security challenges with practical business strategy.
