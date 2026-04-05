# Knox — How It Works
## A Plain English Guide for All Users

---

## What is Knox?

Knox is your team's shared memory. It stores procedures, guides, decisions, development logs and working notes — and keeps everything in one place so any team member, or any AI, can pick up exactly where someone else left off.

Knox works through Claude (or ChatGPT). You start a session, the AI fetches the current state of everything live from GitHub, you do your work, and at the end the AI pushes everything back. No manual saving. No files to manage. No version confusion.

---

## Why It Works This Way

### Why GitHub?

GitHub is free, reliable, version-controlled and accessible from anywhere. Every change is recorded. Nothing is ever permanently lost — the last 30 versions of everything are always available to restore. GitHub also provides a clean URL for every file, which is how Claude fetches the content at session start.

### Why Claude?

Claude reads and writes text fluently, can work across multiple documents simultaneously, and handles the GitHub API directly. You describe what you want, Claude does it, and the result goes straight back to GitHub without you touching a file.

### Why a PAT?

A Personal Access Token is how Claude is authorised to write to GitHub on your behalf. It proves to GitHub that the request is coming from you. It is used once per push, never stored anywhere, and can be revoked from GitHub at any time if needed. Think of it like a one-time key — you hand it to Claude, Claude uses it, the session ends.

---

## The Two PATs

Knox uses two separate GitHub accounts, which means two separate PATs:

| PAT | Account | Used for |
|-----|---------|----------|
| **Knox PAT** | lance505504-tech | Knox dev log, notes, session files |
| **Cape31 PAT** | cape31one-sudo | Cape31 website repos (all regional sites) |

Keep both PATs somewhere secure — a password manager is ideal. You will paste them into Claude at the start of relevant sessions.

---

## Signing In

Before starting a session, sign in to confirm your identity.

**Sign-in page:** lance-knox.netlify.app

Use Face ID, Touch ID, or your access code. This is not just for access control — it creates a verified record of who started the session.

**First time?** You will have received an invitation token by email. Click **Redeem Invitation**, paste the token, and follow the prompts to set up your biometric access. After that, sign-in takes one tap.

---

## Starting a Session

Open a new Claude conversation. You do not need to upload any files. Type exactly this:

```
Start Knox session. Repo: https://github.com/lance505504-tech/Knox
```

Claude will immediately fetch four files live from GitHub:

1. `repository.json` — system configuration
2. `logs/dev-log.md` — the full history of what has been worked on
3. `active/notes.md` — current open tasks and active decisions
4. `backups/manifest.json` — available restore points

Claude will then confirm:
- What was loaded
- The date of the last dev log entry
- Any open To Do items from notes

**Then Claude will ask for your Knox PAT.** Paste it. Claude holds it in context for the session so it can push updates at any point — including if the session is interrupted.

After that, Claude will ask what you want to work on.

---

## During a Session

Work normally. Describe what you need, Claude does it.

At any point you can say:
- *"Push what we have so far"* — Claude pushes immediately, confirms with a commit SHA
- *"Show me the dev log"* — Claude displays the current log
- *"What are the open tasks?"* — Claude reads from notes.md
- *"Restore the version from two weeks ago"* — Claude lists backups and restores after confirmation

**If the session is interrupted** — connection drops, browser closes, you need to stop suddenly — Claude already has your PAT. When you return and mention the interruption, Claude can push everything accumulated so far before closing out.

---

## Ending a Session

At the end of every session Claude will automatically:

**1. Write a dev log entry** covering what was worked on, what was completed, any decisions made, what is awaiting action, and what happens next.

**2. Update notes.md** with any new open tasks or decisions.

**3. Push both files directly to GitHub** using your PAT. Claude will confirm each push with a commit SHA — a unique fingerprint proving the write succeeded.

You do not need to copy anything, download anything, or run any script. When Claude says the SHAs, the work is saved.

---

## Checking It Worked

After every session end you can verify Knox updated correctly by fetching the live dev log:

```
https://raw.githubusercontent.com/lance505504-tech/Knox/main/logs/dev-log.md
```

You should see today's entry at the bottom. If you do not see it, tell Claude and it will push again.

---

## What Goes in Knox

| ✅ Fine to store in Knox | ❌ Never store in Knox |
|--------------------------|------------------------|
| Procedures and policies | Names combined with any personal detail |
| Project records and logs | Medical or care records |
| Technical work and code | HR or payroll information |
| Guides and reference documents | Passwords or API tokens |
| Aggregated data and statistics | DBS or screening records |
| Meeting notes and decisions | Any credential granting system access |

**The one-question test:** Does this file identify a real living person? If yes — private repository. If no — Knox is fine.

---

## Restoring a Previous Version

Knox keeps the last 30 versions of everything.

To restore, say: *"Show me available backups"*

Claude will list versions newest first with dates. Confirm which you want. Claude restores it — the current version is saved first, so nothing is lost.

---

## Quick Reference

| What | Where |
|------|-------|
| Sign-in | lance-knox.netlify.app |
| Knox repo | github.com/lance505504-tech/Knox |
| Cape31 repo | github.com/cape31one-sudo |
| Start a session | Type: Start Knox session. Repo: [URL] |
| Knox PAT | Your password manager — lance505504-tech account |
| Cape31 PAT | Your password manager — cape31one-sudo account |
| Verify last push | Fetch raw dev-log.md from GitHub |
| Need help | Contact your team lead |

---

## Why This Is Better Than the Old System

The previous system generated a Python script (knox-update.py) at session end that you had to download and run manually. If you forgot, lost the file, or it failed silently, Knox stayed out of date with no indication anything had gone wrong.

The new system:
- Claude pushes directly — no script, no manual step
- Every push is confirmed with a commit SHA you can verify
- PAT is held in session from the start, so interruptions do not lose work
- Session start fetches live from GitHub — Claude always sees the current state, never a stale upload

---

*Knox — Est. 2001 — This guide applies to all Knox repositories*
