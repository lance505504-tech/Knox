# Project Notes

## Knox Integrity Protocol
- Version stamp format: DDMM before extension — e.g. Cape31-UK-v2-0604.html
- Every session: output working file AND stamped copy
- Never regenerate a file from scratch if a working version exists — fetch, read, patch
- On session start: read dev-log last entry + notes before touching any file

## Project Baselines (as of 0604)
- Cape31 UK: Cape31-UK-v2-0604.html — 94,806 bytes — READY TO PUSH
- Cape31 International: Cape31-International-v3-0604.html — 120,414 bytes — READY TO PUSH
- Cape31 Noticeboard: onb-0604.html + notices-0604.json — READY TO DEPLOY
- Cape31 CMS Notices module: notices-cms-module-0604.js — READY TO INTEGRATE
- Cape31 Notices admin fallback: notices-admin-0604.html

## Open Tasks
- [ ] Cape31 PAT — push UK v2 to cape31one-sudo/Cape31-UK-website → index.html
- [ ] Cape31 PAT — push International v3 to cape31one-sudo/Cape31-International-website → index.html
- [ ] Confirm both live on Azure after push
- [ ] AUS site — build or check Cape31-Aus-website repo (pending 2 sessions)
- [ ] Wixstatic → S3 image migration — both live sites have 20-24 wixstatic refs
- [ ] Mobile review of International v3
- [ ] CMS developer: integrate notices-cms-module-0604.js into cape31-class-management.html
- [ ] WhatsApp and Telegram real invite links for notices.json
- [ ] Knox PAT renewal reminder: current PAT ghp_xrA0... — check expiry before next session

## Decisions Made
- Nav CTA on UK site: "Find Out More" (links swete@31northyachting.com)
- Hero button on UK site: "Join the Fleet" (links #join)
- Noticeboard data source: CMS API endpoint (cms.cape31class.com/api/notices/{region})
  notices.json is dev fallback only
- messaging_groups model supports WhatsApp and Telegram (type field per group)
- Separate notices-admin.html kept as fallback if CMS integration delayed

## Links
- UK live: https://orange-stone-046c62f03.4.azurestaticapps.net
- International live: https://wonderful-beach-0c8107703.6.azurestaticapps.net
- Knox repo: https://github.com/lance505504-tech/Knox
- Cape31 repos: github.com/cape31one-sudo/[Cape31-UK-website | Cape31-International-website | Cape31-Aus-website]
