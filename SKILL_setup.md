---
name: Project Wiki Setup and Scoring
description: Establish the project Wiki directory system and perform quality scoring on entries. Use this Skill for scenarios such as "Building Wiki Structure", "Organizing Wiki Directories", "Wiki Content Classification", "Scoring Entries", "Wiki Scoring", "Scoring Script", "_scores", etc.
---

# Project Wiki Setup and Scoring Skill

Covers two areas: **establishing the Wiki system** (physical structure + content classification) and **scoring entries** (scoring criteria + script + result storage).

Daily maintenance, health checks, change management, and closing migration are found in → [`SKILL_maintenance.md`](./SKILL_maintenance.md)

---

## I. Wiki Physical Structure

**A Wiki is essentially a folder tree**, composed of a mix of the following file types:

| File Type | Purpose | Naming Suggestion |
|----------|------|----------|
| `.md` Markdown | Main content carrier: Entry text, SOPs, glossary, decision records, etc. | `EntryName.md` |
| Image `.png/.jpg/.svg` | Flowcharts, architecture diagrams, screenshots, illustrations | `EntryName_Illustration.png` |
| Video `.mp4/.mov` | Demo recordings, operation demonstrations, meeting replay segments | `EntryName_Demo.mp4` |
| Audio `.mp3/.m4a` | Meeting recordings, oral memos | `EntryName_Recording.mp3` |
| Other files | Templates, tables, raw attachments (`.xlsx/.pdf`, etc.) | Place in `/raw` read-only zone |
| Folder | Organizes hierarchical structure | See directory standards below |

### Directory Standards

The Wiki directory structure supports **hierarchical nesting**, adapting to various scales from simple projects to large, complex ones. Each level uses an `_index.md` index file to provide an overview and navigation for that level.

#### Level Design Principles

| Level | Meaning | Example |
|------|------|----------|
| L1 | Content categories (Fixed five categories + Support areas) | `ProjectAssets/`, `ProcessRules/`, `raw/`, `ChangeRecords/` |
| L2 | Module / Subsystem / Business Domain | `ClientSide/`, `DataPlatform/`, `Infrastructure/` |
| L3 | Functional Domain / Phase / Topic | `Auth/`, `Payment/`, `Sprint-03/` |
| L4+ | Finer granularity (as needed) | `OAuth2/`, `SMSVerification/` |

> **When to add a level**: Split into a subdirectory when there are more than **8** `.md` files in the same directory, or when it involves **3 or more different sub-topics**.
> **When to keep it flat**: If a subdirectory only has **1–2 files**, distinguish them directly with filename prefixes; do not create a directory.

### Project Example (Multi-module / Multi-subsystem)

```
/wiki
    _index.md                                 ← Wiki Homepage
    /ProjectAssets/
        _index.md
        ProjectOverview.md                    ← Global assets at L1
        ResourceLedger.md
        /ClientSide/                           ← L2: Split by subsystem
            _index.md
            DeliverableDefinition.md
            ProjectStatusSnapshot.md
            ClientArchitecture.svg
            /Auth/                             ← L3: Subdivided by functional domain
                _index.md
                OAuth2Integration.md
                SMSVerification.md
                PermissionMatrix.md
            /Payment/
                _index.md
                PaymentProcess.md
                ReconciliationRules.md
        /DataPlatform/
            _index.md
            DeliverableDefinition.md
            DataArchitecture.svg
            /RealTimeComp/
                _index.md
                FlinkJobList.md
                MonitoringAlertingRules.md
            /DataWarehouse/
                _index.md
                LayeredDesign.md
                DefDefinition.md
        /Infrastructure/
            _index.md
            ContainerPlatform.md
            CI-CDPipeline.md
    /ProcessRules/
        _index.md
        DecisionProcess.md                     ← Global processes at L1
        CommunicationMechanism.md
        /ClientSide/
            _index.md
            ReleaseProcess.md
            CanaryRules.md
        /DataPlatform/
            _index.md
            DataChangeApprovalProcess.md
            DataQualityCheckProcess.md
    /ProjectSemantics/
        _index.md
        GlobalGlossary.md                       ← Global semantics at L1
        /ClientSide/
            _index.md
            ClientGlossary.md
            ClientStatusDefinition.md
        /DataPlatform/
            _index.md
            MetricDefinition.md
            DataPlatformGlossary.md
    /ExperienceAccumulation/
        _index.md
        /DecisionRecords/
            _index.md
            2024-Q1DecisionSummary.md
            2024-Q2DecisionSummary.md
        /BestPractices/
            _index.md
            PerformanceOptimization.md
            CrossTeamCollaboration.md
        RiskAndIssueLog.md
        AntiPatterns.md
        AIUsageExperience.md
    /OperatingProcedures/
        _index.md
        KickoffSOP.md                           ← Global SOP
        ClosingSOP.md
        /ClientSide/
            _index.md
            ReleaseSOP.md
            RollbackSOP.md
            ReleaseDemo.mp4
        /DataPlatform/
            _index.md
            DataMigrationSOP.md
            TroubleshootingSOP.md
    /_scores/                                    ← Scoring results storage
        latest.json                              ← Latest full scoring snapshot
        /2024-03-15/
            scores.json
            report.md

/raw                                            ← Raw documents read-only zone
    /MeetingMinutes/
        /2024-Q1/
        /2024-Q2/
    /Requirements/
        /ClientSide/
        /DataPlatform/
    /ExternalResources/

/ChangeRecords
    _index.md
    /ScopeChanges/
        ClientScopeChangeHistory.md
        DataPlatformScopeChangeHistory.md
    /DefinitionChanges/
        DefinitionChangeHistory.md
    DecisionRecords.md
    RiskAndIssueLog.md
```

#### `_index.md` Index File Standard

The `_index.md` in each directory is the **navigation hub** for that level and must include:

```markdown
# [Directory Name]

## Overview
[One-sentence description of the scope covered by this directory]

## Navigation
- [Subdirectory or Entry Name](./relative-path) — One-sentence description
## Recent Updates
| Date | Entry | Change Summary |
|------|------|----------|
| 2024-03-15 | OAuth2Integration.md | Added third-party login flow |
```

#### Naming Conventions

| Rule | Description | Example |
|------|------|----------|
| Directory names use English phrases | Clearly express the content domain | `Auth/`, `CI-CDPipeline/` |
| Filename = Entry Title | Directly expressive, no numbering | `OAuth2Integration.md`, `PaymentProcess.md` |
| Time prefixes for chronological sorting | Use only when chronological order is needed | `2024-Q1DecisionSummary.md` |
| Multimedia in the same directory as the .md | Avoid cross-directory references | `ReleaseSOP.md` + `ReleaseDemo.mp4` in the same folder |
| Path depth max 5 levels | `/wiki/L1/L2/L3/L4/File.md` is the upper limit | Merge or flatten if exceeded |

### Rules for Using Multimedia Files

- **Images**: Prefer `.svg` (version controllable) for flowcharts/architecture, `.png` for screenshots; use relative paths in md: `![Description](./ImageName.png)`
- **Videos**: Primarily for hands-on demos in operating SOPs; store large files externally (shared drive) and record the link in md instead of embedding
- **Audio**: Store meeting recordings in `/raw` (organized by date subdirectories); do not enter the wiki body; oral memos must be converted to md text within 24 hours
- **Attachments**: Raw files belong in `/raw` (organized by module subdirectories); wiki body only keeps summaries or key conclusions with links to raw files
- **Cross-directory references**: Do not reference multimedia files across L1 categories; if reuse is needed, copy to the referencing directory or extract to `/wiki/_shared/`

---

## II. Content Classification System

Wiki content is organized into five major categories, each with independent scoring dimensions. In complex projects, each category establishes subdirectories by **Module / Subsystem**:

**Project Assets** — Project goals, deliverable definitions, resource ledger, project status snapshots
**Process Rules** — Decision flows, change management rules, communication mechanisms, risk response rules
**Project Semantics** — Glossaries, metric definitions, status definitions, role/responsibility boundaries
**Experience Accumulation** — Decision records, risk and issue logs, best practices, anti-patterns, AI usage experience
**Operating Procedures** — Kickoff SOPs, iteration SOPs, risk handling SOPs, closing SOPs

> **Category × Module**: The five major categories are the **horizontal axis** of content, while modules/subsystems are the **vertical axis**. Global content (e.g., global glossary) is placed under L1; module-specific content is placed in module subdirectories under L1.

> **Key Principle**: Scope changes must be explicitly recorded and cannot be silently extended. AI usage experience is tied to model versions; after a model update, it is automatically marked as "to be verified".

---

## III. Scoring System

### Design Principles

- Each Wiki entry has an independent composite score (1.0–5.0)
- **LLM is responsible for individual item scoring** (1–5 points), while the Python script handles **weighted summation and priority calculation**
- Each rating description must be based on observable criteria, avoiding purely subjective terms
- Scoring results drive the priority queue (P0–P3), with P0 entering the next business day's task list

### Scoring Dimensions for Five Categories (See `scoring_criteria.json` for details)

> **Scoring Scope for Multi-level Projects**: Scoring uses the **leaf entry** (specific `.md` file) as the minimum unit. `_index.md` is not scored individually but must be checked for navigation completeness. Subdirectory health = weighted average of all leaf entry scores within it.

| Category | Scoring Dimensions | Weight Distribution |
|------|----------|----------|
| Project Assets | Acceptance Criteria Clarity / Responsibility Attribution / Info Timeliness | 40/30/30 |
| Process Rules | Step Executability / Exception Branch Coverage / Conflict with Other Processes | 40/35/25 |
| Project Semantics | Definition Clarity / Team Alignment / Last Confirmation Time | 35/40/25 |
| Experience Accumulation | Context Completeness / Traceability / Transferability | 30/35/35 |
| Operating Procedures | Step Completeness / Exception Branch Coverage / Last Execution Verification | 35/35/30 |

### Priority Rules

| Priority | Trigger Conditions |
|--------|----------|
| **P0 Urgent** | Composite score ≤ 1.5, or a single item score of 1 with weight ≥ 30%, or within 3 days of a milestone |
| **P1 High** | Composite score 1.6–2.5, or an open decision unresolved for > 2 days |
| **P2 Medium** | Composite score 2.6–3.5 |
| **P3 Low** | Composite score > 3.5 |

---

## IV. Scoring Script

Scoring consists of two steps: **LLM Scoring → Script Calculation**

### Step 1: LLM Outputs JSON for Individual Scores

```
You are a Project Wiki Quality Assessment Assistant. Please score the following entry content line-by-line according to the scoring dimensions of the corresponding category (1-5 points).

Entry Content:
[ENTRY_CONTENT]

Entry Category: [CATEGORY]
Scoring Dimensions (including descriptions):
[Extract corresponding criteria for the category from scoring_criteria.json]

Please output strictly in the following JSON format, with no other text:
{
  "entry_id": "[Relative path of the entry, e.g., ProjectAssets/ClientSide/Auth/OAuth2Integration]",
  "category": "[Category ID]",
  "scores": {
    "[criterion_id]": {
      "score": [Integer 1-5],
      "reason": "[One-sentence explanation of the score, citing specific info from the entry]"
    }
  }
}
```

> `entry_id` uses the entry's relative path to locate its position in the hierarchy within the scoring report.

### Step 2: Script Calculates Composite Score and Priority

```bash
# Single Entry
python scorer.py --input llm_scores.json --criteria scoring_criteria.json --output-dir wiki/_scores

# Batch
python scorer.py --input batch.json --criteria scoring_criteria.json --batch --output-dir wiki/_scores

# Batch + Milestone Urgent Mode
python scorer.py --input batch.json --batch --milestone-urgent --output-dir wiki/_scores
```

### Output Example

```
Entry: User Acceptance Test Completion Definition
Path: ProjectSemantics/ClientSide/ClientStatusDefinition.md
Category: Project Semantics / Glossary and Definition Quality
─────────────────────────────────────────────────────
  Definition Clarity      2 points × 35% = 0.70   [Has basic definition but boundary scenarios are not described]
  Team Alignment         1 point  × 40% = 0.40   [No alignment records found]
  Last Confirm Time      3 points × 25% = 0.75   [Last confirmed 35 days ago]
─────────────────────────────────────────────────────
Composite Score: 1.85 / 5.0   ▶ 🔴 P0 Urgent

✅ Scoring result saved to: wiki/_scores/2024-03-15/
✅ Latest snapshot updated: wiki/_scores/latest.json
```

---

## V. Scoring Storage and Retrieval

Scoring results are stored in the `wiki/_scores/` directory for revision layer review and trend analysis.

### Storage Structure

```
/_scores/
    latest.json              ← Latest full snapshot, read directly by the revision layer
    /2024-03-15/             ← Historical records archived by date
        scores.json          ← Full scoring results for the day (JSON)
        report.md            ← Human-readable report for the day (with priority list)
    /2024-03-14/
        scores.json
        report.md
```

### `latest.json` Format

```json
{
  "scored_at": "2024-03-15T09:30:00+08:00",
  "total_entries": 42,
  "priority_summary": {"P0": 3, "P1": 5, "P2": 18, "P3": 16},
  "entries": [
    {
      "entry_id": "ProjectAssets/ClientSide/Auth/OAuth2Integration",
      "entry_title": "OAuth2Integration",
      "category_id": "project_assets",
      "composite_score": 3.45,
      "priority": "P2",
      "detail": [...]
    }
  ]
}
```

### Access Methods

| Scenario | What to Read | How to Read |
|------|----------|--------|
| **Daily Audit** | `_scores/latest.json` | Revision layer opens directly, reviewing entry-by-entry in P0→P1 order |
| **View Trends** | `_scores/Date/scores.json` | Compare snapshots across multiple days to see score changes |
| **Weekly Report** | `_scores/latest.json` | LLM reads it to generate a health report |
| **Milestone Check** | `_scores/latest.json` | Filter entries with a composite score < 3.0 |
| **Manual Review** | `_scores/Date/report.md` | Read the human-readable report directly |

---

## Reference Files

- `scoring_criteria.json` — Complete scoring criteria for five categories (including descriptions)
- `scorer.py` — Weighted calculation script (Single / Batch / Milestone Urgent Mode)
- `SKILL_maintenance.md` — Maintenance SOP: Daily process, health checks, change management, closing migration
