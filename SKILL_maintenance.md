---
name: Project Wiki Maintenance
description: Regular maintenance process for the Project Wiki. Use this Skill for scenarios such as "Wiki Daily Process", "Wiki Health Check", "Weekly Wiki Review", "Milestone Wiki Check", "Wiki Change Records", "Wiki Closing Migration", "Trigger Mechanism", "Wiki Freeze", etc. Applicable for: executing daily Wiki maintenance cycles, generating weekly health reports, specific checks before milestones, recording changes and decisions, and project closing knowledge transfer.
---

# Project Wiki Maintenance Skill

Regular maintenance process: **Daily Update → Weekly Health Check → Milestone Specific Check → Change Management → Closing Migration**.

> For scoring system, directory standards, and content classification, see the main Skill: `SKILL.md`

---

## I. Collaboration Model

Wiki maintenance is divided into **Execution Layer / Revision Layer**, not assigned by "AI or Human":

```
Execution Layer (Drafting, Scanning, Scoring, Testing, Updating)
  └─ Completed by LLM / AI Agent + Team Members
       Team members provide first-hand info (task status, meeting conclusions, risk signals)
       LLM/Agent converts info into structured Wiki content drafts

Revision Layer (Confirming, Ruling, Approving, Sampling)
  └─ Project Manager + Relevant Team Members
       Revise drafts, confirm factual accuracy, rule on definition discrepancies
       Not just a "quick glance to pass", but taking responsibility for content quality
```

**Core Principle: LLM/Agent does not make final rulings. Humans are responsible for revision and confirmation, not just signing off.**

---

## II. Daily Process

```
【Execution Layer: LLM/Agent + Team Members】
1. Team members synchronize yesterday's progress (task changes, new risks, unresolved decisions)
2. LLM scans signals, scores entries to be processed, and writes results to _scores/ (automatically archived by date + latest.json updated)
3. LLM drafts change content with suggestions for cross-reference updates

【Revision Layer: Project Manager + Relevant Members】
4. Open _scores/latest.json (or the daily report.md) and review entry-by-entry in P0→P1 order
   ├─ Factual error → Correct on the spot
   ├─ Uncertain definition → Contact relevant people to confirm, record as "to be decided"
   └─ Scope change → Follow change approval process

5. Submit, record: Change reason + Trigger source + Associated decisions

【Auto-completion: LLM/Agent】
6. Update cross-references, re-score (overwrite latest.json), detect contradictions, update change log

【Quality Control】
7. Randomly sample 2-3 LLM scores daily for manual review; record discrepancies as input for scoring iteration
```

---

## III. Weekly Health Check

| Check Item | Trigger Condition | Output |
|------------|-------------------|--------|
| Orphan Pages | Page with no references | Flag + Score; Owner decides whether to archive or add references |
| Contradiction Detection | Inconsistent definitions for the same concept | Auto-flag P0, trigger definition alignment process |
| Timeliness Check | Entry not confirmed for more than set days | Reduce confidence, re-score and add to next day's list |
| Confidence Decay | AI usage experience model version changed | Auto-reduce weight in score, human review to restore |
| Low Score Clusters | P0/P1 ratio > 30% in a category | Suggest targeted governance |
| Overdue Decisions | Item unresolved for > 2 business days | Auto-escalate reminder |
| Orphan Multimedia | Image/Video/Audio with no md reference | Flag for processing, human decides whether to archive or delete |
| Missing Index | No `_index.md` in directory | Generate index draft for Revision Layer confirmation |
| Expired Index | Navigation links in `_index.md` mismatch files | Auto-update index |
| Directory Bloat | > 8 `.md` files in a directory without subdirectories | Suggest splitting, generate split plan |
| Excessive Depth | Entry path exceeds 5 levels | Suggest flattening, merging low-level directories |

---

## IV. Milestone Specific Check (5 business days before)

```
1. LLM fully scans all Wiki entries related to this milestone (including multimedia attachment integrity)
2. Output low-score list, highlighting P0/P1 items
3. Check if deliverable definitions and acceptance criteria are aligned with stakeholders
4. Check if relevant SOPs have been verified by recent execution
5. Project Manager and relevant members jointly revise to ensure related entry scores ≥ 3.0
```

---

## V. Trigger Mechanism Quick Lookup

```
Task status change         → Trigger update to corresponding Wiki page + Re-score
New Risk/Issue             → Auto-associate with Risk Log, generate draft, flag P0
Scope Change request       → Trigger scope change assessment, auto-block during freeze
Overdue Decision           → Auto-escalate reminder
Milestone approaching (5d) → Trigger specific health check
Model version update       → Re-score all AI usage experience entries
Wiki score trend decline   → Composite score drops for 3 consecutive days, trigger specific review
```

---

## VI. Change Management

### Change Record Template

```markdown
## [Date] Change

Change Entry: [Full entry path, e.g., wiki/ProjectAssets/ClientSide/Auth/OAuth2Integration.md]
Change Type: [New / Modify / Deprecate / Move / Split]
Change Reason: [Why it was changed, trigger source]
Before: [Old version summary (for Move/Split, include original path)]
After: [New version summary (for Move/Split, include new path)]
Impact Scope: [Which other entries need linked updates, including _index.md and cross-references]
Confirmed By: [Who approved this change]
Next Review: [Date]
```

### Decision Record Template

```markdown
## [Date] Decision

Decision Item: [Specific decision content]
Background: [Why this decision was needed]
Candidate Options:
  Option A: [Description + Pros/Cons]
  Option B: [Description + Pros/Cons]
Final Choice: [Which one was chosen and why]
Decision Maker: [Who made the decision]
Reserved Opinions: [Any dissenting views not adopted]
Review Conditions: [Under what circumstances should this be reassessed]
```

### Change Freeze Mechanism

Milestone **3 business days prior** enters the freeze period: General changes are automatically intercepted; urgent changes must state the reason and be approved by the project lead.

---

## VII. Project Closing Knowledge Transfer

```
1. LLM scans all Wiki entries and generates a migration candidate list
   - High score (> 3.5) and highly reusable → Migrate to organizational knowledge base
   - Highly project-specific content → Archive, do not migrate
   - Low score entries → Migrate after repair by relevant members, or deprecate directly

2. Project Manager and members together confirm migration categories (not just PM alone)

3. LLM drafts migration version (remove project-specific info, extract general parts)
   Multimedia attachments evaluated: reusable diagrams/videos migrated, expired screenshots deprecated

4. Revision confirmation, submit to organizational knowledge base

5. Project Wiki archived, marking closing date and migration index
```

---

## Reference Files

- `SKILL.md` — Main Skill: Wiki structure, classification, scoring system, scoring script
- `scoring_criteria.json` — Complete scoring criteria for five categories
- `scorer.py` — Weighted calculation script
