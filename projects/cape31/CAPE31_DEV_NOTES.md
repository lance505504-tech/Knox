<!-- KNOX VERSION — credentials sanitised. Store passwords in your password manager, not in Knox. -->

# Cape 31 CMS — Development Environment Reference

## URLs
| Environment | URL | GitHub Repo |
|---|---|---|
| **Production** | https://proud-pebble-0896e5503.2.azurestaticapps.net | cape31one-sudo/Cape31-azure |
| **Development** | https://polite-bay-0d57fd203.6.azurestaticapps.net | cape31one-sudo/Cape31-Development |

## Local Folders
| Environment | Folder |
|---|---|
| Production | `C:\Cape31\` |
| Development | `C:\Cape31\Development\` |

## Deploy Commands

### Development
```powershell
cd C:\Cape31\Development
copy cape31-class-management.html index.html
git add .
git commit -m "your message here"
git push -f https://cape31one-sudo:TOKEN@github.com/cape31one-sudo/Cape31-Development.git master:main
```

### Production (only after dev confirmed working)
```powershell
cd C:\Cape31
copy cape31-class-management.html index.html
git add .
git commit -m "your message here"
git push -f https://cape31one-sudo:TOKEN@github.com/cape31one-sudo/Cape31-azure.git master:main
```

## Audit Tool
Run before every deploy:
```powershell
python3 cape31_audit.py cape31-class-management.html
```
Must show **✓ ALL CLEAR** before pushing anywhere.

Also run Node syntax check:
```powershell
# Extract JS and check (in bash/WSL)
node --check index.html  # won't work directly but audit covers this
```

---

## GitHub Tokens
- Tokens expire / get revoked — generate fresh at https://github.com/settings/tokens
- Needs scopes: **repo** + **workflow**
- Never leave tokens visible in chat — revoke immediately after sharing

---

## Azure Workflow File — CRITICAL

**This is the working workflow format. Do not change it.**

The key differences from Azure's default that caused hours of problems:
- Uses **OIDC authentication** (`github_id_token`) — required by this Azure setup
- `output_location: ""` — NOT `/` and NOT `.`
- `skip_app_build: true` — we have no build step, pure static files
- No `api_location` needed

### Production workflow (C:\Cape31\.github\workflows\azure-static-web-apps-proud-pebble-0896e5503.yml)
```yaml
name: Azure Static Web Apps CI/CD
on:
  push:
    branches:
      - main
jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v3
        with:
          submodules: true
      - name: Install OIDC Client from Core Package
        run: npm install @actions/core@1.6.0 @actions/http-client
      - name: Get Id Token
        uses: actions/github-script@v6
        id: idtoken
        with:
          script: |
            const coredemo = require('@actions/core')
            return await coredemo.getIDToken()
          result-encoding: string
      - name: Build And Deploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN_PROUD_PEBBLE_0896E5503 }}
          action: upload
          app_location: /
          output_location: ""
          skip_app_build: true
          github_id_token: ${{ steps.idtoken.outputs.result }}
```

### Development workflow (C:\Cape31\Development\.github\workflows\azure-static-web-apps-polite-bay-0d57fd203.yml)
```yaml
name: Azure Static Web Apps CI/CD
on:
  push:
    branches:
      - main
jobs:
  build_and_deploy_job:
    runs-on: ubuntu-latest
    name: Build and Deploy Job
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v3
        with:
          submodules: true
      - name: Install OIDC Client from Core Package
        run: npm install @actions/core@1.6.0 @actions/http-client
      - name: Get Id Token
        uses: actions/github-script@v6
        id: idtoken
        with:
          script: |
            const coredemo = require('@actions/core')
            return await coredemo.getIDToken()
          result-encoding: string
      - name: Build And Deploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN_POLITE_BAY_0D57FD203 }}
          action: upload
          app_location: /
          output_location: ""
          skip_app_build: true
          github_id_token: ${{ steps.idtoken.outputs.result }}
```

---

## Login Credentials
| User | Email | Password | Role |
|---|---|---|---|
| Lance Adams | [email — secure store] | [password — secure store] | Admin |
| Dave Swete | [email — secure store] | [password — secure store] | Admin |
| Demo | TRY DEMO button | — | Admin (isolated) |

---|---|---|---|
| Lance Adams | [email — secure store] | [password — secure store] | Admin |
| Dave Swete | [email — secure store] | [password — secure store] | Admin |
| Demo | TRY DEMO button | — | Admin (isolated) |

---

## Storage Keys
| Key | Purpose |
|---|---|
| `c31_cms_v1` | Main app data (localStorage) |
| `cape31_users_v1` | Shared user store |
| `cape31_buttons_v3` | Sail button data |
| `cape31_demo_v1` | Demo mode app data |
| `cape31_demo_buttons_v1` | Demo mode button data |

---

## Key Technical Notes
- `HAS_CLOUD = false` — Azure deployment, localStorage only (no cloud storage)
- Single HTML file app — all HTML, CSS and JS in one file
- Always download working file from Claude chat, never from live site (Cloudflare obfuscates emails)
- Audit tool: `python3 cape31_audit.py cape31-class-management.html`
- Node syntax check: extract JS and run `node --check`

---

## Common Problems & Fixes

### Login not working
- Check emails in `defaultState()` — Cloudflare obfuscation wipes them
- Check `[email — secure store]` is present in the JS
- Seed user injection re-adds them on startup

### doLogin / doDemoLogin not defined
- Always a JS syntax error stopping script parse
- Run audit tool — check braces, backticks, broken escape sequences
- Common culprit: `\\'` inside single-quoted strings in onclick handlers

### renderStats crash after login
- `stats-bar` element not in mobile UI — add null guard
- `var statsEl = document.getElementById('stats-bar'); if(statsEl) statsEl.innerHTML = ...`

### Azure deployment token invalid
- Get fresh token from Azure Portal → Static Web App → Overview → Manage deployment token
- Update GitHub secret immediately
- Workflow must use OIDC format (see above) — Azure's default workflow is wrong for this setup
