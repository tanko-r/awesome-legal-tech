---
wave: 1
depends_on: []
files_modified:
  - readme.md
  - license
  - contributing.md
  - code-of-conduct.md
  - .editorconfig
  - .gitattributes
autonomous: false
---

# Phase 1: Repository Scaffolding & Governance — PLAN

**Phase Goal:** The repository exists in the correct awesome-list shape with all required files, governance documents, and GitHub configuration — before any content is added.

**Requirements covered:** REPO-01, REPO-02, REPO-03, REPO-04, REPO-05, REPO-06

**Success criteria (must all be TRUE):**
1. Running `npx awesome-lint` against the repository returns zero errors on a README.md skeleton (heading, Awesome badge, Contents section)
2. The repository contains `README.md`, `CONTRIBUTING.md`, `license` (CC0, lowercase, no extension), `code-of-conduct.md`, `.editorconfig`, and `.gitattributes`
3. A visitor reading CONTRIBUTING.md can determine whether their tool qualifies for inclusion, what entry format to use, and how to disclose a conflict of interest
4. GitHub repository topics include `awesome-list` and `awesome`, making it discoverable via the awesome topic filter
5. The default branch is `main` and the `license` file is CC0 1.0 Universal (the only license accepted by the awesome index)

---

## Task 1: Create Scaffolding Files

**Wave:** 1
**Depends on:** None
**Output:** Six new files in the repository root, ready for linting validation

### Description

Create all required governance and structural files from verified templates. These files establish the awesome-list conformity baseline and prevent vendor capture through clear inclusion criteria.

### Steps

1. Create `readme.md` with the exact structure provided in 01-RESEARCH.md (heading, description block, Awesome badge, Contents section, skeleton categories, Contributing section)
   - Must include all sections from ROADMAP phase goals: AI Tools, Legal Research, Contract Management, Practice Management, Document Management, Open Source Legal Tools, Access to Justice, Legal NLP & Datasets, Legal Education & Communities, Meta-Lists
   - Each section heading must have a corresponding Contents anchor link in sentence case
   - Do not add any entry content — skeleton only

2. Create `license` (lowercase, no extension) with the complete CC0 1.0 Universal legal text from https://creativecommons.org/publicdomain/zero/1.0/legalcode
   - Exact text required; no modifications or summary versions
   - Verify: GitHub license detection recognizes it

3. Create `contributing.md` (lowercase) with:
   - Contributor Code of Conduct reference and link to code-of-conduct.md
   - Inclusion criteria section defining what qualifies and disqualifies tools
   - Entry format section with example
   - Conflict-of-interest disclosure requirement and sample disclosure language
   - Submission process with 4+ steps
   - Reference to npx awesome-lint validation

4. Create `code-of-conduct.md` (lowercase) with Contributor Covenant v2.1 text from https://contributor-covenant.org/version/2/1/
   - Exact template; no custom modifications
   - Establish community behavioral standards

5. Create `.editorconfig` with:
   ```
   root = true
   [*]
   indent_style = tab
   end_of_line = lf
   charset = utf-8
   trim_trailing_whitespace = true
   insert_final_newline = true
   ```
   - Ensures consistent editor behavior across contributors

6. Create `.gitattributes` with single line:
   ```
   * text=auto eol=lf
   ```
   - Enforces Unix line endings on all files

### Verification

- [ ] All six files exist in the repository root
- [ ] `license` file contains unmodified CC0 1.0 Universal text (minimum 5000 characters)
- [ ] `contributing.md` includes all four required sections: criteria, format, CoI, process
- [ ] `code-of-conduct.md` contains Contributor Covenant v2.1 text
- [ ] `.editorconfig` and `.gitattributes` match the exact patterns from 01-RESEARCH.md
- [ ] `readme.md` has exactly 10 main category sections (AI Tools through Meta-Lists) plus Contributing section

---

## Task 2: Validate Awesome-Lint Compliance Locally

**Wave:** 1
**Depends on:** Task 1 (must complete before validation)
**Output:** Zero-error awesome-lint validation report

### Description

Run awesome-lint against the repository to confirm all six scaffolding files are correctly structured. This is the gate: awesome-lint must pass zero-error before committing.

### Steps

1. Initialize Git if not already done: `git init` (should already be initialized)

2. Stage all scaffolding files: `git add readme.md license contributing.md code-of-conduct.md .editorconfig .gitattributes`

3. Create an initial commit with message: "Initial awesome-list scaffold: governance and structure files"
   - This commit message is required — it's part of the repository's permanent history

4. Run `npx awesome-lint` in the repository root
   - Expected output: No errors, only the git-repo-age warning (normal for new repos)
   - Warning text: `Git repository must be at least 30 days old` — this is expected and will pass automatically after 30 days

5. If awesome-lint returns any ERRORS (not warnings):
   - Read the specific error message
   - Cross-reference against the patterns in 01-RESEARCH.md "Common Pitfalls" section
   - Fix the identified issue
   - Commit the fix: `git add <file> && git commit -m "Fix awesome-lint: <specific issue>"`
   - Re-run `npx awesome-lint` until zero errors

6. Document the validation result: capture the terminal output showing zero errors

### Verification

- [ ] `npx awesome-lint` runs without network errors
- [ ] Output shows zero errors (warnings are acceptable)
- [ ] The only warning present is the 30-day repo age warning (expected for new repos)
- [ ] No lint errors related to badge placement, entry format, section naming, or file presence
- [ ] Validation log is captured for the record

### Common Issues to Watch For

- **Badge placement error:** "Missing Awesome badge after the main heading" → Check `readme.md` has `[![Awesome]...` on its own line after the description block (not inline with the `#` heading)
- **Section naming error:** "Contents heading not found" or "Contents section wrongly named" → Verify heading is exactly `## Contents` (not `## Table of Contents`)
- **Entry format with content:** awesome-lint may catch format issues if skeleton entries are added — avoid entries during Phase 1
- **Branch name error:** "Not on main branch" — Verify `git branch` shows `main` as current branch

---

## Task 3: Set GitHub Repository Topics

**Wave:** 1
**Depends on:** Task 2 (must have pushed to GitHub first)
**Output:** GitHub repository discoverable via awesome-list and awesome topic filters

### Description

GitHub topics are not set via repository files — they must be configured through the GitHub UI or API. This task ensures the repository is discoverable in the awesome ecosystem and passes awesome-lint's topic validation.

### Steps

1. Push the scaffolding commit to GitHub: `git push origin main`
   - Repository must be created on GitHub first and cloned locally OR created locally and pushed to existing GitHub repo
   - Verify `git remote -v` shows an `origin` pointing to your GitHub repo

2. Navigate to the repository's main page on GitHub (e.g., https://github.com/username/awesome-legal-apps)

3. Click the "About" section gear icon (settings icon to the right of the repository name)
   - This opens the "Edit repository details" sidebar

4. In the "Topics" field, add the following topics (minimum required):
   - `awesome-list` (required for awesome-lint topic check)
   - `awesome` (required for awesome-lint topic check)
   - Recommended additional topics for discoverability:
     - `legal-tech`
     - `legaltech`
     - `legal-ai`
     - `curation`

5. Click "Save changes"

6. Verify topics appear on the repository main page (visible below the repository name)

### Verification

- [ ] Repository has at least two topics: `awesome-list` and `awesome`
- [ ] Topics are visible on the GitHub repository main page
- [ ] Awesome-lint can reach the repository URL and validates topics (Phase 2 will test this in CI)

### Why This Matters

awesome-lint can validate topics in a GitHub repository when run against a repository URL rather than a local directory. For Phase 2 CI validation and Phase 6 submission, the repository must have these topics set or awesome-lint will fail.

---

## Task 4: Verify Requirements Traceability

**Wave:** 1
**Depends on:** Task 3 (all scaffolding complete)
**Output:** Confirmation that all Phase 1 requirements are satisfied

### Description

Verify that the completed scaffolding fulfills all six Phase 1 requirements (REPO-01 through REPO-06) by cross-referencing the files created against the requirement definitions in REQUIREMENTS.md.

### Steps

1. For each requirement below, verify the condition is met:

   - **REPO-01**: Repository has correct awesome-list file structure
     - Verify: `readme.md`, `contributing.md`, `license`, `code-of-conduct.md`, `.editorconfig`, `.gitattributes` all exist in the repo root
     - Confirmation: List the six files by running `ls -la readme.md license contributing.md code-of-conduct.md .editorconfig .gitattributes`

   - **REPO-02**: License is CC0 1.0 Universal
     - Verify: `license` file contains the phrase "Creative Commons Zero 1.0 Universal" and references https://creativecommons.org/publicdomain/zero/1.0/
     - Confirmation: `grep -i "creative commons zero" license`

   - **REPO-03**: README.md follows mandatory awesome-list structure
     - Verify: `readme.md` contains (in order):
       - Main heading: `# Awesome Legal Apps`
       - Description block: `> ...`
       - Awesome badge: `[![Awesome]...`
       - Contents section: `## Contents` followed by section links
       - Category sections: ## AI Tools, ## Legal Research, etc.
       - Contributing section: ## Contributing with link to contributing.md
     - Confirmation: Run `npx awesome-lint` shows zero errors related to structure

   - **REPO-04**: Every list entry uses the correct format
     - Verify: README.md skeleton sections have NO entries (Phase 1 is structure only, Phase 3 adds content)
     - Note: This requirement will be fully tested in Phase 3 when entries are added; Phase 1 confirms the format specification exists in contributing.md

   - **REPO-05**: GitHub repository topics include `awesome-list` and `awesome`
     - Verify: Navigate to the GitHub repo settings and confirm two topics are visible
     - Confirmation: Screenshot or note the topic display

   - **REPO-06**: CONTRIBUTING.md defines inclusion criteria, entry format, and conflict-of-interest disclosure
     - Verify: `contributing.md` contains three labeled sections:
       1. Inclusion criteria (what qualifies, what disqualifies)
       2. Entry format (exact `[Name](URL) - Description.` pattern with example)
       3. Conflict-of-interest disclosure (requirement and sample language)
     - Confirmation: `grep -i "inclusion criteria\|entry format\|conflict" contributing.md`

2. Create a verification checklist by running the confirmations above and recording results

### Verification

- [ ] REPO-01 — Six files present in repo root
- [ ] REPO-02 — `license` file contains CC0 1.0 Universal text and URL
- [ ] REPO-03 — `readme.md` structure validated by `npx awesome-lint` zero-error output
- [ ] REPO-04 — `contributing.md` specifies entry format requirement
- [ ] REPO-05 — GitHub repository topics include `awesome-list` and `awesome`
- [ ] REPO-06 — `contributing.md` defines criteria, format, and CoI disclosure
- [ ] All six requirements marked SATISFIED

---

## Task 5: Document Phase Completion

**Wave:** 1
**Depends on:** Task 4 (all verification complete)
**Output:** Phase 1 completion record in STATE.md

### Description

Update the project state file to record Phase 1 completion, document the scaffolding commit hash, and confirm readiness for Phase 2.

### Steps

1. Obtain the commit hash of the scaffolding commit: `git log --oneline -1` (should be "Initial awesome-list scaffold...")

2. Update `.planning/STATE.md`:
   - Change "Phase: 1 of 6 (Repository Scaffolding & Governance)" to "Phase: 2 of 6 (Automation & CI)" OR "Phase: 1 of 6 (Complete)"
   - Update "Plan: 0 of TBD in current phase" to "Plan: 1 of TBD completed"
   - Update "Status: Ready to plan" to "Status: Complete — Ready for Phase 2"
   - Update "Last activity:" with current date and summary "Phase 1 complete: Repository scaffold created; all governance files in place; awesome-lint validation passed"
   - Update Progress bar: Change `[░░░░░░░░░░] 0%` to `[█░░░░░░░░░░] ~17%` (1 of 6 phases)
   - Add to "Performance Metrics" / "By Phase" table:
     ```
     | 1. Repository Scaffolding & Governance | 1 | 1 | 1.0 hours (estimated) |
     ```

3. Add to "Decisions" section in STATE.md:
   - [Phase 1]: Scaffolding deployed with Contributor Covenant v2.1 and CC0 1.0 license; awesome-lint passes zero-error; repository topics set

4. Record the scaffolding commit hash in STATE.md under "Session Continuity":
   - "Scaffolding commit: [hash]"

5. Confirm the next phase gateway: Phase 2 depends on Phase 1 completion — no blockers identified

### Verification

- [ ] STATE.md updated with Phase 1 completion status
- [ ] Progress bar reflects 1 of 6 phases complete
- [ ] Decision recorded in Decisions table
- [ ] Commit hash documented for reference
- [ ] Next phase (Phase 2: Automation & CI) is unblocked

---

## Quality Gates

All tasks must satisfy their verification criteria before Phase 1 is considered complete:

- [ ] Task 1: All six scaffolding files created from verified templates
- [ ] Task 2: `npx awesome-lint` runs with zero errors (warnings acceptable)
- [ ] Task 3: GitHub repository topics set to `awesome-list` and `awesome` (verified in UI)
- [ ] Task 4: All six Phase 1 requirements (REPO-01 through REPO-06) verified as satisfied
- [ ] Task 5: STATE.md updated; Phase 1 marked complete; Phase 2 unblocked

## Must-Haves (Derived from Phase Goal)

To fulfill the phase goal ("The repository exists in the correct awesome-list shape with all required files, governance documents, and GitHub configuration — before any content is added"), the following must be TRUE at phase completion:

1. **awesome-lint zero-error validation** — Running `npx awesome-lint` returns no errors on the repository root. Warnings (e.g., git-repo-age) are expected and acceptable; blocking errors are not.

2. **All six governance files present and correct** — `readme.md`, `license`, `contributing.md`, `code-of-conduct.md`, `.editorconfig`, `.gitattributes` exist in the repo root with content matching verified sources (sindresorhus/awesome, Contributor Covenant v2.1, CC0 1.0 Universal legal text).

3. **Inclusion criteria and CoI governance in place** — A visitor reading CONTRIBUTING.md can identify:
   - What qualifies a tool for inclusion (maintained, legal-domain-specific, not abandonware)
   - What disqualifies a tool (general productivity, unmaintained, archived)
   - The entry format requirement: `[Name](URL) - Description.`
   - The conflict-of-interest disclosure requirement and how to submit one

4. **GitHub repository discoverable via awesome filters** — The repository has topics `awesome-list` and `awesome` set and visible on the GitHub repository main page, enabling discoverability through the GitHub topic filter.

5. **CC0 1.0 Universal license verified** — The `license` file contains unmodified CC0 1.0 Universal legal text from the official Creative Commons source, making the repository compliant with sindresorhus/awesome index requirements. No other license is acceptable.

6. **Default branch is main** — The repository's default branch is named `main` (verified by awesome-lint and GitHub settings); no `master` branch is in use.

---

## Notes

- Phase 1 is the time-sensitive foundation: the repository creation date starts the 30-day clock for Phase 6 eligibility. Complete Phase 1 as early as possible to minimize the Phase 5–6 wait.
- awesome-lint warnings (especially git-repo-age) are expected and do NOT block Phase 1 completion. Only errors prevent progress.
- Tasks 1–2 are local; Task 3 requires GitHub; Task 4–5 are verification and documentation. If working offline, defer Task 3 until GitHub access is available, then re-run Task 2 validation against the repository URL.
- No entry content is added in Phase 1 — this phase is structure and governance only. Content begins in Phase 3.

