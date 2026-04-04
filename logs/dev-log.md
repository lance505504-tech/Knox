# Development Log

---

## 2026-04-04 — Knox initialised
**Worked on:** Repository created and configured via knox-setup.py
**Files created:** All core files, folder structure, GitHub Actions, GitHub Pages
**Next:** Sign in to Knox, set up team members, create first project

---

## 2026-04-04 — Cape31 Website & Hosting — Full Day Session

### Sites Built
- **Cape31-International-v2.html** — Main class website. Hero slideshow, news ticker, UK card spans 2 cols with Union Jack animation, US card spans 2 cols with Stars & Stripes, 7 regions grid, CMS bar (moved to bottom of hero, then moved to full-width band between hero and stats), The Boat, 2026 calendar, fleet register, partners, footer
- **Cape31-UK-v1.html** — UK regional. Hero: "Tough. Engaging. The Solent." Dave Swete as circuit director, 2026 calendar, 29-boat fleet, results, media gallery (6 photos + 5 videos + lightbox), measurement documents, fixed bottom-left All Regions button
- **Cape31-US-v1.html** — US regional. Hero: "Show Up. Win. Two Coasts. One Class." Pacific Yankee, ORC/IRC wins, two-coast structure, media gallery, fixed back button
- **Cape31-EU-v1.html** — Med regional. Hero: "Voilà. La Circuit." Gold accent, 21 teams, 5-event 2026 circuit, media gallery, fixed back button. Domain: med.cape31class.org
- **Cape31-SA-v1.html** — South Africa regional. Hero: "The Doctor Dictates." Green accent. Full origin story — Lord Laidlaw, Davey James, Stephen du Toit, Mark Mills, Elian Perch, Bjorn Geiger. Cape Doctor section, Summer in the South series, build stats, fleet table, visit section
- **Cape31-UK-ONB-v1.html** — UK Online Notice Board (loads notices.json)
- **Cape31-UK-Admin-v1.html** — UK admin panel, password: Cape31UK2026
- **notices-uk.json** — UK notice board content

### Regional Hero Headlines (final)
- SA: **The Doctor Dictates.**
- UK: **Tough. Engaging. The Solent.**
- US: **Show Up. Win. Two Coasts. One Class.**
- Med: **Voilà. La Circuit.**

### GitHub Repos (all private, account: cape31one-sudo)
- cape31-website → cape31class.org
- cape31-uk-website → uk.cape31class.org (+ onb.html + admin.html + notices.json)
- cape31-us-website → us.cape31class.org
- Cape31-Med-website → med.cape31class.org
- Cape31-SA-website → sa.cape31class.org (staging: thankful-flower-0bf3a5703.4.azurestaticapps.net)

### Azure Static Web Apps (Resource Group: Cape31-class)
| App | Staging URL | Custom Domain | Status |
|---|---|---|---|
| cape31-website | wonderful-beach-0c8107703.6.azurestaticapps.net | cape31class.org | ✅ Live |
| cape31-uk-website | orange-stone-046c62f03.4.azurestaticapps.net | uk.cape31class.org | ✅ Live |
| cape31-us-website | ambitious-cliff-034848303.2.azurestaticapps.net | us.cape31class.org | ✅ Live |
| Cape31-Med-website | ashy-bay-004cb4c03.2.azurestaticapps.net | med.cape31class.org | ✅ Live |
| Cape31-SA-website | thankful-flower-0bf3a5703.4.azurestaticapps.net | sa.cape31class.org | ⏳ Validating |

### DNS — The Full Story
**The problem:** cape31class.org was registered at 123-reg but DNS was controlled by an orphaned Cloudflare account (gail/eric nameservers) set up by the original developer. Anything added to 123-reg was ignored. This took several hours to diagnose.

**The solution:**
1. Created new Cloudflare account (Lance505504@gmail.com)
2. Added cape31class.org — Cloudflare assigned stevie/johnathan nameservers
3. Set nameservers at 123-reg to stevie/johnathan
4. Added all DNS records in Cloudflare — A record for root, CNAMEs for uk/us/med/sa, TXT records for Azure validation
5. Sites came live through stevie/johnathan
6. Later discovered Cloudflare reassigned nameservers to henry/ruth for the account
7. Updated 123-reg to henry/ruth
8. All records confirmed correct in Cloudflare — account showing Pending (normal, up to 24hrs)

**Current Cloudflare DNS records (cape31class.org):**
- A: `@` → `20.29.155.69` (DNS only)
- CNAME: `uk` → `orange-stone-046c62f03.4.azurestaticapps.net` (DNS only)
- CNAME: `us` → `ambitious-cliff-034848303.2.azurestaticapps.net` (DNS only)
- CNAME: `med` → `ashy-bay-004cb4c03.2.azurestaticapps.net` (DNS only)
- CNAME: `sa` → `thankful-flower-0bf3a5703.4.azurestaticapps.net` (DNS only)
- TXT: `asuid` → `_kbinddbon2j31020gw4hvh11mz7k2rt`
- TXT: `asuid.sa` → `_ws9r80djz5ba6ande9fc8d27athpe3o`

**123-reg nameservers (confirmed):** henry.ns.cloudflare.com / ruth.ns.cloudflare.com
**Cloudflare account status:** Pending (awaiting internal verification — sites working fine)

### Key Fixes Applied This Session
- CMS bar moved out of hero into full-width band between hero and stats
- All proud-pebble staging URLs replaced with cms.cape31class.com (38 instances)
- Flag emojis removed from hero (Windows renders them as GB/US text not flags)
- YouTube embeds switched to youtube-nocookie.com for better compatibility
- UK and US cards on main site forced to span 2 columns with inline styles
- All Regions back button moved from top-right nav to fixed bottom-left on all regional sites
- YAML skip_app_build: true confirmed in all GitHub workflow files
- Med site consistently named med.cape31class.org (not eu.)

### Pending — Next Session
1. ⏳ SA domain validation — sa.cape31class.org still validating in Azure
2. ⏳ Cloudflare account activation — henry/ruth pending verification
3. ⏳ Upload SA site to Cape31-SA-website GitHub repo
4. ⏳ Confirm video rights with Tor Tomlinson-Cheney
5. ⏳ Add media section to Cape31-International-v2.html (main site)
6. ⏳ ExCom approval before public announcement
7. ⏳ CMS custom domain: cms.cape31class.org
8. ⏳ Phase 2: CMS integration with Tom/TTC Marine (CORS, API endpoints)
9. ⏳ Build Cape31-HK-v1.html and Cape31-AUS-v1.html
10. ⏳ Update Knox repository.json with all current project state
