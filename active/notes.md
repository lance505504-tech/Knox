# Project Notes

## Knox v4 — IN DESIGN (020526)

### Architecture decision
Knox v4 = MCP server. Integration layer confirmed. Claude calls Knox tools natively — no PAT pasting, no prompt engineering, outputs captured via tool call not hope.

### Increment 1 spec
File: docs/knox-v4-increment-1-build-spec.md (committed to Knox repo)
Two tools: knox_push_output, knox_close_session
Repo: lance505504-tech/knox-mcp (to be created at build session start)
Hosting: Render (account exists, needs redirecting to knox-mcp repo)
Supabase: meltlfmxsjfnizsxgavw.supabase.co (existing Knox project — verify empty at build session start)

### Before build session
- [ ] Generate GITHUB_PAT_LANCE — contents:write on Knox repo
- [ ] Redirect Render to lance505504-tech/knox-mcp repo
- [ ] Verify Supabase project empty, create audit_log table at build session start

## Knox Integrity Protocol (carry forward)
- Session start: read dev-log last entry + notes before touching any file
- Never regenerate from scratch — fetch, read, patch, verify, stamp
- UPDATE-NEWS.md now in Knox active/ — use it for news update sessions
- Session rules v1.2 (Rules 1-53) now the Knox operating protocol

## News Update Tool
- File: active/UPDATE-NEWS.md (Knox repo)
- How to use: Claude session → upload regional HTML + UPDATE-NEWS.md → type "Update the news"
- Claude detects region, searches, updates news section, outputs stamped file
- No technical knowledge needed

## Project Baselines (as of end of session 3 — 0604)

### Cape31 Sites — READY TO PUSH (need Cape31 PAT)
- UK v2: Cape31-UK-v2-0604d.html — hero fix applied — push to Cape31-UK-website
- International v3: Cape31-International-v3-0604h.html — push to Cape31-International-website
- SA v1: Cape31-SA-v1-0604.html — push to Cape31-SA-website
- AUS v1: Cape31-Aus-v1-0604.html — HOLDING for review — push to Cape31-Aus-website

### CMM System — BUILT AND CONFIGURED (session 3)
- cape31-media-manager.html — committee tool, runs locally, all credentials baked in
- community-upload.html — open upload page, Google sign-in, ready to add to regional repos
- content.json — regional content schema template, copy to each repo
- cape31-content-loader.js — drop into each regional index.html alongside content.json
- supabase-setup.sql — already run, tables live in Supabase

### Live URLs
- UK: https://orange-stone-046c62f03.4.azurestaticapps.net
- International: https://wonderful-beach-0c8107703.6.azurestaticapps.net

## Open Tasks

### Knox v4
- [ ] Generate GITHUB_PAT_LANCE before build session
- [ ] Redirect Render to lance505504-tech/knox-mcp repo
- [ ] Open build session with docs/knox-v4-increment-1-build-spec.md as briefing
- [ ] Create lance505504-tech/knox-mcp repo at build session start
- [ ] Verify Supabase meltlfmxsjfnizsxgavw.supabase.co and create audit_log table
- [ ] Build and deploy knox_push_output and knox_close_session
- [ ] Connect Claude Desktop/Code to Knox MCP endpoint
- [ ] Dogfood: close build session using knox_close_session

### Cape31 Sites
- [ ] Cape31 PAT — push UK v2, International v3, SA v1, AUS v1 to live repos
- [ ] AUS content confirmation from @pacesailing (fleet register, results, committee)
- [ ] Wixstatic → S3 image migration decision (20-24 wixstatic refs per site)
- [ ] Mobile review of International v3
- [ ] Med regional site — check if Cape31-Med-website repo exists under cape31one-sudo
- [ ] US regional site — check if Cape31-US-website repo exists under cape31one-sudo

### CMM Next Steps
- [ ] Add content.json to UK and International repos
- [ ] Add cape31-content-loader.js to UK and International index.html
- [ ] Replace hardcoded news/gallery/video HTML with loader div containers
- [ ] Test full flow: CMM adds news → content.json pushed → renders on live site
- [ ] Add community-upload.html to regional repos
- [ ] Test community upload → approval → gallery publish flow
- [ ] Add Med and SA/ZA Azure URLs to Google OAuth authorised origins
- [ ] Reset uploads_this_event in Supabase at start of each new event

## CMM Config (stored for reference — do not share publicly)
- Cloudinary: cloud=doi89o1gf, preset=cape31-media
- Supabase project: vlcnqmkrardcismsdnxh
- Google OAuth client created, UK + International + localhost origins added
- EmailJS: service_0us6iod, template_5j6exlb, notify=cape31one@gmail.com

## Decisions Made
- CMM runs locally for now — GitHub Pages requires public repo which would expose credentials
- Community upload: Google sign-in, 2 slots per event default, committee raises per user
- content-loader.js replaces hardcoded HTML — fetches content.json from same origin
- AUS site: green (#00843D), held for review, fleet/news sections marked pending
- Knox v4: MCP server architecture confirmed (020526)
- Knox v4 Increment 1: knox_push_output + knox_close_session only
- Knox v4 hosting: Render, Supabase meltlfmxsjfnizsxgavw.supabase.co, lance505504-tech/knox-mcp repo

## Links
- UK live: https://orange-stone-046c62f03.4.azurestaticapps.net
- International live: https://wonderful-beach-0c8107703.6.azurestaticapps.net
- Knox repo: https://github.com/lance505504-tech/Knox
- Knox v4 design brief: https://github.com/lanceadams/library/blob/main/knox/knox-v4-design-brief.md
- Knox v4 build spec: https://github.com/lance505504-tech/Knox/blob/main/docs/knox-v4-increment-1-build-spec.md
- Cape31 repos: github.com/cape31one-sudo/[repo-name]
- UPDATE-NEWS.md: https://raw.githubusercontent.com/lance505504-tech/Knox/main/active/UPDATE-NEWS.md
