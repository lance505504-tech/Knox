# Project Notes

## Knox Integrity Protocol
- Version stamp: DDMM + incremental letter — e.g. Cape31-UK-v2-0604d.html
- Session start: read dev-log last entry + notes before touching any file
- Never regenerate from scratch — fetch, read, patch, verify, stamp
- UPDATE-NEWS.md now in Knox active/ — use it for news update sessions

## News Update Tool
- File: active/UPDATE-NEWS.md (Knox repo)
- How to use: Claude session → upload regional HTML + UPDATE-NEWS.md → type "Update the news"
- Claude detects region, searches, updates news section, outputs stamped file
- No technical knowledge needed

## Project Baselines (as of end of session 2 — 0604)

### Cape31 Sites — READY TO PUSH (need Cape31 PAT)
- UK v2: Cape31-UK-v2-0604d.html — hero fix applied — push to Cape31-UK-website
- International v3: Cape31-International-v3-0604h.html — push to Cape31-International-website
- SA v1: Cape31-SA-v1-0604.html — push to Cape31-SA-website
- AUS v1: Cape31-Aus-v1-0604.html — HOLDING for review — push to Cape31-Aus-website
  (awaiting content confirmation from @pacesailing before final population)

### Live URLs
- UK: https://orange-stone-046c62f03.4.azurestaticapps.net
- International: https://wonderful-beach-0c8107703.6.azurestaticapps.net

## Open Tasks
- [ ] Cape31 PAT — push UK v2, International v3, SA v1, AUS v1 to live repos
- [ ] AUS content confirmation from @pacesailing (fleet register, results, committee)
- [ ] Wixstatic → S3 image migration decision (20-24 wixstatic refs per site)
- [ ] Mobile review of International v3
- [ ] Med regional site — check if Cape31-Med-website repo exists under cape31one-sudo
- [ ] US regional site — check if Cape31-US-website repo exists under cape31one-sudo
- [ ] Knox PAT renewal — check expiry of current token before next session

## Decisions Made
- AUS site: green (#00843D), held for review, fleet/news sections marked pending
- Noticeboard: CMS API endpoint (cms.cape31class.com/api/notices/{region})
  notices.json is dev fallback — notices-cms-module-0604.js ready for CMS integration
- messaging_groups: supports WhatsApp and Telegram (type field per group)
- UPDATE-NEWS.md: non-technical instruction for news updates — stored in Knox active/

## Links
- UK live: https://orange-stone-046c62f03.4.azurestaticapps.net
- International live: https://wonderful-beach-0c8107703.6.azurestaticapps.net
- Knox repo: https://github.com/lance505504-tech/Knox
- Cape31 repos: github.com/cape31one-sudo/[repo-name]
- AUS class site: https://www.cape31.com.au
- SA class site: https://sa.cape31.com
- UPDATE-NEWS.md: https://raw.githubusercontent.com/lance505504-tech/Knox/main/active/UPDATE-NEWS.md
