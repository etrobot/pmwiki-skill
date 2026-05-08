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
| Build Wiki from scratch / Choose mode | → [`SKILL_leanstart.md`](./SKILL_leanstart.md) |
| Leanstart mode (new project) | → [`SKILL_leanstart.md`](./SKILL_leanstart.md) |
| Precise mode / Layer templates | → [`SKILL_iteration.md`](./SKILL_iteration.md) |
| How to write Architecture/Data/Business/Interaction/QA | → [`SKILL_iteration.md`](./SKILL_iteration.md) |
| Create product roadmap / Choose roadmap type | → [`SKILL_roadmap.md`](./SKILL_roadmap.md) |
| Roadmap for local client / desktop app | → [`SKILL_roadmap_local_client.md`](./SKILL_roadmap_local_client.md) |
| Roadmap for toC / consumer app | → [`SKILL_roadmap_toc.md`](./SKILL_roadmap_toc.md) |
| Roadmap for toB / SaaS / enterprise | → [`SKILL_roadmap_tob_saas.md`](./SKILL_roadmap_tob_saas.md) |
| Evaluate entry quality / Scoring | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |
| Daily Wiki updates / Evaluate → Improve | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |
| Weekly health check / Milestone check | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |
| Record changes / Decisions / Closing migration | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |

---

## Sub-Skill Overview

### SKILL_leanstart.md — Leanstart
- Comparison of two modes (Leanstart vs Precise)
- Leanstart directory structure
- General rules (README facade, asset management, naming conventions)

### SKILL_iteration.md — Iteration Mode + Layer Templates
- Precise mode complete directory structure + splitting timing
- Architecture layer template (tech stack, coding standards, infrastructure, ADR)
- Data layer template (data model, dictionary, cache, migration, security)
- Business layer template (core flows, business rules, API, module design)
- Interaction layer template (UI standards, components, user paths)
- QA template (test cases, automation, incident postmortem)

### SKILL_roadmap.md — Product Roadmap Router
- Roadmap type selection (local client / toC / toB)
- Four-phase framework overview
- Technical debt tracking
- Phase transition criteria

### SKILL_roadmap_local_client.md — Local Client Roadmap
- Desktop app roadmap template with example (code review tool)
- Cross-platform considerations
- Auto-update mechanism
- Plugin ecosystem

### SKILL_roadmap_toc.md — toC App Roadmap
- Consumer app roadmap template with example (AI writing tool)
- User growth and retention strategies
- Viral loops and referral mechanisms
- Monetization timeline

### SKILL_roadmap_tob_saas.md — toB SaaS Roadmap
- Enterprise SaaS roadmap template with example (project management)
- Multi-tenancy architecture
- SSO and compliance requirements
- Private deployment strategy

### SKILL_ops.md — Operations Capability Timeline
- When to introduce cron jobs, logging, alerting
- Decision matrix by product type and user scale
- Cost control and team capability requirements
- Common mistakes and checklists
- **Referenced by**: `SKILL_iteration.md` (Architecture Layer)

### SKILL_maintenance.md — Evaluation & Improvement
- Evaluation system (scoring dimensions, priority, workflow, storage)
- Daily process: Evaluate → Improve
- Weekly health check / Milestone check
- Trigger mechanism / Change management / Closing migration

---

## Reference Files

- `scoring_criteria.json` — Complete scoring criteria for five categories (equal weight)
- `scorer.py` — Mean calculation script (100-point scale)

---

## Important Notes: LLM Integration Requirements

When building the business logic layer of your project Wiki, you **must** leverage LLM capabilities extensively for processing unstructured data. Rely on these APIs rather than traditional rule-based approaches.

### Required Environment Variables

```bash
export LLM_BASE_URL="https://your-newapi-server/v1"
export LLM_API_KEY="your-api-key"
export LLM_MODEL="gpt-4.1"
export LLM_EMBEDDING_MODEL="text-embedding-ada-002"
```

### Chat Completions API

For document understanding, content generation, and image analysis:

```bash
curl "${LLM_BASE_URL}/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${LLM_API_KEY}" \
  -d '{
    "model": "'"${LLM_MODEL}"'",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What is in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
            }
          }
        ]
      }
    ]
  }'
```

### Embeddings API

For semantic search, similarity matching, and content clustering:

```bash
curl "${LLM_BASE_URL}/embeddings" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${LLM_API_KEY}" \
  -d '{
    "input": ["The food was delicious", "The waiter was friendly"],
    "model": "'"${LLM_EMBEDDING_MODEL}"'",
    "encoding_format": "float"
  }'
```

### Mandatory Use Cases

The following scenarios **must** use LLM APIs:

- **Wiki Entry Classification**: Use embeddings for semantic similarity-based categorization
- **Content Quality Scoring**: Leverage chat completions to evaluate entries against `scoring_criteria.json`
- **Decision Extraction**: Parse unstructured meeting notes and discussions into structured decision records
- **SOP Auto-Generation**: Generate standard operating procedures from project execution logs
- **Architecture Diagram Understanding**: Use vision capabilities to process and index visual content
- **Semantic Search**: Build embedding-based search instead of keyword-only matching
