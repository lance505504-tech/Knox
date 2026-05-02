# Claude Session Rules — Generic v1.2

> Generic operating protocol for multi-session development projects.  
> Version 1.2 — copy and adapt per project.  
> Convert this to `docs/SESSION-RULES.md` in each project repository and populate Section G.

---

CLAUDE SESSION RULES
Generic operating protocol for multi-session development projects
Version 1.2 — copy and adapt per project

## How to use this document

This page is your starting point. Read it before anything else. The rules that follow are for Claude — not for you to memorise. Your job is to load this document into a Claude session and let Claude take it from there.

### Starting a new project

Open a new Claude session. Paste or upload this document into the chat. Then send this message exactly:
I am starting a new project. Please read these session rules, then talk me through what needs to be set up before we begin.
Claude will read the document, ask you a short series of questions about the project, and walk you through anything that needs to be in place — repository, local mirror, credentials, Section G. You do not need to read the rest of this document first. Claude will guide you through it.

### Resuming an existing project

Open a new Claude session. Upload this document and the current SessionRestart brief from your repository. Then send this message:
I am resuming an existing project. Please read these session rules and the restart brief, then confirm what you need to get started.
Claude will read both documents, confirm its understanding of the project state, ask for the repository access token, and begin the session opening sequence. You do not need to explain what happened in the last session — the restart brief does that.

### The one thing you need to have ready

Before starting any session where Claude will write or commit code, you need a Personal Access Token (PAT) for your repository. See Appendix A6 for how to create one. It takes about two minutes. Have it copied and ready to paste when Claude asks for it. Without it, Claude can read your repository but cannot commit anything back.

### What Claude will do from here

Once you send the opening message, Claude takes over. For a new project, Claude will:
- Ask the name and purpose of the project
- Ask whether a repository exists or needs creating
- Walk through the Appendix A setup checklist with you
- Ask for the repository URL and PAT when ready
- Set up the repository structure and commit the initial documents
- Ask you to complete Section G (project-specific configuration)
- Write and commit the first SessionRestart brief
- Confirm the project is ready for development
For a resuming project, Claude will confirm current state from the restart brief, ask for the PAT, pull the repository, check tickets, read BuildState.md, and confirm what the session will work on. You approve, and work begins.
Do not start explaining the project to Claude before sending the opening message above. Load the document first. The opening message triggers the structured setup — starting without it means Claude has no protocol and will improvise.



## Purpose and use of this document

This document defines the standing rules for working with Claude AI across sessions on a development project. It is the single source of truth for how sessions operate. Session-restart briefs reference it rather than re-stating it. When a rule changes, it is updated here; the change is not re-stated in briefs or dialogue.
This is a generic version. When starting a new project, copy this document into the project repository at docs/SESSION-RULES.md and replace every [PLACEHOLDER] with project-specific values. Add project-specific rules in the numbered sequence in Section G. Do not remove generic rules unless the project genuinely does not need them.
Before the rules, read Appendix A (new project setup) and Appendix B (working safely with files and code). These contain the practical steps needed to get a project infrastructure in place before the first development session.


### Versioning format — DDMMYYvx

All versioned artefacts in this system carry a version suffix in the format DDMMYYvx — two-digit day, two-digit month, two-digit year, followed by a letter increment starting at va. This suffix is appended to a descriptive filename that has already been chosen; it does not replace the filename. The descriptive name identifies what the file is; the version suffix identifies when it was created and which iteration it is.
Examples showing a complete filename — descriptive name plus version suffix:
SessionRestart-240426va.md   — restart brief, 24 April 2026, first of the day
SessionRestart-240426vb.md   — restart brief, same day, second iteration
Session-240426va.md          — session dialogue, same date
TKT-240426va.md              — ticket opened 24 April 2026
BuildState.md                — no version suffix; this file is updated in place
The version suffix alone — 240426va — is never a complete filename. It is always combined with a descriptive prefix that makes the file's purpose immediately readable without opening it.
When the letter increment reaches vz, the next is vz2, then vz3, and so on. The letter resets to va when the date changes.
The date must always be verified against the actual current date before tagging any artefact. Claude checks the date in the session context or asks — it does not assume. Getting this wrong corrupts the archive. At session close, before writing any document, Claude confirms the current date and verifies all tags use the correct DDMMYYvx format.


## A. Context and continuity


### Rule 1. Decisions carry forward — do not re-litigate

A decision made in a previous session stands until the owner explicitly reopens it. Session-restart briefs must fully capture the decisions of the session they close out, including the reasoning, so the next session does not have to re-derive them. Claude does not re-ask questions the brief already answers.
If Claude thinks a decision needs revisiting, Claude names the decision, names the reason, and waits — it does not silently reopen it.

### Rule 2. Session dialogue is archived to the repository

The dialogue from every session is preserved and committed to library/sessions/ at session close, named with the session tag — e.g. Session-240426va.md. The file contains two parts: a highlights section at the top, and the full dialogue summary below it.
The highlights section captures conclusions, insights, and resolved side-thoughts — not decisions (those go in the restart brief) but the reasoning and context behind them. It is written to be read in two minutes. The full dialogue section below captures the substance of the conversation in enough detail that a future session can trace the reasoning behind any specific conclusion.
Future sessions read the highlights from prior dialogues as part of their opening context, alongside SESSION-RULES, research memos, design documents, and the restart brief. The full dialogue is available if deeper tracing is needed. Nothing important lives only in a closed chat window.

### Rule 3. Session-restart briefs archive to the repository

Session-restart briefs live in docs/. Reviewed proposals and working documents live in docs/proposals/. If it matters, it goes to the repository so it survives the session. A file that exists only on a local desktop or in a session working directory does not survive.

### Rule 4. Build state document — read at open, update at close

Every project maintains a docs/BuildState.md in its repository. Every session reads it as its first action after pulling repos and checking tickets. It is the authoritative record of what is built, what is live, what is empty, and what the next task is.
Every session updates docs/BuildState.md at close — before writing the restart brief — to reflect what was built, what changed in the database, and what the next task is. A session that does not update the build state document has not closed properly.
BuildState.md uses this language precisely:
"Committed to repo"   — file exists in the repository, will be present next session
"Applied to database" — migration has been run against the database
"Deployed"            — function or app build is live
Never "written", "created", or "exists" unless the file is committed to the repo

### Rule 5. Session close sequence — three artefacts, in order

Every session produces three close-out artefacts, written and committed in this order:
1. docs/BuildState.md              — updated to reflect the session's work
2. library/sessions/Session-DDMMYYvx.md   — session dialogue with highlights
3. library/sessions/SessionRestart-DDMMYYvy.md — restart brief for the next session
The restart brief is named with the next session's tag (same day increments the letter; new day resets to va). It is the last written and the first lost if the session ends abruptly. If context is running short, write the restart brief before the dialogue. The dialogue can be reconstructed; the restart brief cannot.

### Rule 6. Commit before close — no artefacts left in working directory

Every file produced in a session — SQL migrations, scripts, configuration files, documentation — must be committed and pushed to the repository before the session closes. BuildState.md must never describe a file as "written" or "exists" unless it is committed.


## B. Working mode


### Rule 7. Think, build, review, loop

Two working modes form a cycle, not a binary switch.
Thinking-this-through is the owner's pace. Ideas are held in tension, contradictions left open where productive, no premature structure. Claude slows down, does one thing at a time, asks one question at a time, and does not reach for frameworks or plans unless the thinking calls for them. If Claude notices itself systematising — turning a live question into a process rule — Claude stops.
Let's-build-this is Claude's speed. The thinking has landed enough that there is a defined thing to build. Claude executes the defined work end-to-end, commits, pushes, reports. No staccato check-ins mid-build. The only reason to pause is if building reveals the definition was broken in a way judgement cannot resolve — Claude stops, reports, and returns to thinking-this-through.
Review happens after a build, against the logic of the definition: does it match what was specified, does it actually work. Review is honest. If the build is wrong, that is learned now.
Default is thinking-this-through. Mode changes when the owner signals with "thinking this through" or "let's build this", or equivalent natural language. Thinking that never reaches a build is also a failure mode.

### Rule 8. Questions in chat by default

Questions raised during work stay in chat unless the owner explicitly promotes them to a document. Do not block progress waiting for answers to non-blocking questions. Genuinely deep or structural questions get promoted to a document for formal answer and archiving.

### Rule 9. Document format

Plain paragraphs. No tables unless data demands it. No frames. No nested bullets. No AI flourishes. Memos, not decks. One-page front with the core, detail behind.


## C. Repository structure


### Rule 10. Standard repository layout

Every project repository follows this layout. Establish it in the first session.
repo-root/
docs/
SESSION-RULES.md        — this document (project-adapted copy)
BuildState.md           — current build state
proposals/              — reviewed proposals and design docs
library/
sessions/               — session dialogues and restart briefs
tickets/
open/
closed/
TicketRecord.md
README.md
_template.md
scripts/                  — build, migration, and utility scripts
src/                      — application source code
.gitignore               — must exclude .env, secrets, node_modules
README.md                — project overview and setup instructions
Nothing important lives outside the repository. If it matters, it is committed.

### Rule 11. Session opening sequence

Every session opens with the same steps, in this order, before reading any other document:
Step 1 — Pull the repository. Even if already cloned, pull before reading anything.
git pull origin main
Step 2 — Check open tickets.
ls library/tickets/open/
cat library/tickets/TicketRecord.md
Step 3 — Read BuildState.md. Step 4 — Read the restart brief. This is the complete opening sequence. Do not skip or reorder it.

### Rule 12. Ticket protocol

When one workstream identifies a gap, ambiguity, or needed change that affects another, the issue is raised as a ticket. Tickets are Markdown files named TKT-DDMMYYvx.md. New tickets go in library/tickets/open/. Resolved tickets move to library/tickets/closed/. Every ticket has an entry in TicketRecord.md. A ticket whose response exists in dialogue but whose Resolution section is blank has not been closed.

### Rule 13. Ticket resolution before build

When a session can resolve a ticket that targets its own workstream, it records the resolution before starting any build work: fill the Resolution section, move the file to closed/, update TicketRecord.md — all in a single commit. The build does not start until this is done.


## D. Infrastructure and credentials


### Rule 14. Development sessions have infrastructure access

Development sessions access the full development stack: the repository (read, write, commit, push), the development database, cloud hosting resources, and third-party services. Access is granted session-by-session through session-scoped credentials supplied by the project owner. Claude does not hold long-lived credentials between sessions.
Claude notes when credentials have been pasted into the transcript — not as a rotation prompt during development, but so the owner has a record of what is in the session.

### Rule 15. Development and production are always separate

Do not design patterns that would break when development and production are separated. Do not accept shortcuts — shared credentials, production-only features absent from development, unversioned migrations — that would make separation painful later. When in doubt, design as though they are already separated.
When a workstream moves to production, credential hygiene upgrades: rotate after every session, never paste into transcripts if avoidable, use minimum-permission keys. Until that flag is explicitly raised, development practices apply.

### Rule 16. Hard infrastructure boundary — each project owns its own infrastructure

Every workstream has its own dedicated infrastructure: its own database project, its own cloud resources, its own credentials. No session ever touches another project's infrastructure directly. The only legitimate cross-project connection is through HTTP API calls. No direct database cross-access in any direction, ever.
If a session finds itself holding credentials for a project it does not own, it must not use them and must flag the situation immediately. This rule has no exceptions.
[Infrastructure registry — add one row per resource at project start:]
Project: [NAME] | Provider: [name] | Identifier: [ID/URL] | Purpose: [description]

### Rule 17. GitHub authentication — PATs and multi-account setup

Claude accesses GitHub repositories during development sessions using fine-grained Personal Access Tokens (PATs). PATs are provided by the project owner at session start. The scope of access required is: Contents — read and write, on a single named repository. Set expiry to 1 day for session work. Rotate or let expire after the session.
Where multiple GitHub accounts are in use, each must have its own SSH host alias. Repositories must not be located on paths synced by cloud file sync services (OneDrive, Dropbox, iCloud) — git and live sync conflict. Use a local unsynced path. See Appendix A for full setup guidance.

### Rule 18. Scope lists and provision scripts must stay in sync

Where the project uses provisioning scripts to create API keys or service accounts, the scope list in those scripts must be updated whenever new scopes are added to the API. A scope that exists in the API but not in the provision script causes silent authorisation failures. The restart brief confirms whether the provision script scope list is current.


## E. Database and external services


### Rule 19. Database migrations are committed before being applied

Every database migration — schema changes, seed data, function definitions — is committed to the repository in scripts/migrations/ before it is applied. A migration applied but not committed is invisible to future sessions. BuildState.md records both the commit and the application status separately.
Migration naming convention: NNNN-description.sql where NNNN is a zero-padded sequence number. Never apply out of sequence. Never edit a migration that has already been applied — write a new one.

### Rule 20. Deployments are documented and repeatable

Deployment commands are documented in docs/ or in a script in scripts/ so any session can repeat the deployment without reconstructing the command. A function or app committed but not deployed is not live. A function deployed from a local working directory without being committed does not survive the session.

### Rule 21. Third-party service configuration is documented in the repository

Any third-party service used by the project has its configuration documented in docs/ with: the service name, the account/project identifier, what it is used for, and what credentials are needed. Credential values are not stored in the repository — only what exists and what it is for. See Section G for the services registry.

### Rule 22. API specifications are the shared contract

Where multiple workstreams connect to a shared API, the API specification is owned by the workstream that runs the API and committed to that workstream's repository. Consuming workstreams read the specification as their input contract. Changes are proposed via the ticket system. The API specification must be versioned. Consuming workstreams record which version they built against in their own BuildState.md.


## F. Multi-project coordination


### Rule 23. Sessions coordinate through the repository, not through conversation

Where a project involves multiple sessions or workstreams, they coordinate through committed artefacts — documents, tickets, BuildState.md — not through conversation. No session has the context of another session's conversation. Each session builds from the documentation the other has committed.

### Rule 24. A shared library repository holds cross-project artefacts

Where multiple projects share artefacts — API specifications, shared documentation, tickets — these live in a shared library repository that every project session can read. The library repository follows the same commit discipline as project repositories.
[Library repository URL: ___________]

### Rule 25. Decision ownership is explicit

Every domain of decision has an explicit owner. When a question touches a decision boundary, it routes to the right owner. Decision owners are named in Section G. Claude does not decide ownership — the project owner does.


## F. Build safety and integrity

The rules in this section address ten failure modes that arise during build sessions: Claude completing a task partially but presenting it as done; silently changing existing functionality; hallucinating that something exists when it does not; doing more than was asked; losing deferred items; filling gaps by assumption without flagging them; producing code that only works in its own environment; applying migrations without a rollback plan; treating draft documents as authoritative; and resuming a partial build by re-doing work already done. All of these are serious. None of them should require Claude to stop and ask during a build. The mechanism that prevents them without interrupting the build is the pre-build declaration and the post-build report.

### Rule 26. Pre-build declaration — one checkpoint before touching anything

Before writing, editing, or deleting any file, running any migration, or executing any deployment command, Claude produces a pre-build declaration. This is the single checkpoint where everything is surfaced. Once the owner reads it and says go, Claude builds without interrupting. The declaration is not a conversation — it is a structured statement that makes Claude's understanding, scope, assumptions, and risks explicit before any of them become consequential.
The pre-build declaration covers seven things, in this order:
1. SCOPE
Every file, function, migration, and service endpoint the build will
touch. Anything not listed will not be touched.

2. EXISTING FUNCTIONALITY AFFECTED
Any existing code, schema, or behaviour that will be changed, removed,
or restructured as a side effect of the build, even if incidental.
If nothing existing will be affected, state that explicitly.

3. ASSUMPTIONS
Every decision the build will make that the definition did not specify:
default values, error handling, naming conventions, fallback behaviours.
Each stated as "I will assume X unless told otherwise."

4. DEPENDENCIES VERIFIED
Every file, function, database table, API endpoint, or service the
build depends on, confirmed to exist before the build starts.
Anything that cannot be verified is listed as UNVERIFIED, not assumed.

5. ENVIRONMENT NOTES
Any aspect of the build that depends on the deployment environment
rather than the Claude container: environment variables required,
service versions assumed, OS-specific behaviour, anything that works
in Claude's environment but may not work in the actual environment.

6. ROLLBACK
For any database migration, the rollback procedure. If no rollback
procedure exists, that is stated explicitly as a risk requiring
owner confirmation before the migration is applied.

7. DEFERRED ITEMS
Anything identified during declaration that is out of scope for this
build but must not be lost. Each deferred item is named here and
will be captured as a ticket or in the restart brief at session close.
The owner reads the declaration, corrects any misunderstanding or missing item, and confirms go. Claude then builds end-to-end without further check-ins. The only exception: if the build itself reveals that the definition was broken in a way that cannot be resolved by judgement — Claude stops, states the specific problem, and waits. A build that starts without a pre-build declaration has not followed the protocol.

### Rule 27. Post-build report — structured account of what actually happened

When the build is complete, Claude produces a post-build report before updating BuildState.md or writing the restart brief. The report covers the same seven areas as the declaration, now as actuals rather than intentions:
1. COMPLETED
Every file, function, migration, and endpoint actually touched,
with a one-line description of what changed.

2. NOT COMPLETED
Anything that was in scope in the declaration but was not completed,
and why.

3. SIDE EFFECTS
Any existing functionality changed or removed as a side effect,
including anything not anticipated in the declaration.

4. ASSUMPTIONS MADE
Every assumption from the declaration that was acted on, plus any
new assumptions made during the build that were not in the declaration.

5. ENVIRONMENT GAPS
Any point where the build could not be verified against the actual
deployment environment. Distinguishes verified (tested and consistent
with known deployment environment) from unverified (Claude container only).

6. ROLLBACK STATE
Confirmation that rollback procedures exist for any migrations applied,
or explicit statement that they do not and owner risk-acceptance was given.

7. DEFERRED ITEMS CAPTURED
Confirmation that every deferred item named in the declaration has been
written into a ticket or the restart brief. A deferred item not
captured here is lost.
The sequence is: declaration → owner confirms go → build → post-build report → BuildState.md → restart brief. BuildState.md draws on the post-build report. The restart brief draws on both.

### Rule 28. Completeness — Claude must account for everything in scope

A build is not complete when Claude stops working. It is complete when the post-build report accounts for every item in the declaration — either as completed, not completed with a reason, or explicitly deferred. "Done" without this accounting is not done. If a build covers eight of ten scoped items, the post-build report names all ten: eight as completed, two as not completed with reasons. The owner then knows exactly what is and is not in place.

### Rule 29. No silent changes to existing functionality

Claude does not modify, remove, comment out, refactor, or rename existing code, schema, or configuration that is outside the declared scope — even if the change would be an improvement, even if the existing code is wrong, even if the change is incidental to making the new code work. If a change to existing functionality is necessary to complete the build, that change is named in the pre-build declaration under EXISTING FUNCTIONALITY AFFECTED and confirmed before the build starts.
If Claude identifies a problem with existing code while building but fixing it is out of scope, that observation goes into DEFERRED ITEMS in the declaration and becomes a ticket at session close. It is not silently fixed during the build.

### Rule 30. No scope creep — Claude builds only what was declared

The pre-build declaration defines the boundary of the build. Claude does not add features, improve adjacent code, extend the API beyond what was specified, or make "while I'm here" changes. If something useful is identified during the build, it goes into DEFERRED ITEMS in the post-build report and becomes a ticket. It is not added to the build in progress.
This is not rigidity — it is auditability. A build that touches only what was declared produces a diff the owner can review. A build that also improved three adjacent things produces a diff that cannot be audited without reading every line.

### Rule 31. Verify existence before declaring a dependency

In the pre-build declaration, every dependency listed under DEPENDENCIES VERIFIED must be confirmed to exist — in the repository, in the database, in the deployed service — before the build starts. A dependency is not verified because it was discussed in planning or because it should exist. It must be confirmed.
Verification steps:
File or function:     git show HEAD:path/to/file
Database table:       query information_schema or equivalent
API endpoint:         check route definitions in the codebase
Environment variable: check .env documentation — not assumed present
If a dependency cannot be verified, it is listed as UNVERIFIED in the declaration. An unverified dependency is a named risk, not a silent assumption.

### Rule 32. Deferred items must be formally captured before session close

Any item named as deferred in a declaration or post-build report must be formally captured before the session closes. Formally captured means one of:
- A ticket file written and committed to library/tickets/open/
- An entry in TicketRecord.md for that ticket
- A named item in the Next Session section of the restart brief
An item named as deferred but absent from all three places at session close is lost. The post-build report confirms which mechanism was used for each deferred item. Claude does not say "I'll note that" without noting it somewhere findable.

### Rule 33. Assumptions must be stated before being acted on

When the build definition does not specify something Claude needs to decide — a default value, an error message, a fallback behaviour, a naming choice — Claude does not silently choose and continue. The assumption is stated in the pre-build declaration. If the assumption is wrong, the owner corrects it before the build starts. If an assumption only becomes apparent during the build, it is added to the post-build report under ASSUMPTIONS MADE.
The test: if the owner read the post-build report, would they be surprised by any choice Claude made? If yes, that choice should have been in the declaration. Surprises discovered weeks later when something breaks are not acceptable.

### Rule 34. Environment assumptions are flagged, not hidden

Claude tests and runs code in its own container. That environment may differ from the actual deployment environment: environment variables, service versions, operating system, network access, file paths. Claude does not present code as working when it has only been verified in the Claude container.
The pre-build declaration lists every assumption made about the deployment environment under ENVIRONMENT NOTES. The post-build report distinguishes verified (tested in Claude container and consistent with known deployment environment) from unverified (Claude container only). The owner then knows what needs testing in the actual environment before the build is considered complete.

### Rule 35. Every migration has a rollback procedure

Before applying any database migration, a rollback procedure must exist — the SQL or commands needed to undo the migration. It is committed to the repository alongside the migration file:
scripts/migrations/0001-add-users-table.sql
scripts/migrations/0001-add-users-table-rollback.sql
If a rollback procedure is not possible — for example, a migration that drops a column and its data cannot be recovered — that is stated explicitly in the pre-build declaration as a risk, and the owner confirms acceptance before the migration is applied. A migration applied without a rollback and without explicit owner confirmation is a protocol violation.

### Rule 36. Draft status must be explicit and respected

Documents produced during thinking-this-through mode are drafts unless explicitly marked otherwise. A draft is not authoritative. A subsequent build session may not treat a draft as the settled definition for a build without the owner explicitly confirming it has been decided. Draft documents carry a status line at the top:
Status: DRAFT — not authoritative. Confirm with owner before building against this.
When decided, the status line is updated:
Status: DECIDED — [DDMMYYvx] — authoritative for build.
A document without a status line is treated as a draft. The absence of a status line is not permission to build against it.

### Rule 37. Resuming a partial build — check before re-doing

If a build session was interrupted and resumes — whether in the same session or a new one — Claude does not restart from the beginning. Before executing any step, Claude checks what was already completed: reads BuildState.md, checks the repository for committed files, checks the database for applied migrations. Only steps not already completed are executed. A step confirmed as already done is recorded as such in the post-build report under COMPLETED, with a note that it was verified as pre-existing rather than executed in this session.
The risk this rule addresses is double-application: running a migration twice, creating a file that already exists in a different state, overwriting a commit that contained work from the interrupted session. Check before acting.



### Rule 38. Push verification — confirmed means confirmed

Every file push must be verified before declaring it done. After pushing to GitHub, confirm the returned SHA, check the file size is consistent with what was sent, and where practical fetch the file back and verify key content.

**Pushed means confirmed in the repository — not just that the API call was made.**

Never say a file is pushed, committed, or saved until the verification step confirms it. An API call that returns without error is not the same as a file that exists correctly in the repository. Check the SHA. Check the size. Where the file is critical, fetch it back and verify key content is present.

This rule exists because push failures are silent — the API may return a response without the file actually landing correctly, and the next session opens with a missing file and no record of why.

Established 240426 after observing that AI assistants routinely declare files pushed without verifying the result, leading to lost work discovered only at the next session open.

## G. Project-specific configuration

Populate this section when the generic rules are adapted for a specific project. Replace every placeholder. Add project-specific rules in sequence after Rule 37.
Project-specific rules typically fall into four categories: application boundary rules (which tool or application a change must land in, and how to verify it); tooling and access rules (how to authenticate, which method to use for file operations, which tools cannot work for this stack); verification rules (how to confirm that an operation succeeded, beyond Claude's assertion that it did); and stack-specific failure mode rules (patterns of silent failure discovered in this specific technology combination). The generic rules describe principles; project-specific rules make those principles concrete for the actual tools, services, and failure modes of the project.

### Project identity

Project name:         [NAME]
Primary repository:   [URL]
Library repository:   [URL or "subdirectory of primary"]
Project owner:        [NAME]
GitHub account:       [username]
First session:        [DDMMYYva]

### Decision ownership

Legal and contractual:  [NAME]
Technical architecture: [NAME]
Commercial:             [NAME]
Design and UX:          [NAME]
Content and copy:       [NAME]

### Application boundaries

If the project contains more than one distinct application or tool, name them here and state the boundary rule: what goes in each, what never crosses between them, and how to identify which application a request targets.
Application 1: [NAME] — [description, hosting, data store]
Application 2: [NAME] — [description, hosting, data store]
Boundary rule: [state explicitly what must never cross between them]

### Infrastructure registry

Resource: [type] | Provider: [name] | ID: [identifier] | Purpose: [description]

### Third-party services registry

Service: [name] | Account: [identifier] | Purpose: [desc] | Credential: [type]

### Project-specific rules

Add rules here. For each rule: give it a G-prefixed number (G1, G2...), a title, the specific instruction, and the establishing session tag. The examples below show the pattern — replace with rules relevant to this project.
G1. Confirm the file before touching it — [instruction] — Established [DDMMYYva].
G2. Application boundary enforcement — [instruction] — Established [DDMMYYva].
G3. Authentication method for this stack — [instruction] — Established [DDMMYYva].
G4. File push method for this stack — [instruction] — Established [DDMMYYva].
G5. Push verification — [instruction] — Established [DDMMYYva].
These five categories — file confirmation, application boundary, authentication, file operations, and push verification — are the minimum set to consider for any project that involves Claude writing to a remote repository. Add further rules as new failure modes are discovered.


## Appendix A: New project setup guide

This appendix explains how to set up the infrastructure a new project needs before the first development session. It covers: creating a GitHub repository, setting up a local mirror, installing GitHub Desktop, creating a PAT for Claude, and organising your local file store. Read this before starting any project.

### A1. Why a repository is essential

Claude has no memory between sessions. Every session starts fresh. The repository is the mechanism by which a project survives from one session to the next — all code, all documentation, all decisions, all session records live there. Without a repository, every session starts from scratch.
The repository also means that you and Claude are always looking at the same thing. When Claude reads a file from the repository, it is reading the same file you have on your machine. When Claude commits a change, you pull it and have it locally. This shared, version-controlled store is the foundation of everything else.

### A2. Creating a GitHub repository

GitHub is the recommended hosting platform. An account is free. Private repositories (only you and people you invite can see them) are free on all plans.
Steps to create a repository:
1. Go to github.com and sign in (or create an account)
2. Click the + icon top right, then "New repository"
3. Give it a name — short, lowercase, hyphens not spaces (e.g. my-project)
4. Set it to Private unless the code is intended to be public
5. Tick "Add a README file" — this creates the main branch automatically
6. Click "Create repository"
You now have a repository at github.com/your-username/your-project-name. This is the remote — the version hosted on GitHub.

### A3. Local mirror — why you need one and how to set it up

GitHub hosts the remote copy of the repository. You also need a local copy on your machine — the local mirror. This is where you edit files, where Claude commits changes during a session, and where you pull those changes to keep your machine in sync.
The local mirror is a folder on your machine that is connected ("cloned") to the GitHub repository. Changes made locally can be pushed to GitHub. Changes made on GitHub (by Claude during a session) can be pulled down to your machine.
IMPORTANT — location of the local mirror. Do not put the local mirror inside a folder that is synced by OneDrive, Dropbox, iCloud, or any other cloud file sync service. These services and git conflict: the sync service tries to manage files at the same time as git, which causes corruption, conflicts, and data loss. Use a plain local folder that is not synced.
Good location: C:\Projects\my-project (Windows) or ~/Projects/my-project (Mac/Linux)
Bad location: C:\Users\You\OneDrive\my-project or ~/Dropbox/my-project

### A4. Installing GitHub Desktop

GitHub Desktop is a free application that gives you a visual interface for the most common git operations: cloning a repository, pulling changes, committing changes, pushing to GitHub. It is the recommended way to manage the local mirror for most users.
1. Go to desktop.github.com
2. Download and install GitHub Desktop for your operating system
3. Open GitHub Desktop and sign in with your GitHub account
4. Click File > Clone Repository
5. Find your repository in the list and select it
6. Set the Local Path to a folder NOT inside OneDrive/Dropbox/iCloud
7. Click Clone
You now have the repository on your machine. GitHub Desktop shows you the current state: what branch you are on, what has changed, what has been committed, what needs pushing or pulling.
After each Claude session: open GitHub Desktop, click Pull Origin (to get any changes Claude committed), review what changed, and you are up to date.

### A5. Multiple GitHub accounts

If you use GitHub for other purposes (another project, a work account) and have more than one account, GitHub Desktop supports multiple accounts since version 3.3. Sign each account in separately via File > Accounts. When cloning a repository, make sure you select the correct account.
For Claude sessions using git via the command line (which Claude does when committing), each account needs its own SSH host alias configured. This is a one-time setup per machine. If you only have one GitHub account, you do not need to do this.
SSH alias setup for multiple accounts (in ~/.ssh/config):
Host github-account1
HostName github.com
User git
IdentityFile ~/.ssh/id_rsa_account1

Host github-account2
HostName github.com
User git
IdentityFile ~/.ssh/id_rsa_account2
Then use git@github-account1:username/repo.git as the remote URL for repositories belonging to account1. If this applies to your setup, document the alias used in Section G of this document so Claude sessions know which host alias to use.

### A6. Creating a Personal Access Token (PAT) for Claude

Claude cannot sign in to GitHub the way you do. Instead, Claude authenticates using a Personal Access Token (PAT) — a generated key that grants specific, limited access to your repository for a limited time. You create the PAT, give it to Claude at the start of a session, and it expires automatically.
How to create a fine-grained PAT:
1. Go to github.com, click your profile picture top right, Settings
2. Scroll down the left sidebar to "Developer settings"
3. Click "Personal access tokens" > "Fine-grained tokens"
4. Click "Generate new token"
5. Name it something recognisable: "Claude session — my-project"
6. Set Expiration to 1 day (enough for a session; expires automatically)
7. Under "Repository access", select "Only select repositories"
8. Choose the specific repository Claude will work on
9. Under "Permissions", find "Contents" and set it to "Read and write"
10. Scroll down and click "Generate token"
11. COPY THE TOKEN IMMEDIATELY — GitHub will only show it once
At the start of a Claude session, paste the token into the chat when Claude asks for it (or before it asks). Claude uses it to pull and push to the repository. The token expires after 1 day. You do not need to rotate it manually — just generate a fresh one for the next session.
Never share a PAT publicly, never commit it to the repository, and never paste it anywhere except directly to Claude in a session chat. Treat it like a temporary password.

### A7. Local file organisation for a project

Outside the repository, you may need a local working area for files that are not committed to the repository — for example, large binary files, working drafts not yet ready to commit, or environment configuration files with secrets. Organise this clearly.
Suggested local structure alongside the repository clone:
C:\Projects\my-project\          ← the repository clone (managed by git)
C:\Projects\my-project-working\  ← local working files NOT in git
.env                              ← environment variables with secrets
drafts\                           ← working drafts not yet committed
exports\                          ← generated files for distribution
The .env file contains API keys, database connection strings, and other secrets needed to run the project locally. It must never be committed to the repository. The .gitignore file in the repository should include .env so git ignores it automatically.
Anything in the working folder that is not committed to the repository does not survive a session handover. If it matters, commit it or document it.

### A8. First session checklist

Before starting the first development session, confirm:
- □  GitHub repository created and set to Private
- □  Local mirror cloned to a path NOT inside OneDrive/Dropbox/iCloud
- □  GitHub Desktop installed and signed in
- □  Repository cloned in GitHub Desktop and visible
- □  Fine-grained PAT generated with Contents read/write on this repository only
- □  PAT copied and ready to give to Claude at session start
- □  docs/SESSION-RULES.md created (this document, adapted) and committed
- □  docs/BuildState.md created (initial state) and committed
- □  library/ directory structure created and committed
- □  .gitignore created excluding .env and secrets and committed
- □  README.md created with project overview and committed
- □  Section G of SESSION-RULES populated with project identity and infrastructure
- □  First SessionRestart brief written (even if brief) and committed


## Appendix B: Working safely with files and code in Claude

Claude has a drag-and-drop upload area in the chat interface. This is useful for certain things and actively counterproductive for others. Understanding the difference prevents a category of problems that are expensive to undo.

### B1. What the upload window is for

The upload window is designed for sharing documents with Claude so Claude can read them and respond to their content. Appropriate uses include:
- Sharing a PDF, Word document, or image for Claude to read and analyse
- Uploading a data file (CSV, spreadsheet) for Claude to process
- Showing Claude a screenshot or diagram
- Sharing a short text file for Claude to review or edit in chat
In all of these cases, you want Claude to read the file and produce a response. The file is input to the conversation, not part of the project infrastructure.

### B2. What the upload window is NOT for — code files

Do not upload code files, configuration files, or repository files via the drag-and-drop window. This is the wrong mechanism for sharing code with Claude during a development session.
When you drag a code file into Claude:
- Claude reads it as a snapshot at the moment of upload
- Claude cannot commit changes back to the file
- Claude cannot see other files in the same project
- Claude cannot maintain consistency across files
- The file is disconnected from your repository
Any changes Claude suggests must be manually copied back. If Claude edits multiple files, you must manually apply each change. Mistakes in copying are likely. The session ends and the context is gone — if you missed copying something, it is lost.
The correct approach is to give Claude access to the repository via a PAT (see Appendix A6) and let Claude read and write files directly. Claude can then commit changes, check consistency across files, and leave a complete record of what changed. The next session picks up exactly where the last one left off.

### B3. The specific problem with secrets and credentials

Never drag and drop a file that contains API keys, passwords, connection strings, or any credentials into the Claude chat window.
Files commonly containing secrets that should never be uploaded:
.env and .env.local and .env.production
config.js or config.json if they contain API keys
Any file with a name like secrets.json or credentials.json
SSH private key files (id_rsa, id_ed25519)
Cloud provider credential files (AWS credentials, service account JSON)
When you upload a file to Claude, its contents enter the session transcript. The transcript is stored by Anthropic. Even if the session ends, the transcript and its contents persist according to Anthropic's data retention policy. A secret that entered the transcript should be considered potentially exposed and rotated immediately.
If Claude needs to know about an API key or connection string to help with a task, describe it by its name and purpose — do not paste the value. For example: "I have a Supabase service role key configured as SUPABASE_SERVICE_KEY in my .env file." Claude can work with that description without needing the value itself.

### B4. The specific problem with large codebases

Uploading many code files via drag and drop compounds the problems above. Claude's context window is finite. When many files are uploaded, Claude may not be able to hold all of them in context at once, leading to partial or inconsistent responses. It also creates a maintenance problem: as the code changes during development, the uploaded files become stale, and Claude is working from an out-of-date snapshot.
Repository access solves this cleanly. Claude reads only the files it needs for the current task, reads them fresh from the repository at the start of each session, and always has the current version.

### B5. Summary — what to do instead of drag and drop for code

For a development session where Claude will work on code:
1. Give Claude the repository URL
2. Give Claude a PAT with Contents read/write on that repository
3. Let Claude clone or pull the repository at session start
4. Claude reads what it needs, makes changes, commits, pushes
5. You pull in GitHub Desktop after the session to see what changed
For a document or data file you want Claude to read and respond to — not modify as part of a codebase — drag and drop is fine. The distinction is whether the file is project infrastructure (use the repository) or input to a conversation (upload is fine).


## Appendix C: Repository setup checklist

Use this to confirm the repository is correctly structured before the first development session.
- □  Repository created on GitHub (private)
- □  Local mirror cloned to a path NOT inside cloud sync folders
- □  GitHub Desktop installed, signed in, repository visible
- □  docs/SESSION-RULES.md — this document adapted and committed
- □  docs/BuildState.md — initial state committed
- □  docs/proposals/ — directory created
- □  library/sessions/ — directory created
- □  library/tickets/open/ — directory created
- □  library/tickets/closed/ — directory created
- □  library/tickets/TicketRecord.md — empty index committed
- □  library/tickets/README.md — ticket protocol committed
- □  library/tickets/_template.md — standard template committed
- □  scripts/ — directory created
- □  src/ or equivalent source directory created
- □  .gitignore — excludes .env, node_modules, secrets, OS files
- □  README.md — project overview and setup instructions committed
- □  Section G populated: project identity, decision ownership, infrastructure registry, services registry
- □  Fine-grained PAT prepared: 1-day expiry, Contents read/write, single repo
- □  First SessionRestart-DDMMYYva.md committed

When this checklist is complete, the repository is ready for development sessions. Give Claude the repository URL and the PAT at the start of the first session.
## H. Rules established 240426 (Knox build session)

These rules were established during the session that built Knox — a session that itself violated most of them. They are added here because they address failure modes observed in practice, not in theory.

### Rule 39. Demented terrier rule

Do not suggest, plan, propose, or begin any work until the owner has stated today's focus and said go. Read the briefing. Confirm the state. Ask one grounded question. Wait. Enthusiasm is not the same as usefulness.

### Rule 40. Session opening sequence

After reading the briefing, confirm the current state in two or three sentences based on what the briefing says. Ask one question — the most important open item from the briefing, or simply "What are we working on today?" Wait for the answer. Do not proceed until the owner says go.

### Rule 41. Show before pushing

Before pushing any file to a repository or making any change that cannot easily be undone, show the proposed content or change to the owner and wait for confirmation. Do not push first and report after.

### Rule 42. Pre-build declaration

Before writing, editing, or deleting any file, state the scope, assumptions, and risks. Wait for the owner to confirm before touching anything. A build that starts without a declaration has not followed protocol.

### Rule 43. No scope creep

Build only what was declared. If something useful is identified during the build, note it as deferred — do not add it to the build in progress. A build that touches only what was declared produces a diff the owner can review.

### Rule 44. Thinking-this-through vs let's-build-this

Default mode is thinking-this-through. Ideas held in tension, no premature structure, one question at a time. Switch to let's-build-this only when the owner explicitly signals it. Do not assume a request is a build request because it sounds like one.

### Rule 45. Summarise at end of each task

At the end of every task, summarise what changed, what files were touched, and what was confirmed. Do not move to the next task without this summary.

### Rule 46. Ask before deleting or renaming

Do not delete or rename any file, variable, record, or credential without explicitly asking first, regardless of how obvious the change seems.

### Rule 47. Context window checkpoint

If the context window is running low, say so explicitly and propose a checkpoint before continuing. Do not let the session run out of context mid-task without warning.

*All rules in this section established 240426 during the Knox build session. The irony that most were violated during that session is noted and documented on the Knox landing page.*

### Rule 48. The finding rule

When something useful emerges during a session — a better approach, a correction to a previous assumption, a pattern that worked or failed — flag it explicitly. Draft it as a potential Knox rule in one sentence. Post it automatically to Knox Findings and GitHub Discussions. Tell the user what was posted. Default is capture not confirmation.

### Rule 49. The capture rule

For ephemeral insights that emerge during a session, default to capture rather than confirmation. Post findings automatically to Knox and GitHub Discussions. The cost of losing a good idea is higher than the cost of a deletable post. Flag what was posted but do not block on permission.

*Both rules established 240427. The finding rule makes insight capture an AI responsibility. The capture rule makes the default action capture rather than confirmation — reversing the usual bias toward caution for this specific case.*

### Rule 50. Line-count gate

If a planned change will produce more than 50 net lines of diff, the build must be broken into stages. Each stage is shown to the owner before the next stage begins. No stage is committed until the owner has seen and approved it. A single declaration does not authorise an unlimited number of lines.

### Rule 51. Show-before-push is mandatory, not optional

Rule 41 says show before pushing. This rule makes it unambiguous: for any change over 10 lines, paste the actual changed sections in the conversation before running git add. The owner must acknowledge before the commit happens. "Confirm and I'll go" is not a blank cheque for unlimited lines of implementation.

### Rule 52. Declaration scope is a ceiling, not a floor

What is declared in the pre-build declaration is the maximum scope of the build. If during implementation something additional seems useful or necessary, stop — return to the owner, describe the addition, get explicit approval, then continue. Never expand scope silently during implementation. The owner cannot review what they were not told was being added.

### Rule 53. One logical change per commit

Each commit should do one thing. DOM, JS, CSS, and routing changes for a single feature are separate steps, each shown and approved before the next begins — not combined into one monolithic commit. A commit message that requires "and" to describe what changed probably contains too much.

*Rules 50-53 established 020526 following a scope creep incident in which 622 lines were committed across three commits without staged review. The revert cost more time than the original build. These rules exist because "confirm and I'll go" was treated as permission for unlimited implementation rather than permission for what was declared.*
