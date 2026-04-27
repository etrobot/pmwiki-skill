---
name: Project Wiki
description: Main entry point for the Project Management Wiki system. Use this Skill for scenarios such as "Project Wiki", "Knowledge Base", "Wiki Scoring", "Wiki Structure", "Wiki Health Check", "Wiki Maintenance", "Content Classification", "Definition Alignment", "Glossary", "Decision Records", "SOP", "Wiki Changes", etc.
---

# Project Wiki Skill Entry Point

Select a sub-Skill based on user intent:

---

## Routing Logic

| User Intent | Loaded Skill |
|-------------|--------------|
| Build Wiki from scratch / Choose mode | → [`SKILL_lintstart.md`](./SKILL_lintstart.md) |
| Lightstart mode (new project) | → [`SKILL_lintstart.md`](./SKILL_lintstart.md) |
| Precise mode / Layer templates | → [`SKILL_iteration.md`](./SKILL_iteration.md) |
| How to write Architecture/Data/Business/Interaction/QA | → [`SKILL_iteration.md`](./SKILL_iteration.md) |
| Evaluate entry quality / Scoring | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |
| Daily Wiki updates / Evaluate → Improve | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |
| Weekly health check / Milestone check | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |
| Record changes / Decisions / Closing migration | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |

---

## Sub-Skill Overview

### SKILL_lintstart.md — Lightstart
- Comparison of two modes (Lightstart vs Precise)
- Lightstart directory structure
- General rules (README facade, asset management, naming conventions)

### SKILL_iteration.md — Iteration Mode + Layer Templates
- Precise mode complete directory structure + splitting timing
- Architecture layer template (tech stack, coding standards, infrastructure, ADR)
- Data layer template (data model, dictionary, cache, migration, security)
- Business layer template (core flows, business rules, API, module design)
- Interaction layer template (UI standards, components, user paths)
- QA template (test cases, automation, incident postmortem)

### SKILL_maintenance.md — Evaluation & Improvement
- Evaluation system (scoring dimensions, priority, workflow, storage)
- Daily process: Evaluate → Improve
- Weekly health check / Milestone check
- Trigger mechanism / Change management / Closing migration

---

## Reference Files

- `scoring_criteria.json` — Complete scoring criteria for five categories (equal weight)
- `scorer.py` — Mean calculation script (100-point scale)
