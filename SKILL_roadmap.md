---
name: Product Roadmap Router
description: Route to appropriate roadmap template based on project type. Use this Skill for scenarios such as "create roadmap", "product planning", "roadmap template", etc.
---

# Product Roadmap Skill

Select the appropriate roadmap template based on project type.

---

## Routing Logic

| Project Type | Loaded Skill | Key Characteristics |
|--------------|--------------|---------------------|
| Local Client (Desktop App) | → [`SKILL_roadmap_local_client.md`](./SKILL_roadmap_local_client.md) | Desktop apps, offline-first, cross-platform, auto-update |
| toC App (Consumer App) | → [`SKILL_roadmap_toc.md`](./SKILL_roadmap_toc.md) | Web/mobile apps, user growth, retention metrics, viral loops |
| toB SaaS (Enterprise SaaS) | → [`SKILL_roadmap_tob_saas.md`](./SKILL_roadmap_tob_saas.md) | Enterprise software, multi-tenancy, SSO, compliance, private deployment |

---

## Four-Phase Framework

All roadmap types follow a unified four-phase structure:

| Phase | Goal | Success Criteria Varies By Type |
|-------|------|--------------------------------|
| **Phase 1** | Single core feature available | Local: Installs & runs / toC: Users feel value / toB: Sign first deal |
| **Phase 2** | Polish core experience | Local: Smooth UX & auto-update / toC: Measurable retention / toB: Customer self-serve |
| **Phase 3** | Multi-module expansion | Local: Workbench scenarios / toC: Natural next-step needs / toB: Complete workflow |
| **Phase 4** | Plugin system & ecosystem | Local: Plugin ecosystem / toC: Open API & growth / toB: Integration platform & compliance |

---

## Operations Capability

For guidance on when to introduce cron jobs, logging, alerting, and other operational capabilities (part of architecture layer):
→ [`SKILL_ops.md`](./SKILL_ops.md)

---

## Reference Files

- [`SKILL_roadmap_local_client.md`](./SKILL_roadmap_local_client.md) — Local client roadmap with code review tool example
- [`SKILL_roadmap_toc.md`](./SKILL_roadmap_toc.md) — toC app roadmap with AI writing tool example
- [`SKILL_roadmap_tob_saas.md`](./SKILL_roadmap_tob_saas.md) — toB SaaS roadmap with project management example
- [`SKILL_ops.md`](./SKILL_ops.md) — Operations capability timeline (cron jobs, logging, alerting)
