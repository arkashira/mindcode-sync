# Roadmap – Mindcode‑Sync

| Phase | Release | Theme | Key Deliverables | MVP‑Critical |
|-------|---------|-------|------------------|--------------|
| **MVP** | **v0.1.0** | Core wizard plumbing | • Register `mindcode.sync.architecture` command <br>• Render wizard UI in a VSCode webview <br>• Persist user selections to the workspace <br>• Basic unit & integration tests | ✅ |
| **v1** | **v1.0.0** | Feature expansion & UX polish | • Multi‑step wizard with validation <br>• Context‑aware suggestions (e.g., project type, language) <br>• Export generated architecture files <br>• Basic telemetry (usage stats, error reporting) <br>• Accessibility improvements |  |
| **v2** | **v2.0.0** | AI‑powered insights & collaboration | • Integrate LLM (e.g., vLLM) for architecture recommendations <br>• Real‑time collaboration mode (shared wizard state) <br>• Version‑controlled architecture snapshots <br>• Advanced analytics dashboard |  |

---

## 1. MVP – v0.1.0

### Goal
Deliver a stable, test‑covered VSCode extension that lets a developer launch the architecture wizard, make selections, and persist those selections to the workspace. This is the minimum viable product for a public release and for internal validation.

### Must‑Have Features

| Feature | Description | Acceptance Criteria |
|---------|-------------|---------------------|
| **Command Registration** | `mindcode.sync.architecture` command appears in Command Palette and keybindings. | • Command triggers wizard <br>• No errors in console |
| **Webview Wizard** | Simple UI rendered in a VSCode webview. | • UI loads without flicker <br>• Responsive to user input |
| **Persist Selections** | Selections are stored in a JSON file under `.mindcode/` in the workspace. | • File created on first run <br>• Subsequent runs load existing selections |
| **Unit & Integration Tests** | Tests cover command registration, webview rendering, and persistence logic. | • 90%+ coverage <br>• CI passes on every push |
| **Packaging & Publishing** | Extension packaged for the VSCode Marketplace. | • `vsce` build succeeds <br>• Extension installs without warnings |

### Timeline (4 weeks)

| Week | Tasks |
|------|-------|
| 1 | Scaffold extension, set up `poetry`, create basic command. |
| 2 | Implement webview, basic UI skeleton. |
| 3 | Add persistence layer, write tests. |
| 4 | CI/CD, packaging, release candidate. |

---

## 2. Phase v1 – v1.0.0

### Theme
**Feature Expansion & UX Polish**

### Objectives
- Make the wizard more useful and user‑friendly.
- Provide a richer set of architecture options.
- Enable exporting of generated files.

### Key Deliverables

| Feature | Description | Acceptance Criteria |
|---------|-------------|---------------------|
| **Multi‑Step Wizard** | Break wizard into logical steps (project type → language → framework → components). | • Navigation controls (Next/Back) <br>• Validation before proceeding |
| **Context‑Aware Suggestions** | Auto‑detect project type/language from workspace files. | • Suggestions match detected context <br>• User can override |
| **Export Architecture** | Generate a folder with architecture files (README, diagram, config). | • Files correctly formatted <br>• Export path configurable |
| **Telemetry** | Basic usage analytics (feature usage, errors). | • Data sent to a secure endpoint <br>• Opt‑in prompt |
| **Accessibility** | WCAG 2.1 AA compliance for webview. | • Screen reader support <br>• Keyboard navigation |

### Timeline (6 weeks)

| Week | Tasks |
|------|-------|
| 1‑2 | Design wizard flow, update UI. |
| 3 | Implement context detection logic. |
| 4 | Add export functionality. |
| 5 | Integrate telemetry and opt‑in flow. |
| 6 | Accessibility audit, bug fixes, release. |

---

## 3. Phase v2 – v2.0.0

### Theme
**AI‑Powered Insights & Collaboration**

### Objectives
- Leverage LLMs to suggest architecture patterns.
- Enable real‑time collaboration on wizard state.
- Provide analytics for teams.

### Key Deliverables

| Feature | Description | Acceptance Criteria |
|---------|-------------|---------------------|
| **LLM Integration** | Use vLLM to generate architecture recommendations based on user selections. | • Recommendations appear in wizard <br>• Low latency (<2 s) |
| **Collaboration Mode** | Shared wizard state via WebSocket or VSCode Live Share. | • Multiple users see same state <br>• Conflict resolution |
| **Versioned Snapshots** | Store architecture snapshots in Git, with diff view. | • Snapshots commit automatically <br>• Diff UI shows changes |
| **Analytics Dashboard** | In‑extension dashboard showing usage, adoption, and architecture trends. | • Data visualized in webview <br>• Exportable reports |
| **Security & Privacy** | Ensure LLM queries and telemetry comply with data‑handling policies. | • Data encryption at rest & in transit <br>• User consent flow |

### Timeline (8 weeks)

| Week | Tasks |
|------|-------|
| 1‑2 | Set up vLLM inference server, integrate API. |
| 3 | Build collaboration backend (WebSocket). |
| 4 | Implement snapshot storage & diff UI. |
| 5 | Design analytics data model. |
| 6 | Build analytics dashboard. |
| 7 | Security audit, privacy compliance. |
| 8 | Final testing, documentation, release. |

---

## 4. Release Cadence

| Release | Frequency | Notes |
|---------|-----------|-------|
| **MVP** | 1 release | Target: 4 weeks |
| **v1.0.0** | 1 release | Target: 10 weeks after MVP |
| **v2.0.0** | 1 release | Target: 18 weeks after MVP |

---

## 5. Dependencies & Risks

| Category | Item | Mitigation |
|----------|------|------------|
| **Technical** | VSCode API changes | Keep extension on latest LTS, monitor deprecations |
| **LLM** | vLLM availability | Use fallback static recommendations |
| **Collaboration** | Network latency | Graceful degradation, local caching |
| **Security** | Data privacy | Enforce encryption, provide opt‑out |

---

## 6. Success Metrics

| Metric | Target |
|--------|--------|
| **Installation** | 1,000+ installs within 3 months |
| **Active Users** | 70% of installs open wizard at least once |
| **Export Rate** | 30% of users export architecture |
| **LLM Adoption** | 50% of users enable AI recommendations |
| **Retention** | 60% of users return within 30 days |

---

### Next Steps

1. **Kickoff** – Assign owners for each feature set.  
2. **Sprint Planning** – Break tasks into 2‑week sprints.  
3. **CI/CD** – Ensure automated tests and packaging.  
4. **Community Feedback** – Early beta invites after MVP.

---
