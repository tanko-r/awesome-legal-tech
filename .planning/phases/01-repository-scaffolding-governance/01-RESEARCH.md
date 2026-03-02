# Phase 1: Repository Scaffolding & Governance - Research

**Researched:** 2026-03-02
**Domain:** GitHub awesome-list repository structure, governance files, and sindresorhus/awesome standards
**Confidence:** HIGH

## Summary

Phase 1 creates a repository that conforms to the sindresorhus/awesome standard before any content is added. The awesome-list ecosystem has well-documented, strictly enforced requirements: specific files must exist in the repo root, the README must follow an exact structure, and the repository must pass `awesome-lint` with zero errors before being eligible for index submission. All of these requirements are verifiable against official sources (the sindresorhus/awesome repository and the awesome-lint tool).

The governance layer — CONTRIBUTING.md, code-of-conduct.md, license — exists both to satisfy awesome-lint rules and to establish the curation quality standards that prevent vendor capture and taxonomy churn. The project decision to "scaffold before content" is sound: awesome-lint failures on the README structure or missing files would cascade into every content phase if deferred.

GitHub repository topics (`awesome-list`, `awesome`) are required for index eligibility and are set through the GitHub UI or API — they cannot be set through repository files. The 30-day `git-repo-age` rule in awesome-lint means the Phase 1 commit that initializes the repository starts the clock for Phase 6 (index submission). This makes Phase 1 time-sensitive: it must be completed as early as possible to minimize the wait before Phase 6 can proceed.

**Primary recommendation:** Create all required files in a single initial commit following the exact awesome-list structure, run `npx awesome-lint` locally to confirm zero errors before committing, and immediately set repository topics after the repo is created on GitHub.

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|-----------------|
| REPO-01 | Repository has correct awesome-list file structure (README.md, CONTRIBUTING.md, license, code-of-conduct.md, .editorconfig, .gitattributes) | File inventory documented in Standard Stack section; exact content for each file provided in Code Examples |
| REPO-02 | License is CC0 1.0 Universal (no other license accepted by sindresorhus/awesome) | Verified: sindresorhus/awesome pull_request_template.md explicitly states CC0 or Creative Commons only; code licenses (MIT, BSD, GPL) are unacceptable |
| REPO-03 | README.md follows mandatory awesome-list structure (heading, Awesome badge, Contents section, category sections, entry format) | README structure fully documented; exact badge markdown, heading format, Contents placement, and entry format verified from official sources and live examples |
| REPO-04 | Every list entry uses the correct format: `[Name](URL) - Description.` (sentence case, ends with period) | Entry format verified from awesome-nodejs contributing.md and sindresorhus/awesome awesome.md: `- [Name](url) - Description.` uppercase first letter, period end |
| REPO-05 | GitHub repository topics include `awesome-list` and `awesome` for discoverability | Verified as explicit requirement in sindresorhus/awesome pull_request_template.md; set via GitHub UI "Manage topics" on repo settings page |
| REPO-06 | CONTRIBUTING.md defines inclusion criteria, entry format, and conflict-of-interest disclosure requirements | CONTRIBUTING.md content requirements documented; conflict-of-interest disclosure language patterns from ecosystem examples included |
</phase_requirements>

## Standard Stack

### Core Files Required

| File | Required By | Purpose | Notes |
|------|-------------|---------|-------|
| `readme.md` | awesome-lint | Main list document | Lowercase `readme.md` is Sindre's convention; awesome-lint accepts `README.md` too |
| `license` | awesome-lint + sindresorhus/awesome | Legal terms | Must be CC0 or Creative Commons; named `license` (no extension) per Sindre's convention |
| `contributing.md` | sindresorhus/awesome pull_request_template | Contribution guidelines | Must define inclusion criteria and entry format |
| `code-of-conduct.md` | sindresorhus/awesome convention | Community standards | Contributor Covenant v2.1 is standard |
| `.editorconfig` | sindresorhus convention | Consistent editor settings | Verified content from sindresorhus/awesome repo |
| `.gitattributes` | sindresorhus convention | Consistent line endings | Single-line `* text=auto eol=lf` |

### Supporting

| Tool | Version | Purpose | When to Use |
|------|---------|---------|-------------|
| awesome-lint | latest (npm) | Validate awesome-list rules | Before every commit and in CI (Phase 2); run locally in Phase 1 to validate scaffold |
| Contributor Covenant | v2.1 | Code of conduct template | Source for code-of-conduct.md content |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| CC0 license | MIT or Apache | MIT/Apache are explicitly rejected by sindresorhus/awesome; CC0 is required for index eligibility |
| Contributor Covenant | Custom CoC | Contributor Covenant is the ecosystem standard; a custom CoC adds no value and must still meet the same behavioral norms |
| `license` (no extension) | `LICENSE.md` | Both are accepted; sindresorhus uses no-extension convention; GitHub recognizes both |

**Installation (for local validation only — CI comes in Phase 2):**
```bash
npm install -g awesome-lint
# or run without installing:
npx awesome-lint
```

## Architecture Patterns

### Recommended Repository Structure

```
awesome-legal-apps/
├── readme.md             # Main list — the canonical file
├── license               # CC0 1.0 (no file extension)
├── contributing.md       # Inclusion criteria, entry format, CoI disclosure
├── code-of-conduct.md    # Contributor Covenant v2.1
├── .editorconfig         # Editor consistency settings
└── .gitattributes        # Git line-ending normalization
```

Note: `.github/` directory (for workflows and PR templates) is Phase 2. This phase creates only the governance files.

### Pattern 1: README Structure

**What:** The README must follow a specific layout that awesome-lint enforces. The heading, badge, description, and Contents section ordering is not negotiable.

**When to use:** Every awesome list README.

**Exact structure:**

```markdown
# Awesome Legal Apps

> A curated list of awesome legal technology tools, AI models, research resources, and
> open source projects for legal professionals and technologists.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Contents

- [AI Tools](#ai-tools)
- [Legal Research](#legal-research)
- [Contract Management](#contract-management)
- [Practice Management](#practice-management)
- [Document Management](#document-management)
- [Open Source Legal Tools](#open-source-legal-tools)
- [Access to Justice](#access-to-justice)
- [Legal NLP & Datasets](#legal-nlp--datasets)
- [Legal Education & Communities](#legal-education--communities)
- [Meta-Lists](#meta-lists)
- [Contributing](#contributing)

## AI Tools

- [Name](URL) - Description in sentence case ending with a period.

## Contributing

Contributions welcome! Read the [contribution guidelines](contributing.md) first.
```

**Badge variants (both are valid):**
- `[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)` — standard
- `[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)` — flat style

**Badge placement note:** awesome-lint requires the badge to appear after the main `#` heading. The `<img align="right">` approach (mentioned in PR template) can conflict with awesome-lint's `awesome-badge` rule. Use the simpler markdown badge on its own line after the heading description.

### Pattern 2: Entry Format

**What:** Every list entry follows one exact format. awesome-lint enforces this.

**Format:** `- [Name](url) - Description.`

**Rules (verified from sindresorhus/awesome and awesome-nodejs contributing.md):**
- Dash-space before `[`
- Name in title case
- URL links to the tool/project directly
- ` - ` separator (space-dash-space)
- Description in sentence case (only first word capitalized unless proper noun)
- Description ends with a period
- Do not start description with "A" or "An" (recommended, not always enforced by lint)
- Description should be factual, not marketing copy

**Examples:**
```markdown
- [Clio](https://www.clio.com) - Cloud-based legal practice management software for law firms.
- [Docassemble](https://docassemble.org) - Open-source guided interview and document assembly platform for legal aid.
- [CourtListener](https://www.courtlistener.com) - Free legal research tool with millions of US court opinions and oral arguments.
```

### Pattern 3: Contents Section

**What:** The table of contents section must be named "Contents" (not "Table of Contents") and must be the first section after the heading/description/badge.

**Rules:**
- Section heading: `## Contents`
- Links use lowercase slugs matching section headings: `[AI Tools](#ai-tools)`
- Special characters in headings are dropped in anchors: `Legal NLP & Datasets` → `#legal-nlp--datasets`
- "Contributing" can be listed at the bottom of Contents or omitted from Contents (awesome-lint allows footnote-style sections)

### Pattern 4: CC0 License

**What:** The CC0 1.0 Universal public domain dedication. No other license is acceptable for sindresorhus/awesome index inclusion.

**Source:** https://creativecommons.org/publicdomain/zero/1.0/legalcode

**The license file should contain the CC0 legal text.** GitHub provides a shortcut to generate it at `https://github.com/<user>/<repo>/community/license/new?branch=main&template=cc0-1.0`.

### Anti-Patterns to Avoid

- **Putting the license text in README:** Don't add a "License" section to readme.md. GitHub shows the license at the top of the repo automatically. Adding it to the README is redundant and clutters the document.
- **Adding CI badges to README:** awesome-lint rule `no-ci-badges` — do not add GitHub Actions status badges or similar CI badges to the README.
- **Adding "Inspired by" links:** awesome-lint flags these. The Awesome badge is sufficient attribution.
- **Hard-wrapping markdown:** Use soft-wrap (no manual line breaks at 80 chars). awesome-lint will flag hard-wrapped lines.
- **Trailing slashes on URLs:** awesome-lint flags `https://example.com/` — should be `https://example.com`.
- **Using master as default branch:** The default branch must be named `main`. This is verified by awesome-lint.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| License text | Writing CC0 summary or custom license | Copy CC0 1.0 legal text verbatim | Any modification voids CC0; sindresorhus/awesome requires unmodified CC0 |
| Code of conduct | Custom behavioral rules | Contributor Covenant v2.1 verbatim | Ecosystem standard; maintainers and contributors recognize it immediately |
| README validation | Manual checklist review | `npx awesome-lint` | Catches >15 specific rules including badge placement, entry format, TOC naming, repo age |
| Entry format enforcement | Documentation only | awesome-lint + PR template checklist | Humans skip manual checklists; lint catches format violations on every PR |

**Key insight:** For awesome lists, the "don't hand-roll" principle is about governance documents: use the canonical templates verbatim rather than writing custom versions. The ecosystem has established conventions that contributors and reviewers expect. Deviating from them creates confusion and may fail awesome-lint.

## Common Pitfalls

### Pitfall 1: Badge Placement Conflict

**What goes wrong:** Following the PR template advice to "place badge on the right side of the heading" using HTML `<img align="right">`, then failing awesome-lint's `awesome-badge` rule which expects the badge immediately after the `#` heading.

**Why it happens:** The official PR template and the linter have slightly conflicting guidance. The linter is the ground truth.

**How to avoid:** Place the Awesome badge as standard markdown on a line after the heading description block (not inline in the `#` heading line, not in an HTML `align="right"` tag). The pattern from `awesome-whisper` (placing badge inside a `<div align="center">` block) works but adds complexity. For a new list, the simple approach is:
```markdown
# Awesome Legal Apps

> Description here.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Contents
```

**Warning signs:** `awesome-lint` error: `Missing Awesome badge after the main heading remark-lint:awesome-badge`

### Pitfall 2: git-repo-age Rule Fails in CI

**What goes wrong:** awesome-lint's `awesome-git-repo-age` rule fails in GitHub Actions because Actions uses `--depth 1` shallow clone by default, which hides the repository's first commit date.

**Why it happens:** The rule checks the timestamp of the root commit. Shallow clones don't include it.

**How to avoid:** Use `fetch-depth: 0` in the GitHub Actions `actions/checkout` step (this is a Phase 2 concern for CI setup, but the Phase 1 repo structure must use `main` as the branch name, which the rule also checks).

**Warning signs:** `awesome-lint` CI error: `Git repository must be at least 30 days old remark-lint:awesome-git-repo-age`

Note: This rule will ALSO fail for the first 30 days regardless of fetch-depth. This is expected behavior — it will pass automatically after 30 days. **Do not suppress this rule.** It is a Phase 6 gate requirement.

### Pitfall 3: Repository Named Incorrectly

**What goes wrong:** Using uppercase, spaces, or a non-`awesome-` prefix in the repository slug.

**Why it happens:** Oversight during repo creation.

**How to avoid:** Repository must be named `awesome-legal-apps` (all lowercase, hyphenated). This is already the working directory name — confirm it matches the GitHub repo name exactly.

### Pitfall 4: CONTRIBUTING.md Missing Inclusion Criteria

**What goes wrong:** CONTRIBUTING.md only defines entry format but omits specific inclusion criteria, leaving the list vulnerable to vendor spam and scope drift.

**Why it happens:** Contributors add files hastily and forget that CONTRIBUTING.md is a governance document, not just a formatting guide.

**How to avoid:** CONTRIBUTING.md must explicitly state:
1. What qualifies a tool for inclusion (active, maintained, legal-domain specific)
2. What disqualifies a tool (abandonware, general productivity, no legal use case)
3. The conflict-of-interest disclosure requirement
4. The entry format (with example)

### Pitfall 5: CC0 License Applied Incorrectly

**What goes wrong:** Using a `LICENSE.md` with a CC0 summary, or placing the license name in README.md.

**Why it happens:** Copying patterns from MIT-licensed repos without understanding CC0-specific requirements.

**How to avoid:** Create a file named `license` (no extension) with the full CC0 1.0 legal text. Do not add a license section to README.md. GitHub auto-detects it and shows the license badge.

### Pitfall 6: GitHub Topics Not Set

**What goes wrong:** Repository files are perfect but the `awesome-list` and `awesome` topics are not set on the GitHub repo settings, causing awesome-lint's topic check to fail when the repo URL is linted.

**Why it happens:** Topics are set via the GitHub UI, not via repository files — easy to overlook.

**How to avoid:** Immediately after pushing the initial scaffold to GitHub, navigate to the repo's main page, click the gear icon next to "About," and add `awesome-list` and `awesome` as topics. Also add `legal-tech`, `legaltech`, `legal-ai` for discoverability.

## Code Examples

Verified patterns from official sources:

### .editorconfig (from sindresorhus/awesome)

```ini
# Source: https://github.com/sindresorhus/awesome/blob/main/.editorconfig
root = true

[*]
indent_style = tab
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
```

### .gitattributes (from sindresorhus/awesome-whisper)

```gitattributes
# Source: https://github.com/sindresorhus/awesome-whisper/blob/main/.gitattributes
* text=auto eol=lf
```

### README.md Minimal Valid Structure

```markdown
# Awesome Legal Apps

> A curated list of awesome legal technology tools, apps, AI systems, open source
> projects, and resources for legal professionals, technologists, and researchers.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Contents

- [AI Tools](#ai-tools)
- [Legal Research](#legal-research)
- [Contributing](#contributing)

## AI Tools

- [Example Tool](https://example.com) - Brief factual description in sentence case ending with a period.

## Legal Research

- [Example Resource](https://example.com) - Brief factual description in sentence case ending with a period.

## Contributing

Contributions welcome! Read the [contribution guidelines](contributing.md) first.
```

### CONTRIBUTING.md Structure Pattern

```markdown
# Contribution Guidelines

Please note that this project is released with a [Contributor Code of Conduct](code-of-conduct.md).
By participating in this project you agree to abide by its terms.

## Inclusion Criteria

A tool or resource may be added to Awesome Legal Apps if it:

- Is specifically useful for legal professionals, legal technologists, or legal researchers
- Is actively maintained (last commit or update within 18 months, or clearly stable/complete)
- Has documentation sufficient for evaluation
- Is not abandonware, deprecated, or archived

A tool will NOT be added if it:

- Is a general productivity tool with no specific legal use case
- Is unmaintained or archived
- Is marketing copy for a service with no evaluable product

## Entry Format

Entries must follow this exact format:

```
- [Tool Name](https://url.com) - One-sentence description in sentence case, ending with a period.
```

## Conflict of Interest Disclosure

If you are the creator, maintainer, or employee of a company behind a tool you are
submitting, you must disclose this in your pull request. Self-submissions are allowed
but subject to stricter review. Add a note like:

> Disclosure: I am the creator of [Tool Name].

Undisclosed conflicts of interest are grounds for immediate rejection.

## Submission Process

1. Search existing entries to avoid duplicates.
2. Add your entry at the bottom of the appropriate section.
3. Submit a pull request with the title `Add [Tool Name]`.
4. Verify the entry passes `npx awesome-lint` before submitting.
```

### Running awesome-lint Locally

```bash
# Validate the current directory (must be in repo root, must have git initialized)
npx awesome-lint

# Validate a specific file
npx awesome-lint readme.md

# Validate by GitHub URL (requires fetch-depth: 0 for git-repo-age)
npx awesome-lint https://github.com/user/awesome-legal-apps
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| `LICENSE.md` file | `license` (no extension) | Sindre's convention; not strictly versioned | GitHub recognizes both; convention is no-extension |
| `master` default branch | `main` default branch | GitHub default changed ~2020; awesome-lint enforces it | awesome-lint will flag `master` branch; must use `main` |
| CI badges in README | No CI badges in README | awesome-lint rule `no-ci-badges` | Removing CI badges is required, not optional |
| Optional code-of-conduct | code-of-conduct.md expected | Community norms ~2018+; Contributor Covenant popularized it | Most reviewers expect it; reference ecosystem lists include it |

**Deprecated/outdated:**
- `TABLE OF CONTENTS` section name: Replaced by `Contents` (exact string). awesome-lint validates this.
- `Inspired by` links: Explicitly prohibited by sindresorhus/awesome guidelines; remove if present.

## Open Questions

1. **Exact awesome-lint version pinning for Phase 2 CI**
   - What we know: awesome-lint is available on npm; `npx awesome-lint` uses latest
   - What's unclear: Whether to pin to a specific version in the CI workflow
   - Recommendation: Use unpinned `npx awesome-lint` for Phase 1 local validation; pin version in Phase 2 when CI workflow is created

2. **Logo/illustration requirement**
   - What we know: sindresorhus/awesome pull_request_template.md says "Include a project logo/illustration... Only high-DPI images"
   - What's unclear: Whether absence of a logo causes awesome-lint failure or is just a soft recommendation
   - Recommendation: Treat as optional for Phase 1 scaffold; add before Phase 6 submission if awesome-lint does not flag it. Research confirms awesome-lint does not have an automated logo-presence rule.

3. **`contributing.md` vs `CONTRIBUTING.md` casing**
   - What we know: sindresorhus uses lowercase; GitHub recognizes both; awesome-lint accepts both
   - What's unclear: Whether awesome-lint enforces lowercase specifically
   - Recommendation: Use lowercase `contributing.md` to match sindresorhus convention. Same for `code-of-conduct.md`, `license`, `readme.md`.

## Sources

### Primary (HIGH confidence)

- https://raw.githubusercontent.com/sindresorhus/awesome/main/pull_request_template.md — Full checklist of awesome list requirements, including license, badge, topics, entry format, branch name
- https://raw.githubusercontent.com/sindresorhus/awesome/main/awesome.md — Awesome manifesto; badge requirements, entry format, README structure
- https://github.com/sindresorhus/awesome-lint — awesome-lint tool; rules list including `awesome-badge`, `awesome-git-repo-age`, `awesome-toc`, `awesome-list-item`
- https://github.com/sindresorhus/awesome/blob/main/.editorconfig — Exact .editorconfig content verified
- https://github.com/sindresorhus/awesome-whisper/blob/main/.gitattributes — Exact .gitattributes content verified
- https://raw.githubusercontent.com/sindresorhus/awesome-nodejs/main/readme.md — Live example of README structure, badge placement, entry format, contributing.md reference
- https://raw.githubusercontent.com/sindresorhus/awesome-nodejs/main/contributing.md — Detailed inclusion criteria and entry format requirements from canonical Sindre list

### Secondary (MEDIUM confidence)

- https://github.com/officeanddragons/awesome-lawtech — Existing legal tech awesome list; file structure and badge format observed
- https://github.com/lawvable/awesome-legal-skills — Existing legal skills list; file inventory observed
- https://contributor-covenant.org/version/2/1/ — Contributor Covenant v2.1 text for code-of-conduct.md
- https://github.com/sindresorhus/awesome/issues/2097 — Badge placement vs. awesome-lint conflict documented; resolution guidance

### Tertiary (LOW confidence)

- General WebSearch results on awesome-lint rules and git-repo-age behavior — cross-referenced with official repo but individual rule behavior not independently verified via Context7

## Metadata

**Confidence breakdown:**
- Standard stack (required files): HIGH — verified directly from sindresorhus/awesome pull_request_template.md and live example repositories
- Architecture (README structure, entry format): HIGH — verified from multiple official Sindre repositories and awesome-lint documentation
- Pitfalls (badge conflict, git-repo-age, topics): MEDIUM-HIGH — badge conflict verified from GitHub issue; git-repo-age solution verified from awesome-lint README; topics requirement verified from PR template
- CONTRIBUTING.md conflict-of-interest pattern: MEDIUM — derived from ecosystem examples (github/explore CONTRIBUTING.md) and awesome-nodejs CONTRIBUTING.md; no single canonical template exists

**Research date:** 2026-03-02
**Valid until:** 2026-06-01 (stable domain — awesome-list standard changes infrequently; sindresorhus/awesome conventions are stable year-over-year)
