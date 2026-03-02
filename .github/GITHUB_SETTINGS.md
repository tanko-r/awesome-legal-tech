# GitHub Repository Settings Configuration

This document outlines the settings that need to be configured on GitHub when the repository is first pushed. These settings ensure the project maintains quality standards, security, and governance consistency.

## Repository Settings

### General

**Default Branch**
- Set to: `main`
- Purpose: Ensure stable, reviewed code is the default branch
- Action: Settings > Default branch > Select "main"

**Description**
- Set to: "A curated list of awesome legal technology tools, AI models, research resources, and open source projects for legal professionals and technologists."
- Purpose: Clear description for GitHub search and discovery
- Action: Settings > About > Edit repository details

**Topics/Tags**
Add the following topics to improve discoverability:
- `awesome-list`
- `awesome`
- `legal-tech`
- `legal-tools`
- `legal-technology`
- `curated-list`
- `open-source`

Action: Settings > About > Topics field (click "Manage topics")

**Visibility**
- Set to: Public
- Purpose: Open-source community project
- Action: Settings > Danger Zone > Change visibility (if not already public)

### License

**License**
- Select: CC0 1.0 Universal
- Current File: `/license`
- Action: Settings > License > Select "CC0 1.0 Universal" from dropdown
- Note: GitHub may automatically detect this license from the `/license` file

## Branch Protection Rules

### Main Branch Protection

**Path:** Settings > Branches > Branch protection rules > Add rule

**Branch name pattern:** `main`

**Protection Settings:**

1. **Require pull request reviews before merging**
   - Required approving reviews: 1
   - Dismiss stale PR approvals when new commits are pushed: Enabled
   - Require review from code owners: Disabled (optional, enable if CODEOWNERS file is created)

2. **Require status checks to pass before merging**
   - Require branches to be up to date before merging: Enabled
   - Do not add required status checks yet (will be added when CI/CD is configured)

3. **Require branches to be up to date before merging**
   - Enabled

4. **Include administrators**
   - Unchecked (administrators can bypass)

5. **Restrict who can push to matching branches**
   - Unchecked (allow all contributors to create branches)

6. **Require up-to-date branches before merging**
   - Checked

## Collaboration Settings

### Team Access

When team members are added:
- Assign "Maintain" role to trusted reviewers
- Assign "Triage" role to contributors who help with issues
- Keep base access at "Read" for general community

Action: Settings > Collaborators and teams

### Discussions

**Enable GitHub Discussions** (optional but recommended)
- Purpose: Community discussion separate from issues
- Action: Settings > Features > Enable "Discussions"
- Purpose: Allow community to discuss ideas before formal proposals

## Issue Settings

### Issue Templates

The following templates are configured:
- `.github/ISSUE_TEMPLATE/tool-suggestion.md` - Standard tool suggestion form

Enable issue templates to guide users:
- Action: Settings > Features > Issues > Enabled

## Pull Request Settings

### Pull Request Template

The following template is configured:
- `.github/PULL_REQUEST_TEMPLATE.md` - Standard PR checklist

This will automatically appear when contributors create new PRs.

## Security Settings

### Dependabot (if package.json exists)

If the project uses npm (for awesome-lint, etc.):

1. **Enable Dependabot version updates**
   - Action: Settings > Code security and analysis > Enable "Dependabot alerts" and "Dependabot security updates"

2. **Configure `.github/dependabot.yml`** (optional)
   - Useful if the project has npm dependencies

## Labels

Create standard labels for issue organization:

| Label | Color | Description |
|-------|-------|-------------|
| `suggestion` | #0366d6 | Tool suggestion or feature request |
| `fix` | #d73a49 | Bug fix or broken link |
| `documentation` | #0075ca | Documentation improvements |
| `good-first-issue` | #7057ff | Good issue for first-time contributors |
| `conflict-of-interest` | #ffa500 | Requires conflict of interest review |
| `waiting-for-info` | #cccccc | Waiting for contributor clarification |

Action: Settings > Labels > Create new label

## Actions & CI/CD (Future)

When ready to add CI/CD:

1. **Awesome-lint validation** (recommended)
   - Validates list format and links
   - File: `.github/workflows/awesome-lint.yml`

2. **Link checker** (optional)
   - Periodically checks for broken links
   - File: `.github/workflows/link-checker.yml`

3. **Stale issue management** (optional)
   - Auto-closes inactive issues
   - File: `.github/workflows/stale.yml`

## README Badge

Add this badge to display awesome-list status:

```markdown
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
```

Status: Already included in README.md

## Suggested GitHub Features

### 1. Repository Releases

When ready to release stable snapshots:
- Action: Click "Create a new release"
- Tag format: `v0.1.0` (semantic versioning)
- Include changelog of added/updated tools

### 2. GitHub Pages (Optional)

Create a website for the project:
- Action: Settings > Pages
- Source: Deploy from a branch (main or /docs)
- Use a theme like `minimal` or `slate`

### 3. Community Profile

Ensure community profile is complete:
- Action: Insights > Community
- Check: README, License, Contributing, Code of Conduct, Pull Request Template

## Verification Checklist

Before declaring GitHub setup complete:

- [ ] Main branch set as default
- [ ] Repository description and topics added
- [ ] License automatically detected or manually selected (CC0 1.0 Universal)
- [ ] Branch protection rule created for main branch
- [ ] Pull request template visible when creating PRs
- [ ] Issue templates available in issue creation
- [ ] Labels created for issue management
- [ ] Code of Conduct visible in Community profile
- [ ] Contributing guidelines linked properly
- [ ] Governance documentation in place

## Notes

- All files in `.github/` folder are automatically discovered and used by GitHub
- No additional configuration needed for templates to work
- Branch protection rules can be modified later without affecting existing content
- Settings can be imported from command line using GitHub CLI if needed

## References

- [GitHub Docs - Repository Settings](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features)
- [GitHub Docs - Branch Protection Rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches)
- [Awesome GitHub Discussions Guide](https://docs.github.com/en/discussions)
