# Project Rules & AI Guardrails

## Core Coding Guidelines

### What We Do
- **Zero-Dependency Core**: Use native web standards (HTML5, Vanilla CSS, modern JavaScript) and Python standard library for maximum reliability, speed, and zero installation friction.
- **Realistic & Minimalist Styling**: Pure, polished interfaces with high contrast, subtle borders, and zero gaudy neon/glowing effects.
- **Strict File Isolation**: Ensure all backend operations execute safely within the project boundary.
- **Deterministic 3-Layer Build**:
  - Layer 1: SOPs in `architecture/`
  - Layer 2: Decision routing in `app.js` and `server.py`
  - Layer 3: Atomic deterministic scripts in `tools/`
- **Mandatory Documentation Integrity**: Maintain the 9 Core Documents and the 4 workspace log files in `project-logs/`.

### What We Avoid
- **Avoid Heavy Framework Bloat**: No complex bundlers, Webpack, or large node module trees unless explicitly required.
- **Avoid Asking Permission**: The agent is authorized for 100% autonomous operation; never ask the user for confirmation or button clicks.
- **Avoid Neon/Cyberpunk Aesthetic**: Strictly forbidden to use eye-straining glowing text, purple/cyan neon borders, or generic AI templates.

## Proven Libraries & Standards
- **Icons**: Clean SVG icon system (Lucide compatible).
- **Git**: Direct standard Git CLI execution (`git init`, `git add`, `git commit`).
- **Data Formatting**: Strict ISO 8601 timestamps and standard Markdown formatting.

## AI Boundary Rules
- Never delete user files without an explicit autonomous replacement.
- Always self-anneal when errors occur: diagnose stack traces, patch scripts, and verify.
