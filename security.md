# 03 Security & Access Document

## Authentication Method
OmniPilot OS V1 runs as a local-first application bound to `127.0.0.1`. No remote external ports are opened. Authentication for GitHub syncing utilizes the user's existing local `git` credential helper (`credential.helper=manager` on Windows) or a temporary Personal Access Token (PAT) stored only in memory during the active session.

## User Roles & Permissions Matrix
| Role | View Docs | Edit Docs | Run 1-Click Autonomy | Execute Git Commits | Configure Remote |
|------|-----------|-----------|----------------------|---------------------|------------------|
| **Pilot (Local Owner)** | Allowed | Allowed | Allowed | Allowed | Allowed |
| **Viewer (Read-Only)** | Allowed | Denied | Denied | Denied | Denied |
| **External Web Crawler**| Allowed (SEO metadata, manifest) | Denied | Denied | Denied | Denied |

## Row-Level Security & Data Isolation
- Local workspace isolation: All file operations are strictly jailed within the project directory. Path traversal attempts (`../`) are sanitized and rejected by `server.py`.
- No sensitive keys or tokens are ever written to git history or markdown files.

## Error Handling Guide
| Failure Scenario | System Response | Recovery Action |
|------------------|-----------------|-----------------|
| **Git Not Installed** | Returns 400 with diagnostic message. | UI displays warning with download link; enables manual export mode. |
| **File Permission Locked** | Returns 500 with locked file path. | Engine retries 3 times with exponential backoff before surfacing error. |
| **Port Conflict (8765 occupied)** | Finds next available port (`8766`, `8767`). | Auto-redirects browser to allocated port. |
| **Invalid JSON Input** | Returns 422 Unprocessable Entity. | UI highlights malformed fields with schema explanation. |

## Edge Cases
- **Empty Project Name**: Defaults automatically to "OmniProject" with generated slug.
- **Disconnected Network**: All local operations (doc generation, local Git commits, export) function 100% offline.
- **Git User Name/Email Not Set**: Backend falls back to local git config `OmniPilot <pilot@local>` so commit never fails.
