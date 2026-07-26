# 04 Frontend Specification Document

## Design Philosophy: Realistic Minimalism & Understated Luxury
The visual identity of OmniPilot OS embodies **realistic minimalism**: high-contrast legibility, calm dark and warm neutral surfaces, delicate 1px borders, and disciplined typography.
- **Strict Prohibition**: No oversaturated fluorescent neon glows, no tacky cyber glowing buttons, no cheap AI marketing gradients.
- **Visual Feel**: High-precision engineering workbench, akin to Linear, Raycast, and Vercel.

## Color Palette
### Dark Theme (Default)
| Role | Token Name | Hex Code | Purpose |
|------|------------|----------|---------|
| **Background** | `--bg-canvas` | `#0c0d0e` | Deep canvas, matte finish |
| **Surface** | `--bg-surface` | `#141618` | Cards, panels, toolbars |
| **Surface Elevated** | `--bg-elevated`| `#1b1e22` | Popovers, active items |
| **Border Subtle** | `--border-subtle`| `#25292e` | Structural dividers, cards |
| **Border Active** | `--border-active`| `#383f47` | Focused inputs, hovered cards |
| **Text Primary** | `--text-primary` | `#f0f3f6` | High readability headers & body |
| **Text Secondary** | `--text-secondary`| `#8b949e` | Labels, captions, hints |
| **Accent Primary** | `--accent-primary`| `#2563eb` | Main action buttons (clean royal blue) |
| **Accent Hover** | `--accent-hover`| `#1d4ed8` | Interactive button hover |
| **Status Success**| `--status-success`| `#10b981` | Completed checks, clean states |
| **Status Amber** | `--status-amber` | `#f59e0b` | Pending sync, warnings |

## Typography
- **Font Family**: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", sans-serif`
- **Code & Monospace**: `ui-monospace, SFMono-Regular, "Cascadia Code", "Roboto Mono", Consolas, monospace`
- **Hierarchy**:
  - `Display / H1`: 28px / 1.25 weight 700 (Tracking -0.02em)
  - `H2 Section`: 20px / 1.3 weight 600 (Tracking -0.01em)
  - `H3 Subheading`: 15px / 1.4 weight 600
  - `Body / Standard`: 14px / 1.5 weight 400
  - `Labels / Badges`: 12px / 1.4 weight 500 (Uppercase tracking 0.05em)

## Component Styles
- **Buttons**:
  - Primary: Solid royal blue (`#2563eb`), white text, border radius 6px, padding 8px 16px, subtle box shadow `0 1px 2px rgba(0,0,0,0.2)`.
  - Secondary: Surface background (`#1b1e22`), subtle border (`#25292e`), text `#f0f3f6`, hover background `#25292e`.
- **Cards**:
  - Background: `#141618`, border 1px solid `#25292e`, radius 8px, padding 20px.
- **Tabs**:
  - Horizontal pill-bar, active tab with `#1b1e22` background and text `#f0f3f6`, inactive tabs with text `#8b949e`.
- **Status Badges**:
  - Height 22px, pill radius, border 1px solid, font size 11px, weight 500.

## Spacing Scale
- 4px (`--space-xs`), 8px (`--space-sm`), 16px (`--space-md`), 24px (`--space-lg`), 32px (`--space-xl`).

## API & Integrations
- Local HTTP endpoints:
  - `GET /api/status`: Health check and system readiness.
  - `POST /api/generate-docs`: Generates and persists the 9 core project docs.
  - `POST /api/git-action`: Executes Git init, commit, or branch creation.
  - `GET /manifest.webmanifest`: Progressive Web App discovery.
