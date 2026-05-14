---
name: Project Wiki
description: Build and maintain project Wiki documentation. Use this Skill for scenarios such as "create project Wiki", "Wiki structure", "Wiki templates", "product roadmap", "Wiki scoring", "Wiki health check", etc. This is about WRITING DOCUMENTATION, not developing the project itself.
---

# Project Wiki Skill Entry Point

**What This Skill Does**: Help you build, organize, and maintain **project Wiki documentation**.

**What This Skill Does NOT Do**: Project development, coding, deployment, or executing the roadmap.

---

## Routing Logic

| What You Want to Do | Which Skill to Use |
|-------------|--------------|
| New project just started, need basic Wiki | → [`SKILL_leanstart.md`](./SKILL_leanstart.md) |
| Project in iteration, need detailed layer docs | → [`SKILL_iteration.md`](./SKILL_iteration.md) |
| Create product roadmap | → [`SKILL_roadmap.md`](./SKILL_roadmap.md) |
| When to add ops capabilities | → [`SKILL_ops.md`](./SKILL_ops.md) |
| Maintain and improve Wiki quality | → [`SKILL_maintenance.md`](./SKILL_maintenance.md) |

---

## Sub-Skill Overview

### SKILL_leanstart.md — New Project Quick Start
**When to use**: Project just started, need to set up basic Wiki structure quickly

- Lightweight Wiki directory structure (5 .md files + assets)
- General Wiki rules (README facade, asset management, naming conventions)
- Comparison with iteration approach

### SKILL_iteration.md — Project Iteration Phase
**When to use**: Project is iterating, need to add detailed documentation for each layer

- Complete Wiki directory structure + when to split files
- Architecture layer Wiki template (tech stack, coding standards, infrastructure, ADR)
- Data layer Wiki template (data model, dictionary, cache, migration, security)
- Business layer Wiki template (core flows, business rules, API, module design)
- Interaction layer Wiki template (UI standards, components, user paths)
- QA Wiki template (test cases, automation, incident postmortem)

### SKILL_roadmap.md — Product Roadmap Router
**When to use**: Need to create product roadmap (roadmap is part of Wiki documentation)

- Roadmap type selection (desktop app / consumer / enterprise)
- Four-phase framework overview
- Technical debt tracking
- Phase transition criteria

### SKILL_roadmap_local_client.md — Desktop App Roadmap
**When to use**: Writing roadmap for desktop applications (to be written in Wiki)

- Desktop app roadmap template with example (code review tool)
- Cross-platform considerations
- Auto-update mechanism
- Plugin ecosystem

### SKILL_roadmap_toc.md — Consumer App Roadmap
**When to use**: Writing roadmap for consumer applications (to be written in Wiki)

- Consumer app roadmap template with example (AI writing tool)
- User growth and retention strategies
- Viral loops and referral mechanisms
- Monetization timeline

### SKILL_roadmap_tob_saas.md — Enterprise SaaS Roadmap
**When to use**: Writing roadmap for enterprise SaaS (to be written in Wiki)

- Enterprise SaaS roadmap template with example (project management)
- Multi-tenancy architecture
- SSO and compliance requirements
- Private deployment strategy

### SKILL_ops.md — Operations Capability Timeline
**When to use**: Guidance on when to introduce ops capabilities (part of architecture layer Wiki)

- When to introduce cron jobs, logging, alerting
- Decision matrix by product type and user scale
- Cost control and team capability requirements
- Common mistakes and checklists

### SKILL_maintenance.md — Wiki Evaluation & Improvement
**When to use**: Maintain Wiki quality, keep documentation up-to-date

- Wiki entry scoring system (5 categories, LLM-based evaluation)
- Daily Wiki process: Evaluate Wiki quality → Improve low-score entries
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
