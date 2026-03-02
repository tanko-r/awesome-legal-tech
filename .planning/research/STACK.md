# Stack Research

**Domain:** GitHub awesome-list repository (legal technology)
**Researched:** 2026-03-02
**Confidence:** HIGH

---

## Overview

An awesome list is a plain Markdown repository, not a software application. The "stack" is entirely conventions, tooling, and GitHub automation — no runtime, no framework, no database. Every choice below is about maintaining quality and staying eligible for inclusion in the sindresorhus/awesome index.

---

## Recommended Stack

### Core Technologies

| Technology | Version | Purpose | Why Recommended |
|------------|---------|---------|-----------------|
| Markdown (README.md) | GFM (GitHub Flavored) | Canonical list content | Required by sindresorhus/awesome; GitHub renders natively; no tooling required to read |
| Git + GitHub | Latest | Repository hosting, PR workflow, CI | The awesome-list ecosystem is GitHub-native; discoverability, CI/CD, and community tooling all assume GitHub |
| CC0 1.0 Universal | — | License | Explicitly required by awesome index guidelines; code licenses (MIT, Apache, GPL) are rejected; CC0 places content in public domain which is correct for a curated list, not code |

### Required Files

| File | Purpose | Notes |
|------|---------|-------|
| `README.md` | The actual list — single canonical document | Must have: Awesome badge, "Contents" ToC section, consistent `link - Description.` format, no CI badges, no hard-wrapping |
| `contributing.md` | Contribution guidelines | Required by awesome-lint `contributing` rule; must be lowercase filename |
| `license` | CC0 license text | Required by awesome-lint `license` rule; use CC0, not MIT |
| `code-of-conduct.md` | Community standards | Strongly recommended; awesome-lint checks for it via `code-of-conduct` rule |
| `.github/workflows/ci.yml` | Run awesome-lint on every PR | Standard practice for all maintained awesome lists |
| `.github/workflows/links.yml` | Scheduled link rot detection | Best practice; run lychee on a cron schedule |
| `.editorconfig` | Editor consistency | Used by sindresorhus/awesome itself; enforces consistent whitespace |
| `.gitattributes` | Normalize line endings | Prevents CRLF/LF issues in cross-platform contributions |

### CI/CD: Linting

| Tool | Version | Purpose | Why |
|------|---------|---------|-----|
| awesome-lint | 2.2.3 (Jan 2026) | Enforces all awesome-list conventions | The canonical linter from sindresorhus; runs 15 specific rules covering badges, ToC, headings, license, contributing, list-item format, spell-check, duplicate links, no-CI-badges, repo age, and 40+ general Markdown rules. Actively maintained with releases through January 2026 |
| Node.js | LTS (22.x) | Runtime for awesome-lint | awesome-lint is an npm package; use Node LTS for stability in CI |
| GitHub Actions | — | CI orchestration | Free for public repos; native GitHub integration; standard across all mainstream awesome lists |

### CI/CD: Link Checking

| Tool | Version | Purpose | Why |
|------|---------|---------|-----|
| lychee | v2 (lychee-action@v2) | Detect broken/dead URLs on a schedule | Written in Rust; extremely fast (576 links in ~1 minute); native GitHub Actions integration; can auto-open issues when links break; preferred over markdown-link-check which is slower and less configurable |

### Discovery and Ecosystem Integration

| Tool | Purpose | Notes |
|------|---------|-------|
| GitHub Topics | Make list discoverable | **Required**: add `awesome-list` and `awesome` topics to the repository settings |
| awesome.re badge | Signal membership in the awesome ecosystem | Use official badge only: `[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)` — no modifications |
| TrackAwesomeList | Automated daily tracking by third party | Automatically indexes lists once they are included in sindresorhus/awesome |
| ecosyste.ms/awesome | Open API indexing | Automatically aggregates listed resources once the repo is in the index |

---

## GitHub Actions Workflows

### Workflow 1: Lint on Every PR

```yaml
# .github/workflows/ci.yml
name: CI
on:
  pull_request:
    branches: [main]
jobs:
  awesome-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Required: awesome-lint checks repository age
      - run: npx awesome-lint
```

`fetch-depth: 0` is non-optional. awesome-lint checks that the repo is at least 30 days old before passing (mirroring the sindresorhus/awesome submission requirement).

### Workflow 2: Scheduled Link Checker

```yaml
# .github/workflows/links.yml
name: Links
on:
  schedule:
    - cron: "0 18 * * 1"  # Weekly on Monday at 18:00 UTC
  workflow_dispatch:       # Allow manual trigger
jobs:
  link-checker:
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      - uses: actions/checkout@v4
      - name: Check links
        id: lychee
        uses: lycheeverse/lychee-action@v2
        with:
          args: '--verbose --no-progress README.md'
          fail: false
      - name: Create issue for broken links
        uses: peter-evans/create-issue-from-file@v5
        if: steps.lychee.outputs.exit_code != 0
        with:
          title: 'Link rot detected'
          content-filepath: ./lychee/out.md
          labels: maintenance
```

---

## README.md Structure Conventions

These are enforced by awesome-lint and the sindresorhus/awesome PR checklist:

```markdown
<div align="center">
  <img src="logo.svg" width="400" alt="Awesome Legal Apps">
  <br>
  <a href="https://awesome.re">
    <img src="https://awesome.re/badge.svg" alt="Awesome">
  </a>
</div>

# Awesome Legal Apps

> A curated list of awesome legal technology tools, apps, and resources.

## Contents

- [Category One](#category-one)
- [Category Two](#category-two)
- [Contributing](#contributing)

## Category One

- [Tool Name](https://example.com) - One-sentence description starting uppercase, ending with period.

## Contributing

Contributions welcome! Read the [contribution guidelines](contributing.md) first.
```

Key structural rules enforced by awesome-lint:
- Heading must be `# Awesome [Name]` (title case)
- ToC section must be named "Contents" (not "Table of Contents")
- Each entry: `- [Name](url) - Description starting uppercase, ending with period.`
- No CI badges in the README (awesome-lint `no-ci-badge` rule)
- Unordered list marker must be `-` not `*`
- Awesome badge must be present and unmodified
- No trailing slashes on URLs
- No duplicate links

---

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|-------------------------|
| CC0 license | Creative Commons Attribution | Only if you require attribution; CC0 is simpler and explicitly permitted |
| awesome-lint (npx) | max/awesome-lint GitHub Action (v2.0.0) | Never — unmaintained since 2019; use `npx awesome-lint` directly in CI instead |
| lychee for link checking | markdown-link-check | If you want a pure JS solution and don't mind slower runs; lychee is faster and more reliable for large lists |
| Plain README.md | Docsify/GitBook/MkDocs site | Only if building a searchable web portal beyond GitHub; the awesome-list format explicitly requires a non-generated Markdown file for the index |
| Yeoman generator (generator-awesome-list) | Manual scaffolding | The generator is unmaintained (last release August 2020); scaffold manually using the file list above — it's only 6 files |

---

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| MIT / Apache / GPL license | Explicitly rejected by sindresorhus/awesome PR checklist | CC0 1.0 Universal |
| max/awesome-lint GitHub Action | Last release 2019, unmaintained, unknown compatibility with awesome-lint 2.x | `npx awesome-lint` directly in CI workflow |
| jthegedus/github-action-awesome-lint | Deprecated — its own README says to use `npx -y awesome-lint` instead | `npx awesome-lint` |
| CI/status badges in README.md | Explicitly prohibited by awesome-lint (`no-ci-badge` rule) and sindresorhus/awesome guidelines | Only use the official Awesome badge |
| `* ` bullet markers | awesome-lint enforces `-` markers | `-` for all list items |
| "Table of Contents" as ToC heading | awesome-lint requires the section to be named "Contents" | `## Contents` |
| Hard line wrapping | Prohibited by awesome-lint | One item per line, no manual wrapping |
| generator-awesome-list (Yeoman) | Unmaintained since August 2020 | Manual file creation from the file list above |
| `master` branch name | sindresorhus/awesome requires `main` | `main` as the default branch |

---

## Stack Patterns by Variant

**If submitting to the sindresorhus/awesome index:**
- Wait 30 days from first commit before submitting the PR
- Run `npx awesome-lint` locally before submitting and resolve all warnings
- Add topics `awesome-list` and `awesome` in GitHub repository settings
- Review at least 2 other open PRs to the awesome index (required by PR checklist)

**If building a standalone legal tech list (not submitted to awesome index):**
- Still use CC0 and awesome-lint for quality
- Can relax the 30-day rule
- Consider adding a `legaltech` topic alongside `awesome-list`

**If the list grows beyond ~100 entries:**
- Split categories into subsections but keep ToC nesting minimal (awesome-lint warns on deep nesting)
- Consider a `contributing.md` checklist that describes your specific quality criteria for legal tool inclusion

---

## Version Compatibility

| Package | Compatible With | Notes |
|---------|-----------------|-------|
| awesome-lint@2.2.3 | Node.js 18.x, 20.x, 22.x | Requires Node LTS; uses ESM; v2.x dropped CommonJS support |
| lycheeverse/lychee-action@v2 | GitHub Actions ubuntu-latest | v2 is the current stable action version as of 2025 |
| actions/checkout@v4 | GitHub Actions ubuntu-latest | Use v4; v3 is deprecated |

---

## Installation

```bash
# Verify awesome-lint locally before pushing
npm install --save-dev awesome-lint

# Or run directly without installing
npx awesome-lint

# Verify links locally (requires Rust/cargo or use Docker)
# Easier: rely on the GitHub Actions workflow for this
```

`.lycheeignore` file for suppressing known false-positive URLs:
```
# .lycheeignore
# Add URLs that are valid but lychee can't reach (auth-gated, etc.)
https://example-legal-tool.com/pricing
```

---

## Sources

- [sindresorhus/awesome-lint GitHub](https://github.com/sindresorhus/awesome-lint) — Rules enumeration, v2.2.3 release date (Jan 30, 2026), CI workflow pattern — HIGH confidence (official source)
- [sindresorhus/awesome pull_request_template.md](https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md) — Full PR checklist: file requirements, naming, badge, license, ToC, formatting — HIGH confidence (official source)
- [sindresorhus/awesome create-list.md](https://github.com/sindresorhus/awesome/blob/main/create-list.md) — 30-day maturation rule, Yeoman generator reference — HIGH confidence (official source)
- [sindresorhus/awesome awesome.md (manifesto)](https://github.com/sindresorhus/awesome/blob/main/awesome.md) — Curation principles, CC0 rationale — HIGH confidence (official source)
- [lycheeverse/lychee-action](https://github.com/lycheeverse/lychee-action) — Link checker GitHub Action, v2 current version — HIGH confidence (official source)
- [lychee.cli.rs GitHub Actions recipe](https://lychee.cli.rs/github_action_recipes/check-repository/) — Complete workflow YAML, scheduled link checking pattern — MEDIUM confidence (official docs)
- [awesome-lint config.js](https://github.com/sindresorhus/awesome-lint/blob/main/config.js) — Full remark-lint rule set — HIGH confidence (official source)
- [awesome-lint rules directory](https://github.com/sindresorhus/awesome-lint/tree/main/rules) — 15 specific awesome rules enumerated — HIGH confidence (official source)
- [max/awesome-lint](https://github.com/max/awesome-lint) — Confirmed unmaintained (last release 2019) — HIGH confidence (direct inspection)
- [generator-awesome-list](https://github.com/dar5hak/generator-awesome-list) — Confirmed unmaintained (last release August 2020) — HIGH confidence (direct inspection)
- [officeanddragons/awesome-lawtech](https://github.com/officeanddragons/awesome-lawtech) — Real-world legal awesome list example structure — MEDIUM confidence (secondary source)
- [jthegedus/github-action-awesome-lint](https://github.com/jthegedus/github-action-awesome-lint) — Deprecated, confirms npx approach — MEDIUM confidence (official deprecation notice)

---

*Stack research for: GitHub awesome-list (legal technology domain)*
*Researched: 2026-03-02*
