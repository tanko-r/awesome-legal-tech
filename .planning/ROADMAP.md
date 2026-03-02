# Roadmap: Awesome Legal Apps

## Overview

Six phases take the repository from an empty directory to a sindresorhus/awesome-indexed list. Governance and scaffolding come first because every downstream pitfall — lint failures, vendor capture, link rot, taxonomy churn — is prevented only by getting Phase 1 right. Content follows in two waves: core sections that table-stakes users expect (Phase 3), then differentiator sections that no existing list covers (Phase 4). Automation runs in parallel concern: CI gates in Phase 2 and an autonomous update skill in Phase 5. Phase 6 opens only after the 30-day repo-age constraint is satisfied.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Repository Scaffolding & Governance** - Create the correct file structure, license, and governance documents before any content is added
- [ ] **Phase 2: Automation & CI** - Wire up awesome-lint PR gating and lychee link checking so quality is enforced automatically from this point forward
- [ ] **Phase 3: Core Content Population** - Populate all table-stakes sections with a minimum of 50 curated, verified entries
- [ ] **Phase 4: Differentiator Content** - Add the sections no competing list covers: A2J, Legal NLP & Datasets, and Legal Education & Communities
- [ ] **Phase 5: Automated Update System** - Build and schedule a Claude Code skill that researches new projects and auto-pushes validated additions
- [ ] **Phase 6: Index Submission & Launch** - Pass final lint audit and submit the pull request to sindresorhus/awesome (requires 30-day repo age)

## Phase Details

### Phase 1: Repository Scaffolding & Governance
**Goal**: The repository exists in the correct awesome-list shape with all required files, governance documents, and GitHub configuration — before any content is added
**Depends on**: Nothing (first phase)
**Requirements**: REPO-01, REPO-02, REPO-03, REPO-04, REPO-05, REPO-06
**Success Criteria** (what must be TRUE):
  1. Running `npx awesome-lint` against the repository returns zero errors on a README.md skeleton (heading, Awesome badge, Contents section)
  2. The repository contains `README.md`, `CONTRIBUTING.md`, `license` (CC0, lowercase, no extension), `code-of-conduct.md`, `.editorconfig`, and `.gitattributes`
  3. A visitor reading CONTRIBUTING.md can determine whether their tool qualifies for inclusion, what entry format to use, and how to disclose a conflict of interest
  4. GitHub repository topics include `awesome-list` and `awesome`, making it discoverable via the awesome topic filter
  5. The default branch is `main` and the `license` file is CC0 1.0 Universal (the only license accepted by the awesome index)
**Plans**: TBD

### Phase 2: Automation & CI
**Goal**: Every pull request is automatically linted and every broken link surfaces as a GitHub issue — quality is machine-enforced, not dependent on manual review
**Depends on**: Phase 1
**Requirements**: AUTO-01, AUTO-02, AUTO-03
**Success Criteria** (what must be TRUE):
  1. Opening a pull request with a malformed entry (wrong format, missing period, duplicate link) causes the CI check to fail and blocks merge
  2. Broken links discovered by the weekly lychee cron automatically open a GitHub issue with the affected URL identified
  3. A contributor opening a pull request sees a checklist that includes a conflict-of-interest disclosure field and the inclusion criteria items
**Plans**: TBD

### Phase 3: Core Content Population
**Goal**: The list is independently useful — all five table-stakes sections are populated with at least 50 curated, actively maintained entries, each with an original description that explains what the tool does and who it is for
**Depends on**: Phase 2
**Requirements**: CONT-01, CONT-02, CONT-03, CONT-04, CONT-05, CONT-06, CONT-07, CONT-08, QUAL-01, QUAL-03
**Success Criteria** (what must be TRUE):
  1. A legal professional visiting the list can find tools in at least six distinct sections: AI Tools, Legal Research, Contract Management, Practice Management, Document Management, and Open Source Legal Tools
  2. The list contains a minimum of 50 entries total across all core sections
  3. Every entry follows the `[Name](URL) - Description.` format with a description written from scratch (no vendor marketing copy) that names the tool's purpose and intended user
  4. Every entry links to an active, maintained resource — no 404s, no acquired/shut-down products, no abandonware — verified at time of inclusion
  5. A Meta-resources section exists listing other curated awesome-legal lists (including Lawvable and awesome-lawtech) so visitors can discover peer collections
**Plans**: TBD

### Phase 4: Differentiator Content
**Goal**: The list covers ground no other awesome-legal repository covers — Access to Justice tools, academic NLP datasets and models, and legal education resources — with open-source and free markers applied across all sections
**Depends on**: Phase 3
**Requirements**: DIFF-01, DIFF-02, DIFF-03, QUAL-02
**Success Criteria** (what must be TRUE):
  1. A legal aid developer or law school clinic researcher visiting the list finds a dedicated Access to Justice section with tools like Docassemble, Upsolve, LegalServer, and A2J Author
  2. A legal NLP researcher finds a dedicated section containing academic datasets, annotated corpora, and open-source legal language models with enough description to evaluate relevance
  3. A law student or new entrant to legaltech finds a Legal Education & Communities section with newsletters, online courses, conferences, and community groups
  4. Open-source and free-tier entries across all sections carry a visible marker so users can filter by cost or self-hostability
**Plans**: TBD

### Phase 5: Automated Update System
**Goal**: The list stays current without requiring manual research — a Claude Code skill autonomously identifies new legal tech projects, proposes additions, and pushes validated entries to GitHub on a scheduled basis
**Depends on**: Phase 3
**Requirements**: UPDT-01, UPDT-02, UPDT-03
**Success Criteria** (what must be TRUE):
  1. A Claude Code skill exists that, when invoked, researches new legal tech projects and outputs a structured proposal of candidate entries in the correct `[Name](URL) - Description.` format
  2. A cron job is configured to run the update skill on a scheduled basis (monthly or more frequently) without manual intervention
  3. Validated additions are automatically committed and pushed to GitHub — the list receives new entries without requiring the maintainer to manually trigger or draft them
**Plans**: TBD

### Phase 6: Index Submission & Launch
**Goal**: The repository passes every automated check and the pull request to sindresorhus/awesome is submitted — the list enters the official awesome index
**Depends on**: Phase 4, Phase 5
**Requirements**: SUBM-01, SUBM-02, SUBM-03
**Success Criteria** (what must be TRUE):
  1. Running `npx awesome-lint` against the repository returns zero errors — no format violations, no missing files, no badge issues
  2. The repository is at least 30 days old (enforced by awesome-lint's `git-repo-age` rule), satisfying the maturation requirement
  3. A pull request is open against sindresorhus/awesome with the required 2 peer PR reviews completed, following the sindresorhus/awesome pull request template exactly
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4 → 5 → 6
Note: Phase 5 depends on Phase 3 (not Phase 4), so Phases 4 and 5 can be worked in parallel if desired.

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Repository Scaffolding & Governance | 0/TBD | Not started | - |
| 2. Automation & CI | 0/TBD | Not started | - |
| 3. Core Content Population | 1/1 | **COMPLETE** | ✅ 2026-03-02 (117 entries) |
| 4. Differentiator Content | 0/TBD | Not started | - |
| 5. Automated Update System | 0/TBD | Not started | - |
| 6. Index Submission & Launch | 0/TBD | Not started | - |
