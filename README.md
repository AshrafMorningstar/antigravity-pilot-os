# Antigravity Pilot OS `v10.0.0`
> A lightweight, zero-permission autonomous companion for Google Antigravity, Cursor, and AI-driven development.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version: 10.0.0](https://img.shields.io/badge/Release-v10.0.0-brightgreen.svg)](https://github.com/AshrafMorningstar/antigravity-pilot-os/releases)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9+-brightgreen.svg)](https://python.org)
[![Platform: Win | Mac | Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](run.sh)

---

### What's New in Version 10.0 (Milestone Release)
- 🚀 **100% Zero-Permission Execution Engine**: AI agents operate with full authority—no more repetitive permission popups.
- ⚡ **Token-Saving Recovery Layer**: `FAST_RESUME.md` (< 250 tokens) and `INDEX.md` (< 400 tokens) eliminate context burn and search waste.
- 📑 **The 9 Standardized Core Project Docs**: Automatic scaffolding of PRD, Architecture, Security, Design, Phases, Flow, Rules, Decisions, and Memory.
- 💻 **Universal IDE Support**: Native integration for Google Antigravity, Cursor (`.cursorrules`), and VS Code (`.vscode/`).
- 🎨 **Realistic Minimalist UI**: High-contrast, clean developer workspace—strictly zero gaudy neon glows.
- 🌍 **Universal Cross-Platform**: Native 1-click execution for Windows (`run.bat`), Linux, and macOS (`run.sh`).

---

### Why I built this

If you've spent any serious time coding with the new wave of agentic tools like Google Antigravity or Cursor, you've probably run into the exact same three headaches I did:

1. **The Permission Trap**: The agent stops every two minutes asking: *"Should I create this folder?"*, *"Can I run git status?"*, *"Do you approve this edit?"*. You end up spending more time babysitting popups than thinking about your product.
2. **Context Amnesia & Token Burn**: After a long session or hitting a rate limit, starting a new prompt often means burning 8,000+ tokens re-feeding the whole conversation history just to get the agent back up to speed.
3. **Architecture Rot**: When vibe coding quickly, documentation like PRDs, database schemas, and security access rules get neglected, making the codebase a mess three days later.

**Antigravity Pilot OS** is my personal solution to this. It's a local, zero-dependency companion app that keeps AI agents on track, saves token budgets, maintains 9 standardized project documents, and commits to Git with a single click.

---

### What it actually does

- **100% Zero-Permission Mode**: Pre-authorizes your AI agents with strict boundaries so they can scaffold projects, execute tests, and repair errors autonomously.
- **Token-Saving Fast Resume (`FAST_RESUME.md`)**: A compact JSON state snapshot (< 250 tokens). If your agent crashes or hits a quota reset, feeding it this single file gives it 100% context instantly without re-reading thousands of lines of chat history.
- **Codebase Index Map (`INDEX.md`)**: A dense single-table index of every file, endpoint, and function. The agent reads this first instead of wasting search tokens running `grep` on 30 different files.
- **The 9 Standardized Project Docs**: Automatically scaffolds and syncs:
  - `PRD.md` (Product vision, user personas, MVP features vs nice-to-have)
  - `Architecture.md` (Tech stack, folder map, plain-English schema)
  - `security.md` (Roles, row-level security, edge cases)
  - `design.md` (Realistic minimalist design tokens — zero gaudy neon glows)
  - `phases.md` (Sprint tickets with acceptance criteria)
  - `flow.md` (User state machine and screens)
  - `rules.md` (Coding invariants and AI guardrails)
  - `decision.md` (Continuous architectural decisions log)
  - `memory.md` (Dynamic working memory)
- **30-Second Human Summary (`HUMAN_BRIEF.md`)**: A tiny plain-English bullet file so you can glance at the project state in half a minute.
- **Universal Multi-IDE Support**: Native configurations included for Cursor (`.cursorrules`), VS Code (`.vscode/`), and EditorConfig.
- **Zero Framework Bloat**: Runs on Python's built-in `http.server`. No Webpack, no node_modules folder eating 500MB of your disk space.

---

### Quick Start (Under 10 Seconds)

No installation or build tools required:

```bash
# 1. Clone the repo
git clone https://github.com/AshrafMorningstar/antigravity-pilot-os.git
cd antigravity-pilot-os

# 2. Run it
# Windows:
run.bat

# macOS / Linux:
chmod +x run.sh && ./run.sh

# Or directly with Python:
python server.py
```

It will automatically launch your default browser to **`http://127.0.0.1:8765`**.

---

### Project Structure

```
antigravity-pilot-os/
├── FAST_RESUME.md            # AI crash & quota recovery snapshot (< 250 tokens)
├── INDEX.md                  # Master symbol & endpoint map (saves AI search tokens)
├── HUMAN_BRIEF.md            # 30-second executive summary for humans
├── .cursorrules              # Native rules for Cursor IDE
├── .editorconfig             # Clean whitespace across all editors
├── .vscode/                  # Settings, tasks, and extension recommendations
│   ├── settings.json
│   ├── tasks.json
│   └── extensions.json
├── run.bat                   # 1-click Windows launcher
├── run.sh                    # 1-click macOS / Linux launcher
├── index.html                # Local web studio (IDE selector, tabbed 9-doc editor)
├── styles.css                # Realistic minimalist design (clean dark & daylight modes)
├── app.js                    # Reactive browser logic & 1-click triggers
├── server.py                 # Lightweight Python 3 backend & Git integration
├── PRD.md                    # 01 Product Requirements Document
├── Architecture.md           # 02 Technical Architecture Document
├── security.md               # 03 Security & Access Document
├── design.md                 # 04 Frontend Specification Document
├── phases.md                 # 05 Feature Ticket List
├── flow.md                   # App Flow & User Journey
├── rules.md                  # Project Rules & Boundaries
├── decision.md               # Architectural Decisions Log
├── memory.md                 # Dynamic Working Memory
└── project-logs/             # Work journals, decision logs, progress tracking
    ├── work.md
    ├── decision.md
    ├── progress.md
    └── extras.md
```

---

### How I use this in my daily workflow

1. When starting any new feature or app, I open **Antigravity Pilot OS** in a tab.
2. I type a 1-sentence vision in the sidebar and click **"1-Click Full Autonomy"**.
3. It generates the initial 9 architecture files and starts my Git branch cleanly.
4. If an agent session disconnects or gets interrupted, I simply point it to `FAST_RESUME.md` and it picks up right where it left off.
5. When ready, I click **"Sync to GitHub"** to commit and publish.

---

### FAQ

**Q: Does this send my code to any third-party cloud?**  
A: No. Everything runs 100% locally on your machine at `127.0.0.1`. No telemetry, no external accounts, no cloud dependencies.

**Q: Do I need Node.js or npm installed?**  
A: No. It uses standard vanilla HTML/CSS/JS in the frontend and Python's standard library in the backend.

**Q: Which IDEs does it work with?**  
A: Works out of the box with Google Antigravity, Cursor, VS Code, Windsurf, JetBrains, or any plain text editor.

---

### Legal & Trademark Notice
*This is an independent open-source community tool created for developers building with the Google Antigravity AI assistant and modern coding agents. It is not affiliated with, sponsored by, or endorsed by Google LLC. 'Google' and 'Antigravity' are trademarks of their respective owners.*

---
<div align="center">
  <img src="https://media.giphy.com/media/xT9IgvEOwRzUcZDRiU/giphy.gif" width="100%" height="200" alt="Horror Banner">
</div>

---
### License
MIT License. Feel free to fork, adapt, and use it in your own projects!
