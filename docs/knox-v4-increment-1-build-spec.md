# Knox v4 — Increment 1 Build Spec
**Status:** Ready to build  
**Author:** Lance Adams / Claude (Sonnet 4.6)  
**Date:** 2026-05-02  
**Repo target:** lance505504-tech/knox-mcp (to be created)  
**Design brief:** lanceadams/library/knox/knox-v4-design-brief.md

---

## What this increment does

Builds the Knox MCP server — increment 1 only. Two tools. No credential vault yet. No session tokens yet. Those come in increment 2.

**This increment solves one problem:** Claude does good work in a session and the outputs don't make it back to the repo. After this increment, they do — via a native MCP tool call.

---

## Tools to build

### Tool 1: `knox_push_output`

Pushes a file to a GitHub repo via the GitHub Contents API.

**Input parameters:**
```
file_path      string   Path in the repo (e.g. "logs/dev-log.md")
content        string   Full file content (plain text)
repo           string   Repo name (e.g. "Knox") — owner is always lance505504-tech for increment 1
commit_message string   Commit message
workstream     string   One of: Knox, Cape31, Nouvita, BroadOak, IbizaMediaRoom
summary        string   Human-readable description of what was pushed and why
```

**Behaviour:**
1. Fetch current file SHA from GitHub Contents API (required for update — if file doesn't exist, SHA is omitted and file is created)
2. Base64-encode the content
3. PUT to `https://api.github.com/repos/lance505504-tech/{repo}/contents/{file_path}`
4. On success: write audit log row, return commit SHA
5. On failure: write audit log row with error, return error message

**Auth:** GitHub PAT stored as environment variable `GITHUB_PAT_LANCE` on the Render server. Never exposed to Claude.

---

### Tool 2: `knox_close_session`

Writes the session close-out to Knox repo — dev log entry and updated notes.md.

**Input parameters:**
```
session_date   string   YYYY-MM-DD
workstream     string   One of: Knox, Cape31, Nouvita, BroadOak, IbizaMediaRoom
title          string   Brief session title (e.g. "Cape31 UK site hero fix")
worked_on      string   What was covered
completed      string   Bullet list of completed items (plain text, one item per line)
decisions      string   Bullet list of decisions made (plain text, one item per line)
awaiting       string   Anything blocked or waiting
next           string   What happens next session
notes_update   string   Full replacement content for notes.md (plain text markdown)
```

**Behaviour:**
1. Fetch current SHA for `logs/dev-log.md`
2. Append new entry (formatted per Knox dev log standard — see format below) to existing content
3. Push updated dev-log.md via `knox_push_output` logic
4. Fetch current SHA for `active/notes.md`
5. Replace notes.md with `notes_update` content
6. Push updated notes.md via `knox_push_output` logic
7. Write two audit log rows (one per push)
8. Return: "Knox updated — dev-log SHA: {sha} — notes SHA: {sha}"

**Dev log entry format:**
```
---
## YYYY-MM-DD — [title]
**Worked on:** [worked_on]
**Completed:**
- [completed items]
**Decisions:**
- [decisions]
**Awaiting:** [awaiting]
**Next:** [next]
```

---

## Infrastructure to build

### 1. Supabase — new project

Create a new Supabase project for Knox infrastructure (separate from the Cape31 CMM project at vlcnqmkrardcismsdnxh).

**Suggested project name:** knox-infrastructure

**Table to create: `audit_log`**

```sql
create table audit_log (
  id uuid default gen_random_uuid() primary key,
  timestamp timestamptz default now(),
  session_date date not null,
  workstream text not null,
  tool_called text not null,
  repo text,
  file_path text,
  commit_sha text,
  summary text,
  outcome text not null
);
```

No RLS required for increment 1 — server-side only access via service role key.

---

### 2. GitHub repo — lance505504-tech/knox-mcp

Create new repo: `knox-mcp` under `lance505504-tech`.

**Suggested repo structure:**
```
knox-mcp/
  src/
    index.js          ← MCP server entry point
    tools/
      push_output.js  ← knox_push_output tool
      close_session.js← knox_close_session tool
    lib/
      github.js       ← GitHub Contents API calls
      supabase.js     ← audit log writes
  package.json
  .env.example        ← documents required env vars, no values
  README.md
```

**Language:** Node.js (JavaScript). Keeps it consistent with existing Knox HTML/JS tooling.

**MCP transport:** Streamable HTTP (not stdio). Knox is a remote server — it must be accessible from any Claude session, not just local.

**MCP SDK:** `@modelcontextprotocol/sdk` — official Anthropic SDK.

---

### 3. Environment variables (Render)

```
GITHUB_PAT_LANCE        GitHub PAT for lance505504-tech — needs: contents:write scope on Knox repo
SUPABASE_URL            meltlfmxsjfnizsxgavw.supabase.co
SUPABASE_SERVICE_KEY    Knox infrastructure service role key (not anon key)
PORT                    Set by Render automatically
```

These are set in Render dashboard — never committed to the repo.

---

### 4. Render deployment

- **Service type:** Web Service
- **Runtime:** Node.js
- **Start command:** `node src/index.js`
- **Plan:** Free tier is acceptable for increment 1 (note: free tier sleeps after inactivity — acceptable limitation, address in increment 2 if needed)
- **Auto-deploy:** on push to main branch of knox-mcp repo

---

## How Claude connects to Knox MCP

Once deployed, a Claude session connects via:

```
claude mcp add --transport http knox https://{render-url}/mcp
```

Or in Claude Desktop config:
```json
{
  "mcpServers": {
    "knox": {
      "type": "http",
      "url": "https://{render-url}/mcp"
    }
  }
}
```

After connection, Claude has `knox_push_output` and `knox_close_session` available as native tools in every session.

---

## What increment 1 does NOT include

- Credential vault (increment 2)
- Session tokens / scope declaration (increment 2)
- Multi-account GitHub support — Cape31 PAT, lanceadams PAT (increment 2)
- Session briefing tool — `knox_get_briefing()` (increment 2)
- OAuth / authenticated MCP endpoint (increment 2)
- Monitor session / dual-agent model (increment 3+)

---

## Build session rules (carry into the build session)

- Demented terrier rule: don't act before being told to go
- Pre-build declarations: state what you're about to do before doing it
- Show before pushing: present output for review before any GitHub push
- Fetch-back verification: confirm pushes by fetching back
- Commit before close: always leave Knox in a committed state

---

## Definition of done for increment 1

- [ ] `knox-mcp` repo created at lance505504-tech/knox-mcp
- [ ] MCP server runs locally and passes basic tool call test
- [ ] Deployed to Render — URL confirmed live
- [ ] `audit_log` table created in Knox Supabase project
- [ ] Environment variables set in Render dashboard
- [ ] `knox_push_output` tested: pushes a test file to Knox repo, SHA returned, audit row written
- [ ] `knox_close_session` tested: dev-log and notes.md updated in Knox repo, both SHAs returned
- [ ] Claude Desktop or Claude Code connected to Knox MCP endpoint
- [ ] This build spec committed to knox-mcp repo as `docs/increment-1-build-spec.md`
- [ ] Knox dev-log updated with session close-out via `knox_close_session` (dogfooding)

---

## Credentials needed at build session start

The build session operator will need:
- `GITHUB_PAT_LANCE` — PAT for lance505504-tech with `contents:write` scope on Knox repo
- Render account login (or deploy hook)
- Knox Supabase project credentials (created during this build session)
- lanceadams PAT — to read the design brief from lanceadams/library if needed

---

*This spec is self-contained. A fresh Claude session with this document needs no other context to execute the build.*
