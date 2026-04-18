---
name: Project Wiki
description: Main entry point for the Project Management Wiki system. Use this Skill for scenarios such as "Project Wiki", "Knowledge Base", "Wiki Scoring", "Wiki Structure", "Wiki Health Check", "Wiki Maintenance", "Content Classification", "Definition Alignment", "Glossary", "Decision Records", "SOP", "Wiki Changes", etc.
---

# Project Wiki Skill Entry Point

This Skill is divided into two sub-Skills. Select one based on user intent:

---

## Routing Logic

| User Intent | Loaded Skill |
|-------------|--------------|
| Build Wiki directory structure from scratch | → [`SKILL_setup.md`](./SKILL_setup.md) |
| Score / Assess quality of an entry | → [`SKILL_setup.md`](./SKILL_setup.md) |
| Understand Wiki content classification | → [`SKILL_setup.md`](./SKILL_setup.md) |
| Daily Wiki update process | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |
| Weekly health check / Milestone check | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |
| Record changes / Decisions | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |
| Project closing knowledge transfer | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |

---

## Sub-Skill Overview

### SKILL_setup.md — Setup and Scoring
Applicable for **initial setup** or **entry quality assessment**:
- Wiki physical structure (hierarchical nesting standards, `_index.md` standards)
- Five major content classification systems
- Scoring dimensions and priority rules
- LLM scoring prompt + scoring script usage
- Scoring result storage and retrieval (`_scores/` directory)

### SKILL_maintenance.md — Maintenance and Checks
Applicable for **daily operations** and **regular reviews**:
- Daily update process (Execution layer / Revision layer collaboration)
- Weekly health check items (Orphans, contradictions, timeliness, index, etc.)
- Milestone-specific checks
- Rapid lookup of trigger mechanisms
- Change record / Decision record templates
- Project closing knowledge transfer

---

## Reference Files

- `scoring_criteria.json` — Complete scoring criteria for five categories
- `scorer.py` — Weighted calculation script
