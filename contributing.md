# Contributing to Awesome Legal Apps

Thank you for your interest in contributing to Awesome Legal Apps! This document explains how to suggest additions and what we look for in entries.

## Before You Suggest a Tool

Please review these guidelines to ensure your suggestion aligns with our standards:

### Inclusion Criteria

Tools must meet **all** of these criteria to be included:

1. **Maintained**: The tool is actively developed or maintained. No abandonware, no projects abandoned for >2 years without updates.
2. **Active Resource**: The tool is publicly accessible, working, and available for legal use. No dead links, no paywalls without public tier.
3. **Legal Focus**: The tool serves a clear legal use case — legal professionals, law students, or legal technologists are the primary audience.
4. **FOSS or Development Targeted**: The tool is either free and open source software or it is private commercial software that is intended to be used to facilitate legal tech development.  Otherwise, the list would grow out of control to include all commercial legal tech.
5. **Quality**: The tool has clear documentation or public information explaining what it does, who uses it, and how to access it.
6. **Not Marketing Copy**: Descriptions must be written independently and accurately, not copied from vendor marketing materials.
7. **No Conflicts Disqualified**: Conflict of interest does not automatically disqualify an entry — but must be fully disclosed.
8. **Verifiable**: At time of inclusion, the tool must be verified to exist, be active, and meet the above criteria.

### Entry Format

All entries follow this exact format:

```
- [Tool Name](https://link-to-tool.com) - Brief, original description that names the purpose and target user.
```

**Rules:**
- Tool name in square brackets, link in parentheses
- Single space, hyphen, single space before description
- Description starts with a capital letter and ends with a period
- Description should be 1–2 sentences maximum
- No vendor marketing language; explain what the tool does and who it's for
- Examples:
  - ✓ "Docassemble is an open source platform for generating legal documents through automated interviews, used by legal aid organizations and solo practitioners."
  - ✗ "Docassemble is the leading document automation platform for law firms" (marketing language)

### License Column

Entries are maintained as rows in the section tables, with these columns:

```
| Name | Description | Tech Stack | License | Date Added |
```

The **License** column records how each tool is licensed. It enforces inclusion criterion #4 (FOSS or development-targeted) and tells readers whether they can freely reuse the tool. Fill it as follows:

- **FOSS tools** — the SPDX identifier from the project's `LICENSE` file (e.g., `MIT`, `Apache-2.0`, `AGPL-3.0`, `GPL-3.0`, `BSD-3-Clause`, `CC0-1.0`). For GitHub repos, this is the license shown on the repo page.
- **`Other`** — the project has a license file, but it is non-standard or cannot be matched to an SPDX identifier.
- **`No license`** — a public repository with no `LICENSE` file. The code is visible but grants no reuse rights, so treat it as all-rights-reserved.
- **`Not FOSS`** — proprietary or commercial software that is *not* open source but still qualifies under criterion #4 (a private tool that facilitates legal tech development, or an already-accepted public-good resource).
- **`Public domain`** — government sources and works dedicated to the public domain (e.g., U.S. federal data).
- **`—`** — not applicable (a community, newsletter, or research lab rather than a software artifact).

A `Not FOSS` label is only valid if the tool independently satisfies criterion #4 — a general commercial legal product that does not facilitate development does not qualify.

## How to Suggest a Tool

### Step 1: Open a Pull Request

Click **New Pull Request** and use our template. The template includes:
- A checklist for the inclusion criteria above
- A field to disclose any conflicts of interest
- A field for the tool's category

### Step 2: Provide Required Information

Fill in:
- **Tool Name**: Exact name as it appears publicly
- **URL**: Direct link to the tool (not a review or blog post about it)
- **Category**: Which section it belongs in (AI Tools, Legal Research, etc.)
- **Description**: 1–2 sentences, original description
- **Criteria Checklist**: Confirm the tool meets all 7 criteria
- **Conflict of Interest**: If you're affiliated with the tool, say so clearly. This doesn't disqualify you.

### Step 3: Description Guidelines

Good descriptions answer:
- What does the tool do?
- Who is it for?

Examples:

- **Bad**: "Amazing contract management software" (too vague, marketing language)
- **Good**: "AI-powered contract review and negotiation platform for enterprise legal teams"

- **Bad**: "Best legal research tool" (subjective)
- **Good**: "Free access to case law, statutes, and court opinions covering U.S. federal and state courts"

- **Bad**: "All-in-one solution" (marketing cliché)
- **Good**: "Practice management system for solo and small law firms, including time tracking, billing, and client database"

### Step 4: Verification

At time of inclusion, we verify:
- The link is live and accessible
- The tool is actively maintained (recent commits, updates, or company updates)
- The description accurately reflects what the tool does
- The tool is not abandonware or defunct

## Conflict of Interest Disclosure

If you maintain, work for, or are affiliated with a tool you're suggesting, **disclose it in your PR**. Conflicts of interest do not automatically disqualify suggestions — they must simply be transparent.

Examples of disclosure:
- "I am the maintainer of [Tool]"
- "I work for [Company] which built [Tool]"
- "I have a financial stake in [Company]"
- "No conflict of interest"

Transparent disclosure lets reviewers and community members evaluate your suggestion with full context.

## Review Process

1. You open a PR with a suggested tool
2. A maintainer reviews for:
   - Compliance with inclusion criteria
   - Entry format and description quality
   - Conflict of interest transparency
3. We may ask for changes (e.g., rewording a description, verifying a link)
4. Once approved, we merge and the tool appears in the list

## Questions?

See our [Code of Conduct](code-of-conduct.md) for community standards. Feel free to open an issue if you have questions about whether a tool qualifies or need clarification on any guideline.

Thank you for helping curate the best legal technology resources!
