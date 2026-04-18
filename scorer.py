#!/usr/bin/env python3
"""
Project Wiki Scoring Calculation Script

LLM is responsible for individual item scoring (outputting JSON). This script handles:
  - Weighted summation → Composite score
  - Priority calculation (P0-P3)
  - Outputting human-readable score reports
  - Batch processing multiple entries, outputting summary statistics

Usage:
  Single entry:
    python scorer.py --input llm_scores.json --criteria scoring_criteria.json

  Batch:
    python scorer.py --input batch_scores.json --criteria scoring_criteria.json --batch

  Pass JSON string directly:
    python scorer.py --json '{"entry_id":"e1","category":"project_semantics","scores":{...}}' \
                     --criteria scoring_criteria.json
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Optional


# ─── Priority Rules ────────────────────────────────────────────────────────────

def get_priority(composite_score: float, scores: dict, criteria: list,
                 milestone_urgent: bool = False) -> str:
    """
    Determines priority based on composite score and individual item scores.
    milestone_urgent: Whether it is within 3 days of a milestone (passed externally)
    """
    if milestone_urgent:
        return "P0"

    # Check if any individual item score is 1 and weight >= 30%
    weight_map = {c["id"]: c["weight"] for c in criteria}
    for cid, info in scores.items():
        score_val = info["score"] if isinstance(info, dict) else info
        if score_val == 1 and weight_map.get(cid, 0) >= 30:
            return "P0"

    if composite_score <= 1.5:
        return "P0"
    elif composite_score <= 2.5:
        return "P1"
    elif composite_score <= 3.5:
        return "P2"
    else:
        return "P3"


# ─── Core Calculation ──────────────────────────────────────────────────────────

def compute_composite(entry: dict, criteria_db: dict,
                       milestone_urgent: bool = False) -> dict:
    """
    Calculates composite score and priority for a single entry.

    entry format (LLM output):
    {
      "entry_id": "e1",
      "entry_title": "UAT Completion Definition",   # Optional
      "category": "project_semantics",              # Corresponds to ID in criteria_db
      "scores": {
        "definition_clarity": {"score": 2, "reason": "..."},
        "team_alignment":     {"score": 1, "reason": "..."},
        "last_confirmed":     {"score": 3, "reason": "..."}
      }
    }
    """
    category_id = entry["category"]

    # Find the scoring criteria for the corresponding category
    category_cfg = next(
        (c for c in criteria_db["categories"] if c["id"] == category_id), None
    )
    if not category_cfg:
        raise ValueError(f"Unknown category ID: {category_id}. "
                         f"Available categories: {[c['id'] for c in criteria_db['categories']]}")

    criteria = category_cfg["criteria"]
    scores_input = entry["scores"]

    # Verify all dimensions are provided
    missing = [c["id"] for c in criteria if c["id"] not in scores_input]
    if missing:
        raise ValueError(f"Missing scoring dimensions: {missing}")

    # Weighted summation
    detail_lines = []
    composite = 0.0
    total_weight = sum(c["weight"] for c in criteria)

    for c in criteria:
        cid = c["id"]
        raw = scores_input[cid]
        score_val = raw["score"] if isinstance(raw, dict) else int(raw)
        reason = raw.get("reason", "") if isinstance(raw, dict) else ""
        weight = c["weight"]
        contribution = score_val * weight / 100

        composite += contribution
        detail_lines.append({
            "criterion_id": cid,
            "criterion_name": c["name"],
            "score": score_val,
            "weight": weight,
            "contribution": round(contribution, 4),
            "reason": reason
        })

    composite = round(composite, 4)
    priority = get_priority(composite, scores_input, criteria, milestone_urgent)

    return {
        "entry_id": entry.get("entry_id", "unknown"),
        "entry_title": entry.get("entry_title", entry.get("entry_id", "unknown")),
        "category_id": category_id,
        "category_name": category_cfg["name"],
        "scoring_name": category_cfg["scoring_name"],
        "composite_score": composite,
        "priority": priority,
        "detail": detail_lines,
        "total_weight_check": total_weight   # Should be 100
    }


# ─── Report Rendering ──────────────────────────────────────────────────────────

PRIORITY_EMOJI = {"P0": "🔴", "P1": "🟠", "P2": "🟡", "P3": "🟢"}

def render_report(result: dict) -> str:
    lines = []
    priority_label = f"{PRIORITY_EMOJI.get(result['priority'], '')} {result['priority']}"
    lines.append(f"\nEntry: {result['entry_title']}")
    # If entry_id contains path info (contains /), display the path
    if "/" in result.get("entry_id", ""):
        lines.append(f"Path: {result['entry_id']}")
    lines.append(f"Category: {result['category_name']} / {result['scoring_name']}")
    lines.append("─" * 55)

    for d in result["detail"]:
        reason_snippet = f"  [{d['reason'][:30]}...]" if d["reason"] else ""
        lines.append(
            f"  {d['criterion_name']:<14} {d['score']}pt × {d['weight']:>2}% "
            f"= {d['contribution']:.2f}{reason_snippet}"
        )

    lines.append("─" * 55)
    lines.append(
        f"Composite Score: {result['composite_score']:.2f} / 5.0   ▶ {priority_label}"
    )
    return "\n".join(lines)


def render_batch_summary(results: list) -> str:
    """Output summary stats after batch processing."""
    from collections import Counter
    priority_count = Counter(r["priority"] for r in results)
    category_scores: dict = {}

    for r in results:
        cat = r["category_name"]
        category_scores.setdefault(cat, []).append(r["composite_score"])

    lines = ["\n" + "=" * 55, "📊 Batch Scoring Summary", "=" * 55]
    lines.append(f"Total Entries: {len(results)}")
    lines.append("\nPriority Distribution:")
    for p in ["P0", "P1", "P2", "P3"]:
        count = priority_count.get(p, 0)
        bar = "█" * count
        lines.append(f"  {PRIORITY_EMOJI.get(p, '')} {p}: {count:>3} entries  {bar}")

    lines.append("\nAverage Score by Category:")
    for cat, scores in sorted(category_scores.items()):
        avg = sum(scores) / len(scores)
        lines.append(f"  {cat:<12} Avg {avg:.2f}  ({len(scores)} entries)")

    p0_items = [r for r in results if r["priority"] == "P0"]
    if p0_items:
        lines.append(f"\n🔴 P0 Urgent Entries (Action Needed Immediately):")
        for r in p0_items:
            lines.append(f"  - {r['entry_title']}  [{r['composite_score']:.2f}]")

    lines.append("=" * 55)
    return "\n".join(lines)


# ─── Entry Point ──────────────────────────────────────────────────────────────

def load_criteria(criteria_path: str) -> dict:
    path = Path(criteria_path)
    if not path.exists():
        # Try looking in references/ under the script's parent directory
        alt = Path(__file__).parent.parent / "references" / "scoring_criteria.json"
        if alt.exists():
            path = alt
        else:
            raise FileNotFoundError(f"Could not find scoring criteria file: {criteria_path}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(
        description="Project Wiki Scoring Calculation Script (Weighted Sum + Priority)"
    )
    parser.add_argument("--input", "-i", help="LLM scoring JSON file path")
    parser.add_argument("--json", "-j", help="Directly pass LLM scoring JSON string")
    parser.add_argument("--criteria", "-c",
                        default="references/scoring_criteria.json",
                        help="Scoring criteria JSON file path (default: references/scoring_criteria.json)")
    parser.add_argument("--batch", "-b", action="store_true",
                        help="Batch mode: input is a JSON array containing multiple entries")
    parser.add_argument("--milestone-urgent", "-m", action="store_true",
                        help="Within 3 days of a milestone (all entries forced to P0)")
    parser.add_argument("--output-json", "-o", help="Output results to a JSON file")
    args = parser.parse_args()

    # Load scoring criteria
    try:
        criteria_db = load_criteria(args.criteria)
    except FileNotFoundError as e:
        print(f"❌ {e}", file=sys.stderr)
        sys.exit(1)

    # Load data to be scored
    if args.json:
        raw = json.loads(args.json)
    elif args.input:
        with open(args.input, encoding="utf-8") as f:
            raw = json.load(f)
    else:
        print("Please provide data to be scored via --input or --json", file=sys.stderr)
        parser.print_help()
        sys.exit(1)

    # Determine single/batch
    if args.batch or isinstance(raw, list):
        entries = raw if isinstance(raw, list) else [raw]
    else:
        entries = [raw]

    results = []
    for entry in entries:
        try:
            result = compute_composite(entry, criteria_db, args.milestone_urgent)
            results.append(result)
            print(render_report(result))
        except (ValueError, KeyError) as e:
            print(f"\n⚠️  Entry {entry.get('entry_id', '?')} processing failed: {e}", file=sys.stderr)

    if len(results) > 1:
        print(render_batch_summary(results))

    # Optional: Output JSON
    if args.output_json:
        out = results if len(results) > 1 else results[0]
        with open(args.output_json, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        print(f"\n✅ JSON results saved to: {args.output_json}")


if __name__ == "__main__":
    main()
