---
phase: 05-automated-update-system
plan: 02
subsystem: infra
tags: [github-actions, cron, claude-code-action, git-auto-commit, automation]

# Dependency graph
requires:
  - phase: 05-automated-update-system
    provides: ".claude/skills/update-list/SKILL.md — skill invoked by this workflow's prompt"
provides:
  - ".github/workflows/update-list.yml — monthly cron workflow that invokes update-list skill and auto-commits README.md changes"
affects: ["phase-06"]

# Tech tracking
tech-stack:
  added:
    - anthropics/claude-code-action@v1
    - stefanzweifel/git-auto-commit-action@v5
    - actions/checkout@v4
  patterns: [cron-scheduled-workflow, gh-pat-oidc-workaround, scoped-auto-commit]

key-files:
  created:
    - .github/workflows/update-list.yml
  modified: []

key-decisions:
  - "GH_PAT used on both checkout and claude-code-action steps — GITHUB_TOKEN fails on cron-triggered runs due to OIDC bug #814"
  - "file_pattern: README.md scopes commit detection to README.md only — prevents spurious commits"
  - "claude_args: --max-turns 20 caps execution to prevent infinite loops"
  - "workflow_dispatch included for manual testing without waiting for cron schedule"
  - "Checkpoint auto-approved (human-verify type, auto_advance=true) — structural verification passed; user must still add GH_PAT and ANTHROPIC_API_KEY secrets before first run"

patterns-established:
  - "Cron workflow pattern: always use fine-grained PAT for both checkout and action auth in scheduled workflows"
  - "Auto-commit pattern: always scope file_pattern to specific file(s) to prevent unintended commits"

requirements-completed:
  - UPDT-02
  - UPDT-03

# Metrics
duration: 5min
completed: 2026-03-02
---

# Phase 05-02: GitHub Actions Workflow Summary

**Monthly cron workflow that invokes the update-list Claude Code skill and auto-commits README.md changes using GH_PAT to bypass known OIDC cron auth failure**

## Performance

- **Duration:** 5 min
- **Started:** 2026-03-02T00:05:00Z
- **Completed:** 2026-03-02T00:10:00Z
- **Tasks:** 1 automated + 1 checkpoint (auto-approved)
- **Files modified:** 1

## Accomplishments
- Created `.github/workflows/update-list.yml` with cron schedule `0 9 1 * *` (09:00 UTC, 1st of month)
- Included `workflow_dispatch` for manual testing without waiting for cron
- Configured `anthropics/claude-code-action@v1` with `GH_PAT` workaround for OIDC cron bug
- Auto-commit step scoped to `README.md` only — no noise on months with no new entries
- `--max-turns 20` safety cap on Claude execution

## Task Commits

1. **Task 1: Create .github/workflows/update-list.yml** - `81c91a9` (feat)

**Checkpoint (Task 2):** ⚡ Auto-approved (human-verify, auto_advance=true). Structural validation passed.

## Files Created/Modified
- `.github/workflows/update-list.yml` - Monthly cron workflow invoking update-list skill with auto-commit

## Decisions Made
- GITHUB_TOKEN explicitly excluded — known OIDC auth failure on cron-triggered runs (issue #814 open as of 2026-03-02). Fine-grained PAT required.
- `prompt: "/update-list"` triggers automation mode in claude-code-action (no @claude mention needed)
- `fetch-depth: 0` on checkout ensures full git history available to Claude during skill execution

## Deviations from Plan
None - plan executed exactly as written.

## Issues Encountered
None during code creation. Runtime testing requires manual secrets setup (see User Setup Required below).

## User Setup Required

**External services require manual configuration before the workflow can run:**

1. **Create a fine-grained Personal Access Token:**
   - Go to: https://github.com/settings/tokens?type=beta
   - Name: `awesome-legal-apps-update-bot`
   - Repository access: Select this repository only
   - Permissions: Contents → Read and write
   - Expiration: 1 year or no expiration

2. **Add GH_PAT secret to repository:**
   - Go to: https://github.com/{your-username}/awesome-legal-apps/settings/secrets/actions
   - New repository secret → Name: `GH_PAT`, Value: (PAT from step 1)

3. **Add ANTHROPIC_API_KEY secret:**
   - Same Secrets page → New repository secret
   - Name: `ANTHROPIC_API_KEY`, Value: (your Anthropic API key from console.anthropic.com)

4. **Run manual test:**
   - Go to: https://github.com/{your-username}/awesome-legal-apps/actions
   - Click "Auto-Update Legal Apps List" → "Run workflow"
   - Verify: green check, no auth errors, commit appears or "nothing to commit" message

## Next Phase Readiness
- Automated update pipeline complete — skill + workflow fully wired
- Phase 5 ready for verification
- Phase 6 (awesome-list submission) requires 30-day repo age (see STATE.md blockers)

---
*Phase: 05-automated-update-system*
*Completed: 2026-03-02*
