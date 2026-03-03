---
name: sync-and-update
description: Pulls latest, researches new legal tech entries via web search and GitHub topic crawl, checks for link rot, updates README.md, commits, and pushes to remote — fully autonomous, no user input required.
context: fork
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Bash, WebSearch, WebFetch, Grep, Glob
argument-hint: "[optional: target section name]"
---

# Skill: sync-and-update

Fully autonomous end-to-end update cycle for the awesome-legal-apps list. Pulls latest from remote, dynamically discovers all categories from README.md, researches new entries via web search and GitHub topic crawl, checks all GitHub repos for link rot (marking stale entries), updates the file, commits, and pushes — all without user input.

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

## Step 2b: GitHub Topic Crawl

Crawl GitHub Topics pages to discover repositories tagged with legal-tech-related topics. This supplements the WebSearch queries in Step 2 by directly surfacing repositories that self-identify as legal tools via their GitHub topic tags.

### Topic List

Crawl the following GitHub Topics pages using WebFetch on `https://github.com/topics/{TOPIC}`:

**Primary topics (directly legal — include all results as candidates):**

| Topic slug | Description |
|---|---|
| `legaltech` | Core legal technology tag |
| `legal-tech` | Alternative spelling |
| `lawtech` | UK-style alternative |
| `legal` | Broad legal tag |
| `law` | General law tag |
| `legal-ai` | AI tools for law |
| `legal-nlp` | NLP for legal text |
| `legal-research` | Legal research tools |
| `caselaw` | Case law databases and tools |
| `contract-analysis` | Contract review and analysis |
| `contract-management` | Contract lifecycle management |
| `ediscovery` | eDiscovery tools |
| `regtech` | Regulatory technology |
| `legal-document` | Legal document processing |

**Secondary topics (adjacent — require legal-domain filtering in Step 3):**

| Topic slug | Description |
|---|---|
| `e-signature` | Electronic signature tools |
| `gdpr` | GDPR compliance tools |
| `compliance` | Regulatory compliance |
| `case-management` | Court/legal case management |
| `smart-contracts` | Smart legal contracts (filter for legal-specific only) |

### Crawl Procedure

1. For each topic in the list above, fetch `https://github.com/topics/{TOPIC}` using WebFetch.
2. Extract all repository URLs (`https://github.com/{owner}/{repo}`) and their descriptions from the page.
3. Add each repository URL to the candidate pool alongside candidates from Step 2.
4. All candidates (from both Step 2 and Step 2b) are deduplicated against the set from Step 1a before proceeding to Step 3.

### Throttling and Scope

- If `$ARGUMENTS` is not empty (targeted update), skip secondary topics entirely. Only crawl primary topics whose descriptions relate to the target section.
- For a full update, crawl all primary topics and all secondary topics.
- If a topic page returns zero results or fails to load, skip it silently and continue.
- Do NOT paginate beyond the first page of each topic — the first page (30 repos sorted by relevance) is sufficient.

### Mapping Topics to README Sections

When a repository is discovered via topic crawl, use both its topic tags and its description to determine which README section it belongs to. Use the following heuristics as a guide:

| GitHub Topic(s) | Likely README Section |
|---|---|
| `legal-ai`, `legaltech` + AI-related | AI Tools |
| `legal-nlp`, NLP + legal | Legal NLP & Datasets |
| `legal-research`, `caselaw` | Legal Research |
| `contract-analysis`, `contract-management` | Contract Management |
| `ediscovery` | eDiscovery & Litigation Support |
| `regtech`, `compliance` + legal | Compliance & Regulatory Technology |
| `gdpr`, `data-protection` | Privacy & Data Protection |
| `e-signature` | Document Management |
| `case-management` + legal/court | Practice Management |
| `smart-contracts` + legal | Legal Workflow Automation |
| `legal-document` | Document Management |

These are heuristics — always verify by reading the repository description and comparing against existing README section headings.

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

## Step 5: Link Rot Check

After writing new entries (Step 4) and before committing, check all GitHub repository entries in README.md for staleness.

### Procedure

1. Parse every GitHub URL in README.md matching `https://github.com/{owner}/{repo}`.
2. For each URL, fetch the repository's last push date using `gh api repos/{owner}/{repo} --jq '.pushed_at'` via Bash. If `gh` is unavailable, fall back to WebFetch on the repo page.
3. Calculate the age since the last update relative to today's date.

### Stale Threshold

A GitHub repository is **stale** if its most recent push is **more than 2 years** before the current date.

### Formatting Stale Entries

For any entry whose repo is stale, wrap the entire line content (after the `- `) in an HTML `<sub><i>` tag and add a staleness note. Transform the line from:

```
- [Name](URL) - Description.
```

to:

```
- <sub><i>[Name](URL) - Description. (Last updated: YYYY-MM)</i></sub>
```

If the entry already has a jurisdiction flag, preserve it outside the tag:

```
- FLAG <sub><i>[Name](URL) - Description. (Last updated: YYYY-MM)</i></sub>
```

### Unflagging Recovered Entries

If an entry is currently wrapped in `<sub><i>` staleness tags but the repo has been updated within the last 2 years, remove the staleness formatting and the `(Last updated: ...)` note to restore it to normal format.

### Scope

- Only check GitHub repository URLs. Skip non-GitHub URLs (commercial tools, web apps, etc.).
- If a repo returns a 404, mark it stale with `(Last updated: archived/removed)` instead of a date.
- Process all existing entries in the file, not just newly added ones.
- Rate limit: if more than 50 GitHub URLs need checking, batch them in groups of 10 with a brief pause between batches to avoid hitting GitHub rate limits.

---

## Step 6: Commit and Push

After all edits are complete (new entries from Step 4 and staleness updates from Step 5), run the following shell commands:

```bash
# Stage only README.md
git add README.md

# Check if there are staged changes
git diff --cached --quiet && echo "NO_CHANGES" || echo "HAS_CHANGES"
```

**If NO_CHANGES:** Skip commit and push. Go directly to Step 7 and report that no new entries were found.

**If HAS_CHANGES:** Commit and push:

```bash
# Count how many new entries were added
ENTRY_COUNT=$(git diff --cached README.md | grep '^\+- ' | wc -l)

# Count staleness formatting changes (lines changed to/from <sub><i>)
STALE_CHANGES=$(git diff --cached README.md | grep -c '<sub><i>' || true)

# Commit with descriptive message
git commit -m "chore: add ${ENTRY_COUNT} new entries, update staleness markers

Automated update via sync-and-update skill (search + topic crawl + link rot check).

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"

# Push to remote
git push origin HEAD
```

Do NOT use `--force`. If the push fails, print the error and stop. Do NOT retry destructively.

---

## Step 7: Print Summary

After completion, print a summary:

```
=== sync-and-update complete ===
- Pulled latest from remote: [yes/no]
- Categories discovered: [number]
- Search queries run: [number]
- GitHub topics crawled: [number]
- Total candidates found (search + topics): [number]
- Candidates after filtering: [number]
- New entries added: [number]
  - [Entry Name] → [Section]
  - [Entry Name] → [Section]
- Link rot check:
  - GitHub repos checked: [number]
  - Newly marked stale: [number]
  - Recovered from stale: [number]
  - Marked archived/removed: [number]
- Committed: [yes/no]
- Pushed to remote: [yes/no]
```

If zero entries were added and no staleness changes were made:
```
No new entries found — all candidates were duplicates, inactive, or out of scope.
No staleness changes detected.
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
- Do NOT remove stale entries — only format them with staleness markers
- Do NOT mark non-GitHub URLs as stale (commercial tools, web apps are exempt from link rot checks)
- Do NOT paginate GitHub topic pages beyond the first page
