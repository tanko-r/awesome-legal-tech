# Requirements: Awesome Legal Apps

**Defined:** 2026-03-02
**Core Value:** The definitive, most rigorously curated starting point for anyone exploring legal technology — where quality of curation beats quantity of links.

## v1 Requirements

Requirements for initial release. Each maps to roadmap phases.

### Repository Foundation

- [ ] **REPO-01**: Repository has correct awesome-list file structure (README.md, CONTRIBUTING.md, license, code-of-conduct.md, .editorconfig, .gitattributes)
- [ ] **REPO-02**: License is CC0 1.0 Universal (no other license accepted by sindresorhus/awesome)
- [ ] **REPO-03**: README.md follows mandatory awesome-list structure (heading, Awesome badge, Contents section, category sections, entry format)
- [ ] **REPO-04**: Every list entry uses the correct format: `[Name](URL) - Description.` (sentence case, ends with period)
- [ ] **REPO-05**: GitHub repository topics include `awesome-list` and `awesome` for discoverability
- [ ] **REPO-06**: CONTRIBUTING.md defines inclusion criteria, entry format, and conflict-of-interest disclosure requirements

### Automation & CI

- [ ] **AUTO-01**: GitHub Actions workflow runs awesome-lint on every pull request (blocks merge on failure)
- [ ] **AUTO-02**: GitHub Actions workflow runs lychee link checker on weekly cron schedule and auto-creates issues for broken links
- [ ] **AUTO-03**: PR template requires conflict-of-interest disclosure and inclusion criteria checklist

### Content — Core Sections (Table Stakes)

- [ ] **CONT-01**: AI Tools section with categorized entries (legal-specific LLMs, AI drafting tools, AI research assistants)
- [ ] **CONT-02**: Legal Research section (databases, search tools, case law platforms)
- [ ] **CONT-03**: Contract Management section (drafting, review, CLM platforms)
- [ ] **CONT-04**: Practice Management section (billing, case management, client portals)
- [ ] **CONT-05**: Document Management section (DMS, e-signature, document assembly)
- [ ] **CONT-06**: Open Source Legal Tools section (self-hostable and free tools)
- [ ] **CONT-07**: Meta-resources section (other awesome-legal lists including Lawvable, awesome-lawtech, and similar curated collections)
- [ ] **CONT-08**: Minimum 50 curated entries across all core sections at launch

### Content — Differentiator Sections

- [ ] **DIFF-01**: Access to Justice (A2J) section (Docassemble, LegalServer, Upsolve, A2J Author — underserved audience, no other list covers this)
- [ ] **DIFF-02**: Legal NLP & Datasets section (academic models, legal corpora, court data)
- [ ] **DIFF-03**: Legal Education & Communities section (newsletters, Discords, conferences, courses)

### Curation Quality

- [ ] **QUAL-01**: Each entry includes a description that explains what the tool does and who it's for (not marketing copy)
- [ ] **QUAL-02**: Entries include open-source/free markers where applicable
- [ ] **QUAL-03**: Entries are verified as active and maintained at time of inclusion (no abandonware)

### Automated Update System

- [ ] **UPDT-01**: Claude Code skill created that researches new legal tech projects and proposes additions to the list
- [ ] **UPDT-02**: Cron job configured to run the update skill on a scheduled basis (e.g., monthly)
- [ ] **UPDT-03**: Automated workflow pushes validated updates to GitHub (auto-commit and push new entries)

### Index Submission

- [ ] **SUBM-01**: Repository passes all awesome-lint checks with zero errors
- [ ] **SUBM-02**: Repository is at least 30 days old before submission (enforced by awesome-lint git-repo-age rule)
- [ ] **SUBM-03**: Pull request submitted to sindresorhus/awesome index (with 2 peer PR reviews as required)

## v2 Requirements

Deferred to future release. Tracked but not in current roadmap.

### Enhanced Discovery

- **DISC-01**: GitHub Pages / docsify site for browseable web interface
- **DISC-02**: Jurisdictional tags on entries (US, UK, EU, etc.)
- **DISC-03**: Pricing tier markers (free, freemium, paid) on commercial tools

### Community Growth

- **COMM-01**: Regular "call for contributions" campaigns
- **COMM-02**: Co-maintainer recruitment and onboarding documentation
- **COMM-03**: CHANGELOG.md tracking significant additions

## Out of Scope

| Feature | Reason |
|---------|--------|
| Building any of the listed tools | Curation only — linking, not building |
| Real-time pricing comparisons | Maintenance burden too high; link to tool pages instead |
| Legal advice or tool recommendations | Resource directory, not a law firm |
| General productivity tools (not legal-specific) | Scope discipline — legal domain only |
| Abandoned/unmaintained projects | Quality threshold — active tools only |

## Traceability

Which phases cover which requirements. Confirmed during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| REPO-01 | Phase 1 | Pending |
| REPO-02 | Phase 1 | Pending |
| REPO-03 | Phase 1 | Pending |
| REPO-04 | Phase 1 | Pending |
| REPO-05 | Phase 1 | Pending |
| REPO-06 | Phase 1 | Pending |
| AUTO-01 | Phase 2 | Pending |
| AUTO-02 | Phase 2 | Pending |
| AUTO-03 | Phase 2 | Pending |
| CONT-01 | Phase 3 | Pending |
| CONT-02 | Phase 3 | Pending |
| CONT-03 | Phase 3 | Pending |
| CONT-04 | Phase 3 | Pending |
| CONT-05 | Phase 3 | Pending |
| CONT-06 | Phase 3 | Pending |
| CONT-07 | Phase 3 | Pending |
| CONT-08 | Phase 3 | Pending |
| DIFF-01 | Phase 4 | Pending |
| DIFF-02 | Phase 4 | Pending |
| DIFF-03 | Phase 4 | Pending |
| QUAL-01 | Phase 3 | Pending |
| QUAL-02 | Phase 4 | Pending |
| QUAL-03 | Phase 3 | Pending |
| UPDT-01 | Phase 5 | Pending |
| UPDT-02 | Phase 5 | Pending |
| UPDT-03 | Phase 5 | Pending |
| SUBM-01 | Phase 6 | Pending |
| SUBM-02 | Phase 6 | Pending |
| SUBM-03 | Phase 6 | Pending |

**Coverage:**
- v1 requirements: 29 total
- Mapped to phases: 29
- Unmapped: 0

---
*Requirements defined: 2026-03-02*
*Last updated: 2026-03-02 after roadmap creation*
