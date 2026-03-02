---
created: 2026-03-02T21:35:00.689Z
title: Add jurisdiction flag emojis to entries
area: general
files:
  - README.md
---

## Problem

The awesome-legal-apps list currently doesn't differentiate tools and projects by their jurisdiction or origin. Users looking for legal tech solutions specific to their country (e.g., India, UK, Canada) have to research each tool individually to determine applicability. Adding jurisdiction flags would improve discoverability and help users quickly identify region-relevant solutions.

Example: A lawyer in India needs legal tech that works within Indian law — flag emojis like 🇮🇳 would make it immediately clear which entries are relevant.

## Solution

1. Add 2-letter country code flag emojis (🇮🇳, 🇬🇧, 🇨🇦, etc.) next to entries in README.md that are:
   - Developed by companies based in specific jurisdictions
   - Explicitly designed for a jurisdiction's legal system
   - Have jurisdiction-specific features or compliance (e.g., India GST compliance, UK GDPR focus)

2. Add a legend in the README explaining the flag meanings

3. Update the update-list skill (Phase 5) to detect and preserve jurisdiction flags when researching new entries

4. Consider: Should multi-jurisdiction tools get multiple flags, or only the primary jurisdiction?
