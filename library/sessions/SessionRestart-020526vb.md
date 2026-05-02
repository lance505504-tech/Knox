# SessionRestart-020526vb — Knox v4 Increment 1 Build Session
**For session opening:** Read this brief, read BuildState.md, read the build spec at docs/knox-v4-increment-1-build-spec.md. Then confirm state and ask for the PAT.
**Prior session:** Session-020526va (design session — full dialogue in library/sessions/)
**Session rules:** Claude-Session-Rules-Generic-v1.2.md

---

## Current state

Knox v3 is live and operational. Knox v4 is designed but not yet built.

The design session (020526va) produced one output: `docs/knox-v4-increment-1-build-spec.md` — a self-contained build brief for the Knox v4 MCP server, increment 1 only.

This build session executes that spec.

---

## The single architectural decision that governs everything

**Knox v4 is an MCP server.** Claude connects to Knox at session start via `claude mcp add --transport http knox https://{render-url}/mcp`. Knox tools (`knox_push_output`, `knox_close_session`) become native Claude tools in every session. Claude never holds raw credentials — it calls Knox, Knox decides, Knox logs.

This decision was reached by answering the brief's Q2 and Q3 first: MCP is mature (Streamable HTTP, OAuth 2.1, 18,000+ servers as of May 2026), and it is exactly the right integration layer for Knox. Full reasoning in Session-020526va.

---

## What this session builds

Two tools. Nothing else.

**`knox_push_output`** — pushes a file to GitHub via Contents API, writes audit log row, returns commit SHA.

**`knox_close_session`** — appends dev-log entry, replaces notes.md, pushes both, writes two audit rows, returns both SHAs.

Full spec: `docs/knox-v4-increment-1-build-spec.md`

---

## Infrastructure — confirmed at design session

| Resource | Status | Detail |
|---|---|---|
| Supabase | Exists, likely empty | meltlfmxsjfnizsxgavw.supabase.co — verify at session start |
| Render | Exists, nothing deployed | Lances Workspace — redirect to knox-mcp repo |
| knox-mcp repo | To be created | lance505504-tech/knox-mcp |
| GITHUB_PAT_LANCE | To be generated | contents:write on Knox repo — ask operator at session start |

---

## Session opening sequence

1. Read this brief
2. Read `docs/BuildState.md`
3. Read `docs/knox-v4-increment-1-build-spec.md`
4. Confirm state in 2-3 sentences
5. Ask: "Ready to build — please paste GITHUB_PAT_LANCE and confirm Render and Supabase are ready."
6. Wait for go

Do not begin building until operator confirms all three infrastructure items are ready.

---

## Decisions carried forward

- Knox v4 = MCP server (not a session file, not a credential HTML app)
- Increment 1 scope: lance505504-tech account only. Cape31 and lanceadams accounts in increment 2.
- Supabase project for Knox is meltlfmxsjfnizsxgavw.supabase.co — NOT vlcnqmkrardcismsdnxh (that is Cape31 CMM)
- Node.js, Streamable HTTP transport, `@modelcontextprotocol/sdk`
- Render free tier acceptable for increment 1
- Audit log workstream field: Knox, Cape31, Nouvita, BroadOak, IbizaMediaRoom
- Knox v4 serves a larger horizon not yet detailed in this context. Build the foundation right — the membrane, the evolutionary model, the audit trail — because something beyond the four current workstreams will run on it. Details to be introduced by Lance when the time is right. Do not reach for them.

---

## Definition of done

The build session is not done until `knox_close_session` has been called to close it. Knox must dogfood itself on the first session after being built.

Full checklist in build spec: `docs/knox-v4-increment-1-build-spec.md`

---

## Open tasks not in scope for this session (carry to increment 2)

- Credential vault (section 2-5 of v4 design brief)
- Session tokens and scope declaration
- Multi-account GitHub support (Cape31 PAT, lanceadams PAT)
- `knox_get_briefing()` tool
- OAuth-authenticated MCP endpoint
- Monitor session / dual-agent model

### Cape31 (separate thread — needs Cape31 PAT)
- Push UK v2, International v3, SA v1, AUS v1 to live repos
- AUS content confirmation from @pacesailing
- CMM integration (content.json, content-loader.js) into UK and International repos

---

*This brief was written by Claude (Sonnet 4.6) at close of Session-020526va. Full session reasoning in library/sessions/Session-020526va.md.*
