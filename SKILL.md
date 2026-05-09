---
name: Project Wiki
description: Build and maintain project Wiki documentation. Use this Skill for scenarios such as "create project Wiki", "Wiki structure", "Wiki templates", "product roadmap", "Wiki scoring", "Wiki health check", etc. This is about WRITING DOCUMENTATION, not developing the project itself.
---

# Project Wiki Skill Entry Point

**What This Skill Does**: Help you build, organize, and maintain **project Wiki documentation**.

**What This Skill Does NOT Do**: Project development, coding, deployment, or executing the roadmap.

---

## Routing Logic

| User Intent | Loaded Skill |
|-------------|--------------|
| Build Wiki from scratch / Choose Wiki mode | → [`SKILL_leanstart.md`](./SKILL_leanstart.md) |
| Leanstart Wiki mode (new project) | → [`SKILL_leanstart.md`](./SKILL_leanstart.md) |
| Precise Wiki mode / Wiki layer templates | → [`SKILL_iteration.md`](./SKILL_iteration.md) |
| How to write Architecture/Data/Business/Interaction/QA Wiki | → [`SKILL_iteration.md`](./SKILL_iteration.md) |
| Create product roadmap / Choose roadmap type | → [`SKILL_roadmap.md`](./SKILL_roadmap.md) |
| Roadmap for local client / desktop app | → [`SKILL_roadmap_local_client.md`](./SKILL_roadmap_local_client.md) |
| Roadmap for toC / consumer app | → [`SKILL_roadmap_toc.md`](./SKILL_roadmap_toc.md) |
| Roadmap for toB / SaaS / enterprise | → [`SKILL_roadmap_tob_saas.md`](./SKILL_roadmap_tob_saas.md) |
| When to add cron jobs / logging / alerting / ops | → [`SKILL_ops.md`](./SKILL_ops.md) |
| Evaluate Wiki entry quality / Wiki scoring | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |
| Daily Wiki updates / Evaluate → Improve Wiki | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |
| Weekly Wiki health check / Milestone Wiki check | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |
| Record Wiki changes / Decisions / Closing Wiki migration | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |

---

## Sub-Skill Overview

### SKILL_leanstart.md — Leanstart Wiki Mode
**Purpose**: Quickly set up Wiki structure for new projects

- Comparison of two Wiki modes (Leanstart vs Precise)
- Leanstart Wiki directory structure (5 .md files + assets)
- General Wiki rules (README facade, asset management, naming conventions)

### SKILL_iteration.md — Precise Wiki Mode + Layer Templates
**Purpose**: Detailed Wiki structure and templates for complex projects

- Precise Wiki mode complete directory structure + when to split files
- Architecture layer Wiki template (tech stack, coding standards, infrastructure, ADR)
- Data layer Wiki template (data model, dictionary, cache, migration, security)
- Business layer Wiki template (core flows, business rules, API, module design)
- Interaction layer Wiki template (UI standards, components, user paths)
- QA Wiki template (test cases, automation, incident postmortem)

### SKILL_roadmap.md — Product Roadmap Router
**Purpose**: Route to appropriate roadmap template (roadmap is part of Wiki documentation)

- Roadmap type selection (local client / toC / toB)
- Four-phase framework overview
- Technical debt tracking
- Phase transition criteria

### SKILL_roadmap_local_client.md — Local Client Roadmap
**Purpose**: Roadmap template for desktop applications (to be written in Wiki)

- Desktop app roadmap template with example (code review tool)
- Cross-platform considerations
- Auto-update mechanism
- Plugin ecosystem

### SKILL_roadmap_toc.md — toC App Roadmap
**Purpose**: Roadmap template for consumer applications (to be written in Wiki)

- Consumer app roadmap template with example (AI writing tool)
- User growth and retention strategies
- Viral loops and referral mechanisms
- Monetization timeline

### SKILL_roadmap_tob_saas.md — toB SaaS Roadmap
**Purpose**: Roadmap template for enterprise SaaS (to be written in Wiki)

- Enterprise SaaS roadmap template with example (project management)
- Multi-tenancy architecture
- SSO and compliance requirements
- Private deployment strategy

### SKILL_ops.md — Operations Capability Timeline
**Purpose**: Guidance on when to introduce ops capabilities (part of architecture layer Wiki)

- When to introduce cron jobs, logging, alerting
- Decision matrix by product type and user scale
- Cost control and team capability requirements
- Common mistakes and checklists

### SKILL_maintenance.md — Wiki Evaluation & Improvement
**Purpose**: Maintain Wiki quality, keep documentation up-to-date

- Wiki entry scoring system (5 categories, LLM-based evaluation)
- Daily Wiki process: Evaluate Wiki quality → Improve low-score Wiki entries
- Weekly Wiki health check (orphaned pages, contradictions, timeliness)
- Milestone Wiki check (5 days before milestone)
- Wiki change management & decision records
- Project closing: Wiki knowledge migration to organizational knowledge base

---

## Reference Files

- `scoring_criteria.json` — Complete scoring criteria for five Wiki categories (equal weight)
- `scorer.py` — Mean calculation script (100-point scale)

---

## Important Notes: LLM Integration for Projects

**Note**: The following section is about **project architecture planning**, NOT about the Wiki system itself.

When planning a project, if it needs to process unstructured data (documents, images, user input, etc.), consider integrating LLM capabilities from the start. This should be documented in the Wiki's architecture layer.

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

### When Projects Should Use LLM APIs

Consider LLM integration if the project involves:

- **Content Classification**: Categorizing user-generated content, documents, or messages
- **Quality Evaluation**: Scoring, reviewing, or moderating content
- **Information Extraction**: Parsing unstructured text (emails, meeting notes, forms) into structured data
- **Document Generation**: Auto-generating reports, summaries, or documentation
- **Image Understanding**: Processing and analyzing visual content
- **Semantic Search**: Building search that understands meaning, not just keywords
- **Chatbots / Conversational UI**: Natural language interaction with users

**Document this in the Wiki's architecture layer** (`01-architecture/tech-stack.md` or `01-architecture/ai-integration.md`).
