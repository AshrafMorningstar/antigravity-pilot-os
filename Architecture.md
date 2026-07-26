# 02 Technical Architecture Document

## Tech Stack
- **Frontend Core**: HTML5 semantic markup, Vanilla ES6+ JavaScript (zero build step, instant execution).
- **Styling**: Modern Vanilla CSS3 with CSS custom properties (tokens), responsive flex/grid, and realistic minimalism.
- **Backend & Automation Engine**: Python 3.11 Standard Library (`http.server`, `urllib.parse`, `subprocess`, `json`, `os`, `sys`).
- **Version Control & Publishing**: Git 2.55+ local CLI integration and GitHub REST API / remote setup.
- **SEO & Search Standards**: Schema.org `SoftwareApplication` / `WebApplication` JSON-LD, W3C Web App Manifest.

## File & Folder Structure
```
omnipilot/
├── PRD.md                    ← 01 Product Requirements Document
├── Architecture.md           ← 02 Technical Architecture Document
├── security.md               ← 03 Security & Access Document
├── design.md                 ← 04 Frontend Specification Document
├── phases.md                 ← 05 Feature Ticket List
├── flow.md                   ← App Flow & User Journey
├── rules.md                  ← Project Rules & Boundaries
├── decision.md               ← Architectural Decisions Log
├── memory.md                 ← Dynamic Working Memory
├── index.html                ← Main Browser Tab Application
├── styles.css                ← Realistic Minimalist Design System
├── app.js                    ← Frontend State & UI Controllers
├── server.py                 ← Python API & Automation Backend
├── manifest.webmanifest      ← PWA & Search Engine App Store Manifest
├── sitemap.xml               ← Search Engine Crawler Map
├── robots.txt                ← Crawler Directive File
├── README.md                 ← GitHub Repository Master Readme
├── .gitignore                ← Standard Git Exclusions
├── project-logs/             ← Mandatory Workspace Journal
│   ├── work.md
│   ├── decision.md
│   ├── progress.md
│   └── extras.md
├── architecture/             ← Layer 1: SOPs (The "How-To")
│   ├── git-workflow.md
│   └── doc-generation.md
└── tools/                    ← Layer 3: Deterministic Scripts (The "Engines")
    ├── init_git.py
    └── generate_docs.py
```

## Database Schema (Local In-Memory / File-Backed)
OmniPilot operates on a file-backed deterministic model:
- **Project State Entity**:
  - `id`: String (UUID v4)
  - `projectName`: String (App title)
  - `vision`: String (North star summary)
  - `techStack`: Array of Strings
  - `documents`: Object containing contents of the 9 markdown artifacts
  - `gitStatus`: Object `{ initialized: Boolean, committed: Boolean, branch: String, commitHash: String }`
  - `updatedAt`: ISO 8601 Timestamp

## Environment & Configuration
- `PORT`: Server listening port (default: `8765`).
- `HOST`: Server bind address (default: `127.0.0.1` for secure local access).
- Zero hardcoded secrets: GitHub access tokens are passed via user session or native Git credential helper.

## A.N.T. 3-Layer Build
- **Layer 1: Architecture (`architecture/`)**: Markdown SOPs describing Git workflows and document generation algorithms.
- **Layer 2: Navigation**: `app.js` and `server.py` request router orchestrating execution.
- **Layer 3: Tools (`tools/`)**: Deterministic scripts for Git lifecycle and document scaffolding.
