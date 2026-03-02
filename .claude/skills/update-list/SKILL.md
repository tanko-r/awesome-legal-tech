---
name: update-list
description: Researches new legal tech projects, filters duplicates and abandonware, and appends validated entries to README.md in awesome-list format. Use only when explicitly invoked.
context: fork
disable-model-invocation: true
allowed-tools: Read, Write, WebSearch
argument-hint: "[optional: target section name]"
---

# Skill: update-list

Research new legal technology projects and append validated entries to README.md in the correct awesome-list format. Runs fully autonomously — no human input required during execution.

## Step 1: Extract Existing URLs from README.md

Read `README.md` and parse every line matching the pattern `- [Name](URL) -`. Extract the URL from each match. Store as a deduplication set. This set is used in Step 3 to filter candidates and ensure no duplicate entries are ever written.

## Step 2: Research New Candidates

Run at minimum 6 WebSearch queries covering different legal tech categories. Queries must target tools published or significantly updated within the last 90 days. Required queries:

1. `legal AI tools 2026 site:github.com OR site:producthunt.com`
2. `new legal technology software launch 2026`
3. `legal research platform contract review tool launch 2026`
4. `access to justice software open source 2026`
5. `legal NLP model dataset 2026`
6. `practice management billing software law firm 2026`

Add additional queries if initial results are sparse (fewer than 10 candidates after deduplication).

If `$ARGUMENTS` is not empty, treat it as a target section name and restrict research queries to that section only.

## Step 3: Filter Candidates

For each candidate URL, apply all four checks — discard on ANY failure:

1. **Deduplication:** URL is not already in the deduplication set from Step 1
2. **Liveness:** URL resolves (not a 404 — verify by attempting to access it via WebSearch or Read)
3. **Domain specificity:** Tool is legal-domain-specific (not general productivity software without legal-specific features)
4. **Active maintenance:** For GitHub repos, last commit within 12 months; for commercial tools, company homepage resolves and is not a redirect to an acquirer

## Step 4: Write Entries

For each candidate that passes all four checks:

- **Compose description:** One sentence explaining what the tool does and who it is for. No marketing copy. Sentence case. Ends with a period.
- **Determine correct section:** Match the tool to the README.md section whose heading best describes it:
  - `## AI Tools`
  - `## Legal Research`
  - `## Contract Management`
  - `## Practice Management`
  - `## Document Management`
  - `## Backend Utilities & Libraries`
  - `## Access to Justice`
  - `## Legal NLP & Datasets`
  - `## Legal Education & Communities`
  - `## Meta-Resources`
- **Append entry:** Use the exact format `- [Name](URL) - Description.` — append within the appropriate subsection if one exists, or at the end of the section if no subsections match.
- If `$ARGUMENTS` is not empty, only append to the specified section.

## Step 5: Print Summary

After all writes are complete, print:

- Total candidates found (before filtering)
- Candidates that passed all filters
- Entries added (with names and target sections)
- If zero entries added: print "No new entries found — all candidates were duplicates, inactive, or out of scope."

---

## Explicit Prohibitions

- Do not add any URL already present in README.md
- Do not copy vendor marketing copy into descriptions
- Do not add tools that are general-purpose productivity apps without legal-specific features
- Do not add GitHub repos with zero commits in the past 12 months
- Do not add tools whose company homepage redirects to an acquirer (acquired/shut-down indicator)
