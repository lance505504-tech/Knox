import os, json, base64, urllib.request, urllib.error, subprocess
from datetime import datetime

token = os.environ['GH_TOKEN']
repo  = os.environ['REPO']
api   = f'https://api.github.com/repos/{repo}/contents'

def gh(method, path, body=None):
    req = urllib.request.Request(
        f'{api}/{path}', method=method,
        data=json.dumps(body).encode() if body else None)
    req.add_header('Authorization', f'token {token}')
    req.add_header('Accept', 'application/vnd.github.v3+json')
    req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read()), r.status
    except urllib.error.HTTPError as e:
        return json.loads(e.read().decode() or '{}'), e.code

def put_file(path, content_bytes, msg):
    existing, code = gh('GET', path)
    body = {
        'message': msg + ' [skip ci]',
        'content': base64.b64encode(content_bytes).decode()
    }
    if code == 200 and 'sha' in existing:
        body['sha'] = existing['sha']
    res, code = gh('PUT', path, body)
    if code in (200, 201):
        print(f'  OK: {path}')
    else:
        print(f'  SKIP: {path} — {res.get("message","")}')

def list_dir(path):
    res, code = gh('GET', path)
    if code == 200 and isinstance(res, list):
        return [f['name'] for f in res if f['type'] == 'file']
    return []

def delete_file(path):
    existing, code = gh('GET', path)
    if code == 200 and 'sha' in existing:
        gh('DELETE', path, {
            'message': f'knox: prune {path} [skip ci]',
            'sha': existing['sha']
        })
        print(f'  pruned: {path}')

# Get changed files
r = subprocess.run(
    ['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'],
    capture_output=True, text=True)
if r.returncode != 0 or not r.stdout.strip():
    r = subprocess.run(
        ['git', 'show', '--name-only', '--pretty=format:', 'HEAD'],
        capture_output=True, text=True)
changed = [f for f in r.stdout.strip().split('\n') if f]
ts = datetime.utcnow().strftime('%Y-%m-%d-%H%M%S')
print(f'Changed files: {changed}')

# Back up tracked files
mapping = {
    'repository.json': f'backups/repository/{ts}.json',
    'logs/dev-log.md': f'backups/dev-log/{ts}.md',
    'active/notes.md': f'backups/notes/{ts}.md',
}
for src, dst in mapping.items():
    if src in changed and os.path.exists(src):
        with open(src, 'rb') as f:
            put_file(dst, f.read(), f'knox: backup {src}')

# Back up any other active/* files
for src in changed:
    if src.startswith('active/') and src not in mapping and os.path.exists(src):
        name = src.replace('active/', '').replace('/', '-')
        with open(src, 'rb') as f:
            put_file(f'backups/active/{ts}-{name}', f.read(), f'knox: backup {src}')

# Prune each folder to 30
MAX = 30
for folder in ['backups/repository', 'backups/notes', 'backups/dev-log', 'backups/active']:
    for old in sorted(list_dir(folder), reverse=True)[MAX:]:
        delete_file(f'{folder}/{old}')

# Update manifest
m = {'generated': datetime.utcnow().isoformat() + 'Z', 'folders': {}}
for d in ['repository', 'notes', 'dev-log', 'active']:
    vs = sorted(list_dir(f'backups/{d}'), reverse=True)
    m['folders'][d] = {'count': len(vs), 'newest': vs[0] if vs else None, 'versions': vs}
put_file('backups/manifest.json', json.dumps(m, indent=2).encode(), 'knox: update manifest')
print('Done.')
