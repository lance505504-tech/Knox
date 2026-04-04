# Knox — Lances-Team

Secure Knowledge Repository · Est. 2001

## Quick Start

| Task | How |
|---|---|
| Sign in | Open the app URL below and use Face ID / Touch ID or your access code |
| Start a Claude session | Upload `CLAUDE_SESSION.md` and say "load session" |
| Save changes | Export from the app → commit as `repository.json` |
| Roll back | Browse `backups/`, download, import into app |

## App URL

```
https://lance505504-tech.github.io/Knox/
```

## Folder Structure

```
repository.json          ← live app state
CLAUDE_SESSION.md        ← load this into Claude each session
BACKUP_PROTOCOL.md       ← how backups work
RATIONALE.md             ← why this system exists
index.html               ← Knox sign-in (GitHub Pages)
active/
  notes.md               ← live project notes
logs/
  dev-log.md             ← development history
backups/
  manifest.json          ← auto-updated version index
  repository/            ← 30 versions of repository.json
  notes/                 ← 30 versions of notes.md
  dev-log/               ← 30 versions of dev-log.md
  active/                ← 30 versions of other active files
.github/workflows/
  per-file-backups.yml   ← auto-backup on every push
```
