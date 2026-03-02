# Quick GitHub Setup Reference

**Use this checklist when pushing the repository to GitHub for the first time.**

## Step 1: Push Repository to GitHub

```bash
git remote add origin https://github.com/[USERNAME]/awesome-legal-apps.git
git branch -M main
git push -u origin main
```

## Step 2: Configure Repository Settings (5 minutes)

### 2a. Set Default Branch
- Navigate to: **Settings > Branches**
- Default branch: Select `main`
- Click Save

### 2b. Add Description and Topics
- Navigate to: **Settings > About**
- Description: `A curated list of awesome legal technology tools, AI models, research resources, and open source projects for legal professionals and technologists.`
- Topics: Click "Manage topics" and add:
  - `awesome-list`
  - `awesome`
  - `legal-tech`
  - `legal-tools`
  - `legal-technology`
  - `curated-list`
  - `open-source`
- Click Save

### 2c. Verify License
- Navigate to: **Settings > License**
- License should show: `CC0 1.0 Universal`
- If not auto-detected, select manually from dropdown

## Step 3: Enable Features (2 minutes)

- Navigate to: **Settings > Features**
- Ensure enabled:
  - [x] Issues
  - [x] Discussions (recommended)
  - [x] Projects (optional)
- GitHub Pages: Leave disabled for now

## Step 4: Create Branch Protection Rule (5 minutes)

- Navigate to: **Settings > Branches**
- Click "Add rule"
- Branch name pattern: `main`
- Check:
  - [x] Require a pull request before merging
  - [ ] Dismiss stale pull request approvals when new commits are pushed
  - [x] Require branches to be up to date before merging
  - [ ] Include administrators
- Click Create

## Step 5: Create Issue Labels (3 minutes)

- Navigate to: **Issues > Labels**
- Create these labels:

| Name | Color | Description |
|------|-------|-------------|
| `suggestion` | #0366d6 | Tool suggestion or feature request |
| `fix` | #d73a49 | Bug fix or broken link |
| `documentation` | #0075ca | Documentation improvements |
| `good-first-issue` | #7057ff | Good issue for first-time contributors |
| `conflict-of-interest` | #ffa500 | Requires conflict of interest review |
| `waiting-for-info` | #cccccc | Waiting for contributor clarification |

## Step 6: Verify Community Profile

- Navigate to: **Insights > Community**
- Should show green checkmarks for:
  - [x] Code of Conduct
  - [x] Contributing
  - [x] License
  - [x] README
  - [x] Issue templates
  - [x] Pull request template

## Step 7: Enable Status Checks (Optional - Do Later)

When CI/CD is configured:
- Navigate to: **Settings > Branches > main > Require status checks**
- Add workflows as they are created:
  - awesome-lint validation
  - Link checker
  - etc.

## Verification Checklist

After completing all steps:

- [ ] Repository is public
- [ ] Default branch is `main`
- [ ] Description added with correct text
- [ ] 7 topics/tags added
- [ ] License shows CC0 1.0 Universal
- [ ] Branch protection rule created for main
- [ ] 6 issue labels created
- [ ] Issues and Discussions enabled
- [ ] Community profile shows all green checkmarks
- [ ] PR template appears when creating new PRs
- [ ] Issue template available when creating issues

## Time Estimate

Total setup time: **15-20 minutes**

## Need Help?

- Full documentation: See `GITHUB_SETTINGS.md`
- Governance: See `GOVERNANCE.md`
- Code of Conduct: See `CODE_OF_CONDUCT.md`
- Contributing: See `../contributing.md`

## After Setup

1. Create first release: GitHub > Releases > Create release v0.1.0
2. Announce project to legal tech community
3. Begin accepting contributions via PR template
4. Monitor issues and discussions

---

**Note:** Screenshots and detailed instructions for each step are available in `GITHUB_SETTINGS.md` if you need more detail.
