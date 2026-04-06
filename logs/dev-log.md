# Development Log

---
## 2026-04-04 -- Knox initialised
**Worked on:** Repository created and configured via knox-setup.py
**Files created:** All core files, folder structure, GitHub Actions, GitHub Pages
**Next:** Sign in to Knox, set up team members, create first project

---
## 2026-04-04 -- Broadoak Manor website project initiated
**Worked on:** Full website redesign scoping for broadoakmanor.co.uk
**Completed:**
- Homepage prototype (HTML/CSS) -- people-first design, green/gold palette, Cormorant Garamond + Jost typography
- Comprehensive design paper (Word .docx, 15 sections, 57 questions for the team)
- knox-update.py updated to push all three Knox files in one command with content baked in
**Key decisions:**
- Technology: Next.js + Azure Static Web Apps + Azure Functions for forms
- Design direction: people not buildings -- residents, staff and families lead every page
- Stories section: self-contained GitHub markdown files, no CMS login required
- Founding year corrected to 1986 (current site incorrectly states 1976)
- CQC Outstanding in Caring to be displayed, subject to current rating verification
- knox-update.py is the standard method for all Knox file updates
- Session end workflow: Claude outputs one knox-update.py with content baked in, download and run, done
**Research findings:**
- Current site: WordPress 2020, slow, building-led, testimonials buried
- Facebook: original page (556 followers) lost to password issue; newer page (40 followers) now active
- CQC: three registrations (Nursing Home, Care Home, Domiciliary Care)
- Real Google reviews extracted and used as homepage testimonial content
- Assisted Living undersold -- barn, community, restaurant missing from current site
**Awaiting:** 57 questions in design paper from Broadoak team
**Next:** Team reviews design paper -> Phase 2 copywriting -> Phase 3 Next.js build

---
## 2026-04-05 -- Session protocol standardised
**Worked on:** Knox session protocol and multi-session conflict prevention
**Completed:**
- CLAUDE_SESSION.md rewritten with full protocol -- session start, during, end, knox-update.py template
- CHATGPT_SESSION.md rewritten with matching protocol -- manual GitHub copy-paste end-of-session workflow
- knox-update.py updated to fetch-then-append for dev-log, preventing simultaneous session overwrites
- Both session files now self-contained -- any AI reading them behaves consistently
**Decisions:**
- Claude sessions: knox-update.py generated at end with content baked in
- ChatGPT sessions: file contents output as labelled blocks for manual GitHub commit
- dev-log always appended, never replaced
**Next:** Broadoak team to review design paper -> Phase 2 copywriting -> Phase 3 build

---
## 2026-04-05 -- Cape31 websites infrastructure planning
**Worked on:** Azure Static Web Apps issues and migration planning to Cloudflare Pages
**Completed:**
- Investigated Azure portal branch dropdown bug when creating Static Web Apps
- Troubleshot all standard fixes (revoke/reauthorize GitHub, browser cache, sign out)
- Created Azure CLI script to deploy 7 regional Cape31 static web apps via Cloud Shell
- Successfully deployed Skandi, D and FR before hitting Azure free tier limit (10 max per subscription)
- Attempted second Azure subscription -- blocked, only one free account allowed per person
- Decided to move all 12 Cape31 websites from Azure to Cloudflare Pages
- Confirmed Cape31-class and Cape31-Dev stay on Azure (used for other services)
- Investigated Cloudflare DNS issue -- nameserver mismatch between 123-reg (henry/ruth) and Cloudflare (johnathan/stevie)
- Confirmed all 5 live sites working despite Cloudflare showing domain as pending
- 123-reg unavailable (holiday) -- cannot update nameservers until they reopen
- Knox session loaded and all work logged
**Decisions:**
- All Cape31 regional/country websites to move to Cloudflare Pages (no site limits, free, DNS already there)
- Cape31-class and Cape31-Dev remain on Azure
- Transfer cape31class.org from 123-reg to Cloudflare Registrar when 123-reg reopens (28 day window)
- Cloudflare Pages setup to proceed after domain transfer completes
**Awaiting:**
- 123-reg to reopen to obtain EPP/Auth transfer code
- Subdomains for the 7 new regional sites still to be confirmed by Lance
**Next:**
- Call 123-reg, get EPP code, initiate domain transfer to Cloudflare Registrar
- Set up Cloudflare Pages for all 12 Cape31 websites
- Delete 3 failed Azure deployments (Skandi, D, FR)
- Delete 4 working Azure regional sites once Cloudflare Pages versions are live and tested
- Confirm subdomain structure for all new regions
---
## 2026-04-05 — Cape31 Website Build + Knox Protocol Overhaul

**Worked on:** Full Cape31 website build session across six regional sites. Knox session protocol redesigned from script-based to direct GitHub API push.

**Completed:**
- UK site: Katabatic race record, Dave Swete credential block, Cowes 2025 quintuple, correct founding fleet history (Mike Bartholomew / Tokoloshe / sold to Russell Peters as Squirt / new Tokoloshe / Katabatic / Jiraffe / Gallivanter)
- UK site: Tor Tomlinson-Cheney role corrected to International Class Secretary (non-voting). Dave Swete added as Circuit Director (non-voting ExCom)
- International site: US vs AUS one-design challenge tracker with America's Cup 1983 narrative
- SA site: Canadian flag emoji removed, correct SA flag CSS stripe added
- Med + US sites: National flag CSS stripes added
- HK site: Built from scratch — Where Dragons Race / 龍爭虎鬥, 888 cultural bar, fleet table, RHKYC venues, dragon culture section
- All regional sites: All Regions button moved from bottom left to bottom right
- All six sites pushed directly to GitHub via API (cape31one-sudo account) — all confirmed with commit SHAs
- Knox CLAUDE_SESSION.md rewritten with robust PAT-in-session protocol
- Knox user instruction manual written and pushed to docs/HOW-TO-USE-KNOX.md
- Identified two GitHub accounts: lance505504-tech (Knox) and cape31one-sudo (Cape31 sites)

**Decisions:**
- Ireland and New Zealand sites on hold — fleets not currently active enough
- HK hero confirmed: Where Dragons Race. / 龍爭虎鬥。
- AUS hero confirmed: Dare to Win. The Whitsundays.
- No names for TP52 owner in Cowes 2025 copy (Dave Swete advice)
- Knox protocol: PAT pasted at session start, Claude pushes directly, no scripts
- Knox PAT: lance505504-tech account. Cape31 PAT: cape31one-sudo account

**Research confirmed:**
- Katabatic: Queen's Cup 2024 (RSYC confirmed in writing), IRC Class 1 Overall 2024 Cowes
- Cowes 2025 quintuple: Britannia Cup (Flying Jenny), NYYC Challenge Cup (Bullitt), Queen's Cup — all beating professional TP52
- Giraglia 2025: Cape31s beat all TP52s in IRC1 inshore (Giornale della Vela)
- Dave Swete: Fastnet 2021 overall winner on Sunrise (Tom Kneen) — only pro on board
- Easter Challenge 2023: Corby 36 Oui — separate boat unrelated to Cape31 programme
- Founding fleet order: Tokoloshe (Mike Bartholomew) → sold to Russell Peters as Squirt → new Tokoloshe ordered → Katabatic (Lance Adams) → Jiraffe (Simon Perry) → Gallivanter

**Awaiting:**
- AUS site: Push to Cape31-Aus-website (repo exists, file built)
- SA domain validation still pending in Azure
- Confirm second Cowes 2024 Katabatic trophy
- Confirm HK floating dock detail with fleet
- ExCom approval before public announcement
- CMS integration with Tom at TTC Marine
- Knox PAT renewal before expiry (check date)

**Next:**
- Push AUS site to Cape31-Aus-website
- Set up aus.cape31class.org DNS CNAME in Cloudflare
- Review international site on Android (reported rendering issues)
- Expand Med site with European ORC/IRC market (French/German language elements)
- Add offshore/IRC racing section to UK site (Malta, Middle Sea Race angle)
---
## 2026-04-05 — Cape31 UK v2 + International v3 rebuilt and delivered
**Worked on:** Two Cape31 site files rebuilt from live Azure staging URLs and dev-log context.

**Completed:**
- Cape31-UK-v2.html: Dave Swete prominence reduced from 58 to exactly 6 references
  - Removed: ticker, hero subtitle, hero tag, origin blurb, dedicated credential block (CV table, Fastnet story, What he brings panel), Talk to Dave Swete CTA, join section sub, join button, join footer micro, footer blurb
  - Kept: hero tag (Circuit Director title only), founding history mention, quote block attribution, circuit section single line, governance table entry, footer link to swetesailing.com
- Cape31-International-v3.html: Two new sections added to existing live file
  - Story section (id=story): Angelo Lavranos design origin, Cape Doctor context, 2016-2026 founding timeline (SA→UK→Med→US→AUS/HK→future), one-design purity/IRC/offshore panels
  - Governance section (id=governance): ExCom structure, regional authority explanation, committee cards (Lance Adams Chair, Tor Tomlinson-Cheney Intl Secretary non-voting, Andy Wibroe Technical Officer non-voting, Dave Swete Circuit Director UK non-voting), Class Rules/Measurement/New Fleet document links
  - Both sections linked in desktop and mobile nav
- push-cape31-sites.ps1: one-click PowerShell script to push both files to cape31one-sudo repos
- Files delivered for manual download — cape31one-sudo PAT not available this session

**Decisions:**
- Knox PAT (lance505504-tech) used for Knox only — cannot push to cape31one-sudo repos
- User will download HTML files and run push-cape31-sites.ps1 with cape31one-sudo PAT
- File naming: Cape31-UK-v2.html → index.html, Cape31-International-v3.html → index.html

**Next:**
- User to run push-cape31-sites.ps1 with cape31one-sudo PAT
- Verify UK live site: https://orange-stone-046c62f03.4.azurestaticapps.net
- Verify International live site: https://wonderful-beach-0c8107703.6.azurestaticapps.net
- Delete HTML files and script from C:\ immediately after push
---
## 2026-04-05 — Cape31 UK v2 + International v3 full session

**UK v2 — READY FOR UPLOAD (cape31one-sudo/Cape31-UK-website → index.html)**
- Dave Swete reduced from 59 to 5 name references
- Removed: ticker, hero tag, nav button (renamed "Buy a C31"), hero subtitle, origin blurb, credential block, quote block button, join section, footer blurb
- Kept (5 refs all below fold): founding history, quote attribution, circuit section, committee card, footer link
- Tor Tomlinson-Cheney removed from UK committee (International and Med role only)
- Nav CTA renamed: "Buy a C31" — links to swete@31northyachting.com
- Mobile CSS fixes: record rows, Cowes grids, quick links bar
- Noticeboard confirmed present as #news with 4 race reports
- File size: 97,357 bytes

**International v3 — READY FOR UPLOAD (cape31one-sudo/Cape31-International-website → index.html)**
- 4 new sections: Story, Series, Rules, Governance
- Story: Cape Doctor, Lavranos spec table, 2016-2024 timeline
- Series: Med (STIG, Europeans, Trinity Racing, Giraglia vs TP52), UK (Flying Jenny, Katabatic, Cowes quintuple), US (Pacific Yankee), SA/AUS/HK cards
- Rules: Class Rules, Constitution, Measurement, Technical Decisions TD-001/002/003, IRC/ORC, NOR, Protest
- Governance: ExCom structure, 6 circuits, committee cards, AGM/Measurement/New Fleet links
- div balance: 607/607 perfect. File size: 136,298 bytes

**Push status: PENDING — cape31one-sudo PAT needed**
**Knox PAT (lance505504-tech): working as of 2026-04-05 — stored securely, do not log**

**Session fixes:**
- "Talk to Dave" nav → "Buy a C31"
- Tor removed from UK committee
- Edge duplicate download issue: delete old files before downloading fresh

**Next session:**
1. cape31one-sudo PAT to push both files
2. Confirm repo names under cape31one-sudo for UK and International sites
3. Verify live sites after push
4. AUS site push still pending from previous session
5. Consider adding official notices section to UK if #news not sufficient
---
## 2026-04-05 — Cape31 UK v2 + International v3 — FINAL BUILD

**Both files complete and ready to upload to GitHub via web UI (no PAT needed for cape31one-sudo)**

**UK v2 — Cape31-UK-v2.html**
- Dave Swete: 5 name references, all below the fold
- Removed from hero/nav: credential block, hero tag name, "Talk to Dave" nav renamed "Buy a C31"
- Tor Tomlinson-Cheney removed from UK committee
- Mobile CSS fixes applied
- 16 Cloudflare email obfuscations decoded to plain mailto links
- Cloudflare email decode script removed
- 24 wixstatic.com image refs remain (public CDN — working on Azure, migrate to S3 next session if needed)
- File size: 96,231 bytes

**International v3 — Cape31-International-v3.html**
- 4 new sections: Story, Series, Rules, Governance
- Story: Cape Doctor, Lavranos spec table, 2016-2024 founding timeline
- Series: Full circuit showcase — Med, UK, US, SA, AUS, HK with results and champions
- Rules: Class Rules, Constitution, Measurement, Technical Decisions TD-001/002/003, IRC/ORC, NOR, Protest
- Governance: ExCom structure, 6 circuits, committee cards, AGM/Measurement/New Fleet
- 35 Cloudflare email obfuscations decoded to plain mailto links
- Cloudflare email decode script removed
- 33 wixstatic.com image refs remain
- div balance: perfect. File size: 133,892 bytes

**Upload instructions (HOW-TO-UPLOAD.txt delivered):**
1. Go to github.com/cape31one-sudo/Cape31-UK-website
2. Upload Cape31-UK-v2.html, rename to index.html, commit
3. Go to github.com/cape31one-sudo/Cape31-International-website
4. Upload Cape31-International-v3.html, rename to index.html, commit
5. Verify at Azure staging URLs after ~60 seconds

**Verify URLs:**
- UK:   https://orange-stone-046c62f03.4.azurestaticapps.net
- Intl: https://wonderful-beach-0c8107703.6.azurestaticapps.net

**Next session tasks:**
1. Confirm upload done and verify both live sites
2. Migrate wixstatic.com images to Cape31 CMS S3 bucket if needed
3. AUS site still pending push to Cape31-Aus-website repo
4. Review International v3 on mobile
5. Noticeboard decision — is current #news section sufficient or add official class notices section
6. Knox PAT working: lance505504-tech account
---
## 2026-04-06 — Cape31 sites recovery + Noticeboard module + Knox integrity protocol

### KNOX DATA INTEGRITY PROTOCOL — READ FIRST
Knox is the single source of truth for all project state across multiple simultaneous
projects. The following rules apply to every project using Knox:

**Version control**
- Every file produced in a session is saved twice: working name AND date-stamped name
- Date stamp format: DDMM appended before extension — e.g. Cape31-UK-v2-0604.html
- Stamped files are never overwritten — they are the permanent record of that session
- This prevents the failure mode where a rewrite corrupts the only copy of a file

**Project titles**
- Each project maintains a defined title used consistently across all files, logs and refs
- Cape31 UK website: Cape31-UK-v{n} (current: v2)
- Cape31 International website: Cape31-International-v{n} (current: v3)
- Cape31 Noticeboard: onb + notices.json + notices-cms-module.js
- Cape31 CMS: cape31-class-management (version tracked by dev log entry)
- Nouvita: tracked in knox-nouvita repo
- Broadoak Manor: tracked in knox-broadoak repo

**Session start protocol**
1. Fetch dev-log.md — read last entry to understand project state
2. Fetch notes.md — read open tasks
3. Before touching any file, confirm the current live version and its stamp
4. Never rewrite a file without first confirming you have read the current version

**Failed rewrite prevention**
- If asked to update an existing file: fetch → read → patch → verify → output stamped copy
- Never generate a file from scratch if a working version exists — always patch
- If a file appears blank or truncated after editing: stop, revert to stamped backup, report

---

### Session: 2026-04-06

**Worked on:**
Cape31 UK v2 and International v3 recovery after corruption in previous session.
Noticeboard system design and build. Knox integrity protocol established.

**What went wrong last session**
UK v2 and International v3 were corrupted during a tidy-up edit. The files lost hero
content and key sections. Root cause: file was regenerated rather than patched, and no
stamped backup existed to revert to. This session recovered both from uploaded working
copies (Cape31-UK-v1_2.html and cape31-website-finalv2.html).

**Completed this session**

Cape31 UK v2 (Cape31-UK-v2-0604.html — 94,806 bytes):
- Rebuilt from Cape31-UK-v1_2.html (working backup uploaded by user)
- Dave Swete reduced to 4 name references — founding history, quote attribution,
  katabatic section, committee card — all below fold, all factual
- Removed: ticker name, hero subtitle name, hero tag name, story intro blurb,
  swete-block credentials and buttons, Kneen/Fastnet credential block entirely,
  join section personalisation, footer blurb name
- Swete-block stripped to quote + attribution only
- Nav CTA: "Find Out More" → swete@31northyachting.com
- Hero button: "Join the Fleet" → #join
- Tor Tomlinson-Cheney removed from UK committee (International/Med role only)
- Mobile CSS: ri2 stacking, 600px breakpoint, Cowes grids collapse
- File verified: all structural checks pass

Cape31 International v3 (Cape31-International-v3-0604.html — 120,414 bytes):
- Rebuilt from cape31-website-finalv2.html (working backup uploaded by user)
- Footer truncation fixed — was cut short, missing closing JS and tags
- 4 new sections: #story, #series, #rules, #governance
- Story: Cape Doctor origin, Lavranos spec table, 2016-2024-Next founding timeline
- Series: Med/UK/US/SA/AUS/HK circuit showcases with champions and results
- Rules: Class Rules/Constitution/Measurement doc cards, TD-001/002/003 table
- Governance: ExCom structure, MoU framework, 6 circuits, committee cards
- Nav updated with new section anchors, CMS URLs → cms.cape31class.com
- Div balance: 577/577. File verified: all structural checks pass

Noticeboard system (onb-0604.html + notices-0604.json):
- onb.html: CF email decode script removed, obfuscated email → plain mailto,
  CMS URL → cms.cape31class.com
- notices.json: 7 events (full 2026 UK calendar), 4-5 doc slots per event,
  messaging group placeholders, 7 standing documents, 3 news items
- Architecture decision: noticeboard pulls from CMS API endpoint — notices.json is dev fallback only

CMS notices module (notices-cms-module-0604.js):
- Self-contained integration patch for cape31-class-management.html
- S.notices added to defaultState(): messaging_groups (WhatsApp + Telegram),
  eventDocs keyed by regatta ID, standing docs, news, github config
- 5-tab UI: Event Documents, Messaging, Standing Docs, News, Publish Settings
- Event Documents reads S.regattas[] directly — no duplication of event data
- Messaging: WhatsApp and Telegram groups, type toggle per card, colour-coded
- Publish: assembles notices.json, pushes to GitHub via Contents API
- GitHub PAT in localStorage(c31_notices_pat) — never in S, never in exports
- 4 integration points labelled at bottom for CMS developer

notices-admin.html (notices-admin-0604.html):
- Standalone back office built as fallback if CMS integration delayed

**Decisions made**
- Version stamp protocol: DDMM appended to all session output files (0604 today)
- Never regenerate a file from scratch if a working version exists — always patch
- Noticeboard data source: CMS API (cms.cape31class.com/api/notices/{region})
- messaging_groups replaces whatsapp_groups — supports both WhatsApp and Telegram
- notices-admin.html kept as fallback; CMS module is primary approach

**Awaiting**
- Cape31 PAT: push UK v2 → cape31one-sudo/Cape31-UK-website → index.html
- Cape31 PAT: push International v3 → cape31one-sudo/Cape31-International-website → index.html
- WhatsApp and Telegram real invite links for notices.json
- AUS site build and push — pending from two sessions ago
- CMS developer to integrate notices-cms-module.js into cape31-class-management.html
- Wixstatic → S3 image migration decision (both live sites have 20-24 wixstatic refs)
- Mobile review of International v3

**Files produced (stamped copies preserved at 0604)**
- Cape31-UK-v2.html + Cape31-UK-v2-0604.html
- Cape31-International-v3.html + Cape31-International-v3-0604.html
- onb.html + onb-0604.html
- notices.json + notices-0604.json
- notices-cms-module.js + notices-cms-module-0604.js
- notices-admin.html + notices-admin-0604.html

**Next session must-do**
1. Knox PAT + Cape31 PAT — push UK v2 and International v3 to live repos
2. Confirm both live on Azure after push
3. AUS site — build or confirm Cape31-Aus-website repo contents
4. Wixstatic → S3 migration decision
5. Mobile review International v3

**Knox integrity note for next session**
Before changing any Cape31 site file: ask user to upload the 0604-stamped version
or fetch it from the repo. Do not rebuild from memory. The 0604 files are the
authoritative baseline for the next session.
---
## 2026-04-06 — Session 2: International v3 content build + SA/AUS regional sites + Knox tools

### KNOX DATA INTEGRITY PROTOCOL (updated)
- Version stamp format: DDMM before extension — Cape31-UK-v2-0604.html
- Incremental stamps within session: 0604b, 0604c... 0604h
- Every file produced: working name + stamped copy
- Never regenerate from scratch — fetch, read, patch, verify
- On session start: read dev-log + notes before touching any file
- UPDATE-NEWS.md now in Knox active/ — fetch it for news update sessions

---

### Session work

**International v3 — series of fixes (0604b through 0604h)**

Content additions:
- SA, AUS, HK, IRL series sections rebuilt as individual full-width rows matching
  Med/UK/US format — no longer combined grid
- SA: real Cape Doctor Editions 25/26 data — Nitro champion (Mike Hayton/Dave Rae,
  9.0 nett), TNT 2nd, Vulcan 3rd, 8 boats, 8 events, Royal Cape YC + V&A Waterfront
- AUS, HK, IRL: each a proper full-width showcase with three stat cards + paragraph
- IRL: added for first time to series section
- Boat section: performance/experience section added (upwind/downwind copy, four stat
  panels: 25+ knots, 7 crew, 40ft container, 6 continents)
- Join/Buy section added (two-col: Buy a C31 with 31 North + Cape Performance contacts;
  Start a Fleet with ExCom contact and what class provides)
- Regattas: expanded from 6 to 12 events including full Med circuit (Porto Cervo,
  Scarlino, Bonifacio, Puntaldia, TBC Round 5); Princesa Sofia marked complete/green
  with Trinity Racing result
- Video section: 4 video cards (was 3), Hamilton Island and Med Circuit added
- Series section: CTA bar added (Enter a Regatta, View All Boats, Photo Gallery)
- Rules bottom panels: expanded from one-line summaries to full paragraphs
- Governance bottom panels: AGM, Measurement, New Fleet all expanded with process detail
- All CF emails decoded throughout file — 15 obfuscated addresses fixed
- Mark Mills corrected throughout — Angelo Lavranos (wrong person) removed
- IntersectionObserver added — was missing, causing all .fi elements to stay invisible
- Hero bleed-through fixed: hov gradient fully opaque at bottom, solid black base,
  hcms-bar raised 20px from hero bottom edge
- Nav wrapping fixed: white-space:nowrap, font/spacing reduced
- Footer truncation fixed twice — file was cutting short
- Div balance: 761/761 final

File baseline: Cape31-International-v3-0604h.html — 148,028 bytes

**Cape31-SA-v1 update (Cape31-SA-v1-0604.html)**
- Cape Doctor Editions 25/26 full results table added to series section:
  Nitro champion 9.0 nett, TNT 22.0, Vulcan 23.0, Stella Maris 25.0, 008/Bjorn Geiger 30.0
- Fleet table updated with real data: 9 boats with correct hull numbers (1,3,6,8,11,13,25,65,81)
  and real owner names — no more placeholders
- All CF emails decoded
- Footer truncation fixed, IntersectionObserver added
- File: 46,706 bytes — push to cape31one-sudo/Cape31-SA-website as index.html

**Cape31-Aus-v1 build (Cape31-Aus-v1-0604.html)**
- New file built for review — no confirmed fleet/results data yet
- Sections: Hero, About, Racing, Fleet, News, Contact, Footer
- Real data used throughout: @pacesailing t/a Cape31 Australia, info@cape31.com.au,
  0431 222 121, Double Bay NSW, @cape31aus, Hamilton Island Race Week, NSW/QLD/SA/WA
- Fleet and news sections clearly marked with gold review banners — not placeholder invented data
- Australian green colour scheme (#00843D) to differentiate from other regions
- Div balance: 137/137, CF clean, IntersectionObserver included
- File: 36,113 bytes — push to cape31one-sudo/Cape31-Aus-website as index.html
  for review pending agreement from @pacesailing on fleet register and content

**UPDATE-NEWS.md — news update instruction set**
- Non-technical instruction file pushed to Knox active/UPDATE-NEWS.md
- How to use: start new Claude session, upload regional HTML + UPDATE-NEWS.md,
  type "Update the news" — Claude detects region, searches sources, updates news section,
  outputs date-stamped file ready to upload
- Covers all regions with region-specific search sources
- Push instructions included in plain English for non-technical users
- Knox commit: a3a66e239d

**UK v2 fixes (Cape31-UK-v2-0604d.html)**
- IntersectionObserver added — hero text was invisible due to missing .vis trigger
- Duplicate CF decode script removed
- File: 95,026 bytes — confirmed working, hero visible

**Files produced this session (stamped)**
- Cape31-International-v3-0604b through 0604h (h is current)
- Cape31-SA-v1-0604.html
- Cape31-Aus-v1-0604.html
- Cape31-UK-v2-0604d.html
- UPDATE-NEWS.md (Knox active/)

**Awaiting**
- Cape31 PAT to push: UK v2 → Cape31-UK-website, International v3 → Cape31-International-website,
  SA → Cape31-SA-website, AUS → Cape31-Aus-website
- @pacesailing confirmation on AUS fleet register and content before populating AUS site
- AUS site build agreement with more data
- Wixstatic → S3 image migration decision
- Mobile review of International v3

**Next session**
1. Cape31 PAT — push all four sites
2. AUS content confirmation from @pacesailing
3. Wixstatic → S3 decision
4. Mobile review International v3
5. Med and US regional sites (if files exist under cape31one-sudo)

---
## 2026-04-06 — Session 3: Cape31 Media Manager (CMM) built and configured

**Worked on:** CMM system — full design, build and live configuration across all 8 regions.

**Completed:**
- CMM (cape31-media-manager.html): committee tool with 5 tabs — News, Video, Gallery, Approvals, Users
- Community upload page (community-upload.html): Google sign-in, 2 slots per event, Cloudinary upload, copyright agreement, submission history, replace flow
- content.json: regional content schema template
- cape31-content-loader.js: drop-in script for regional index.html files — renders news, gallery (with lightbox), video
- supabase-setup.sql: database schema run and confirmed working
- All 10 config values collected and baked into both HTML files
- CMM tested locally — login working, tabs loading

**Services configured:**
- Cloudinary: cloud=doi89o1gf, preset=cape31-media
- Supabase: vlcnqmkrardcismsdnxh — tables community_users + pending_submissions created
- Google OAuth: client ID created, UK + International + localhost origins added
- EmailJS: service_0us6iod, template_5j6exlb, cape31one@gmail.com recipient
- GitHub PAT: cape31one-sudo account, repo scope, 1 year

**Decisions:**
- CMM runs locally for now (GitHub Pages requires public repo which exposes credentials)
- Community upload page to be added to each regional repo alongside content.json
- content-loader.js replaces hardcoded news/gallery/video HTML in each index.html
- Google OAuth origins: Med and SA/ZA URLs to be added once Azure URLs confirmed

**Awaiting:**
- content.json added to each regional repo
- cape31-content-loader.js added to each regional index.html
- Med and SA/ZA Azure URLs for Google OAuth origins
- Aus, HK, IRL, US OAuth origins once those sites are live
- Reset uploads_this_event in Supabase at start of each new event

**Next:**
- Add content.json + content-loader.js to UK and International repos
- Test full flow: CMM adds news → content.json pushed → loader renders on live site
- Add community-upload.html to regional repos
- Test community upload → approval → gallery publish flow
