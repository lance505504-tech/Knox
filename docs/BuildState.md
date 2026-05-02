# Knox — Build State
**Last updated:** 2026-05-02 (Session-020526va)
**Language:** "Committed to repo" = exists in repository. "Applied to database" = migration run. "Deployed" = live.

---

## Knox v3 — Operational (current live system)

| Component | State | Location |
|---|---|---|
| Knox credential HTML app | Committed to repo | `knox-credential.html` |
| Knox sign-in page | Committed to repo | `index.html` (GitHub Pages) |
| Session opener | Committed to repo | `CLAUDE_SESSION.md` |
| Dev log | Committed to repo | `logs/dev-log.md` |
| Project notes | Committed to repo | `active/notes.md` |
| News update tool | Committed to repo | `active/UPDATE-NEWS.md` |
| Backup protocol | Committed to repo | `BACKUP_PROTOCOL.md` |
| Auto-backup GitHub Action | Committed to repo | `.github/workflows/` |
| Repository app state | Committed to repo | `repository.json` |
| Session rules v1.2 | Committed to repo | `Claude-Session-Rules-Generic-v1.2.md` |

**Live URL:** https://lance505504-tech.github.io/Knox/ (GitHub Pages)

---

## Knox v4 — In Design / Pre-build

| Component | State | Notes |
|---|---|---|
| v4 design brief (19 sections) | Committed to lanceadams/library | `knox/knox-v4-design-brief.md` |
| Increment 1 build spec | Committed to repo | `docs/knox-v4-increment-1-build-spec.md` |
| knox-mcp repo | NOT CREATED | To be created at build session start |
| MCP server code | NOT BUILT | Increment 1 build session required |
| Render service | NOT DEPLOYED | Account exists, needs redirecting to knox-mcp repo |
| Supabase audit_log table | NOT APPLIED | Project meltlfmxsjfnizsxgavw.supabase.co exists, table not yet created |

---

## Infrastructure Registry

| Resource | Provider | Identifier | Purpose |
|---|---|---|---|
| Knox repo | GitHub (lance505504-tech) | lance505504-tech/Knox | Operational Knox v3 system |
| Knox library | GitHub (lanceadams) | lanceadams/library | Design docs, prior versions |
| Knox MCP repo | GitHub (lance505504-tech) | lance505504-tech/knox-mcp | Knox v4 MCP server (to be created) |
| Knox Supabase | Supabase | meltlfmxsjfnizsxgavw.supabase.co | Knox infrastructure DB (exists, empty) |
| Knox Render | Render | Lances Workspace | Knox v4 hosting (exists, not deployed) |
| Cape31 CMM Supabase | Supabase | vlcnqmkrardcismsdnxh | Cape31 CMM only — NOT Knox |

---

## Next Task

Open Knox v4 Increment 1 build session.
Briefing document: `docs/knox-v4-increment-1-build-spec.md`

Pre-build session checklist:
- [ ] Generate GITHUB_PAT_LANCE — contents:write on Knox repo
- [ ] Redirect Render to lance505504-tech/knox-mcp repo
- [ ] Verify Supabase meltlfmxsjfnizsxgavw.supabase.co is empty and ready

Definition of done: `knox_close_session` closes the build session. Knox dogfoods itself.
