# Knox Backup Protocol

## What Is Backed Up

Each of these files gets its own independent version history:

| File | Backup folder | Versions kept |
|---|---|---|
| `repository.json` | `backups/repository/` | 30 |
| `logs/dev-log.md` | `backups/dev-log/` | 30 |
| `active/notes.md` | `backups/notes/` | 30 |
| Any `active/*` file | `backups/active/` | 30 per file |

Every push to `main` that changes a tracked file automatically creates a
timestamped backup of that file only. No manual action required.

A `backups/manifest.json` is updated automatically, listing every available
version in every folder with newest-first ordering.

---

## How Backups Are Named

```
YYYY-MM-DD-HHMMSS.ext
```

Example: `2025-01-15-143022.json` is a backup of `repository.json`
created at 14:30:22 UTC on 15 January 2025.

Active-folder files use: `YYYY-MM-DD-HHMMSS-filename.ext`

---

## Protection Rules

### You cannot accidentally destroy a backup by:
- Editing `repository.json` — this creates a new backup, not overwrites one
- Deleting `repository.json` — backups folder is independent
- Running the backup workflow — it only ADDS files, then prunes oldest

### Backups ARE automatically removed when:
- A folder exceeds 30 versions — the oldest file is deleted
- This is intentional and predictable: the newest 30 are always safe

### To prevent accidental deletion of backups manually:
Enable branch protection in GitHub:
  - Settings → Branches → Add rule → `main`
  - Enable: "Require pull request before merging"
  - This means no one can push directly to main — changes need a PR review
  - Even repo owners cannot accidentally delete backup files with a direct push

---

## How to View Available Backups

**In the Knox app:** Open the project → click "Versions"

**On GitHub:** Browse to `backups/` folder — files are listed newest first.

**Via Claude session:**
> "Show me available backups for repository.json"

Claude will fetch `backups/manifest.json` and list all available versions.

---

## How to Restore a Backup

Restoring is a deliberate, two-step process that cannot happen accidentally.

### Step 1 — Identify the version

Open `backups/manifest.json` or browse the relevant backup folder.
Note the filename of the version you want.

Raw URL format:
```
https://raw.githubusercontent.com/[USERNAME]/[REPO]/main/backups/[FOLDER]/[FILENAME]
```

### Step 2 — Restore via Claude session

Tell Claude:
> "Restore repository.json from backups/repository/2025-01-14-092100.json"

Claude will:
1. Fetch the backup file from GitHub
2. Show you a summary of what it contains
3. Ask you to confirm before proceeding
4. Output the file content for you to commit as `repository.json`
5. Your commit automatically creates a new backup of the restored version

**The old current version is NOT lost** — it remains in backup history.
Restoring is non-destructive: it adds a new version, not removes anything.

---

## How to Save a New Version

The backup workflow runs automatically on every push.
You do not need to do anything except commit your changes to `main`.

For manual sessions with Claude:
1. Export from the Knox app → rename the file if needed
2. Commit to `main` as `repository.json`
3. The GitHub Action fires within seconds and saves a backup

---

## Emergency Recovery

If `repository.json` is missing or corrupted:

1. Go to GitHub → `backups/repository/`
2. Find the most recent file (top of list)
3. Click it → click "Raw" → copy the URL
4. Tell Claude: "Restore from this URL: [URL]"
5. Claude outputs the restored content
6. Commit it as `repository.json`

If the backup folder itself is somehow corrupted:
- GitHub keeps full commit history — every file that was ever committed is
  recoverable via `git log` and `git show`
- Contact your GitHub admin or repository owner

---

## Backup Manifest

`backups/manifest.json` is auto-generated and looks like this:

```json
{
  "generated": "2025-01-15T14:30:22Z",
  "folders": {
    "repository": {
      "count": 12,
      "newest": "2025-01-15-143022.json",
      "oldest": "2025-01-03-091500.json",
      "versions": ["2025-01-15-143022.json", "..."]
    }
  }
}
```

Claude reads this manifest at session start to know what backup history is available.

