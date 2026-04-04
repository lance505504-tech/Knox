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
