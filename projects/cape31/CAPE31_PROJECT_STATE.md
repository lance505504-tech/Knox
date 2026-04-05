<!-- KNOX VERSION — credentials sanitised. Store passwords in your password manager, not in Knox. -->

# Cape 31 International Class Association — Project State
**Last updated: 1 Apr 2026**

---

## PASTE THIS AT THE TOP OF EVERY NEW CONVERSATION

> "This is the Cape 31 Class Association management system project state. Read fully before doing anything.
> Live URL: https://proud-pebble-0896e5503.2.azurestaticapps.net
> GitHub: github.com/cape31one-sudo/Cape31-azure (private)
> Local files: C:\cape31
> Deploy: git add . && git commit -m "message" && git push -f origin master:main"

---

## Accounts
| Service | Account | Notes |
|---|---|---|
| Azure | Cape31one@gmail.com | Free tier Static Web App |
| GitHub | cape31one-sudo | Private repo Cape31-azure |

## Live URL
https://proud-pebble-0896e5503.2.azurestaticapps.net

## Login Credentials
| User | Email | Password | Role |
|---|---|---|---|
| Lance Adams | [email redacted] | [see secure store] | admin |
| Dave Swete | [email redacted] | [see secure store] | admin |

---

## Architecture — SINGLE FILE APP
One file: cape31-class-management.html (245KB)
- No separate auth page
- No separate sail register
- Login screen built into the app
- Session stored in localStorage (cape31_session_v1)
- Sail button data stored in localStorage (cape31_buttons_v3)

## Files in C:\cape31
| File | Size | Purpose |
|---|---|---|
| cape31-class-management.html | 245KB | The entire app |
| index.html | 245KB | Copy of above — Azure serves this as default |
| staticwebapp.config.json | 1KB | Azure routing config |
| .github/workflows/ | — | GitHub Actions deployment |

## Tabs in the App
Fleet · Class Fees · Regattas · Entries & Crew · Race Management · Results · 🔵 Sail Buttons · 💳 Payments · Admin

---

## Sail Button Register (built-in tab)
Sub-tabs: Fleet · Button Register · My Buttons · Settings

Data included:
- BOATS_SEED: ~50 boats from original SR
- BOAT_BUTTONS: 78KB of button history (all hulls 2025/2026)
- Data persists in localStorage

## Outstanding Items

### P1 — Verify data completeness
- [ ] Check all boats are in BOATS_SEED (compare against original SR)
- [ ] Check all BOAT_BUTTONS entries are correct and complete
- [ ] Test sail button allocation workflow end-to-end

### P2 — Login security
- [ ] Add password hashing (currently plaintext [password — secure store])
- [ ] Add proper session expiry handling

### P3 — Features to build out
- [ ] Class Fees tab — payment tracking
- [ ] Regattas tab — event management
- [ ] Entries & Crew tab
- [ ] Race Management tab
- [ ] Results tab
- [ ] Payments tab (Stripe integration)

### P4 — Nice to have
- [ ] Custom domain (cape31class.com or similar)
- [ ] Email notifications for access requests
- [ ] Member self-service password reset

---

## How to Deploy Updates
1. Edit cape31-class-management.html
2. Copy to index.html: `copy cape31-class-management.html index.html`
3. Push:
```
cd C:\cape31
git add .
git commit -m "description of change"
git push -f origin master:main
```
4. GitHub Actions deploys automatically (~60 seconds)

---

## Next Session — Start Here
1. Read this file fully
2. Check live site is still working
3. Verify boat and sail button data completeness
4. Ask Lance what to prioritise next
