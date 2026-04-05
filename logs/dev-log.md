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
