---
name: toC App Roadmap
description: Product roadmap template for consumer applications. Use this Skill for scenarios such as "toC app roadmap", "consumer app planning", "user growth strategy", "SaaS product roadmap", "mobile app roadmap", etc.
---

# AI Writing Assistant Roadmap (toC App Example)

## Project Attributes
- **Type**: toC Application
- **Core Value**: Help users quickly generate high-quality articles
- **Target Users**: Content creators, self-media, students

---

## Phase 1 — Single Core Feature Available (0-2 months)
**Goal**: New users feel "AI writing is actually useful" on first use

### Requirements Iteration
- ✅ Only do "input topic → generate article" core workflow
- ✅ Registration flow: Email + Google OAuth, complete within 3 steps
- ✅ Generated results have "wow factor": beautiful formatting, one-click copy, shareable link

### Feature Checklist
- [ ] User registration / login (Email + Google OAuth)
- [ ] Article generator (input topic + keywords → generate 800-1500 word article)
- [ ] Result display page (Markdown rendering + one-click copy + share link)
- [ ] Basic error messages (API timeout, generation failed)

### Architecture Decisions
- **Backend**: Node.js + Express, monolith
- **Database**: PostgreSQL single database (user table + article table)
- **AI Integration**: Direct OpenAI API calls (no caching)
- **Deployment**: Single VPS (Vercel / Railway)
- **Monitoring**: No analytics, rely on user feedback

### Acceptance Criteria
- [ ] New user from registration to first article < 3 minutes
- [ ] Generation success rate > 95%
- [ ] At least 10 real users willing to share results on social media

---

## Phase 2 — Polish Core Experience (2-4 months)
**Goal**: Users who tried once want to come back, 7-day retention > 20%

### Requirements Iteration
- Onboarding: Show example topics on first use, lower input barrier
- History: Users can see all articles they've generated
- Recall mechanism: Send weekly email reminding users of "this week's hot topics"

### Feature Checklist
- [ ] Onboarding flow (3-step guide + example topics)
- [ ] My Articles (history + favorites)
- [ ] Email notification system (weekly push hot topics)
- [ ] Personal homepage (generation stats: total words, article count)
- [ ] Empty state optimization (show "start creating" guide when no history)
- [ ] Loading state (show progress bar + estimated time during generation)

### Architecture Upgrades
- **Message Queue**: Introduce Bull (Redis) for async email sending
- **Analytics**: Integrate Mixpanel, track user behavior (registration, generation, sharing)
- **CDN**: Migrate static assets to Cloudflare CDN
- **Caching**: Redis cache hot topic generation results (24-hour expiration)

### Acceptance Criteria
- [ ] 7-day retention rate > 20%
- [ ] Email open rate > 15%
- [ ] Users average > 3 articles/week

---

## Phase 3 — Multi-Module Expansion (4-8 months)
**Goal**: From single-function tool to platform users want to stay on

### Requirements Iteration
- Pre-need: Provide "outline generation" to help users clarify thoughts
- Post-need: Provide "article polish" to optimize existing content
- Social elements: Users can like and comment on excellent articles
- Payment validation: Free users 5 articles/month, Pro users unlimited

### Feature Checklist
- [ ] Outline generator (input topic → generate 3-5 level outline)
- [ ] Article polisher (upload text → AI optimizes language, logic)
- [ ] Community square (display excellent articles + likes + comments)
- [ ] Subscription system (Free vs Pro: $9.9/month)
- [ ] Search function (search history + community articles)
- [ ] Billing management & invoice download

### Architecture Upgrades
- **Feature Flag**: LaunchDarkly control Pro feature gradual rollout
- **Payment Integration**: Stripe (credit card) + Alipay
- **Read-Write Separation**: PostgreSQL master-slave replication
- **Search Engine**: PostgreSQL full-text index (later consider Elasticsearch)

### Acceptance Criteria
- [ ] Payment conversion rate > 3%
- [ ] Pro user monthly retention > 60%
- [ ] Community DAU > 500

---

## Phase 4 — Open Platform & Growth Flywheel (8-12 months)
**Goal**: Users extend product themselves, growth no longer relies only on paid acquisition

### Requirements Iteration
- Referral mechanism: Existing users invite new users, both get 3 free articles
- API opening: Let developers integrate AI writing into their own products
- Personalized recommendations: Recommend related content based on user history topics

### Feature Checklist
- [ ] Referral system (generate invite link + reward mechanism)
- [ ] Open API (provide REST API + API Key management)
- [ ] Webhook (callback to user server after article generation)
- [ ] Zapier integration (connect Notion, Google Docs)
- [ ] Personalized recommendation feed (recommend topics based on user interests)
- [ ] A/B experiment framework (test different UI / copy impact on conversion)

### Architecture Upgrades
- **Recommendation Service**: Independent microservice (Python + TensorFlow)
- **API Gateway**: Kong / AWS API Gateway (rate limiting + auth)
- **A/B Experiment Platform**: Self-built or integrate Optimizely
- **Event Bus**: Kafka (user behavior → trigger Webhook)

### Acceptance Criteria
- [ ] Referral-driven new users > 30%
- [ ] API calls > 100k/month
- [ ] Recommendation click-through rate > 10%

---

## Milestone Checkpoints

| Phase | Timeline | Core Metrics | Go / No-Go Decision |
|-------|----------|--------------|---------------------|
| Phase 1 | 2 months | 100 registered users, generation success > 95% | If success < 90%, optimize AI Prompt |
| Phase 2 | 4 months | 7-day retention > 20%, email open > 15% | If retention < 15%, redesign recall mechanism |
| Phase 3 | 8 months | Payment conversion > 3%, Pro users > 100 | If conversion < 2%, adjust pricing or features |
| Phase 4 | 12 months | Referral ratio > 30%, API calls > 100k/month | If growth stalls, consider pivot or fundraising |

---

## Technical Debt Management

### Phase 1 → 2 Must Resolve
- [ ] Add unit tests (core generation logic coverage > 80%)
- [ ] Introduce logging system (Winston + Sentry)

### Phase 2 → 3 Must Resolve
- [ ] Database migration solution (use Prisma Migrate)
- [ ] API rate limiting (prevent abuse)

### Phase 3 → 4 Must Resolve
- [ ] Microservice split (recommendation service independent deployment)
- [ ] Monitoring & alerting (Prometheus + Grafana)
