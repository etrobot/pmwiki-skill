---
name: Project Wiki Lightstart
description: Quick-start Wiki for new projects. Use this Skill for scenarios such as "Building Wiki Structure", "Organizing Wiki Directories", "Wiki Content Classification", "Creating Wiki", "Wiki Setup", "Lightstart", etc.
---

# Project Wiki Lightstart Skill

Focuses on building Wiki from scratch, providing two modes: **Lightstart** (new projects) and **Precise** (refactoring/iteration).

Evaluation and improvement process → [`SKILL_maintenance.md`](./SKILL_maintenance.md)

---

## I. Two Modes

| | Lightstart Mode | Precise Mode |
|--|-----------------|--------------|
| **Use Case** | New project, quick start | Refactoring project, iteration phase, multi-module |
| **Structure** | Flat, 5 .md files搞定 | Directories by layer, files split by topic |
| **Principle** | One file covers all, good enough is enough | Split files by topic, each in its place |
| **Evolution** | Upgrade to Precise when content expands | Add/remove sub-files as needed, structure already in place |

> **Upgrading from Lightstart to Precise**: Split `01-architecture.md` into `01-architecture/` directory, move original .md content into sub-files, update navigation links in `README.md`.

Complete directory structure, splitting timing, and detailed layer templates for Precise mode → [`SKILL_iteration.md`](./SKILL_iteration.md)

---

## II. Lightstart Mode (New Project)

```
docs/
├── README.md            # Facade: project overview, navigation
├── 01-architecture.md   # Tech stack, standards, deployment
├── 02-data.md           # Table structure, ER diagram, cache
├── 03-business.md       # Core logic, flowcharts, API
├── 04-interaction.md    # Frontend logic, UI design
├── 05-qa.md             # Test cases, incident postmortem
└── assets/              # Only folder: stores images, screenshots
```

> **5 .md + 1 assets + README**, each file covers the full content of its layer, no sub-files.

### One-Sentence Positioning per Layer

| Layer | Question Answered | What to Write in Lightstart Mode |
|-------|-------------------|----------------------------------|
| **Architecture** | How the system is built, why | Tech stack + coding standards + infrastructure + architecture decisions |
| **Data** | What the data looks like, where stored, how it flows | Table structure + data dictionary + cache + migration + security |
| **Business** | What the system does, what the rules are | Core flows + business rules + API interfaces + module design |
| **Interaction** | What the user sees, how they operate | UI standards + core components + user paths |
| **QA** | How to verify, what went wrong | Test cases + automation + incident postmortem |

---

## III. General Rules

### README.md Facade

Regardless of mode, `README.md` is the entry point and must include:

```markdown
# Project Name

## Overview
[One sentence describing what the project does]

## Documentation Navigation
| Document | Description |
|----------|-------------|
| [01-Architecture](./01-architecture/) | Tech stack, deployment, architecture decisions |
| [02-Data](./02-data/) | Table structure, cache, data dictionary |
| [03-Business](./03-business/) | Core flows, interfaces, module design |
| [04-Interaction](./04-interaction/) | UI standards, components, user paths |
| [05-QA](./05-qa/) | Test cases, incident postmortem |
```

### Asset Management

All asset files are stored uniformly in `assets/`, **not mixed with .md files**:

- **Images**: Flowcharts/architecture diagrams prefer `.svg` (version controllable), screenshots use `.png`
  - Reference: `![Description](../assets/images/architecture-diagram.svg)`
- **Attachments**: `.xlsx/.pdf` etc. stored in `assets/files/`; .md only keeps summary + link
- **Cross-document reuse**: When the same asset is referenced by multiple .md files, no need to copy, just point to the same file

### Naming Conventions

| Rule | Description | Example |
|------|-------------|---------|
| Directories in English, with numeric prefix | Numeric prefix ensures ordering, English ensures path safety | `01-architecture/`, `02-data/` |
| File name = Topic | Directly express content, no numbering | `tech-stack.md`, `cache.md` |
| Time prefix only for time-based ordering | Decision records, changelogs, etc. | `2024-Q1-decision-summary.md` |
| Assets named by content | Unified under `assets/` | `architecture-diagram.svg`, `payment-sequence-diagram.png` |
| Maximum path depth 3 levels | `docs/03-business/core-flows/order-flow.md` is the limit | Flatten if exceeded |

---

## Reference Files

- [`SKILL_iteration.md`](./SKILL_iteration.md) — Precise mode: complete directory structure + detailed layer templates
- [`SKILL_maintenance.md`](./SKILL_maintenance.md) — Evaluation & improvement: scoring system, daily process, health check, change management, closing migration
- `scoring_criteria.json` — Complete scoring criteria for five categories (with descriptions)
- `scorer.py` — Mean calculation script (single / batch / milestone urgent mode)
