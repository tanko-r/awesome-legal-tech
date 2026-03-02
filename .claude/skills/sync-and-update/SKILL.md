---
name: sync-and-update
description: Pulls latest, researches new legal tech entries across all README categories, updates README.md, commits, and pushes to remote — fully autonomous, no user input required.
context: fork
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Bash, WebSearch, WebFetch, Grep, Glob
argument-hint: "[optional: target section name]"
---

# Skill: sync-and-update

Fully autonomous end-to-end update cycle for the awesome-legal-apps list. Pulls latest from remote, dynamically discovers all categories from README.md, researches new entries for each, updates the file, commits, and pushes — all without user input.

---

## Step 0: Pull Latest

Run these shell commands to ensure the local repo is up to date:

```
git pull --rebase origin main
```

If the pull fails due to conflicts, abort and print the error. Do NOT force-push or discard local changes.

---

## Step 1: Extract Existing URLs and Categories from README.md

Read `README.md` and perform two extractions:

### 1a. Deduplication Set
Parse every line matching the pattern `- [Name](URL)` or `- FLAG [Name](URL)`. Extract all URLs into a deduplication set. This set prevents duplicate entries in all later steps.

### 1b. Dynamic Category Discovery
Parse all `## Level-2 Headings` from README.md. These are the categories to search for. Skip non-content headings: `Contents`, `Jurisdiction Flags`, `Contributing`, `Code of Conduct`, `License`.

Store each category name for use in Step 2. Example categories that may be discovered:
- AI Tools
- Law-Focused LLMs & Fine-Tuned Models
- Legal Research
- Contract Management
- Practice Management
- Document Management
- Backend Utilities & Libraries
- Access to Justice
- Legal NLP & Datasets
- Compliance & Regulatory Technology
- eDiscovery & Litigation Support
- Legal Analytics & Prediction
- IP & Patent Technology
- Privacy & Data Protection
- Legal Workflow Automation
- Court & Government Filing Systems
- Legal Ontologies & Knowledge Graphs
- MCP Servers & AI Agent Tools for Law
- Legal Education & Communities
- Advanced Legal Tools & Citation Systems
- Meta-Resources

---

## Step 2: Research New Candidates

### If `$ARGUMENTS` is not empty:
Treat `$ARGUMENTS` as a target section name and restrict queries to that topic only. Run at least 3 targeted WebSearch queries for that category.

### If `$ARGUMENTS` is empty (full update):
For EACH category discovered in Step 1b, generate and run 1-2 WebSearch queries using the current year. The query should combine the category topic with terms like `site:github.com`, `open source`, `launch`, or the current year.

**Query generation rules:**
- Always include the current year in queries
- For GitHub-heavy categories, use `site:github.com`
- For categories with online tools, also search without `site:github.com`
- Vary search terms to maximize coverage

**Example generated queries per category:**
- "AI Tools" → `new legal AI tools site:github.com {YEAR}`, `legal AI assistant launch {YEAR}`
- "Law-Focused LLMs" → `legal LLM fine-tuned model site:github.com {YEAR}`, `legal language model huggingface {YEAR}`
- "Legal Research" → `legal research platform open source site:github.com {YEAR}`
- "Contract Management" → `contract management tool open source {YEAR}`
- "Compliance & Regulatory Technology" → `regtech compliance tool open source site:github.com {YEAR}`
- "eDiscovery & Litigation Support" → `ediscovery tool open source site:github.com {YEAR}`
- "Legal Analytics & Prediction" → `legal analytics prediction model site:github.com {YEAR}`
- "IP & Patent Technology" → `patent search tool open source site:github.com {YEAR}`
- "Privacy & Data Protection" → `privacy GDPR compliance tool open source {YEAR}`
- "Legal Workflow Automation" → `legal workflow automation tool site:github.com {YEAR}`
- "Court & Government Filing Systems" → `court e-filing system open source {YEAR}`
- "Legal Ontologies & Knowledge Graphs" → `legal ontology knowledge graph site:github.com {YEAR}`
- "MCP Servers & AI Agent Tools for Law" → `MCP server legal site:github.com {YEAR}`, `legal AI agent framework {YEAR}`
- "Meta-Resources" → `awesome legal technology list site:github.com {YEAR}`

Add more queries if initial results yield fewer than 10 total candidates after deduplication.

---

## Step 3: Filter Candidates

For each candidate URL, apply ALL of these checks. Discard on ANY failure:

1. **Deduplication:** URL is NOT already in the deduplication set from Step 1a
2. **Liveness:** URL resolves and returns content (not 404, not parked domain). Verify via WebFetch or WebSearch.
3. **Domain specificity:** Tool is legal-domain-specific or has clear legal-specific features. General-purpose tools (e.g., generic note-taking apps) are excluded.
4. **Active maintenance:** For GitHub repos, last commit within 12 months. For commercial tools, homepage resolves and is not a redirect to an acquirer.
5. **Quality bar:** Project has meaningful documentation or a clear public description. Empty/placeholder repos are excluded.

---

## Step 4: Write Entries

For each candidate that passes all filters:

- **Compose description:** One sentence explaining what the tool does and who it is for. No marketing copy. Sentence case. Ends with a period.
- **Determine correct section:** Match to the README.md section whose `## Heading` best fits. Use the categories discovered in Step 1b.
- **Place correctly:** GitHub repos go under `### GitHub Repositories` subsections when they exist. Free web tools go under `### Free Online Tools` subsections when they exist. Other entries go at the end of their section.
- **Jurisdiction flags:** If the tool is designed for a specific jurisdiction's legal system, add the appropriate flag emoji before the link (e.g., `- 🇺🇸 [Name](URL) - Description.`). If the tool is globally applicable, do not add a flag. Refer to the Jurisdiction Flags table in README.md for valid flags.
- **Use exact format:** `- [Name](URL) - Description.` or `- FLAG [Name](URL) - Description.`
- If `$ARGUMENTS` is not empty, only append to the specified section.

Use the Edit tool to insert entries at the correct location in README.md. Do NOT rewrite the entire file — only insert new lines.

---

## Step 5: Commit and Push

After all edits are complete, run the following shell commands:

```bash
# Stage only README.md
git add README.md

# Check if there are staged changes
git diff --cached --quiet && echo "NO_CHANGES" || echo "HAS_CHANGES"
```

**If NO_CHANGES:** Skip commit and push. Go directly to Step 6 and report that no new entries were found.

**If HAS_CHANGES:** Commit and push:

```bash
# Count how many new entries were added
ENTRY_COUNT=$(git diff --cached README.md | grep '^\+- ' | wc -l)

# Commit with descriptive message
git commit -m "chore: add ${ENTRY_COUNT} new legal tech entries

Automated update via sync-and-update skill.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

# Push to remote
git push origin HEAD
```

Do NOT use `--force`. If the push fails, print the error and stop. Do NOT retry destructively.

---

## Step 6: Print Summary

After completion, print a summary:

```
=== sync-and-update complete ===
- Pulled latest from remote: [yes/no]
- Categories discovered: [number]
- Search queries run: [number]
- Total candidates found: [number]
- Candidates after filtering: [number]
- New entries added: [number]
  - [Entry Name] → [Section]
  - [Entry Name] → [Section]
- Committed: [yes/no]
- Pushed to remote: [yes/no]
```

If zero entries were added:
```
No new entries found — all candidates were duplicates, inactive, or out of scope.
```

---

## Explicit Prohibitions

- Do NOT add any URL already present in README.md
- Do NOT copy vendor marketing language into descriptions
- Do NOT add general-purpose tools without legal-specific features
- Do NOT add GitHub repos with zero commits in the past 12 months
- Do NOT add tools whose homepage redirects to an acquirer
- Do NOT use `--force` or `--no-verify` with any git command
- Do NOT modify any file other than README.md
- Do NOT prompt the user for input at any point — this skill is fully autonomous
- Do NOT hardcode the list of categories — always read them dynamically from README.md
