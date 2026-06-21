# Technical Specification – mindcode‑sync

---

## 1. Overview

**mindcode‑sync** is a VS Code extension that provides an interactive *Architecture Wizard* for generating and persisting architectural artifacts within a workspace.  
The extension is built on the VS Code Extension API, uses a lightweight webview for the wizard UI, and stores user selections in the workspace folder.

---

## 2. Architecture

```
+------------------+          +---------------------+          +-----------------+
|  VS Code Host    |          |  Extension Host     |          |  Webview UI     |
|  (Extension API) |<-------->|  (Node.js runtime)  |<-------->|  (HTML/TS)      |
+------------------+          +---------------------+          +-----------------+
          |                              |                            |
          | 1. Register command           | 2. Handle command          | 3. Render UI
          |------------------------------>|-------------------------->|---------------->
          |                              |                            |
          | 4. Persist selections         | 5. Read/write workspace   | 6. Send/receive events
          |<------------------------------|<--------------------------|<----------------
```

### 2.1 Components

| Component | Responsibility | Tech |
|-----------|----------------|------|
| **Extension Host** | Registers commands, manages state, reads/writes workspace files | Node.js (ES6), VS Code API |
| **Webview UI** | Renders wizard, captures user input, communicates with host | HTML5, CSS, TypeScript, VS Code Webview API |
| **Persistence Layer** | Stores selections in a JSON file under `.mindcode/` | File System (Node.js `fs`) |
| **Command** | `mindcode.sync.architecture` | VS Code command palette |

---

## 3. Data Model

```json
{
  "architecture": {
    "layers": [
      {
        "name": "Presentation",
        "components": ["UI", "Controller"]
      },
      {
        "name": "Business Logic",
        "components": ["Service", "Repository"]
      }
    ],
    "communication": "REST",
    "database": "PostgreSQL"
  },
  "metadata": {
    "generatedAt": "2026-06-21T12:34:56Z",
    "generatedBy": "mindcode-sync@0.1.0"
  }
}
```

*File path:* `<workspace>/.mindcode/architecture.json`

*Schema:*  
- `architecture.layers` – array of layers, each with `name` and `components`.  
- `architecture.communication` – string (e.g., REST, gRPC).  
- `architecture.database` – string.  
- `metadata` – audit fields.

---

## 4. Key APIs / Interfaces

| API | Purpose | Parameters | Returns |
|-----|---------|------------|---------|
| `registerCommand('mindcode.sync.architecture', handler)` | VS Code command registration | `handler: () => void` | void |
| `showWizard()` | Opens the webview | none | `Promise<void>` |
| `persistSelections(data: ArchitectureData): Promise<void>` | Writes JSON to workspace | `data` – architecture object | void |
| `loadSelections(): Promise<ArchitectureData | null>` | Reads JSON from workspace | JSON object or null |
| `postMessageToWebview(message: any): void` | Host → UI | message | void |
| `onMessageFromWebview(callback: (msg) => void): void` | UI → Host | callback | void |

---

## 5. Technology Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **Extension Host** | Node.js 20.x | Stable, VS Code runtime |
| **Package Manager** | Poetry (Python) | Existing dev tooling; tests are Python‑based |
| **Testing** | PyTest | Existing test harness |
| **UI** | TypeScript, React (optional), Webview API | Modern UI, easy to bundle |
| **Bundler** | esbuild | Fast, minimal config |
| **Linting / Formatting** | ESLint, Prettier | Code quality |
| **Versioning** | Semantic Versioning | Clear release cycle |

---

## 6. Dependencies

| Dependency | Version | Purpose |
|------------|---------|---------|
| `vscode` | `^1.90.0` | Extension API |
| `@vscode/webview` | `^1.0.0` | Webview utilities |
| `esbuild` | `^0.20.0` | Bundling |
| `typescript` | `^5.4.0` | Type safety |
| `prettier` | `^3.0.0` | Formatting |
| `eslint` | `^8.0.0` | Linting |
| `pyproject.toml` | – | Poetry configuration |
| `pytest` | `^8.0.0` | Test runner |

All dependencies are declared in `package.json` and `pyproject.toml`. No external runtime is required beyond VS Code.

---

## 7. Deployment

1. **Development**  
   ```bash
   git clone <repo>
   cd mindcode-sync
   poetry install
   npm install
   npm run build   # bundles extension
   code .
   ```

2. **Packaging**  
   ```bash
   npm run package   # creates .vsix
   ```

3. **Publishing**  
   ```bash
   vsce publish
   ```

   *Prerequisite:* VS Code Marketplace publisher account.

4. **Distribution**  
   - Users install via VS Code Marketplace or by running `code --install-extension mindcode-sync-0.1.0.vsix`.

5. **Runtime**  
   - Extension activates on command registration (`onCommand`).
   - Webview is sandboxed; communication via `postMessage`.

---

## 8. Security & Privacy

- All persisted data resides in the workspace folder; no external network calls.
- Webview content is loaded from local files; CSP set to `default-src 'none'; script-src 'self'; style-src 'self'`.
- No telemetry or data exfiltration.

---

## 9. Extensibility

- **Plugin Hooks** – expose `onArchitectureGenerated` event for downstream tools.
- **Template Engine** – plug in Mustache/Handlebars for generating code files.
- **Multi‑Language Support** – add language packs via `package.json` contributes.

---

## 10. Roadmap (Short Term)

| Feature | Description | Status |
|---------|-------------|--------|
| UI Enhancements | Drag‑and‑drop layer ordering | Planned |
| Validation | Schema validation on save | Planned |
| Export | Generate README.md with architecture diagram | Planned |

---

## 11. Appendix

### 11.1 File Structure

```
mindcode-sync/
├─ src/
│  ├─ extension.ts          # Host logic
│  ├─ webview.ts            # UI entry point
│  └─ persistence.ts        # File I/O
├─ web/
│  ├─ index.html
│  ├─ styles.css
│  └─ app.ts
├─ package.json
├─ tsconfig.json
├─ pyproject.toml
└─ README.md
```

### 11.2 Test Strategy

- **Unit Tests** – Jest for TypeScript modules.  
- **Integration Tests** – PyTest with `vscode-test` to launch an extension host.  
- **End‑to‑End** – Simulate command execution, verify file creation.

---
