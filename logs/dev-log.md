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
