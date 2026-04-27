---
name: Project Wiki Iteration
description: Detailed structure and templates for the precise Wiki mode. Use this Skill for scenarios such as "precise mode", "iteration mode", "refactor project Wiki", "multi-module Wiki", "Wiki layer templates", "architecture layer template", "data layer template", "business layer template", "interaction layer template", "QA template", etc.
---

# Precise Mode: Complete Directory Structure + Detailed Layer Templates

Lightstart mode overview → [`SKILL_lintstart.md`](./SKILL_lintstart.md)

---

## I. Precise Mode Directory Structure

```
docs/
├── README.md                # Facade: project overview, navigation index
├── assets/                  # Global assets: images, attachments, scripts
│   ├── images/
│   └── files/
│
├── 01-architecture/         # [Architecture Layer]
│   ├── tech-stack.md        # Tech stack + coding standards
│   ├── infrastructure.md    # Servers, network, CI/CD pipeline
│   └── decisions/           # Architecture decision records: "why this design"
│
├── 02-data/                 # [Data Layer]
│   ├── schema/              # Database design
│   │   ├── er-diagram.md    # ER diagram
│   │   └── migrations.md    # Migration records
│   ├── cache.md             # Redis/cache strategy
│   └── dictionary.md        # Data dictionary (field details)
│
├── 03-business/             # [Business Layer]
│   ├── core-flows/          # Core business logic
│   │   ├── order-flow.md    # Order flow
│   │   └── payment-flow.md  # Payment flow
│   ├── api/                 # API documentation
│   │   └── swagger.yaml     # or markdown interface definitions
│   └── modules/             # Module detailed design (expand as needed)
│
├── 04-interaction/          # [Interaction Layer]
│   ├── ui-design.md         # UI standards, design draft links
│   ├── components.md        # Core component descriptions
│   └── user-journey.md      # User operation paths
│
├── 05-qa/                   # [QA]
│   ├── test-cases/          # Core test cases
│   ├── automation.md        # Automation test configuration
│   └── incidents/           # Incident postmortems and known issues
│
└── 06-resources/            # [Resources] (optional, split as needed)
    ├── third-party.md       # Third-party services (payments, SMS)
    └── tools.md             # Development tool configuration
```

### When to Split

| Signal | Action |
|--------|--------|
| A .md file exceeds **300 lines** | Split into multiple .md files in a subdirectory by subtopic |
| **3+ independent subtopics** under the same topic | Create subdirectory, one .md per subtopic |
| Subdirectory has only **1–2 files** | Keep flat, don't create directory |
| A layer has more than **8 files** | Consider splitting one more level by module/subdomain |

---

## II. Architecture Layer Template

### What to Write

The architecture layer answers "how the system is built, and why":

| Content Type | Description | Example |
|--------------|-------------|---------|
| Tech Stack | What tech is used, why it was chosen | Next.js vs Tanstack Start selection rationale |
| Coding Standards | Code style, directory structure, naming conventions | ESLint config, Git branch strategy |
| Infrastructure | Servers, network, CI/CD | Deployment topology, pipeline configuration |
| Architecture Decisions | "Why" behind key designs | Why microservices, why event-driven |

### How to Write

```markdown
# Architecture Layer

## Tech Stack
| Technology | Purpose | Selection Rationale | Alternatives |
|------------|---------|---------------------|--------------|
| React | Frontend framework | Team familiarity + mature ecosystem | Vue 3 |

## Coding Standards
[Code style, directory structure, naming conventions, Git strategy]

## Infrastructure
[Deployment topology, server configuration, CI/CD pipeline]

## Architecture Decision Records
### ADR-001: [Decision Title]
- Context: [Why this decision is needed]
- Choice: [Final solution]
- Rationale: [Why this was chosen]
- Impact: [Impact on the system]
```

> **Core Principle**: Architecture decisions must record "why", not just "what". Future readers should understand the constraints and trade-offs at the time by reading the ADR.

---

## III. Data Layer Template

### What to Write

The data layer answers "what the data looks like, where it's stored, how it flows":

| Content Type | Description | Example |
|--------------|-------------|---------|
| Data Model | Table structure, field definitions, indexes, constraints | User table design, order table ER diagram |
| Data Dictionary | Field details, enum values, business meaning | What each value of the status field represents |
| Storage Solution | Selection rationale, sharding strategy, read-write separation | Why MongoDB was chosen, sharding strategy |
| Cache Strategy | What to cache, expiration policy, consistency solution | Redis hot data caching |
| Data Migration | Version-to-version migration records, rollback plans | v2→v3 table structure change scripts |
| Data Security | Sensitive fields, masking rules, backup strategy | Phone number masking rules, GDPR compliance |

### How to Write

```markdown
# Data Layer

## Data Model
[ER diagram link or embedded table]

| Field Name | Type | Required | Description |
|------------|------|----------|-------------|
| id         | BIGINT | Yes | Primary key, auto-increment |
| status     | TINYINT | Yes | See data dictionary |

## Data Dictionary
| Field | Value | Meaning |
|-------|-------|---------|
| status | 0 | Pending Payment |
| status | 1 | Paid |

## Cache Strategy
[Cache key design, expiration time, consistency solution]

## Data Migration
[Version change records, migration script location]

## Data Security
[Sensitive field markers, masking rules, backup strategy]
```

> **Core Principle**: Data dictionary and masking rules must be specific — what each enum value represents, what algorithm is used for masking. Don't leave "to be completed".

---

## IV. Business Layer Template

### What to Write

The business layer answers "what the system does, what the rules are":

| Content Type | Description | Example |
|--------------|-------------|---------|
| Core Flows | Main flows and branch flows | User registration flow, order flow, approval chain |
| Business Rules | Decision conditions, calculation rules, constraints | Discount rules, risk control thresholds, permission logic |
| API Interfaces | Request/response format, auth, error codes | RESTful API documentation |
| Module Design | Responsibilities and interactions of each module | Auth module, payment module |

### How to Write

```markdown
# Business Layer

## Core Flows
### [Flow Name]
[Flow description, with flowchart in assets]

## Business Rules
| Rule ID | Rule Description | Trigger Condition | Exceptions |
|---------|------------------|-------------------|------------|
| BR-001  | ...              | ...               | ...        |

## API Interfaces
### [Interface Name]
- Method: POST
- Path: /api/v1/xxx
- Request: [Parameter description]
- Response: [Return format]
- Error Codes: [Error code definitions]

## Module Design
[Responsibilities, dependencies, interaction methods of each module]
```

> **Core Principle**: Business rules must be executable — clearly state trigger conditions and exceptions, avoid "in principle should...". API docs should be directly usable for development.

---

## V. Interaction Layer Template

### What to Write

The interaction layer answers "what the user sees, how they operate":

| Content Type | Description | Example |
|--------------|-------------|---------|
| UI Standards | Design system, style constraints, design draft links | Color scheme, font size standards, Figma links |
| Core Components | Common component library, usage instructions | Date picker, pagination component |
| User Paths | Main and branch paths of user operations | Register-Login-Use, Order-Pay-Review |

### How to Write

```markdown
# Interaction Layer

## UI Standards
[Design system link, color/font/spacing standards]

## Core Components
| Component | Purpose | Usage Location |
|-----------|---------|----------------|
| DatePicker | Date selection | Form pages |

## User Paths
### [Path Name]
[Operation steps, with wireframes/flowcharts in assets]
```

> **Core Principle**: User paths should be written to the operation level — which button to click, what feedback to see, what to do when an error occurs.

---

## VI. QA Template

### What to Write

The QA layer answers "how to verify, what went wrong":

| Content Type | Description | Example |
|--------------|-------------|---------|
| Test Cases | Positive/negative test cases for core scenarios | Payment success, insufficient balance, network timeout |
| Automation Testing | Framework configuration, coverage requirements | Jest + Cypress configuration |
| Incident Postmortem | Timeline, root cause, improvement measures | 2024-03 Payment Timeout Incident |

### How to Write

```markdown
# QA

## Core Test Cases
| Case ID | Scenario | Preconditions | Steps | Expected Result |
|---------|----------|---------------|-------|-----------------|
| TC-001  | Normal payment | Account has balance | ... | Payment successful |

## Automation Testing
[Framework, configuration, execution method, coverage requirements]

## Incident Postmortem
### [Incident Title] - [Date]
- Impact Scope: [...]
- Timeline: [...]
- Root Cause: [...]
- Improvement Measures: [...]
```

> **Core Principle**: Incident postmortem should write root cause and improvement measures, not "already fixed". Improvement measures should be specific to responsible person and deadline.

---

## Reference Files

- [`SKILL_lintstart.md`](./SKILL_lintstart.md) — Lightstart mode + general rules
- [`SKILL_maintenance.md`](./SKILL_maintenance.md) — Evaluation & improvement
- `scoring_criteria.json` — Complete scoring criteria for five categories
- `scorer.py` — Mean calculation script
