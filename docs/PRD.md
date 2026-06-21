# Product Requirements Document (PRD)

**Project:** Mindcode‑Sync  
**Version:** 1.0.0  
**Author:** Senior Product & Engineering Lead  
**Date:** 2026‑06‑21  

---

## 1. Problem Statement

Software architects and senior developers often struggle to maintain a consistent, up‑to‑date architectural diagram or documentation that reflects the current state of a codebase. Existing tools either require manual effort, external services, or are not tightly integrated into the IDE workflow. This leads to:

- **Fragmented knowledge** – architectural decisions are scattered across emails, wikis, and code comments.  
- **Out‑of‑date artifacts** – diagrams become stale as the code evolves.  
- **Long onboarding times** – new team members spend excessive time understanding the architecture.  

A lightweight, IDE‑centric solution that automatically captures architectural intent and stores it alongside the code would reduce cognitive load, improve onboarding, and ensure documentation fidelity.

---

## 2. Target Users

| Persona | Role | Pain Points | How Mindcode‑Sync Helps |
|---------|------|-------------|------------------------|
| **Lead Architect** | Oversees system design | Needs quick, accurate diagrams; wants to enforce architectural standards | Generates a wizard‑guided architecture snapshot that can be version‑controlled |
| **Senior Developer** | Builds and refactors code | Wants to document decisions without leaving the IDE | Persists selections to the workspace, enabling peer review |
| **New Team Member** | Onboarding | Struggles to understand system structure | Provides an up‑to‑date, IDE‑embedded architecture view |
| **Technical Lead** | Ensures compliance | Needs audit trails of architectural decisions | Stores selections in a reproducible format within the repo |

---

## 3. Goals & Objectives

| Goal | Success Metric | Target |
|------|----------------|--------|
| **Seamless IDE integration** | 90 % of users launch the wizard via the command palette without external steps | 90 % |
| **Accurate architecture capture** | 95 % of generated diagrams match manual reference diagrams | 95 % |
| **Low friction** | Average wizard completion time < 2 min | < 2 min |
| **Version‑controlled artifacts** | 100 % of selections persisted to a JSON file in the workspace | 100 % |
| **Developer satisfaction** | NPS score ≥ 50 after 1‑month usage | ≥ 50 |

---

## 4. Key Features (Prioritized)

| Priority | Feature | Description | Acceptance Criteria |
|----------|---------|-------------|---------------------|
| **P1** | **Command Registration** | Register `mindcode.sync.architecture` in VSCode command palette | Command appears and opens wizard on execution |
| **P1** | **Wizard UI** | Render wizard in a VSCode webview with step‑by‑step prompts (e.g., component selection, dependency mapping) | Webview loads, UI elements are interactive, navigation works |
| **P1** | **Persist Selections** | Save user selections to a workspace‑level JSON file (`.mindcode/architecture.json`) | File created, contains all selections, updates on wizard changes |
| **P2** | **Auto‑Detection of Project Structure** | Pre‑populate wizard options by scanning the workspace for common patterns (e.g., `src/`, `components/`) | Suggested options appear, user can override |
| **P2** | **Export to Diagram** | Generate a Mermaid or PlantUML diagram from selections | Diagram file created, renders correctly in VSCode preview |
| **P3** | **Version Control Integration** | Auto‑stage changes to `.mindcode/architecture.json` in Git | Commit message auto‑generated, file tracked |
| **P3** | **Undo/Redo** | Allow users to revert wizard steps | State restored to previous step |
| **P4** | **Custom Templates** | Let users define custom architecture templates | Templates load, wizard adapts accordingly |
| **P5** | **Analytics** | Track wizard usage anonymously | Metrics collected, no PII |

---

## 5. Success Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| **Wizard Adoption Rate** | % of active VSCode users who run the command | 30 % within 3 months |
| **Diagram Accuracy** | % of diagrams that match a manually curated gold standard | 95 % |
| **User Satisfaction** | NPS score from in‑app survey | ≥ 50 |
| **Persistence Reliability** | % of runs where JSON file is correctly written | 100 % |
| **Performance** | Avg. time to open wizard and finish first run | < 5 s |

---

## 6. Scope

### In‑Scope

- VSCode extension for Windows, macOS, Linux (Electron)
- Webview wizard UI (React/TypeScript)
- JSON persistence in workspace
- Basic diagram export (Mermaid)
- Unit & integration tests (pytest + VSCode Extension Tester)
- Documentation (README, usage guide)

### Out‑of‑Scope

- Native support for other IDEs (JetBrains, Sublime)
- Advanced AI‑based architecture inference
- Cloud synchronization or multi‑user collaboration
- Custom diagram rendering engines beyond Mermaid
- Continuous integration pipeline beyond local tests

---

## 7. Dependencies & Constraints

| Dependency | Source | Version | Notes |
|------------|--------|---------|-------|
| **VSCode Extension API** | Microsoft | Latest | Must support webview and command registration |
| **React** | npm | 18.x | For wizard UI |
| **Mermaid** | npm | 10.x | For diagram generation |
| **Poetry** | Python | 1.8+ | Dependency manager for dev environment |
| **pytest** | Python | 7.x | For unit tests |
| **Git** | System | 2.30+ | For version control integration |

Constraints:

- Must run on the same Python version used in the repo (`poetry install`).
- No external network calls during wizard execution (offline mode).
- All persisted data must be stored under `.mindcode/` to avoid polluting the repo.

---

## 8. Timeline (High‑Level)

| Phase | Duration | Deliverables |
|-------|----------|--------------|
| **Discovery & Design** | 1 week | PRD, wireframes, API contract |
| **Core Implementation** | 3 weeks | Command, wizard UI, persistence |
| **Diagram Export** | 1 week | Mermaid integration |
| **Testing & QA** | 1 week | Unit, integration, E2E tests |
| **Documentation & Release** | 1 week | README, usage guide, VSIX package |

---

## 9. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Low adoption** | Project may not be used | Conduct quick surveys, gather feedback early |
| **Performance lag** | Webview slow on large projects | Lazy load components, optimize file scanning |
| **Data loss** | JSON persistence fails | Implement atomic writes, backup on failure |
| **Compatibility** | VSCode API changes | Keep dependency up‑to‑date, run CI on latest VSCode |

---

## 10. Acceptance Criteria

1. **Command** `mindcode.sync.architecture` appears in the command palette and opens the wizard.  
2. **Wizard** loads within 5 s, offers at least three steps, and validates input.  
3. **Selections** are persisted to `.mindcode/architecture.json` and updated on each change.  
4. **Diagram** can be exported as a `.mmd` file and previewed in VSCode.  
5. **Tests**: ≥ 90 % coverage, all CI checks pass.  
6. **Documentation**: README updated with installation, usage, and troubleshooting.  

---

## 11. Appendix

- **Wireframes**: (link to Figma/Sketch)  
- **API Spec**: (link to JSON schema for `.architecture.json`)  
- **Test Plan**: (link to test suite)  

---
