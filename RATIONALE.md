# Why This System Exists

## The Problem It Solves

Working with Claude across many sessions, on many projects, with multiple people
creates a specific kind of cognitive overhead: where is the file, which version is
current, who has access, and what was decided last time?

This system — Ref.Repo — exists to eliminate that overhead. Everything lives in
one place. Sessions start from a known state. Anyone with the right access can
pick up where someone else left off.

## Two Project Tracks

**Live Projects** contain documentation that is stable and relied upon.
Procedures here are in use. References here are authoritative.
Changes are deliberate and recorded.

**Development Projects** contain work in progress. Drafts, experiments,
logs of decisions made during active development. These may be incomplete
or subject to rapid change.

Keeping them distinct prevents draft material from being mistaken for
authoritative guidance, and prevents live procedures from getting cluttered
with working notes.

## Version Retention

Every time a manual is saved, the previous state is preserved.
The system keeps the last 30 versions per project.

This means mistakes are recoverable. Accidental deletions, wrong edits,
and experiments gone wrong can all be rolled back — simply select a version
and restore it. The GitHub backup adds a second layer: 30 timestamped exports
of the full repository, auto-managed via GitHub Actions.

## Access and Trust

Access is structured around roles:

| Role | What they can do |
|---|---|
| Owner | Everything. Create any role including other Owners. |
| Admin | Full manual management. Create Contributors. |
| Contributor | Create and edit manuals. |
| Reader | Browse and read. No sign-in required. |

New members are invited by an Admin or Owner who creates an invitation token.
The token expires in 7 days. When redeemed, the new member registers their
biometric (Face ID or Touch ID) on their device — no password is ever set or
stored. Subsequent sign-ins require only a biometric prompt.

## Why Biometrics, Not Passwords

Passwords create friction and get reused, written down, or forgotten.
Biometrics via WebAuthn / Passkeys are:
- Stored on the device's secure enclave, never transmitted
- Phishing-resistant by design
- Synced across a user's Apple or Google devices automatically
- No separate app to install — built into iOS and Android

The system detects whether the device supports biometrics. Where it does,
that is the default. A code-based fallback exists for devices or contexts
where biometrics are unavailable.

## Claude Integration

At the start of any Claude session, uploading `CLAUDE_SESSION.md` loads:
- The current state of the repository from GitHub
- The development log showing what was last worked on
- Project notes with active context

Claude fetches files directly from GitHub — there is nothing to locate,
rename, or upload from a local folder. The session file is the only
file the user manages locally, and it changes rarely.

---

*This document should be updated when the purpose or structure of the
system changes significantly.*
