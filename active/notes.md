# Cape31 Project — Active Notes

## Current Status (4 April 2026 — end of session)

### Sites Live
| URL | Status |
|---|---|
| https://cape31class.org | ✅ Live |
| https://uk.cape31class.org | ✅ Live |
| https://us.cape31class.org | ✅ Live |
| https://med.cape31class.org | ✅ Live |
| https://uk.cape31class.org/onb | ✅ Live |
| https://sa.cape31class.org | ⏳ Domain validating |

### Staging URLs
| App | Staging URL |
|---|---|
| International | https://wonderful-beach-0c8107703.6.azurestaticapps.net |
| UK | https://orange-stone-046c62f03.4.azurestaticapps.net |
| US | https://ambitious-cliff-034848303.2.azurestaticapps.net |
| Med | https://ashy-bay-004cb4c03.2.azurestaticapps.net |
| SA | https://thankful-flower-0bf3a5703.4.azurestaticapps.net |
| CMS | https://proud-pebble-0896e5503.2.azurestaticapps.net |

### DNS Infrastructure
- **Registrar:** 123-reg (Lance Adams account)
- **DNS:** Cloudflare (Lance505504@gmail.com account)
- **Nameservers at 123-reg:** henry.ns.cloudflare.com / ruth.ns.cloudflare.com
- **Cloudflare status:** Pending activation (sites working fine, just internal verification)
- **Zone ID:** 074a1e68426c3f40bb4f184b0c201ad3
- **Account ID:** c7fa62bb41d0f9346df334899046757e

### Azure Validation TXT Records
- Main: `asuid` → `_kbinddbon2j31020gw4hvh11mz7k2rt`
- SA: `asuid.sa` → `_ws9r80djz5ba6ande9fc8d27athpe3o`

## Local File Register
All files saved at: `C:\cape31\Website Development\Current Web HTML and docs`

| Local File | GitHub Repo | GitHub Filename | Status |
|---|---|---|---|
| Cape31-International-v2.html | cape31-website | index.html | ✅ Deployed |
| Cape31-UK-v1.html | cape31-uk-website | index.html | ✅ Deployed |
| Cape31-UK-ONB-v1.html | cape31-uk-website | onb.html | ✅ Deployed |
| Cape31-UK-Admin-v1.html | cape31-uk-website | admin.html | ✅ Deployed |
| notices-uk.json | cape31-uk-website | notices.json | ✅ Deployed |
| Cape31-US-v1.html | cape31-us-website | index.html | ✅ Deployed |
| Cape31-EU-v1.html | Cape31-Med-website | index.html | ✅ Deployed |
| Cape31-SA-v1.html | Cape31-SA-website | index.html | ✅ Deployed |

## Design System

### Regional Identity
| Region | Accent | Hero Headline | Domain |
|---|---|---|---|
| International | #ED1C24 | CAPE31. | cape31class.org |
| UK | #C8102E | Tough. Engaging. The Solent. | uk.cape31class.org |
| US | #B22234 | Show Up. Win. Two Coasts. One Class. | us.cape31class.org |
| Med | #D4A017 | Voilà. La Circuit. | med.cape31class.org |
| SA | #2a7a3b | The Doctor Dictates. | sa.cape31class.org |

### Brand Rules
- Always: **Cape31** or **C31** — never in full words, never lowercase
- Font body: Ubuntu | Font display: Barlow Condensed
- Brand red: #ED1C24 (confirmed from SVG logo)
- Association name: Cape31 International Class Association
- Ireland is the seventh region — always include

### Media Policy
Use all available class media with attribution. Seek forgiveness approach.
Rights challenges to team@cape31class.com
Photographers: Rick Tomlinson, Paul Wyeth, Howevideography/Jonathan Howe
Video rights: pending confirmation with Tor Tomlinson-Cheney

## Key Contacts
| Role | Contact |
|---|---|
| Class Association | team@cape31class.com |
| CMS Developer | tom@ttcmarine.com |
| EU/Med & Media | tor@thirtyoneracecircuit.com |
| UK Circuit Director | Dave Swete — swete@31northyachting.com |
| US Class Rep | Drew Freides — drew.freides@ubs.com |
| SA Class Chair | Bjorn Geiger |

## Known Issues / Watch List
- Cloudflare "Pending" — will resolve within 24hrs, sites working fine
- SA domain still validating in Azure — TXT record in place, just needs time
- Flag emojis don't render on Windows — removed from hero sections
- YouTube embeds switched to youtube-nocookie.com — monitor if videos open correctly
- UK/US cards on main site — forced span 2 with inline styles, monitor rendering

## Phase 2 — CMS Integration (with Tom/TTC Marine)
- Add CORS config to CMS Azure Static Web App
- Build API endpoints: /api/news, /api/regattas, /api/boats, /api/results
- Replace all cms.cape31class.com staging refs with cms.cape31class.org once domain connected
- Regional admin logins per region
- Stripe configuration for membership payments
