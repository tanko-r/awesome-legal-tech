# Architecture Research

**Domain:** GitHub awesome-list (curated resource directory)
**Researched:** 2026-03-02
**Confidence:** HIGH — Based on direct inspection of sindresorhus/awesome pull request template, awesome-lint rules directory, and multiple exemplary repositories.

## Standard Architecture

### System Overview

An awesome list is not a software application — it is a structured Markdown repository with a well-defined file layout, enforced by linting tooling and GitHub automation. The "architecture" is the repository itself: its file structure, CI pipeline, and governance model.

```
┌──────────────────────────────────────────────────────────────────┐
│                     Repository Root                               │
│                                                                   │
│  README.md          ← Canonical list (primary artifact)          │
│  CONTRIBUTING.md    ← Submission rules and quality criteria       │
│  license            ← CC0 (required; no extension)               │
│  .lycheeignore      ← URLs excluded from link checking           │
│                                                                   │
├──────────────────────────────────────────────────────────────────┤
│                     .github/ Directory                            │
│                                                                   │
│  .github/                                                         │
│  ├── workflows/                                                   │
│  │   ├── lint.yml           ← awesome-lint on every PR           │
│  │   └── links.yml          ← lychee link checker (scheduled)    │
│  ├── ISSUE_TEMPLATE/                                              │
│  │   └── add-resource.yml   ← Structured form for new entries    │
│  └── pull_request_template.md ← PR checklist for contributors    │
│                                                                   │
├──────────────────────────────────────────────────────────────────┤
│                     Optional Assets                               │
│                                                                   │
│  assets/ or media/   ← Logo, header image (high-DPI)            │
│  footnotes.md        ← Non-critical content, acknowledgements    │
└──────────────────────────────────────────────────────────────────┘
```

### Component Responsibilities

| Component | Responsibility | Typical Implementation |
|-----------|----------------|------------------------|
| `README.md` | Canonical list — the entire product | Structured Markdown with ToC, categorized entries, descriptions, Awesome badge |
| `CONTRIBUTING.md` | Defines what belongs and submission process | Quality criteria, formatting rules, PR instructions |
| `license` | Legal terms for reuse | CC0 1.0 Universal (no extension in filename) |
| `.github/workflows/lint.yml` | Enforces formatting on every PR | `npx awesome-lint` via GitHub Actions |
| `.github/workflows/links.yml` | Detects link rot on a schedule | lychee-action with weekly/daily cron |
| `.github/ISSUE_TEMPLATE/` | Structures contribution submissions | YAML form with required fields |
| `.github/pull_request_template.md` | Checklist to verify submission quality | Checkboxes contributors must confirm |
| `.lycheeignore` | Suppresses false-positive link failures | One URL or regex pattern per line |
| `assets/` | Header image / logo | PNG at 2x resolution for retina displays |

## Recommended Project Structure

```
awesome-legal-apps/
├── README.md                        # The list itself — single canonical artifact
├── CONTRIBUTING.md                  # Submission process and quality criteria
├── license                          # CC0 (no extension — sindresorhus convention)
├── .lycheeignore                    # URLs to skip during link checking
│
├── assets/
│   └── header.png                   # High-DPI logo/header image (optional)
│
└── .github/
    ├── workflows/
    │   ├── lint.yml                 # awesome-lint — runs on every PR
    │   └── links.yml                # lychee — runs on schedule (weekly)
    ├── ISSUE_TEMPLATE/
    │   └── add-resource.yml         # Structured form for new resource submissions
    └── pull_request_template.md     # Checklist contributors must complete
```

### Structure Rationale

- **README.md at root:** The sindresorhus/awesome standard requires the list to live in README.md at the repository root. Entries in the main awesome index are formatted as `[Name](https://github.com/user/repo#readme)` — anchoring to `#readme` only works when README.md is the canonical file. Do not split the list into multiple files for the main index-eligible version.
- **`license` (no extension):** The sindresorhus convention is a file named `license` with no extension. Using `LICENSE.md` or `LICENSE.txt` triggers an awesome-lint warning.
- **`.github/` directory:** All automation lives here — GitHub natively recognizes PR templates, issue templates, and workflow files in this location.
- **`assets/` for imagery:** Keeps the root clean. GitHub renders images in README.md from relative paths, so `assets/header.png` works without any special configuration.
- **No `docs/` folder:** The list is a single README. A docs folder with sub-pages is appropriate only for large lists that outgrow a single file (see Scalability section below).

## README.md Internal Architecture

The README.md itself has a required internal structure enforced by awesome-lint:

```
# Awesome Legal Apps                      ← Title-case heading (rule: heading.js)

[Awesome badge]                           ← Required badge (rule: badge.js)
[Optional header image]

> One-line description of what the list covers.

## Contents                               ← Must be named "Contents" (rule: toc.js)

- [Category A](#category-a)
- [Category B](#category-b)
- [Contributing](#contributing)

## Category A

- [Tool Name](https://example.com) - Description starting with uppercase, ending with period.

## Category B

- [Tool Name](https://example.com) - Description starting with uppercase, ending with period.

## Contributing                           ← Link to CONTRIBUTING.md

## Footnotes                              ← Non-critical content (acknowledgements, etc.)
```

Key README rules (enforced by awesome-lint):
- Heading must be `# Awesome [Name]` in title case
- Awesome badge must appear immediately after the main heading
- First section must be `## Contents` (not "Table of Contents")
- Contents section should have one level of nesting, preferably none
- Every list item must have a description
- Descriptions start with uppercase letter and end with a period
- No trailing slashes on URLs
- No hard line wraps — use soft wrapping
- No CI badge (GitHub Actions badge) in the README

## Architectural Patterns

### Pattern 1: Single-File List with Anchor Navigation

**What:** The entire list lives in README.md. Categories are H2 (`##`) headings. The Contents section links to each heading anchor.
**When to use:** Always — for all lists eligible for the main awesome index. Avoids multi-file complexity at the cost of very long README for large lists.
**Trade-offs:** Pros — simple, searchable by GitHub's built-in search, works with `#readme` anchor in awesome index. Cons — becomes hard to navigate past ~200 entries.

**Example README entry format:**
```markdown
## AI and Legal Research

- [Casetext](https://casetext.com) - AI-powered legal research platform with case law, statutes, and regulations.
- [Lexis+ AI](https://www.lexisnexis.com/en-us/products/lexis-plus-ai.page) - Generative AI legal assistant integrated with LexisNexis research database.
```

### Pattern 2: Sub-Page Architecture (for large lists)

**What:** README.md serves as a navigation hub. Category content lives in dedicated Markdown files in subdirectories.
**When to use:** Only when the list exceeds ~300 entries and single-file navigation becomes unwieldy. Note: sub-page lists cannot be submitted to the main sindresorhus/awesome index in this form — the index requires a single README.md.
**Trade-offs:** Pros — better navigation for very large lists. Cons — breaks awesome-lint compliance for main index; requires more maintenance overhead.

**Example structure:**
```
README.md               ← Navigation hub linking to sub-pages
categories/
├── ai-research.md
├── practice-management.md
└── document-automation.md
```

### Pattern 3: Category-First Taxonomy

**What:** Organize entries by use case / workflow stage rather than by tool type or vendor. Users browse by "what they're trying to accomplish," not "what kind of tool it is."
**When to use:** Legal tech specifically — attorneys think in terms of tasks (research, drafting, review) not technology categories (AI, SaaS, API).
**Trade-offs:** Pros — highly intuitive for target audience. Cons — some tools fit multiple categories; requires clear placement rules in CONTRIBUTING.md.

## Automation Architecture

### Workflow 1: Lint on Pull Request (`lint.yml`)

Runs awesome-lint against every PR targeting `main`. Blocks merge if lint fails. This is the primary quality gate.

```yaml
name: Lint

on:
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0          # Required: awesome-lint checks repo age
      - run: npx awesome-lint
```

**What awesome-lint checks (15 rules):**
- `badge.js` — Awesome badge present after main heading
- `toc.js` — Contents section exists and is correct format
- `heading.js` — Title format is `# Awesome [Name]`
- `list-item.js` — Entries have descriptions, correct punctuation
- `license.js` — `license` file present
- `contributing.js` — `CONTRIBUTING.md` file present
- `double-link.js` — No duplicate URLs
- `no-ci-badge.js` — No GitHub Actions badges in README
- `spell-check.js` — Basic spell checking
- `git-repo-age.js` — Repository is at least 30 days old
- `balanced-punctuation.js` — Punctuation consistency
- `no-repeat-item-in-description.js` — No redundant descriptions
- `github.js` — GitHub-specific validations
- `code-of-conduct.js` — Optional code of conduct validation

### Workflow 2: Link Checker (`links.yml`)

Runs lychee on a weekly schedule to detect link rot. Creates a GitHub Issue automatically when broken links are found.

```yaml
name: Links

on:
  schedule:
    - cron: "0 9 * * 1"          # Every Monday at 9 AM UTC
  workflow_dispatch:               # Allow manual triggering

jobs:
  linkChecker:
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      - uses: actions/checkout@v4

      - name: Link Checker
        id: lychee
        uses: lycheeverse/lychee-action@v2
        with:
          fail: false              # Don't fail the job; open issue instead

      - name: Create Issue From File
        if: steps.lychee.outputs.exit_code != 0
        uses: peter-evans/create-issue-from-file@v5
        with:
          title: Link Checker Report
          content-filepath: ./lychee/out.md
          labels: report, automated issue
```

The `.lycheeignore` file suppresses known false positives (paywalled sites, sites that block bots):

```
# Sites that block automated requests but are legitimate
https://www.westlaw.com
https://www.lexisnexis.com
# Pattern matching
https://app\..+\.com
```

## Governance Model

### Contribution Flow

```
Contributor opens PR
        |
        v
PR template checklist completed?
        |
  NO -> Request changes
        |
  YES ->
        v
GitHub Actions: awesome-lint runs
        |
  FAIL -> Block merge, notify contributor
        |
  PASS ->
        v
Maintainer reviews:
  - Is resource maintained and working?
  - Does it serve the legal domain specifically?
  - Is the category placement correct?
  - Is the description accurate and useful?
        |
  NO -> Request changes or close
        |
  YES -> Merge
```

### Quality Criteria (encode in CONTRIBUTING.md)

Every entry must pass ALL of:
1. **Active** — Resource is currently maintained, not archived or abandoned
2. **Accessible** — Link works and is freely accessible (or clearly labeled if paywalled)
3. **Legal domain** — Serves a legal use case specifically; general productivity tools excluded
4. **Described** — Entry has a clear description (uppercase start, period end)
5. **Categorized** — Placed in the most appropriate existing category, or new category justified
6. **Non-duplicate** — Not already listed, even under a different name
7. **Not promotional** — Maintainer does not have undisclosed commercial interest in entry

### Issue Templates

Create `.github/ISSUE_TEMPLATE/add-resource.yml` with structured fields:

```yaml
name: Add Resource
description: Suggest a new resource for the list
labels: ["addition"]
body:
  - type: input
    id: name
    attributes:
      label: Resource name
      placeholder: e.g., Casetext
    validations:
      required: true
  - type: input
    id: url
    attributes:
      label: URL
      placeholder: https://
    validations:
      required: true
  - type: input
    id: description
    attributes:
      label: Description
      description: One sentence. Start with uppercase, end with period.
    validations:
      required: true
  - type: dropdown
    id: category
    attributes:
      label: Category
      options:
        - AI and Legal Research
        - Document Automation and Drafting
        - Practice Management
        - Contract Analysis and Review
        - Legal Data and Datasets
        - Education and Training
        - Meta-Lists and Directories
    validations:
      required: true
  - type: checkboxes
    id: checklist
    attributes:
      label: Quality checklist
      options:
        - label: Resource is actively maintained (not abandoned)
          required: true
        - label: Link is publicly accessible
          required: true
        - label: Serves a legal use case specifically
          required: true
        - label: Not already listed in the repository
          required: true
```

### Labels to Create

| Label | Color | Purpose |
|-------|-------|---------|
| `addition` | `#0075ca` | New resource suggestion |
| `removal` | `#e4e669` | Link rot or defunct resource |
| `recategorize` | `#d93f0b` | Category placement discussion |
| `automated issue` | `#cccccc` | Created by link checker workflow |
| `report` | `#cccccc` | Automated reports |
| `good first issue` | `#7057ff` | Easy first contribution |

## Data Flow

### Contribution Flow

```
New Resource Discovery
        |
        v
Contributor: Fork → Edit README.md → Open PR
        |
        v
Automated Gate: awesome-lint validates format
        |
        v
Human Gate: Maintainer validates quality, scope, accuracy
        |
        v
Merge to main → Resource live in list
        |
        v
Weekly: lychee checks all URLs → broken links flagged as issues
        |
        v
Maintainer or contributor: fixes or removes dead entries
```

### Maintenance Cycle

```
Weekly automated link check
        |
  Broken? → Issue opened → Maintainer or contributor PR to fix
  Clean?  → No action required
```

## Scalability Considerations

| Scale | Architecture Adjustments |
|-------|--------------------------|
| 0-100 entries | Single README.md — standard pattern, no changes needed |
| 100-300 entries | Add ToC anchors; consider splitting into sub-categories using H3 headings within H2 category sections |
| 300-500 entries | Still manageable in single README.md; keep categories tight to prevent sprawl |
| 500+ entries | Consider sub-page architecture with README.md as navigation hub — accept that this breaks main awesome-index eligibility unless a single-file version is maintained |

### Scaling Priorities

1. **First bottleneck:** README.md becomes unwieldy to navigate. Fix: tighten category count (aim for 8-15 categories max), enforce stricter quality bar to reduce total entries.
2. **Second bottleneck:** Too many PRs to review manually. Fix: stricter issue template validation, branch protection requiring two reviewers, community moderation model with trusted contributors.

## Anti-Patterns

### Anti-Pattern 1: Link Dumping Without Descriptions

**What people do:** Add `- [Tool](https://url.com)` with no description.
**Why it's wrong:** Violates the awesome manifesto ("only put stuff you can personally recommend"), fails awesome-lint `list-item.js` rule, and gives readers no context.
**Do this instead:** Every entry must have `- [Tool](https://url.com) - Description starting with uppercase, ending with period.`

### Anti-Pattern 2: Using LICENSE.md Instead of `license`

**What people do:** Create a `LICENSE.md` or `LICENSE` file with capitalization or extension.
**Why it's wrong:** awesome-lint's `license.js` rule checks specifically for a file named `license` (lowercase, no extension) — the sindresorhus convention. The wrong filename causes lint failure.
**Do this instead:** Create the file as `license` with no extension. Use CC0 1.0 Universal.

### Anti-Pattern 3: CI Badge in README

**What people do:** Add a GitHub Actions workflow status badge to the README (e.g., the green "Lint passing" badge).
**Why it's wrong:** awesome-lint's `no-ci-badge.js` rule explicitly prohibits CI badges. The awesome index maintainers want lists to look clean, not like software projects.
**Do this instead:** Remove all workflow status badges. The lint workflow still runs — it just isn't advertised via badge.

### Anti-Pattern 4: Naming the ToC "Table of Contents"

**What people do:** Use `## Table of Contents` as the section heading.
**Why it's wrong:** awesome-lint's `toc.js` rule requires the section be named exactly `## Contents`.
**Do this instead:** Use `## Contents` as the first section heading.

### Anti-Pattern 5: Submitting Before 30 Days

**What people do:** Create a new list and immediately try to submit it to the main sindresorhus/awesome index.
**Why it's wrong:** The pull request template requires the list to have existed for at least 30 days. awesome-lint's `git-repo-age.js` rule enforces this automatically.
**Do this instead:** Launch the repo, build it out for at least 30 days, then submit. Use the 30-day period to establish quality and gather initial stars.

### Anti-Pattern 6: Nesting in Contents Section

**What people do:** Create multi-level nested ToC like:
```markdown
## Contents
- [Category A](#category-a)
  - [Sub A1](#sub-a1)
  - [Sub A2](#sub-a2)
```
**Why it's wrong:** The awesome standard specifies Contents should have "only one level of nested lists, preferably none." Deep nesting makes the ToC harder to scan.
**Do this instead:** Keep all ToC entries at one level. Use H3 headings for sub-categories within the README body, but don't mirror nesting in the ToC.

## Integration Points

### External Services

| Service | Integration Pattern | Notes |
|---------|---------------------|-------|
| GitHub Actions | YAML workflows in `.github/workflows/` | Lint and link checking; free for public repos |
| shields.io | Badge URL in README.md | Awesome badge only — no status badges |
| lychee-action | GitHub Marketplace action | Best-in-class link checker; Rust-based, fast |
| awesome-lint (npm) | `npx awesome-lint` in workflow | sindresorhus official linter; run with `fetch-depth: 0` |
| peter-evans/create-issue-from-file | GitHub Marketplace action | Auto-creates issues from lychee output |

### Internal Boundaries

| Boundary | Communication | Notes |
|----------|---------------|-------|
| Contributor ↔ README.md | Pull request | All content changes via PR; no direct push to main |
| Contributor ↔ Maintainer | PR review, issue comments | GitHub native review tools |
| Automation ↔ Repository | GitHub Actions triggers | PR triggers lint; cron triggers link check |
| Automation ↔ Issues | peter-evans/create-issue-from-file | Broken links become trackable issues |

## Build Order

Phase dependencies for building this list:

1. **Foundation first** (Day 1): Create `README.md` with correct heading, Awesome badge, `## Contents`, and at least 20 high-quality entries. Create `license` (CC0). Create `CONTRIBUTING.md`.
2. **Automation second** (Day 1-2): Set up `.github/workflows/lint.yml` and run awesome-lint locally to fix all issues before enabling CI.
3. **Link hygiene third** (Day 2-3): Add `.lycheeignore` and `.github/workflows/links.yml`. Verify lychee passes on initial entry set.
4. **Governance fourth** (Day 3-5): Add PR template, issue template, and repository labels. Set branch protection rule requiring lint to pass.
5. **Content build** (Days 5-30): Add entries across all planned categories. Maintain quality bar.
6. **Index submission** (Day 30+): Submit to sindresorhus/awesome after 30-day maturation period.

## Sources

- sindresorhus/awesome pull request template (authoritative submission requirements): https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md — CONFIDENCE: HIGH
- awesome-lint rules directory (15 specific rules): https://github.com/sindresorhus/awesome-lint/tree/main/rules — CONFIDENCE: HIGH
- The Awesome Manifesto (principles): https://github.com/sindresorhus/awesome/blob/main/awesome.md — CONFIDENCE: HIGH
- DEV article on awesome-lint CI integration (lint.yml configuration): https://dev.to/airscript/linting-your-awesome-lists-bai — CONFIDENCE: MEDIUM
- lychee-action documentation (link checker workflow): https://github.com/lycheeverse/lychee-action — CONFIDENCE: HIGH
- awesome-lawtech structure (legal list example): https://github.com/officeanddragons/awesome-lawtech — CONFIDENCE: MEDIUM
- awesome-legal-skills structure (legal list example): https://github.com/lawvable/awesome-legal-skills — CONFIDENCE: MEDIUM
- awesome-legal-nlp structure (legal list example): https://github.com/maastrichtlawtech/awesome-legal-nlp — CONFIDENCE: MEDIUM
- awesome-actions repository (exemplary non-legal awesome list): https://github.com/sdras/awesome-actions — CONFIDENCE: MEDIUM
- max/awesome-lint GitHub Action: https://github.com/max/awesome-lint — CONFIDENCE: MEDIUM

---
*Architecture research for: GitHub awesome-list (curated legal technology resource directory)*
*Researched: 2026-03-02*
