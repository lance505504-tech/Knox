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

### Cape31 Sites
- [ ] Cape31 PAT — push UK v2, International v3, SA v1, AUS v1 to live repos
- [ ] AUS content confirmation from @pacesailing (fleet register, results, committee)
- [ ] Wixstatic → S3 image migration decision (20-24 wixstatic refs per site)
- [ ] Mobile review of International v3
- [ ] Med regional site — check if Cape31-Med-website repo exists under cape31one-sudo
- [ ] US regional site — check if Cape31-US-website repo exists under cape31one-sudo

### CMM Next Steps
- [ ] Add content.json to UK and International repos (copy template, set region field)
- [ ] Add cape31-content-loader.js to UK and International index.html
- [ ] Replace hardcoded news/gallery/video HTML with loader div containers
- [ ] Test full flow: CMM adds news → content.json pushed → renders on live site
- [ ] Add community-upload.html to regional repos
- [ ] Test community upload → approval → gallery publish flow
- [ ] Add Med and SA/ZA Azure URLs to Google OAuth authorised origins
- [ ] Add Aus/HK/IRL/US OAuth origins once those sites go live
- [ ] Reset uploads_this_event in Supabase at start of each new event (SQL: UPDATE community_users SET uploads_this_event = 0)

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
- Noticeboard: CMS API endpoint (cms.cape31class.com/api/notices/{region})
- messaging_groups: supports WhatsApp and Telegram (type field per group)

## Links
- UK live: https://orange-stone-046c62f03.4.azurestaticapps.net
- International live: https://wonderful-beach-0c8107703.6.azurestaticapps.net
- Knox repo: https://github.com/lance505504-tech/Knox
- Cape31 repos: github.com/cape31one-sudo/[repo-name]
- UPDATE-NEWS.md: https://raw.githubusercontent.com/lance505504-tech/Knox/main/active/UPDATE-NEWS.md
