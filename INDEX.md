# INDEX.md — Master Codebase Map (AI Token Saver)
<!-- INGEST THIS FILE INSTEAD OF GREPPING MULTIPLE SOURCE FILES -->

| File | Purpose | Key Exports / Endpoints / Tokens | Dependents |
|------|---------|----------------------------------|------------|
| `server.py` | Python 3.11 Local API & File Server | `GET /api/status`, `GET /api/git-status`, `POST /api/git-commit`, `POST /api/generate-docs`, `POST /api/generate-ide`, Port `8765` | `app.js`, Browser |
| `index.html` | Web Application UI & Studio Shell | `#topNav`, `#metricsBar`, `#docTabs`, `#docContent`, `#gitModal`, `#seoModal`, `#ideModal` | `styles.css`, `app.js` |
| `styles.css` | Realistic Minimalist Design System | `--bg-canvas (#0c0d0e)`, `--bg-surface (#141618)`, `--accent-primary (#2563eb)`, Dark/Light Tokens | `index.html` |
| `app.js` | Client-side State & Event Controller | `DOCS_METADATA`, `loadDocument()`, `switchTab()`, `runFullAutonomy()`, `executeGitCommit()` | `index.html`, `server.py` |
| `FAST_RESUME.md` | Crash/Quota Context Snapshot | Ultra-dense JSON checkpoint for zero-token-loss resumption | Any AI Agent |
| `HUMAN_BRIEF.md` | Human Executive Summary | Ultra-concise bullet digest for fast human review | Human Developer |
| `PRD.md` | 01 Product Requirements | Problem statement, target users, vision, features, MVP scope | Entire Project |
| `Architecture.md` | 02 Technical Architecture | Tech stack, directory tree, database schema, A.N.T. 3-layer build | Entire Project |
| `security.md` | 03 Security & Access | Auth methods, roles matrix, row-level security, edge cases | Entire Project |
| `design.md` | 04 Frontend Specification | Realistic minimalism, typography scale, component tokens | `styles.css`, `index.html` |
| `phases.md` | 05 Feature Ticket List | Sprint roadmap, tickets OP-101 to OP-106 with acceptance criteria | Project Milestones |
| `flow.md` | App Flow & User Journey | State machine, user screen transitions | UI Development |
| `rules.md` | Project Rules & Guardrails | Invariants, what to do, what to avoid, AI boundaries | Agent Behavior |
| `decision.md` | Architectural Decision Log | ADR-001, ADR-002, ADR-003 records | Architecture |
| `memory.md` | Dynamic Working Memory | Active files, system state, Graphify entity link maps | Agent Context |
| `manifest.webmanifest` | PWA & App Store Discovery | App metadata, standalone display, icons | Search Engines, OS |
| `robots.txt` / `sitemap.xml`| Search Engine Crawlers | Directives and page links | Google / Bing |
| `.vscode/` | VS Code Configuration | `settings.json`, `tasks.json`, `extensions.json` | VS Code Editor |
| `.cursorrules` | Cursor IDE AI Rules | Cursor-specific agent guardrails & coding standards | Cursor IDE |
| `run.bat` / `run.sh` | Cross-Platform Launchers | Windows batch & POSIX shell one-click runners | OS Shells |
