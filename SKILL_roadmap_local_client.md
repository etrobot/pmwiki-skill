---
name: Local Client Roadmap
description: Product roadmap template for desktop applications. Use this Skill for scenarios such as "desktop app roadmap", "local client planning", "cross-platform app", "Electron app roadmap", "Tauri app roadmap", etc.
---

# Code Review Tool Roadmap (Local Client Example)

## Project Attributes
- **Type**: Local Client
- **Core Value**: Automated code review to improve code quality
- **Target Users**: Developers, technical teams

---

## Phase 1 — Single Core Feature Available
**Goal**: Install and scan code, find obvious issues

### Requirements Iteration
- ✅ Only do "select project directory → scan → display issue list" workflow
- ✅ Support 3 mainstream languages: JavaScript, Python, Java
- ✅ Results correct but UI rough, users can see issue location and suggestions

### Feature Checklist
- [ ] Main interface (select project directory button)
- [ ] Code scanning engine (integrate ESLint, Pylint, Checkstyle)
- [ ] Issue list display (file path, line number, description, severity level)
- [ ] Basic error messages (directory not found, no permission, scan failed)

### Architecture Decisions
- **Tech Stack**: Electron + React
- **Storage**: Local JSON file for scan history
- **Configuration**: Hardcoded rule sets (no customization)
- **Updates**: No auto-update, manual download new versions

### Acceptance Criteria
- [ ] Scan 100k lines of code < 30 seconds
- [ ] Issue detection rate matches CLI tools
- [ ] Runs normally on Windows / Mac / Linux

---

## Phase 2 — Polish Core Experience
**Goal**: Smooth to use, error feedback, auto-update

### Requirements Iteration
- Installation wizard: Guide users to select default scan rules on first launch
- History: Save each scan result, support comparing two scans
- Auto-update: Background check for new versions, one-click upgrade

### Feature Checklist
- [ ] Installation wizard (select language + rule set)
- [ ] Settings page (custom rules, ignore files, scan depth)
- [ ] Scan history (timeline display + issue trend chart)
- [ ] Undo function (undo last ignore operation)
- [ ] Log viewer (view scan logs + error stack)
- [ ] Crash reporting (auto-send crash logs to server)
- [ ] Auto-update (detect new version + background download + restart install)

### Architecture Upgrades
- **Packaging Tool**: Electron Builder (generate .exe / .dmg / .AppImage)
- **Code Signing**: Windows (Authenticode), Mac (Apple Developer ID)
- **Logging System**: Winston + local file storage (rotate by date)
- **Update Mechanism**: electron-updater (incremental updates)
- **Process Communication**: Main process (scan) ↔ Renderer process (UI) via IPC

### Acceptance Criteria
- [ ] Installer < 100MB
- [ ] Auto-update success rate > 95%
- [ ] Crash rate < 0.1%

---

## Phase 3 — Multi-Module Expansion
**Goal**: From single tool to complete code quality workbench

### Requirements Iteration
- Multi-project management: Support managing multiple projects simultaneously, quick switch
- Data export: Export scan results as PDF / HTML reports
- Shortcuts: Support global shortcuts to quickly launch scan
- External tool integration: Integrate with Git, only scan changed files

### Feature Checklist
- [ ] Multi-project management (project list + quick switch)
- [ ] Data export (PDF / HTML / JSON formats)
- [ ] Global shortcuts (Ctrl+Shift+R launch scan)
- [ ] System tray integration (minimize to tray + right-click menu)
- [ ] Git integration (only scan git diff files)
- [ ] Local data backup / restore (export config + history)
- [ ] Theme switching (light / dark / custom)

### Architecture Upgrades
- **Data Encryption**: Sensitive config (API Key) using Keychain (Mac) / DPAPI (Windows)
- **Workspace Isolation**: Each project independent SQLite database
- **File Association**: Double-click .codereview file auto-opens project

### Acceptance Criteria
- [ ] Support managing > 10 projects
- [ ] Export report < 5 seconds
- [ ] Git integration scan speed improvement > 80%

---

## Phase 4 — Plugin System & Ecosystem
**Goal**: Let third-party developers extend tool capabilities

### Requirements Iteration
- Plugin marketplace: Support installing third-party rule sets, language support, report templates
- Cloud sync: Optional sync of config and history to cloud
- Multi-account: Support team collaboration, shared rule config

### Feature Checklist
- [ ] Plugin marketplace (browse + install + update plugins)
- [ ] Plugin API documentation (provide SDK + sample plugins)
- [ ] Plugin developer tools (debug mode + log viewer)
- [ ] Cloud sync (optional, sync config + history)
- [ ] Multi-account switching (personal account / team account)

### Architecture Upgrades
- **Plugin Sandbox**: Plugins run in separate process, crashes don't affect main program
- **Plugin Lifecycle**: Load → Activate → Unload → Hot Reload
- **Cloud Sync Protocol**: WebSocket + incremental sync
- **Permission Management**: Plugins must declare permissions (file read/write, network access)

### Acceptance Criteria
- [ ] Plugin marketplace > 20 plugins
- [ ] Cloud sync users > 1000
- [ ] Plugin crashes don't affect main program

---

## Milestone Checkpoints

| Phase | Core Metrics | Go / No-Go Decision |
|-------|--------------|---------------------|
| Phase 1 | 100 downloads, scan success rate > 95% | If crash rate > 5%, prioritize stability fixes |
| Phase 2 | 1000 active users, auto-update success > 95% | If update failure > 10%, redesign update mechanism |
| Phase 3 | 5000 active users, multi-project usage > 50% | If usage < 30%, simplify multi-project switching |
| Phase 4 | Marketplace > 20 plugins, cloud sync > 1000 | If plugin ecosystem inactive, consider official core plugins |

---

## Technical Debt Management

### Phase 1 → 2 Must Resolve
- [ ] Add unit tests (core scan logic coverage > 80%)
- [ ] Introduce E2E tests (Playwright)

### Phase 2 → 3 Must Resolve
- [ ] Performance optimization (large project scan time < 1 minute)
- [ ] Memory leak detection (long-running without crashes)

### Phase 3 → 4 Must Resolve
- [ ] Plugin security audit (prevent malicious plugins)
- [ ] Cloud sync data encryption (end-to-end encryption)
