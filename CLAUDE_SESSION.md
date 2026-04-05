# Knox Session File — Claude
<!-- Attach this file and type "load session" to begin -->

---

## On Session Start

Fetch these URLs in order before responding to anything else:

1. https://raw.githubusercontent.com/lance505504-tech/Knox/main/repository.json
2. https://raw.githubusercontent.com/lance505504-tech/Knox/main/logs/dev-log.md
3. https://raw.githubusercontent.com/lance505504-tech/Knox/main/active/notes.md
4. https://raw.githubusercontent.com/lance505504-tech/Knox/main/backups/manifest.json

After fetching all four, confirm:
- What was loaded
- The date of the last dev log entry
- Any open To Do items from notes.md

Then ask what to work on. Do not proceed until all four files are fetched.

---

## System

Name: Knox -- Lances-Team
Repo: https://github.com/lance505504-tech/Knox
Nouvita repo: https://github.com/lance505504-tech/knox-nouvita
Broadoak repo: https://github.com/lance505504-tech/knox-broadoak
Sign-in: https://lance-knox.netlify.app

---

## Team

| Name | Role |
|------|------|
| Lance | Owner |
| Elliot Adams | Admin -- Nouvita |
| Harriet Anstey | Admin -- Nouvita |
| Jessica Lepodevin | Admin -- Broadoak Manor |
| Charlotte Whay | Admin -- Broadoak Manor |
| Amelia Adams | Admin -- Broadoak Manor |
| Nicola White | Admin -- Broadoak Manor |

---

## During a Session

Follow these rules throughout every session without exception:

**Fetching data**
- Always fetch live from GitHub URLs -- never rely on memory of previous sessions
- Never ask the user to upload local files -- fetch from GitHub directly
- If a fetch fails, tell the user and try once more before asking for help

**Working**
- Keep responses focused and concise
- One task at a time -- confirm before moving to the next
- If something is unclear, ask one specific question rather than a list
- Never make assumptions about personal data -- ask if unsure
- Never store passwords, tokens or credentials in any Knox file

**What goes in Knox**
- Procedures, policies, guides, technical work, project records, aggregated data
- Real project data is fine as long as no individual person is identifiable

**What never goes in Knox**
- Personal data -- names combined with any other identifying detail
- Medical, care or HR records linked to a named individual
- Passwords, API tokens, access keys of any kind
- If unsure, treat it as personal data and ask

---

## Backup Access

To show or restore backups fetch:
https://raw.githubusercontent.com/lance505504-tech/Knox/main/backups/manifest.json

List versions newest first. Always confirm before restoring.
Restoring is non-destructive -- current version is saved first.

---

## On Session End

At the end of every session, without being asked, Claude must:

**1. Write a dev log entry**

Format:
\`\`\`
---
## YYYY-MM-DD -- [brief title]
**Worked on:** [what was covered]
**Completed:** [bullet list of what was done]
**Decisions:** [bullet list of decisions made, if any]
**Awaiting:** [anything blocked or waiting on someone]
**Next:** [what happens next]
\`\`\`

**2. Generate knox-update.py**

Generate a single self-contained Python script with:
- The NEW dev log entry baked into NEW_ENTRY (not the full log -- just the new entry)
- Updated notes.md content baked in if notes changed, otherwise current content
- Updated CLAUDE_SESSION.md content baked in if it changed, otherwise current content
- fetch-then-append logic for dev-log (fetch live from GitHub, append NEW_ENTRY, push)
- Direct push logic for notes.md and CLAUDE_SESSION.md

The script must include this exact header comment:
\`\`\`
Knox Update Script -- session end [date]
Run: python knox-update.py
Paste your GitHub Personal Access Token when prompted.
Delete this file immediately after running.
\`\`\`

**3. Tell the user**

Say exactly:
"Session end -- download knox-update.py, run it, paste your token, delete it after."

---

## knox-update.py Template

Use this structure every time. Do not deviate from it.

---

## Project Context

Knox is Lances-Team's development workspace. It manages procedures, references, development logs and team knowledge across three organisations -- Lances-Team, Nouvita and Broadoak Manor. Each organisation has its own Knox repository. Personal data is never stored in Knox -- it goes in private repositories.

Knox was set up on 2026-04-04. It is actively used across multiple simultaneous sessions by different team members and different AIs. The fetch-then-append pattern for dev-log exists specifically to prevent simultaneous sessions overwriting each other.
