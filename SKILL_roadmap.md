# Product Roadmap Skill

Select the appropriate Roadmap template based on project type.

---

## Routing Logic

| Project Type | Loaded Skill | Key Characteristics |
|--------------|--------------|---------------------|
| Local Client (Desktop App) | → [`SKILL_roadmap_local_client.md`](./SKILL_roadmap_local_client.md) | Desktop apps, offline-first, cross-platform, auto-update |
| toC App (Consumer App) | → [`SKILL_roadmap_toc.md`](./SKILL_roadmap_toc.md) | Web/mobile apps, user growth, retention metrics, viral loops |
| toB SaaS (Enterprise SaaS) | → [`SKILL_roadmap_tob_saas.md`](./SKILL_roadmap_tob_saas.md) | Enterprise software, multi-tenancy, SSO, compliance, private deployment |

---

## Four-Phase Roadmap Framework

All roadmap types follow a unified four-phase structure:

### Phase 1 — Single Core Feature Available
- **Goal**: Solve one problem, don't crash
- **Success Criteria**:
  - Local Client: Installs and runs, core feature outputs correctly
  - toC App: New users feel the value
  - toB SaaS: Can demo & sign first deal

### Phase 2 — Polish Core Experience
- **Goal**: Smooth to use, error feedback, updates work
- **Success Criteria**:
  - Local Client: Smooth UX, error handling, auto-update
  - toC App: Measurable retention, recall mechanism established
  - toB SaaS: Customer team can self-serve

### Phase 3 — Multi-Module Expansion
- **Goal**: From single tool to complete workbench/platform
- **Success Criteria**:
  - Local Client: Horizontal expansion to workbench scenarios
  - toC App: Extend to user's natural next-step needs
  - toB SaaS: Cover customer's complete workflow

### Phase 4 — Plugin System & Ecosystem
- **Goal**: Let third parties extend, become a platform
- **Success Criteria**:
  - Local Client: Plugin ecosystem + optional cloud sync
  - toC App: Open API + growth loops
  - toB SaaS: Integration platform + compliance & private deployment

---

## Most Overlooked Technical Debt

| Product Type | Easily Overlooked Debt | Must Resolve By |
|--------------|------------------------|-----------------|
| Local Client | Multi-platform adaptation & auto-update mechanism | Phase 2 |
| toC App | Notification & recall system | Phase 2 |
| toB SaaS | Multi-tenant data isolation | Phase 2 |

---

## Prerequisites for Phase 3 → 4 Transition

| Product Type | Prerequisites |
|--------------|---------------|
| Local Client | Core features stable, no frequent crashes |
| toC App | Stable retention & paying users |
| toB SaaS | Renewal customers & clear ICP |

---

## How to Use

1. **Identify project type**: Determine if it's a local client, toC app, or toB SaaS
2. **Load corresponding template**: Click the link in the table above to view detailed roadmap
3. **Customize**: Adjust features, architecture, timeline based on actual project needs
4. **Set milestones**: Define Go/No-Go decision points for each phase
5. **Track technical debt**: Document what must be resolved at each stage

---

## Operations Capability Timeline

For guidance on when to introduce cron jobs, logging, alerting, and other operational capabilities, this is an important part of the architecture layer.

When writing the architecture layer in Wiki (`01-architecture/ops-capability.md`), refer to:
→ [`SKILL_ops.md`](./SKILL_ops.md)

This document provides:
- Operations capability timeline by product type (local client / toC / toB)
- Decision matrix by user scale
- Cost control and team capability requirements
- Common mistakes and checklists
