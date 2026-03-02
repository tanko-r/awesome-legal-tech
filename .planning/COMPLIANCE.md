# Phase 1 Compliance Baseline: awesome-lint Validation Rules

**Documented:** 2026-03-02
**Purpose:** Validation baseline for Phase 1 completion — what must be verified before the repository passes awesome-lint checks.
**Scope:** Lists all awesome-lint rules and exact requirements for CC0 1.0 Universal license format, badge formats, PR template requirements, and minimum README.md content structure.

---

## 1. awesome-lint: Complete Validation Rules

The `npx awesome-lint` tool enforces **28 validation rules** across two categories:

### 1.1 General Markdown Rules (remark-lint Base)

These are standard markdown formatting rules configured in the awesome-lint `config.js`:

| Rule | Purpose | Validation |
|------|---------|-----------|
| `blockquote-indentation` | Blockquote format | Must use 2-space indentation |
| `code-block-style` | Code block format | Must use fenced code blocks (```) not indented |
| `emphasis-marker` | Emphasis consistency | Use `*` or `_` consistently for italic, not mixed |
| `fenced-code-marker` | Code fence style | Use backticks (```) as code fence markers |
| `heading-style` | Heading format | Use ATX-style headings (#, ##, ###) not setext |
| `link-title-style` | Link title format | Use single quotes around link titles |
| `strong-marker` | Strong emphasis | Use `**` or `__` consistently for bold, not mixed |
| `rule-style` | Horizontal rules | Use dashes (---) for horizontal rules |
| `checkbox-character` | Checkbox content | Checkboxes must use proper X or lowercase x |
| `definition-case` | Definition terms | Definition terms must be lowercase |
| `definition-spacing` | Definition gaps | No blank lines between definitions |
| `final-newline` | File endings | File must end with a single newline character |
| `hard-break-spaces` | Line breaks | Use markdown line breaks, not double spaces |
| `list-item-bullet-indent` | List bullet indent | Bullet markers must have consistent indentation |
| `list-item-indent` | List item text | List item content must be indented one space after bullet |
| `no-blockquote-without-marker` | Blockquote syntax | All blockquote lines must have `>` marker |
| `no-emphasis-as-heading` | Heading style | Don't use emphasis markers (`*`, `_`, `**`) as headings |
| `no-heading-content-indent` | Heading content | No extra spaces between `#` and heading text |
| `no-heading-indent` | Heading indent | Headings must start at column 1 (no indentation) |
| `no-heading-punctuation` | Heading punctuation | Headings must not end with punctuation (. , ; : ! ?) |
| `no-multiple-top-level-headings` | Document structure | Only one top-level `#` heading per document |
| `no-shell-dollar-signs` | Shell code | Don't include `$` prompt in shell code blocks |
| `no-table-indentation` | Table indent | Tables must start at column 1 (no indentation) |
| `table-cell-padding` | Table spacing | Cells must have single space padding around pipes |
| `table-pipes` | Table format | Pipes must align vertically in tables |
| `unordered-list-marker` | List marker style | Must use `-` (dash) for unordered lists, not `*` or `+` |
| `no-repeat-punctuation` | Punctuation rules | Don't repeat punctuation (custom rule; exception: period allowed for ellipsis) |

**Total general rules: 26**

### 1.2 Awesome-Specific Custom Rules

These 15 rules are enforced **only** by awesome-lint and validate awesome-list-specific requirements:

| Rule | File | What It Validates | Failure Condition |
|------|------|-------------------|------------------|
| `awesome-badge` | badge.js | Awesome badge placement | Badge must appear after main `#` heading; no badge = failure |
| `awesome-balanced-punctuation` | balanced-punctuation.js | Punctuation balance in descriptions | Unmatched brackets, parens, quotes in list item descriptions |
| `awesome-code-of-conduct` | code-of-conduct.js | Code of Conduct presence | `code-of-conduct.md` file must exist in repo root |
| `awesome-contributing` | contributing.js | Contributing guidelines | `contributing.md` file must exist in repo root |
| `awesome-double-link` | double-link.js | No duplicate URLs | Same URL appearing in multiple list entries = failure |
| `awesome-git-repo-age` | git-repo-age.js | Repository maturity | Repo must be at least 30 days old (from first commit) |
| `awesome-github-topics` | github.js | GitHub repo metadata | Topics must include `awesome-list` and `awesome` (checked via GitHub API if URL provided) |
| `awesome-heading` | heading.js | README heading format | First heading must be `# Awesome [Name]` exactly; no subtitle in heading |
| `awesome-license` | license.js | License file presence | `license` file must exist in repo root (no extension) |
| `awesome-list-item` | list-item.js | List entry format validation | Entry must follow `- [Name](URL) - Description.` format exactly |
| `awesome-no-ci-badges` | no-ci-badge.js | CI badge prohibition | No GitHub Actions, Travis CI, or similar badges in README |
| `awesome-no-repeat-item-in-description` | no-repeat-item-in-description.js | Description redundancy | Description must not repeat the item name |
| `awesome-spell-check` | spell-check.js | Spelling errors | CommonWords dictionary; flags misspelled words in README |
| `awesome-toc` | toc.js | Table of Contents validation | Must have `## Contents` section with accurate anchor links matching headings |
| `awesome-main-branch` | (github.js) | Default branch name | Repository default branch must be `main`, not `master` |

**Total custom rules: 15**

**Grand Total: 41 validation rules** (26 general + 15 awesome-specific)

---

## 2. CC0 1.0 Universal License: Exact Format

The `license` file (no extension) in repo root must contain the **full, unmodified CC0 1.0 Universal legal text**. The license document has four distinct sections:

### 2.1 License Structure

**Section 1: Statement of Purpose**
- Explains why creators choose to relinquish copyright
- States "The person who associated a work with this deed has dedicated the work to the public domain"
- Defines scope: "copyright and related and neighboring rights"

**Section 2: Copyright and Related Rights**
- Lists specific rights being waived globally:
  - Right to reproduce
  - Right to adapt and modify
  - Right to distribute and make publicly available
  - Right to perform and display publicly
  - Right to communicate and translate
  - Moral rights
  - Privacy rights
  - Rights against unfair competition (where recognized)
  - Database rights
  - Any other rights of similar nature or analogous worldwide

**Section 3: Waiver**
- States: "The person affirms that they have, or the copyright and related or neighboring rights holder has expressly granted to them, the right to waive the Copyright and Related Rights"
- Explicitly states: Person "overtly, fully, permanently, irrevocably and unconditionally waives" all Copyright and Related Rights in the Work globally for any purpose
- Extends to successors and assigns

**Section 4: Limitations and Disclaimers**
- Clarifies that trademark and patent rights are **NOT** waived
- States Creative Commons provides no warranties
- Notes Creative Commons is not a party to the license
- Includes Public License Fallback: if waiver is deemed invalid, converts to a royalty-free, irrevocable, non-exclusive license

### 2.2 License File Format Requirements

**File naming:**
- Must be named `license` (lowercase, no file extension)
- Do NOT use `LICENSE.md`, `LICENSE.txt`, or `License` variants

**Content:**
- Must contain the full, verbatim CC0 1.0 Universal legal text
- No modifications, summaries, or paraphrasing allowed
- Cannot be shortened or edited
- GitHub auto-detects this file and displays license badge on repo main page

**Verification:**
- awesome-lint checks for `license` file presence (rule: `awesome-license`)
- sindresorhus/awesome PR checklist requires CC0 or Creative Commons license
- No code licenses (MIT, Apache, GPL, BSD) accepted for awesome-list index submission

**Obtain the full text from:**
https://creativecommons.org/publicdomain/zero/1.0/legalcode

---

## 3. Badge Formats Required by awesome-lint

The `awesome-badge` rule enforces specific badge markdown syntax. Only the official Awesome badge is allowed.

### 3.1 Valid Badge Formats

**Standard Badge (RECOMMENDED):**
```markdown
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
```

**Flat Style Badge (ALTERNATIVE):**
```markdown
[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)
```

**Flat2 Style Badge (ALTERNATIVE):**
```markdown
[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
```

### 3.2 Badge Placement Rules

**REQUIRED placement:**
- Badge must appear **immediately after** the main `#` heading
- Badge must be on its own line in markdown (not inline in the heading)
- Badge must come **before** the description blockquote or before the `## Contents` section

**CORRECT example:**
```markdown
# Awesome Legal Apps

> A curated list of legal technology tools.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Contents
```

**INCORRECT examples:**
```markdown
# Awesome Legal Apps [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
# Cannot inline badge in heading — awesome-lint will fail
```

```markdown
# Awesome Legal Apps

## Contents

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
# Badge after Contents section — awesome-lint will fail; must be before Contents
```

### 3.3 Badge Variants NOT Accepted

- CI/build status badges (GitHub Actions, Travis, CircleCI, etc.) — rule: `awesome-no-ci-badges`
- Custom project badges
- Maintenance status badges
- "Inspired by" badges or links

---

## 4. sindresorhus/awesome Pull Request Template Requirements

The PR template at https://github.com/sindresorhus/awesome/blob/main/pull_request_template.md defines mandatory requirements for list submission. These are enforced via PR review checklist.

### 4.1 Repository Standards (Checked by awesome-lint)

| Requirement | What It Validates | How to Verify |
|-------------|-------------------|---------------|
| Default branch is `main` | Must not use `master` | awesome-lint rule: `awesome-main-branch` |
| Repository slug is lowercase | `awesome-legal-apps` not `Awesome-Legal-Apps` | GitHub repo URL; check during repo creation |
| GitHub topics set | Topics must include `awesome-list` and `awesome` | GitHub repo settings → "Manage topics" |
| Repository is 30+ days old | Git first commit timestamp must be ≥30 days in past | awesome-lint rule: `awesome-git-repo-age` |
| Non-generated markdown in GitHub | README.md is a human-created markdown file | awesome-lint validates markdown syntax |

### 4.2 Documentation Requirements

| File | Requirement | Details |
|------|-------------|---------|
| `readme.md` | Must have succinct project/theme description | 1-2 sentence description at top under `# Awesome [Name]` |
| `readme.md` | Must have `## Contents` section | Exact name "Contents" (not "Table of Contents"); lists all major sections |
| `readme.md` | Must include Awesome badge | Badge links to https://awesome.re |
| `contributing.md` | Must exist in repo root | Defines inclusion criteria and entry format |
| `code-of-conduct.md` | Must exist in repo root | Contributor Covenant v2.1 recommended |
| `license` | Must be CC0 or Creative Commons | No code licenses (MIT, Apache, GPL, BSD) |

### 4.3 Content Quality Requirements

| Criterion | Rule | Enforcement |
|-----------|------|-------------|
| Only awesome items | Curated best, not exhaustive list | PR reviewer judgment |
| No unmaintained projects | No archived or deprecated items | Submitted list must verify maintenance status |
| No blockchain lists | General exclusion by sindresorhus/awesome | Automatic rejection |
| Entry format consistency | `- [Name](URL) - Description.` | awesome-lint rule: `awesome-list-item` |
| Description quality | Factual, concise description of what tool does | Not marketing copy; reviewer judgment |

### 4.4 Submission Process (from PR template)

1. **Pre-submission checklist (reviewer will verify):**
   - [ ] List passes `npx awesome-lint` with zero errors
   - [ ] Default branch is `main`
   - [ ] Repository is at least 30 days old
   - [ ] GitHub topics include `awesome-list` and `awesome`
   - [ ] CONTRIBUTING.md exists with inclusion criteria
   - [ ] CODE-OF-CONDUCT.md exists
   - [ ] License file is CC0 or Creative Commons

2. **PR title format:**
   - Use: `Add [Name of List]`
   - Example: `Add Awesome Legal Apps`
   - Do NOT include "Awesome" in the title; the list name itself implies it

3. **Entry placement:**
   - Add entry at the **bottom of the appropriate category**
   - Use title case with URL ending in `#readme`
   - Example: `- [Awesome Legal Apps](https://github.com/user/awesome-legal-apps#readme) - Curated legal tech tools.`

4. **PR review requirements:**
   - Must receive substantive reviews on at least 2 other open PRs (not just "looks good")
   - Comment "unicorn" on your PR to confirm reading all guidelines

---

## 5. Minimum README.md Content for awesome-lint to Pass

### 5.1 Minimal Valid Structure (Skeleton)

```markdown
# Awesome Legal Apps

> A curated list of awesome legal technology tools, apps, AI systems, open source
> projects, and resources for legal professionals, technologists, and researchers.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Contents

- [Category One](#category-one)
- [Contributing](#contributing)

## Category One

- [Example Tool](https://example.com) - Brief factual description in sentence case ending with a period.

## Contributing

Contributions welcome! Read the [contribution guidelines](contributing.md) first.
```

### 5.2 Minimum Content Requirements

**What MUST exist for awesome-lint to pass:**

| Element | Requirement | Example |
|---------|-------------|---------|
| Main heading | Exactly `# Awesome [Name]` | `# Awesome Legal Apps` |
| Description | 1+ line blockquote after heading | `> A curated list of...` |
| Awesome badge | Must link to https://awesome.re | `[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)` |
| Contents section | Heading `## Contents` with links to all sections | `- [Category](#category)` |
| Anchor link format | Lowercase, dash-separated, matches heading | `[AI Tools](#ai-tools)` maps to `## AI Tools` |
| At least one category section | Major section heading with level-2 (#) | `## AI Tools` |
| At least one entry | List item in format `- [Name](URL) - Description.` | `- [Clio](https://clio.com) - Practice management software.` |
| Contributing section | Can be named `## Contributing` or similar | Must reference contributing.md file |

### 5.3 Entry Format Requirements

**Every list entry MUST follow this format exactly:**

```markdown
- [Name](URL) - Description ending with period.
```

**Rules (awesome-lint rule: `awesome-list-item`):**
- Starts with `- ` (dash-space)
- Name in square brackets: `[Name]` (matches product/tool name)
- URL in parentheses: `(https://example.com)` (no trailing slash)
- Space-dash-space separator: ` - `
- Description in sentence case (first word capitalized, proper nouns capitalized)
- Description ends with period: `.`
- Description does NOT start with "A" or "An" (soft rule; awesome-lint doesn't enforce but style guide recommends)
- Description does NOT repeat the item name

**Valid examples:**
```markdown
- [Clio](https://www.clio.com) - Cloud-based legal practice management software for law firms.
- [Docassemble](https://docassemble.org) - Open-source guided interview and document assembly platform for legal aid.
- [CourtListener](https://www.courtlistener.com) - Free legal research tool with millions of US court opinions and oral arguments.
```

**Invalid examples:**
```markdown
- [Clio](https://www.clio.com/) - Clio is practice management software.
# Fails: trailing slash AND description repeats name

- [Docassemble] - Open-source document assembly.
# Fails: URL missing

- [Tool](https://example.com) - a tool for lawyers.
# Fails: description starts with article "a"

- [Tool](https://example.com) - Open-source tool for document assembly
# Fails: no period at end
```

### 5.4 Table of Contents Requirements

**What awesome-lint checks (rule: `awesome-toc`):**

1. Section heading must be exactly `## Contents` (not "Table of Contents")
2. Each link must correspond to a level-2 heading (`##`) in the document
3. Link anchors must be lowercase, with dashes replacing spaces
4. Link anchors must be accurate (match the heading they link to)
5. All top-level sections must be listed in Contents (except optional footnotes)

**Anchor link mapping rules:**

| Heading | Anchor Link | Notes |
|---------|-------------|-------|
| `## AI Tools` | `[AI Tools](#ai-tools)` | Lowercase, spaces → dashes |
| `## Legal Research` | `[Legal Research](#legal-research)` | Multiple words, all lowercase |
| `## Legal NLP & Datasets` | `[Legal NLP & Datasets](#legal-nlp--datasets)` | Ampersand stays as `&`; spacing with `--` |
| `## Contract Management (Beta)` | `[Contract Management (Beta)](#contract-management-beta)` | Parens become part of anchor |

**Example Contents section:**
```markdown
## Contents

- [AI Tools](#ai-tools)
- [Legal Research](#legal-research)
- [Contract Management](#contract-management)
- [Practice Management](#practice-management)
- [Document Management](#document-management)
- [Contributing](#contributing)
```

---

## 6. Phase 1 Compliance Checklist

Use this checklist to verify Phase 1 completion before running `npx awesome-lint`:

### Repository Structure
- [ ] File `readme.md` exists in repo root
- [ ] File `license` exists in repo root (no extension)
- [ ] File `contributing.md` exists in repo root
- [ ] File `code-of-conduct.md` exists in repo root
- [ ] File `.editorconfig` exists in repo root
- [ ] File `.gitattributes` exists in repo root
- [ ] Default branch is `main` (not `master`)

### License File
- [ ] `license` file contains full, unmodified CC0 1.0 Universal text
- [ ] License file is readable and formatted as plain text

### README.md Structure
- [ ] First heading is `# Awesome Legal Apps` (exact casing)
- [ ] Heading followed by `>` blockquote description
- [ ] Awesome badge present after heading: `[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)`
- [ ] Badge is on own line, not inline in heading
- [ ] No CI badges present in README (rule violation: `awesome-no-ci-badges`)
- [ ] `## Contents` section exists (not "Table of Contents")
- [ ] Contents section has accurate links to all top-level headings
- [ ] All heading anchors are lowercase with dashes: `[AI Tools](#ai-tools)`
- [ ] At least 2 major category sections present (e.g., `## AI Tools`, `## Legal Research`)
- [ ] Each category has at least one entry
- [ ] All entries follow format: `- [Name](URL) - Description.`
- [ ] No trailing slashes in URLs
- [ ] All descriptions end with period
- [ ] All descriptions in sentence case
- [ ] `## Contributing` section at bottom references contributing.md
- [ ] No unordered list markers other than `-` (no `*` or `+`)

### GitHub Repository Settings
- [ ] Repository slug is lowercase: `awesome-legal-apps`
- [ ] GitHub topics include `awesome-list`
- [ ] GitHub topics include `awesome`
- [ ] Additional topics recommended: `legal-tech`, `legaltech`, `legal-ai`

### Supporting Files
- [ ] `.editorconfig` has correct settings (tabs, LF line endings)
- [ ] `.gitattributes` contains: `* text=auto eol=lf`
- [ ] `contributing.md` includes:
  - [ ] Inclusion criteria (what qualifies for inclusion)
  - [ ] Exclusion criteria (what disqualifies entries)
  - [ ] Entry format with example
  - [ ] Conflict-of-interest disclosure requirement
- [ ] `code-of-conduct.md` includes Contributor Covenant v2.1 text

### Pre-awesome-lint Validation
- [ ] All markdown files have no hard line breaks at 80 characters
- [ ] All files end with exactly one newline
- [ ] No undefined markdown references
- [ ] No trailing whitespace on any line

### awesome-lint Execution
- [ ] Run: `npx awesome-lint` from repo root
- [ ] ALL 41 rules pass (0 errors reported)
- [ ] Specifically verify these rules pass:
  - [ ] `awesome-badge` — badge present and correctly placed
  - [ ] `awesome-license` — license file exists
  - [ ] `awesome-contributing` — contributing.md exists
  - [ ] `awesome-code-of-conduct` — code-of-conduct.md exists
  - [ ] `awesome-toc` — Contents section links are accurate
  - [ ] `awesome-list-item` — all entries follow format
  - [ ] `awesome-no-ci-badges` — no CI badges in README
  - [ ] `awesome-main-branch` — default branch is `main`

---

## 7. Running awesome-lint: Commands and Expected Output

### 7.1 Local Validation Commands

**Validate entire repository (recommended):**
```bash
cd /c/Users/david/Documents/awesome-legal-apps
npx awesome-lint
```

**Validate specific README file:**
```bash
npx awesome-lint readme.md
```

**Validate by GitHub URL (requires repo already pushed):**
```bash
npx awesome-lint https://github.com/username/awesome-legal-apps
```

### 7.2 Expected Output on Success

```
$ npx awesome-lint
✔ No issues found
```

**On first run (within 30 days of initial commit):**
```
$ npx awesome-lint
  1:1  error  Git repository must be at least 30 days old  remark-lint:awesome-git-repo-age

1 error
```

This error is **expected and acceptable** during Phase 1. It will pass automatically 30 days after the first commit. Do not suppress this rule.

### 7.3 Common Failure Messages and Fixes

| Error Message | Rule | Cause | Fix |
|---------------|------|-------|-----|
| `Missing Awesome badge after the main heading` | awesome-badge | Badge not present or placed incorrectly | Add `[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)` after main heading |
| `license` file not found` | awesome-license | No `license` file in repo root | Create `license` file with CC0 text |
| `contributing.md` file not found | awesome-contributing | No `contributing.md` in repo root | Create `contributing.md` with inclusion criteria |
| `code-of-conduct.md` file not found | awesome-code-of-conduct | No `code-of-conduct.md` in repo root | Create `code-of-conduct.md` |
| `Contents section not found` | awesome-toc | `## Contents` heading missing | Add `## Contents` section after badge |
| `Incorrect list item format` | awesome-list-item | Entry doesn't follow `- [Name](URL) - Description.` | Review entry format; remove trailing slashes, add period |
| `Default branch must be `main`` | awesome-main-branch | Default branch is `master` | Change default branch in GitHub settings to `main` |
| `Unrecognized link in Contents` | awesome-toc | Anchor doesn't match actual heading | Fix link anchors to be lowercase with dashes |
| `CI badge detected` | awesome-no-ci-badges | GitHub Actions or other CI badge in README | Remove all CI status badges |

---

## 8. Validation Baseline Summary

**Phase 1 Success Criteria:**
- [ ] All 41 awesome-lint rules pass locally (0 errors)
- [ ] Repository files match standard awesome-list structure
- [ ] CC0 1.0 Universal license file verified (unmodified text)
- [ ] Badge format is standard Awesome badge with correct placement
- [ ] README.md skeleton contains minimum required sections and entries
- [ ] sindresorhus/awesome PR template requirements understood and implemented

**Timeline:**
- Phase 1 scaffold: create all files and pass awesome-lint
- Phase 1 + 30 days: repository becomes eligible for awesome-lint git-repo-age rule (automatically passes)
- Phase 2: add CI workflow with awesome-lint check on PRs
- Phase 6: submit to sindresorhus/awesome index

---

**Document version:** 1.0
**Last updated:** 2026-03-02
**Valid until:** 2026-06-01 (stable domain — awesome-list standards change infrequently)
