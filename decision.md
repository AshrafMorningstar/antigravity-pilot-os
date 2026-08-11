# Architectural Decision Log

## Decision 001: Autonomous Browser Tab Web Architecture
- **Date**: 2026-09-11
- **What Was Decided**: OmniPilot OS runs as a browser-first application backed by an embedded Python HTTP/API service on port 8765.
- **Why It Was Needed**: The user requested a program that opens in a browser tab with a single-click automation workflow, full 9-document management, and direct Git/GitHub integration.
- **Alternatives Considered**: Desktop GUI framework (Tkinter/PyQt) - rejected due to poor web responsiveness and lack of modern browser tab capabilities.
- **Impact**: Instant launch, accessible from any browser tab, zero build steps.

## Decision 002: Realistic Minimalist UI Aesthetic
- **Date**: 2026-09-11
- **What Was Decided**: Implement an ultra-clean, high-contrast, matte dark & light design system with subtle 1px borders (`#25292e`) and royal blue accenting (`#2563eb`).
- **Why It Was Needed**: Strictly eliminate the tacky neon/fluorescent cyber glow seen in generic AI templates and establish a serious, high-utility engineering tool.
- **Impact**: Professional appearance, maximum readability, high credibility for product and code inspection.

## Decision 003: Single-Click Git Automation Pipeline
- **Date**: 2026-09-11
- **What Was Decided**: Integrate local Git initialization, automated staging, and semantic commits into a single backend API call.
- **Why It Was Needed**: Users can finalize an entire repository and push to GitHub without manually typing terminal commands.
- **Impact**: 100% automated repository lifecycle management.
