---
name: Operations Capability Timeline
description: Guidance on when to introduce operational capabilities like cron jobs, logging, and alerting. Use this Skill for scenarios such as "when to add logging", "alerting timeline", "ops capability planning", "monitoring strategy", "observability roadmap", etc.
---

# Operations Capability Timeline Guide

## Core Principles

**Don't optimize too early, but don't wait until it's on fire**

- Phase 1: Just make it work, handle everything manually
- Phase 2: Start automation, establish basic observability
- Phase 3: Complete monitoring, preventive operations
- Phase 4: Intelligent ops, self-healing capabilities

---

## I. Cron Jobs / Scheduled Tasks

### Phase 1 — Not Needed
**Reason**: Low user count, manual operations sufficient

**Exceptions**:
- ❌ Not needed: Data cleanup, report generation
- ✅ Must have: Certificate expiration check (if using HTTPS)

---

### Phase 2 — Introduce Basic Scheduled Tasks
**Trigger Conditions**:
- User count > 100
- Repetitive work needs periodic execution
- Manual operations starting to fail or be missed

**Must-Have Scheduled Tasks**:

| Task Type | Frequency | Purpose | Example |
|-----------|-----------|---------|---------|
| **Database Backup** | Daily | Prevent data loss | `0 2 * * * pg_dump > backup.sql` |
| **Log Rotation** | Daily | Prevent disk full | `0 0 * * * logrotate /etc/logrotate.conf` |
| **Expired Data Cleanup** | Weekly | Free storage space | Delete temp files older than 30 days |
| **Health Check** | Every 5 minutes | Ensure service alive | `*/5 * * * * curl http://localhost/health` |

**Tech Stack**:
- **Local Client**: System Cron (Linux/Mac), Task Scheduler (Windows)
- **toC/toB**: Cron + scripts, or APScheduler (Python), node-cron (Node.js)

---

### Phase 3 — Complete Business Scheduled Tasks
**Trigger Conditions**:
- User count > 1000
- Complex business logic needs periodic execution
- Need to generate periodic reports

**New Scheduled Tasks**:

| Task Type | Frequency | Purpose | Example |
|-----------|-----------|---------|---------|
| **Report Generation** | Daily/Weekly | Send weekly/monthly reports to users | Generate project progress reports |
| **Data Sync** | Hourly | Sync data with third-party systems | Sync CRM data |
| **Expiration Reminders** | Daily | Remind users of renewals, task deadlines | Send expiration notification emails |
| **Data Aggregation** | Hourly | Pre-calculate statistics | Calculate user activity |
| **Cache Warming** | Daily | Improve access speed | Preload hot data to Redis |

**Tech Stack**:
- **Distributed Scheduling**: Celery Beat (Python), Bull (Node.js)
- **Visual Management**: Airflow, Prefect

---

### Phase 4 — Intelligent Scheduling
**Trigger Conditions**:
- Scheduled tasks > 50
- Complex dependencies between tasks
- Need to dynamically adjust execution time

**New Capabilities**:
- **Task Orchestration**: DAG (Directed Acyclic Graph) manage task dependencies
- **Dynamic Scheduling**: Auto-adjust execution time based on system load
- **Failure Retry**: Auto-retry failed tasks with exponential backoff
- **Task Monitoring**: Real-time view of task execution status, duration

**Tech Stack**:
- **Workflow Engine**: Airflow, Temporal, Prefect
- **Distributed Scheduling**: XXL-Job, Quartz

---

## II. Logging System

### Phase 1 — Minimal Logging
**Reason**: Low user count, console output sufficient

**Must-Have Logs**:
- ✅ Error logs: Record crashes, exceptions
- ✅ Critical operation logs (Info): User login, payment, data modification
- ❌ Not needed: Debug logs, performance logs

**Tech Stack**:
- **Local Client**: Write to local file (`app.log`)
- **toC/toB**: Standard output (stdout) + cloud platform auto-collection

**Log Format**:
```
[2026-05-08 10:30:45] ERROR - User login failed: Invalid password (user_id=123)
```

---

### Phase 2 — Structured Logging + Centralized Collection
**Trigger Conditions**:
- User count > 100
- Hard-to-reproduce bugs appearing
- Need to analyze user behavior

**Must-Have Capabilities**:

| Capability | Purpose | Example |
|------------|---------|---------|
| **Structured Logs** | Easy to query, analyze | JSON format: `{"level":"error","msg":"login failed","user_id":123}` |
| **Log Levels** | Distinguish importance | DEBUG < INFO < WARN < ERROR < FATAL |
| **Log Collection** | Centrally manage multi-server logs | Fluentd, Logstash, Vector |
| **Log Storage** | Persistent, searchable | Elasticsearch, Loki, CloudWatch Logs |
| **Log Query** | Quickly locate issues | Kibana, Grafana, CloudWatch Insights |

**Tech Stack**:
- **Local Client**: Winston (Node.js), Loguru (Python) + local files
- **toC/toB**: ELK Stack (Elasticsearch + Logstash + Kibana) or Grafana Loki

**Log Retention Policy**:
- ERROR logs: Keep 90 days
- INFO logs: Keep 30 days
- DEBUG logs: Keep 7 days

---

### Phase 3 — Log Analysis + Alert Integration
**Trigger Conditions**:
- Log volume > 1GB/day
- Need to proactively discover issues, not wait for user feedback

**New Capabilities**:

| Capability | Purpose | Example |
|------------|---------|---------|
| **Log Aggregation** | Discover common issues | Count most frequent errors in last hour |
| **Log Alerting** | Auto-notify on anomalies | ERROR logs > 100/min → send alert |
| **Log Correlation** | Trace request chain | Trace ID correlates all logs for one request |
| **Sensitive Data Masking** | Protect user privacy | Auto-hide passwords, phone numbers, ID numbers |

**Tech Stack**:
- **Distributed Tracing**: OpenTelemetry, Jaeger, Zipkin
- **Log Alerting**: ElastAlert, Grafana Alerts

---

### Phase 4 — Intelligent Log Analysis
**Trigger Conditions**:
- Log volume > 100GB/day
- Manual log analysis cost too high

**New Capabilities**:
- **Anomaly Detection**: AI auto-identifies abnormal log patterns
- **Root Cause Analysis**: Auto-correlate logs, metrics, events to locate root cause
- **Log Compression**: Intelligent sampling to reduce storage cost

**Tech Stack**:
- **AI Log Analysis**: Datadog, New Relic, Splunk

---

## III. Alerting System

### Phase 1 — Not Needed
**Reason**: Low user count, manual checks sufficient

**Exceptions**:
- ✅ Must have: Alert when service completely down (Uptime monitoring)

**Tech Stack**:
- **Free Tools**: UptimeRobot, Pingdom (free tier)

---

### Phase 2 — Basic Alerting
**Trigger Conditions**:
- User count > 100
- Users starting to use during non-work hours
- Incidents occurred due to delayed problem discovery

**Must-Have Alerts**:

| Alert Type | Trigger Condition | Notification Method | Example |
|------------|-------------------|---------------------|---------|
| **Service Down** | HTTP health check fails | SMS + Phone | Service unresponsive > 2 minutes |
| **Error Rate Spike** | Error logs > 100/min | Email + Slack | Login failure rate > 10% |
| **Disk Space Low** | Disk usage > 85% | Email | Database disk remaining < 10GB |
| **Memory Leak** | Memory usage continuously rising | Email | Memory usage > 90% for 10 minutes |
| **Certificate Expiring** | SSL cert < 7 days to expiry | Email | HTTPS cert expires in 7 days |

**Tech Stack**:
- **Local Client**: Sentry (crash reporting)
- **toC/toB**: Prometheus + Alertmanager, CloudWatch Alarms

**Alert Rules**:
```yaml
# Prometheus alert rule example
- alert: HighErrorRate
  expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
  for: 5m
  labels:
    severity: critical
  annotations:
    summary: "High error rate detected"
```

---

### Phase 3 — Complete Alert System
**Trigger Conditions**:
- User count > 1000
- Have SLA commitments (e.g., 99.9% availability)
- Too much alert noise, needs optimization

**New Capabilities**:

| Capability | Purpose | Example |
|------------|---------|---------|
| **Alert Severity** | Distinguish urgency | P0 (immediate), P1 (within 1 hour), P2 (same day) |
| **Alert Aggregation** | Reduce noise | Same alert within 5 minutes only sent once |
| **Alert Escalation** | Ensure issues handled | P0 alert unacknowledged for 10 min → notify supervisor |
| **Alert Silencing** | Don't send during maintenance | Silence "service down" alert during deployment |
| **Alert Correlation** | Quickly locate issues | Alert includes related logs, metrics links |

**Alert Notification Channels**:
- **P0 (Critical)**: SMS + Phone + Slack
- **P1 (Important)**: Slack + Email
- **P2 (General)**: Email

**Tech Stack**:
- **Alert Management**: PagerDuty, Opsgenie, OnCall (Grafana)

---

### Phase 4 — Intelligent Alerting + Self-Healing
**Trigger Conditions**:
- Alert count > 100/day
- Need to reduce manual intervention

**New Capabilities**:
- **Intelligent Noise Reduction**: AI identifies false positives, auto-filters
- **Anomaly Prediction**: Early warning of potential issues (e.g., disk will be full in 3 days)
- **Auto-Remediation**: Auto-execute fix scripts after alert triggers (e.g., restart service, scale up)
- **Alert Root Cause Analysis**: Auto-correlate multiple alerts, find root cause

**Tech Stack**:
- **AIOps Platform**: Moogsoft, BigPanda
- **Self-Healing System**: Kubernetes (auto-restart Pods), AWS Auto Scaling

---

## IV. Comprehensive Decision Matrix

### By Product Type

| Ops Capability | Local Client | toC App | toB SaaS |
|----------------|--------------|---------|----------|
| **Cron Jobs** | Phase 2 (local backup) | Phase 2 (data cleanup) | Phase 2 (data backup) |
| **Logging** | Phase 1 (local file) | Phase 2 (centralized) | Phase 2 (centralized) |
| **Alerting** | Phase 2 (crash reporting) | Phase 2 (service monitoring) | Phase 2 (service monitoring) |
| **Distributed Tracing** | Not needed | Phase 3 | Phase 3 |
| **Auto-Scaling** | Not needed | Phase 3 | Phase 3 |
| **Disaster Recovery** | Phase 3 (cloud sync) | Phase 3 (multi-region) | Phase 3 (multi-region) |

---

### By User Scale

| User Scale | Cron Jobs | Logging | Alerting | Monitoring |
|------------|-----------|---------|----------|------------|
| **< 100** | Manual execution | Local files | Uptime monitoring | None |
| **100-1000** | Cron + scripts | Structured + centralized | Basic alerts (down, errors) | Basic metrics (CPU, memory) |
| **1000-10000** | Distributed scheduling | Log analysis + alert integration | Alert severity + aggregation | APM (Application Performance Monitoring) |
| **> 10000** | Workflow engine | AI log analysis | Intelligent alerts + self-healing | Full-stack monitoring + AIOps |

---

### By Incident Impact

| Incident Type | Impact Scope | Introduction Timing | Priority |
|---------------|--------------|---------------------|----------|
| **Service Down** | All users cannot use | Phase 1 | P0 |
| **Data Loss** | User data permanently lost | Phase 2 | P0 |
| **Performance Degradation** | User experience worsens | Phase 2 | P1 |
| **Feature Malfunction** | Some features unavailable | Phase 2 | P1 |
| **UI Error** | Interface display issues | Phase 3 | P2 |

---

## V. Implementation Recommendations

### 1. Priority Ranking (Phase 2 Must-Do)

```
1. Database backup (prevent data loss)
2. Service down alert (ensure timely response)
3. Error log collection (quickly locate issues)
4. Disk space monitoring (prevent service crash)
5. Log rotation (prevent disk full)
```

### 2. Cost Control

| Phase | Monthly Budget | Recommended Solution |
|-------|----------------|----------------------|
| Phase 1 | $0 | Free tools (UptimeRobot, Sentry free tier) |
| Phase 2 | $50-200 | Cloud platform built-in monitoring (CloudWatch, Azure Monitor) |
| Phase 3 | $500-2000 | Self-hosted ELK + Prometheus or Datadog Starter |
| Phase 4 | $5000+ | Enterprise APM (Datadog, New Relic) + AIOps |

### 3. Team Capability Requirements

| Phase | Required Roles | Skill Requirements |
|-------|----------------|-------------------|
| Phase 1-2 | Dev Engineers | Can write scripts, configure Cron |
| Phase 3 | Dev + Ops | Familiar with Prometheus, ELK, Docker |
| Phase 4 | SRE Team | Familiar with Kubernetes, distributed systems, AIOps |

---

## VI. Common Mistakes

### ❌ Premature Optimization
- **Mistake**: Build complete ELK + Prometheus + Grafana in Phase 1
- **Consequence**: Waste time, increase maintenance cost
- **Correct Approach**: Use cloud platform built-in monitoring first, good enough is enough

### ❌ Too Late Introduction
- **Mistake**: Phase 3 and still no database backup
- **Consequence**: Data loss, cannot recover
- **Correct Approach**: Phase 2 must have backup + alerting

### ❌ Too Many Alerts
- **Mistake**: Send alert for all ERROR logs
- **Consequence**: Alert fatigue, real issues ignored
- **Correct Approach**: Only alert on issues affecting users

### ❌ Unstructured Logs
- **Mistake**: Chaotic log format, cannot query
- **Consequence**: Difficult to troubleshoot, waste time
- **Correct Approach**: Start using JSON format logs in Phase 2

---

## VII. Checklists

### Phase 1 → Phase 2 Must Complete

- [ ] Database auto-backup daily
- [ ] Send alert when service down (email/SMS)
- [ ] Error logs written to file, keep 30 days
- [ ] Send alert when disk usage > 85%
- [ ] Send reminder 7 days before SSL cert expires

### Phase 2 → Phase 3 Must Complete

- [ ] Centralize logs to Elasticsearch / Loki
- [ ] Alert severity (P0/P1/P2)
- [ ] Key business metrics monitoring (QPS, latency, error rate)
- [ ] Send alert when scheduled task fails
- [ ] Distributed tracing (Trace ID through all logs)

### Phase 3 → Phase 4 Must Complete

- [ ] Alert aggregation + noise reduction
- [ ] Anomaly detection (AI identifies abnormal patterns)
- [ ] Auto-scaling (auto-adjust resources based on load)
- [ ] Disaster recovery drills (quarterly)
- [ ] SLA monitoring (availability, performance metrics)

---

## VIII. Summary

| Ops Capability | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|----------------|---------|---------|---------|---------|
| **Cron Jobs** | ❌ Not needed | ✅ Basic tasks (backup, cleanup) | ✅ Business tasks (reports, sync) | ✅ Intelligent scheduling |
| **Logging** | ✅ Local files | ✅ Structured + centralized | ✅ Analysis + alert integration | ✅ AI analysis |
| **Alerting** | ✅ Uptime monitoring | ✅ Basic alerts (down, errors) | ✅ Severity + aggregation | ✅ Intelligent noise reduction + self-healing |
| **Monitoring** | ❌ Not needed | ✅ Basic metrics (CPU, memory) | ✅ APM + distributed tracing | ✅ Full-stack + AIOps |

**Core Principles**:
1. **Phase 1**: Just make it work, handle manually
2. **Phase 2**: Automate basic ops, establish observability (**most critical phase**)
3. **Phase 3**: Complete monitoring, preventive operations
4. **Phase 4**: Intelligent ops, self-healing capabilities
