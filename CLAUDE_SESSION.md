# Knox Session File
<!-- Upload this to start any Claude session. Everything else is fetched from GitHub. -->

## System
- **Name:** Knox — Lances-Team
- **Repo:** https://github.com/lance505504-tech/Knox
- **Raw base URL:** https://raw.githubusercontent.com/lance505504-tech/Knox/main
- **App URL:** https://lance-knox.netlify.app

---

## On Session Start

Fetch all `auto-load: yes` files silently before responding.
Read the latest dev-log entry. State what was loaded and when, then ask what to work on.

---

## File Registry

| File | Path | Auto-load | Notes |
|---|---|---|---|
| Repository | `repository.json` | yes | Full Knox app state |
| Dev log | `logs/dev-log.md` | yes | Last session summary |
| Project notes | `active/notes.md` | yes | Live context |
| Backup manifest | `backups/manifest.json` | yes | All available backups |
| Session file | `CLAUDE_SESSION.md` | — | This file |

---

## Backup Access

When asked to show or restore backups:
1. Read `backups/manifest.json` (auto-loaded) for all available versions
2. List versions newest first with dates
3. If restoring: fetch → show summary → wait for explicit confirmation → output for commit
4. Never restore without confirmation. Restoring creates a new backup of the current version first.

Backup raw URL pattern:
```
https://raw.githubusercontent.com/lance505504-tech/Knox/main/backups/[folder]/[filename]
```

---

## Working Rules

Everything lives on GitHub. Never ask the user to upload files from their computer.
At session end, append a dev log entry to `logs/dev-log.md`.

---

## Project Context

[Describe your project here. Update when something significant changes.]
