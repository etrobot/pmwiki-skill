---
name: Project Wiki Maintenance
description: Evaluate and improve the Project Wiki. Use this Skill for scenarios such as "Wiki Scoring", "Wiki Health Check", "Weekly Wiki Review", "Milestone Wiki Check", "Wiki Daily Process", "Wiki Change Records", "Wiki Closing Migration", "Trigger Mechanism", "Wiki Freeze", etc. Core workflow: evaluate first, then improve.
---

# Project Wiki Maintenance Skill

Core loop: **Evaluate → Improve**. Identify problems first, then solve them.

Wiki setup method → [`SKILL_lintstart.md`](./SKILL_lintstart.md)

---

## I. Evaluation System

### Scoring Data Model

Each Wiki entry has an independent composite score (100-point scale), calculated by LLM scoring each dimension (1–5 points) with **equal weight average**, then multiplied by 20 to convert to 100-point scale:

| Category | Scoring Dimensions |
|----------|-------------------|
| Project Assets | Acceptance criteria clarity / Responsibility assignment / Information timeliness |
| Process Rules | Step executability / Exception branch coverage / Conflict with other processes |
| Project Semantics | Definition clarity / Team alignment / Last confirmation time |
| Experience Accumulation | Context completeness / Traceability / Portability |
| Operating Procedures | Step completeness / Exception branch coverage / Last execution verification |

> Composite Score = (Sum of dimension scores / Number of dimensions) × 20. Scoring uses **leaf entries** (specific `.md` files) as the smallest unit.

### Priority Rules

| Priority | Trigger Condition |
|----------|-------------------|
| **P0 Urgent** | Composite score ≤ 30, or any single dimension scored 1, or milestone within 3 days |
| **P1 High** | Composite score 31–50, or open decision not closed for > 2 days |
| **P2 Medium** | Composite score 51–70 |
| **P3 Low** | Composite score > 70 |

### Scoring Workflow

**Step 1: LLM scores each dimension → Output JSON**

```
You are a Project Wiki Quality Assessment Assistant. Please score the following entry content line-by-line according to the scoring dimensions of the corresponding category (1-5 points).

Entry Content:
[ENTRY_CONTENT]

Entry Category: [CATEGORY]
Scoring Dimensions (including descriptions):
[Extract corresponding criteria for the category from scoring_criteria.json]

Please output strictly in the following JSON format, with no other text:
{
  "entry_id": "[Relative path of the entry]",
  "category": "[Category ID]",
  "scores": {
    "[criterion_id]": {
      "score": [Integer 1-5],
      "reason": "[One-sentence explanation of the score, citing specific info from the entry]"
    }
  }
}
```

**Step 2: Script calculates composite score and priority**

```bash
# Single entry
python scorer.py --input llm_scores.json --criteria scoring_criteria.json --output-json result.json

# Batch
python scorer.py --input batch.json --criteria scoring_criteria.json --batch --output-json results.json

# Batch + milestone urgent mode
python scorer.py --input batch.json --batch --milestone-urgent --output-json results.json
```

**Output Example**

```
Entry: User Acceptance Test Completion Definition
Path: ProjectSemantics/ClientSide/ClientStatusDefinition.md
Category: Project Semantics / Glossary and Definition Quality
─────────────────────────────────────────────────────
  Definition Clarity             2pt  [Has basic definition but boundary scenarios are not described]
  Team Alignment                1pt  [No alignment records found]
  Last Confirm Time             3pt  [Last confirmed 35 days ago]
─────────────────────────────────────────────────────
Composite Score: 40 / 100   ▶ 🔴 P0 Urgent
```

### Scoring Result Storage

```
/wiki/_scores/
    latest.json              ← Latest full snapshot
    /2024-03-15/             ← Archived by date
        scores.json          ← Full scoring results for the day
        report.md            ← Human-readable report for the day
```

```json
{
  "scored_at": "2024-03-15T09:30:00+08:00",
  "total_entries": 42,
  "priority_summary": {"P0": 3, "P1": 5, "P2": 18, "P3": 16},
  "entries": [
    {
      "entry_id": "Business Logic/Auth Module",
      "entry_title": "Auth Module",
      "category_id": "project_assets",
      "composite_score": 40,
      "priority": "P0",
      "detail": [...]
    }
  ]
}
```

---

## II. Collaboration Model

Evaluation and improvement proceed in two layers, not divided by "AI or human":

```
Execution Layer (scanning, scoring, drafting, updating)
  └─ LLM / AI Agent + Team Members
       Team members provide first-hand information (task status, meeting conclusions, risk signals)
       LLM/Agent converts information into structured Wiki content drafts

Review Layer (confirmation, adjudication, approval, sampling)
  └─ Project Manager + Relevant Team Members
       Review drafts, confirm factual accuracy, adjudicate definition disagreements
       Not just "a quick look", but take responsibility for content quality
```

**Core Principle: LLM/Agent does not make final adjudications. Humans are responsible for review and confirmation, not just signing off.**

---

## III. Daily Process: Evaluate → Improve

```
[Evaluation Phase: Execution Layer]
1. Team members sync yesterday's progress (task changes, new risks, unclosed decisions)
2. LLM scans signals, scores entries that need processing, writes results to _scores/
3. Output daily scoring report, flag P0/P1 entries

[Improvement Phase: Review Layer]
4. Open _scores/latest.json, review entries in P0→P1 order
   ├─ Factual errors → Correct immediately
   ├─ Unclear definitions → Contact relevant personnel for confirmation, mark as "pending"
   └─ Scope change → Follow change approval process
5. Confirm improvement plan, submit: improvement reason + trigger source + related decisions

[Closure: Execution Layer]
6. Update cross-references, re-score (overwrite latest.json), detect contradictions, update changelog

[Quality Check]
7. Randomly sample 2-3 LLM scoring results daily, record deviations as scoring iteration input
```

---

## IV. Weekly Health Check

| Check Item | Trigger Condition | Output |
|------------|-------------------|--------|
| Orphaned pages | Page has no references | Flag + score; owner decides archive or add references |
| Contradiction detection | Inconsistent definitions for the same concept | Auto-flag as P0, trigger definition alignment process |
| Timeliness check | Entry not confirmed for more than set days | Reduce confidence, add to next day's scoring list |
| AI experience decay | AI experience model version updated | Auto-reduce scoring weight, restore after manual review |
| Low-score clustering | P0/P1 ratio in a category > 30% | Suggest targeted governance |
| Overdue decisions | Entry not closed for > 2 working days | Auto-escalate reminder |
| Orphaned assets | Images/videos/audio not referenced by any .md | Flag for processing, human decides archive or delete |
| Directory bloat | > 8 .md files in a directory with no subdirectories | Suggest splitting, generate split plan |
| Excessive depth | Entry path exceeds 4 levels | Suggest flattening, merge low-level directories |

---

## V. Milestone Check (5 Working Days Before)

```
1. LLM scans all Wiki entries related to the milestone (including asset completeness)
2. Output low-score list, highlight P0/P1
3. Check if deliverable definitions and acceptance criteria are aligned with stakeholders
4. Check if related SOPs have recent execution verification
5. Project manager and relevant members jointly review, ensure related entry scores ≥ 60
```

---

## VI. Trigger Mechanism Quick Reference

```
Task status change         → Trigger update of corresponding Wiki page + re-scoring
New risk/issue            → Auto-link to risk log, generate draft, flag P0
Scope change request       → Trigger scope change evaluation, auto-block during freeze period
Overdue decision          → Auto-escalate reminder
Milestone approaching (5 days) → Trigger targeted health check
Model version update      → Re-score all AI experience entries
Scoring trend declining   → Composite score declining for 3 consecutive days, trigger targeted review
```

---

## VII. Change Management

### Change Record Template

```markdown
## [Date] Change

Changed Entry: [Full entry path, e.g., wiki/Business Logic/Auth Module.md]
Change Type: [New / Modified / Deprecated / Moved / Split]
Change Reason: [Why change, trigger source]
Before Change: [Old version summary (include original path for move/split)]
After Change: [New version summary (include new path for move/split)]
Impact Scope: [Which entries need linked updates, including cross-references]
Confirmed By: [Who approved this change]
Next Review: [Date]
```

### Decision Record Template

```markdown
## [Date] Decision

Decision Item: [Specific decision content]
Context: [Why this decision is needed]
Alternatives:
  Option A: [Description + Pros/Cons]
  Option B: [Description + Pros/Cons]
Final Choice: [Which one, why]
Decision Maker: [Who made the decision]
Dissenting Opinions: [Unadopted objections]
Re-review Conditions: [Under what circumstances should re-evaluation occur]
```

### Change Freeze Mechanism

Milestone **3 working days before** enters freeze period: general changes auto-blocked; urgent changes require explanation and project owner approval.

---

## VIII. Project Closing Knowledge Migration

```
1. LLM scans all Wiki entries, generates migration candidate list
   - High score (> 70) and highly reusable → Migrate to organizational knowledge base
   - Strongly project-specific content → Archive, do not migrate
   - Low-score entries → Fixed by relevant members before migration, or directly deprecated

2. Project manager and members jointly confirm migration classification (not PM alone)

3. LLM drafts migration version (remove project-specific info, extract generic parts)
   Asset file evaluation: reusable images/videos migrate, expired screenshots deprecated

4. Review and confirm, submit to organizational knowledge base

5. Project Wiki archived, marked with closing date and migration index
```

---

## Reference Files

- `SKILL_setup.md` — Wiki setup: project structure, business logic layer, data layer, interaction layer
- `scoring_criteria.json` — Complete scoring criteria for five categories (with descriptions), equal weight
- `scorer.py` — Mean calculation script (single / batch / milestone urgent mode)
