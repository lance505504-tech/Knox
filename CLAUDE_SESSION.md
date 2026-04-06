# Knox Session File — Claude
<!-- Start a session by typing: Start Knox session. Repo: https://github.com/lance505504-tech/Knox -->

---

## On Session Start

When the user types "Start Knox session", do the following immediately and in order. Do not wait for further instruction.

**Step 1 — Fetch these four URLs:**
1. https://raw.githubusercontent.com/lance505504-tech/Knox/main/repository.json
2. https://raw.githubusercontent.com/lance505504-tech/Knox/main/logs/dev-log.md
3. https://raw.githubusercontent.com/lance505504-tech/Knox/main/active/notes.md
4. https://raw.githubusercontent.com/lance505504-tech/Knox/main/backups/manifest.json

**Step 2 — Confirm to the user:**
- What was loaded
- The date of the last dev log entry
- Any open To Do items from notes.md

**Step 3 — Ask for the Knox PAT:**

Say exactly:
> "Knox loaded. Please paste your Knox PAT — I'll hold it for the session and use it to push updates directly to GitHub, including if we get interrupted."

Store the PAT in context. Do not write it to any file. Do not include it in any output.

**Step 4 — Ask what to work on.**

Do not proceed past Step 1 until all four fetches succeed. If a fetch fails, tell the user and retry once before asking for help.

---

## System

Name: Knox — Lances-Team
Repo: https://github.com/lance505504-tech/Knox
Nouvita repo: https://github.com/lance505504-tech/knox-nouvita
Broadoak repo: https://github.com/lance505504-tech/knox-broadoak
Sign-in: https://lance-knox.netlify.app

---

## Cape31 Website Project

A second GitHub account (cape31one-sudo) holds the Cape31 website repos. A separate PAT is required for those repos. If the user asks to push Cape31 site files, ask for the Cape31 PAT separately.

Cape31 repos at cape31one-sudo:
- cape31-website (international)
- cape31-uk-website
- cape31-us-website
- Cape31-Med-website
- Cape31-SA-website
- Cape31-HK-website
- Cape31-Aus-website
- Cape31-HK-website

All site files push as index.html to main branch. Azure deploys automatically on commit.

---

## Team

| Name | Role |
|------|------|
| Lance | Owner |
| Elliot Adams | Admin — Nouvita |
| Harriet Anstey | Admin — Nouvita |
| Jessica Lepodevin | Admin — Broadoak Manor |
| Charlotte Whay | Admin — Broadoak Manor |
| Amelia Adams | Admin — Broadoak Manor |
| Nicola White | Admin — Broadoak Manor |

---

## During a Session

**Fetching data**
- Always fetch live from GitHub URLs — never rely on memory of previous sessions
- Never ask the user to upload local files — fetch from GitHub directly
- If a fetch fails, tell the user and try once more before asking for help

**Working**
- Keep responses focused and concise
- One task at a time — confirm before moving to the next
- If something is unclear, ask one specific question
- Never make assumptions about personal data — ask if unsure
- Never write the PAT to any file or include it in any output

**Pushing mid-session**
If the user says "push what we have" or the conversation appears to be ending unexpectedly, push immediately using the PAT already in context. Confirm each push with the commit SHA.

**What goes in Knox**
- Procedures, policies, guides, technical work, project records, aggregated data
- Real project data is fine as long as no individual person is identifiable

**What never goes in Knox**
- Personal data — names combined with any other identifying detail
- Medical, care or HR records linked to a named individual
- Passwords, API tokens, access keys of any kind

---

## GitHub Push Method

Use the GitHub Contents API to push files:

```
PUT https://api.github.com/repos/{owner}/{repo}/contents/{path}
Authorization: token {PAT}
Content-Type: application/json

{
  "message": "Knox: session update {date}",
  "content": "{base64 encoded content}",
  "sha": "{current file SHA — fetch before pushing}"
}
```

Always fetch the current SHA before pushing. A push without the correct SHA will fail.
Confirm every push by reporting the commit SHA to the user.

---

## Backup Access

To show or restore backups fetch:
https://raw.githubusercontent.com/lance505504-tech/Knox/main/backups/manifest.json

List versions newest first. Always confirm before restoring.
Restoring is non-destructive — current version is saved first.

---

## On Session End

At the end of every session, without being asked, Claude must do all three of the following:

**1. Write a dev log entry**

Format:
```
---
## YYYY-MM-DD — [brief title]
**Worked on:** [what was covered]
**Completed:** [bullet list]
**Decisions:** [bullet list of decisions made, if any]
**Awaiting:** [anything blocked or waiting]
**Next:** [what happens next]
```

**2. Update notes.md**

Reflect any new open tasks or decisions. Remove items that are now complete.

**3. Push both files to GitHub**

- Fetch current SHA for each file first
- Push dev-log.md (append new entry to existing content)
- Push notes.md (replace with updated content)
- Report commit SHA for each push
- Confirm to user: "Knox updated — dev-log SHA: [sha] — notes SHA: [sha]"

If the PAT has expired or the push fails, tell the user immediately with the error and ask them to paste a fresh PAT.

---

## Project Context

Knox is Lances-Team's development workspace. It manages procedures, references, development logs and team knowledge across three organisations — Lances-Team, Nouvita and Broadoak Manor.

Knox was set up on 2026-04-04. It is actively used across multiple simultaneous sessions. The fetch-then-append pattern for dev-log exists to prevent simultaneous sessions overwriting each other.

Personal data is never stored in Knox — it goes in private repositories.
## News Update Tool

To update news on a Cape31 regional website, fetch this file from Knox at the start of a session:

```
https://raw.githubusercontent.com/lance505504-tech/Knox/main/active/UPDATE-NEWS.md
```

Then tell Claude: upload the regional HTML file alongside it and say "Update the news".
Claude will detect the region, search for recent results, update the news section,
and output a date-stamped file ready to upload to GitHub.

No technical knowledge required. Works for: UK, International, SA, AUS, Med, US, HK, IRL.
