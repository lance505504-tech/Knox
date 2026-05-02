# Session-020526va — Knox v4 Design Session
**Date:** 2026-05-02
**Session tag:** 020526va
**Operator:** Lance Adams
**Claude instance:** Sonnet 4.6
**Status:** Complete — committed to repo

---

## Highlights

The session that designed Knox v4's architecture. The central conclusion: Knox v4 is an MCP server, not a session file. This single decision resolves the majority of the open questions in the v4 design brief.

**The live example that opened the session:** Lance noted that Claude instances routinely do good work and fail to push outputs back to the repo. This is not a discipline problem — it is an architecture problem. The current Knox model relies on Claude choosing to push. The MCP model makes pushing a tool call with a logged outcome. Either it ran or it didn't. The membrane holds or it doesn't.

**The key insight:** "The plug is the key." MCP is not just a convenient integration layer — it is the mechanism by which Knox v4 becomes a genuine persistence membrane rather than a well-intentioned session file. Claude doesn't hold credentials and hope to use them. Claude calls Knox, Knox decides, Knox logs.

**MCP status as of May 2026:** Mature, cloud-native, enterprise-grade. Streamable HTTP transport, OAuth 2.1, 18,000+ community servers. Not experimental. Ready to build on.

**Increment 1 defined:** Two tools only — `knox_push_output` and `knox_close_session`. Solves the specific problem observed at session open. Everything else (credential vault, session tokens, multi-agent) is increment 2+.

**Infrastructure confirmed:** Supabase project `meltlfmxsjfnizsxgavw.supabase.co` already exists for Knox. Render account exists. New repo `lance505504-tech/knox-mcp` to be created at build session start.

**Session rules:** v1.2 uploaded by Lance including Rules 50-53 (established 020526 following a scope creep incident). Pushed to Knox repo.

**Session close-out:** dev-log, notes, build spec, session rules all pushed and SHA-verified. This dialogue and SessionRestart brief are the final artefacts.

---

## Full Dialogue

### Opening — the problem stated

Lance opened with a project seed document for Knox v4, describing it as "the persistence membrane between human intent and AI session state." The seed document established:

- Operator: Lance Adams, CEO, running Broad Oak Manor, Nouvita Healthcare, IbizaMediaRoom, Cape31
- GitHub accounts: lanceadams, cape31one-sudo, lance505504-tech
- Knox repo: lance505504-tech/Knox
- Knox v4 goal: unified membrane system — not yet built
- Session rules: demented terrier rule, pre-build declarations, show before pushing, fetch-back verification, commit before close

Lance provided the PAT for lance505504-tech. Claude cloned the Knox repo.

**Observation Lance made immediately:** "Another example of Claude not putting stuff in the repo — one of the reasons we need to design this." This was said in response to the general pattern of Claude doing good work that doesn't make it back to the repo. Noted as the live example of the exact problem Knox v4 is designed to solve.

---

### Knox repo review

Claude read the full Knox repo at lance505504-tech/Knox. Findings:

**What exists (Knox v3 operational):**
- `CLAUDE_SESSION.md` — working session opener, fetches 4 URLs on "Start Knox session", loads context, holds PAT
- `repository.json` — live app state for the Knox credential/knowledge HTML app
- `logs/dev-log.md` — active and well-maintained, last entry 2026-04-06
- `active/notes.md` — current, open tasks logged, Cape31 baselines recorded
- `BACKUP_PROTOCOL.md` — 30-version rolling backup via GitHub Actions
- `knox-credential.html` — full credential vault UI with biometric auth/WebAuthn
- `index.html` — sign-in page (GitHub Pages)
- `active/UPDATE-NEWS.md` — news update tool for Cape31 regional sites

**Last session state (2026-04-06):**
- Cape31 CMM system built and fully configured
- Four regional sites ready to push (UK v2, International v3, SA v1, AUS v1) — awaiting Cape31 PAT
- UPDATE-NEWS.md instruction file pushed to Knox

**What Knox v3 does NOT have:**
- No membrane architecture
- No workstream separation
- No multi-agent coordination
- No 19-section v4 design brief (not in lance505504-tech/Knox)

**Critical finding:** The 19-section v4 design brief was not in the Knox repo. Lance said it might be in the lanceadams/library repo.

---

### Finding the v4 design brief

Lance provided the PAT for lanceadams account. Claude listed `lanceadams/library/knox/` and found:

- `Knox-Bootstrap-Protocol.md`
- `knox-v2-generic.html`, `knox-v2.html`, `knox-v3.html`
- `knox-full-export.json`
- `knox-v4-design-brief.md` ← the brief

Claude fetched and read all 19 sections (36,859 bytes, dated 26 April 2026).

---

### The 19-section v4 design brief — key content

**Section 1 — The three gaps Knox v4 solves:**
1. Credential handover is manual and session-scoped — PATs pasted into chat every session
2. Knox cannot verify the AI is who it says it is — no session authentication
3. No audit trail — credentials stored, usage never recorded

**Section 2 — The v4 vision:**
Claude operates through Knox without ever holding any keys itself. Knox is the gatekeeper. Claude is the operator. Keys never leave Knox. Session flow: user pastes Knox briefing + session token → Claude calls Knox API for credentials → Knox verifies token, checks scope, returns time-limited credential → Claude uses it → Knox logs the action → credential expires.

**Section 3 — Architecture options:**
- Option A: Supabase backend (recommended)
- Option B: Self-hosted on Render
- Option C: Local Knox server
- Option D: Hybrid
Brief recommended Option A with Option D as fallback.

**Section 4 — Security model:**
Deliberately right-sized. Knox holds developer service credentials — already sitting in .env files and chat transcripts today. Knox v4 is an improvement on that baseline, not a new risk. Security posture: PIN + HTTPS + scoped session tokens + audit log. No over-engineering.

**Section 5 — Session flow:** Step-by-step defined — token request, scope check, credential release, expiry, logging.

**Section 7 — Viability assessment:** Verdict: "Viable but not now." 4-6 sessions to prototype. Brief said not to build until open questions answered.

**Section 8 — Open questions 1-7:** Including Q2 (how does AI call Knox mid-session?) and Q3 (is MCP the right integration layer?) — flagged as the most important questions to answer first.

**Section 9 — Recommended next steps:** "Answer question 3 first — research MCP server architecture. If Knox v4 can be built as an MCP server, the integration story becomes dramatically simpler."

**Sections 10-13:** Local use definition, dual-session model (work session + monitor session as separate Claude instances), ToS analysis (session monitoring = personal use of own content, clearly within terms), two new open questions on dual-session coordination.

**Section 14 — Direction of travel:** Assisted → supervised agentic → true agentic. Knox v4 as the boundary enforcement layer that makes agentic AI safe. "Without something like Knox, agentic AI across multiple services is too risky to run unsupervised. With Knox, you can let it run within declared boundaries."

**Sections 15-19:** Credential entry UX (guided service templates, paste validation), living system model (findings/rules, GitHub Discussions API), session restart file, full rule set as default, revised open questions 10-13.

**Claude's read on the brief:** The "viable but not now" verdict was written before this session. Two things have changed: (1) we're now in a Claude Project which partially addresses the session restart file problem, and (2) MCP has matured significantly since April. The verdict should be re-evaluated — and the session did re-evaluate it.

---

### The MCP research

Lance confirmed: "Yes, the plug is the key — no pun intended." Claude researched MCP protocol status as of May 2026.

**Key findings:**

**MCP is mature and cloud-native (as of Q1 2026):**
- Transport: Streamable HTTP replaced HTTP+SSE — single-endpoint, stateless-capable, works behind load balancers
- Auth: OAuth 2.1 with PKCE, dynamic client registration, mandatory Resource Indicators
- Scale: 18,000+ community servers, 97M+ monthly SDK downloads, 50+ enterprise partners
- Governance: Donated to Linux Foundation (Agentic AI Foundation) December 2025

**How Claude connects to Knox mid-session (answering Q2):**
Each MCP server declares tools with inputs and outputs. Claude discovers them at session start and calls them natively during conversation — exactly like built-in tools. Protocol handles serialisation, error handling, lifecycle. No glue code, no prompt engineering.

**Remote Knox MCP server (answering Q3):**
One command to connect: `claude mcp add --transport http knox https://{render-url}/mcp`
After that, `knox_push_output()` and `knox_close_session()` are native Claude tools in every session.

**The audit log is a natural byproduct:** Every MCP tool call is logged. Knox doesn't need to remember to log — the protocol requires it.

**Remaining gap:** Most MCP hosts don't yet support Streamable HTTP + OAuth natively. The `mcp-remote` npm package bridges this — one-line workaround, not a blocker.

**Conclusion mapped to brief:** Q2 and Q3 both answered. MCP is the integration layer. The "viable but not now" verdict is overturned by the maturity of the protocol.

---

### Architecture decision

**Knox v4 = MCP server.**

The architecture:

```
Knox MCP Server (Node.js on Render)
  ├── Credential store (Supabase, encrypted)
  ├── Session token issuer (scoped JWT)
  ├── Audit log (Supabase table, append-only)
  └── Tools exposed to Claude:
        knox_get_briefing()
        knox_request_credential(scope, task)
        knox_push_output(file, content, repo)
        knox_log_action(description, outcome)
        knox_close_session()

Claude (MCP client)
  └── Connects once at session start
  └── Calls Knox tools natively mid-session
  └── Never holds raw credentials
```

---

### Increment 1 definition

**Why increment 1 is two tools only:**
The temptation is to build the whole membrane. Wrong move. The first increment solves one thing: outputs not making it back to the repo. Everything else is increment 2+.

**Tool 1: `knox_push_output`**
Parameters: `file_path`, `content`, `repo`, `commit_message`, `workstream`, `summary`
Behaviour: fetch SHA → base64-encode content → PUT to GitHub Contents API → write audit log row → return commit SHA
Auth: GitHub PAT stored as environment variable on Render server. Never exposed to Claude.

**Tool 2: `knox_close_session`**
Parameters: `session_date`, `workstream`, `title`, `worked_on`, `completed`, `decisions`, `awaiting`, `next`, `notes_update`
Behaviour: fetch dev-log SHA → append new entry → push → fetch notes SHA → replace notes → push → write two audit rows → return both SHAs

**Why these two first:**
- Solves the live problem observed at session open
- Proves MCP server works end to end
- Every subsequent session uses `knox_close_session` — habit forms before full architecture is complete
- Short build — one focused session

---

### Infrastructure decisions

Questions Claude asked before locking the spec:

**Hosting:** Render account exists. Confirmed.

**Supabase:** Lance identified existing project `meltlfmxsjfnizsxgavw.supabase.co` set up for Knox (separate from Cape31 CMM at `vlcnqmkrardcismsdnxh`). Use this — no new project needed. Verify empty at build session start.

**Render:** Dashboard screenshot showed Render connected to `lance505504-tech/Knox` but looking for a `render.yaml` blueprint that doesn't exist — nothing deployed. Will redirect to `lance505504-tech/knox-mcp` at build session start.

**GitHub repo:** `lance505504-tech/knox-mcp` — to be created at build session start.

**Scope for increment 1:** `lance505504-tech` account only. Cape31 PAT and lanceadams PAT added in increment 2 when credential architecture is in place.

**Audit log schema:**
```sql
create table audit_log (
  id uuid default gen_random_uuid() primary key,
  timestamp timestamptz default now(),
  session_date date not null,
  workstream text not null,  -- Knox, Cape31, Nouvita, BroadOak, IbizaMediaRoom
  tool_called text not null,
  repo text,
  file_path text,
  commit_sha text,
  summary text,
  outcome text not null
);
```
`workstream` field added on Lance's suggestion — makes the audit log tell you which project generated which action.

---

### Session rules v1.2

Lance uploaded updated Session Rules v1.2 including Rules 50-53 established 020526 following a scope creep incident in which 622 lines were committed across three commits without staged review. The revert cost more time than the build.

Rules 50-53:
- **Rule 50:** Line-count gate — builds producing more than 50 net lines must be broken into stages, each shown before the next begins
- **Rule 51:** Show-before-push is mandatory — for any change over 10 lines, paste changed sections before running git add
- **Rule 52:** Declaration scope is a ceiling — if something additional is identified during implementation, stop, return to owner, get explicit approval
- **Rule 53:** One logical change per commit — a commit message requiring "and" probably contains too much

Claude incorporated these into the Knox operating protocol. Session rules pushed to Knox repo as `Claude-Session-Rules-Generic-v1.2.md`.

---

### Larger horizon — noted, not detailed

Late in the session Lance indicated that Knox v4 and the evolutionary model are intended to serve a larger project not yet introduced into this context. The detail is withheld deliberately — to be introduced when the time is right.

What can be recorded: Knox v4 is not only solving the session memory problem for four current workstreams. It is building foundation infrastructure for market-scale network tools that need to generate real market connections — better, faster, and more freely than current tools allow. The evolutionary model (variation, selection, inheritance, mutation across sessions) is load-bearing for this, not decorative.

The evolutionary mechanism was discussed explicitly: variation, selection, inheritance, occasional leaps. Sessions as generations. Knox as the organism. Fitness functions as the selection environment — workstream-specific, defined as each workstream matures. The audit log stops being a compliance record and starts being a selection environment. The full dialogue capture (not just restart briefs) is true inheritance — the next session builds on reasoning, not just conclusions. Leaps are marked differently from incremental decisions: a departure from prior thinking, naming what it replaces and why.

Implication for Knox v4 design: the membrane has to be good enough for market scale. The audit log, fitness functions, and thinking inheritance are not nice-to-haves. A future session will introduce the larger context when Lance judges the foundation is ready for it. Until then: hold the horizon, build the foundation.

---

### Session close-out

Files pushed to lance505504-tech/Knox, all SHA-verified:

| File | SHA | Notes |
|---|---|---|
| `docs/knox-v4-increment-1-build-spec.md` | `d9415dc4ffd4` | New file — self-contained build brief |
| `logs/dev-log.md` | `7d6a5b5316a3` | Appended session close-out entry |
| `active/notes.md` | `1d116027f787` | Replaced with Knox v4 section added |
| `Claude-Session-Rules-Generic-v1.2.md` | `26337b3ff5de` | Updated to v1.2 including Rules 50-53 |

This session dialogue, BuildState.md, and SessionRestart brief are the final three artefacts per Rule 5.

---

## What the next session needs to know

The build session opens with `docs/knox-v4-increment-1-build-spec.md`. That document is self-contained and tells the build session exactly what to do. This dialogue provides the reasoning behind every decision in that spec.

The three questions to verify at build session start:
1. Is Supabase `meltlfmxsjfnizsxgavw.supabase.co` empty / ready?
2. Render redirected to `lance505504-tech/knox-mcp`?
3. `GITHUB_PAT_LANCE` generated with contents:write on Knox repo?

When those three are confirmed — go.
