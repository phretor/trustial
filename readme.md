# Trustial.org

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

- Hugo Extended (latest)
- Node.js 18+
- NPM for package management
- Git for version control

## Deployment Architecture

### Repository Structure

```
┌─────────────────────────┐    GitHub Actions    ┌─────────────────────────-─┐
│ phretor/trustial        │ ──────────────────►  │ phretor/trustial.org      │
│ (Private Source Repo)   │     Automated CI/CD  │ (Public Hosting Repo)     │
│                         │                      │                           │
│ • Hugo source code      │                      │ • Built static files      │
│ • Content & assets      │                      │ • GitHub Pages hosting    │
│ • Theme customizations  │                      │ • Public website          │
└─────────────────────────┘                      └─────────────────────────-─┘
```

### Automated Deployment

- **Trigger**: Push to `main` branch or manual dispatch
- **Build Process**: Hugo static site generation with optimizations
- **Deployment**: Automated deployment to GitHub Pages via separate public repository
- **Hosting**: Available at the configured GitHub Pages URL

## Configuration & Setup

### Prerequisites

1. **GitHub Personal Access Token** with `repo` permissions
2. **Target Repository** for hosting (public)
3. **GitHub Pages** enabled on target repository

### Required Secrets

Add the following secret to your source repository:

```
DEPLOY_TOKEN = <your-personal-access-token>
```

### Workflow Configuration

The deployment workflow (`.github/workflows/deploy.yml`) is pre-configured with:

- **Source Repository**: `phretor/trustial.org` (this repo)
- **Target Repository**: `phretor/phretor.github.io`
- **Branch**: Deploys from `main` to `main`

To modify the target repository, update the `external_repository` field in the workflow file.

## Development Workflow

### Local Development Setup

1. **Clone the repository**:

   ```bash
   git clone git@github.com:phretor/trustial.org.git
   cd trustial.org
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

```
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

## Maintenance & Updates

### Regular Maintenance

- **Theme Updates**: Use `npm run update-theme` for Hugoplate updates
- **Dependency Updates**: Regular `npm update` for security patches
- **Content Review**: Periodic review of publications and talks
- **Performance Monitoring**: Check site performance and loading times

### Troubleshooting

#### Common Issues

- **Build Failures**: Check Node.js version compatibility
- **Deployment Errors**: Verify GitHub token permissions
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

Content and customizations are proprietary. The underlying Hugoplate theme follows its respective MIT license.

---

**Trustial.org** - Bridging complex security challenges with practical business strategy.
