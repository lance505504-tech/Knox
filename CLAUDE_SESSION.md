Knox Session File
<!-- Attach this file and type "load session" to begin -->
On Session Start
Fetch these URLs in order before responding to anything:
https://raw.githubusercontent.com/lance505504-tech/Knox/main/repository.json
https://raw.githubusercontent.com/lance505504-tech/Knox/main/logs/dev-log.md
https://raw.githubusercontent.com/lance505504-tech/Knox/main/active/notes.md
https://raw.githubusercontent.com/lance505504-tech/Knox/main/backups/manifest.json
After fetching all four, confirm what was loaded and the date of the last dev log entry, then ask what to work on.
System
Name: Knox -- Lances-Team
Repo: https://github.com/lance505504-tech/Knox
Nouvita repo: https://github.com/lance505504-tech/knox-nouvita
Broadoak repo: https://github.com/lance505504-tech/knox-broadoak
Sign-in: https://lance-knox.netlify.app
Team
Name	Role
Lance	Owner
Elliot Adams	Admin -- Nouvita
Harriet Anstey	Admin -- Nouvita
Jessica Lepodevin	Admin -- Broadoak Manor
Charlotte Whay	Admin -- Broadoak Manor
Amelia Adams	Admin -- Broadoak Manor
Nicola White	Admin -- Broadoak Manor
Backup Access
To show or restore backups, fetch:
https://raw.githubusercontent.com/lance505504-tech/Knox/main/backups/manifest.json
List versions newest first. Always confirm before restoring. Restoring is non-destructive -- current version is saved first.
Working Rules
Fetch from the URLs above -- never ask for local file uploads
At session end output a single knox-update.py with all updated file contents baked in
Append a dev log entry to logs/dev-log.md at session end
Keep responses focused
File Update Rules
Use knox-update.py to push files -- never PowerShell scripts
At session end Claude generates one knox-update.py with content baked in -- download and run, one command
Delete knox-update.py after confirmed push -- files left on C: drive risk being overwritten by other sessions
Project Context
Knox is Lances-Team's development workspace. It manages procedures, references, development logs and team knowledge across three organisations -- Lances-Team, Nouvita and Broadoak Manor. Each organisation has its own Knox repository. Personal data is never stored in Knox -- it goes in private repositories.
