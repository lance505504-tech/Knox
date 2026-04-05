#!/usr/bin/env python3
"""
Cape 31 CMS — Auto-backup script
Run before making any changes to cape31-class-management.html
Usage: python3 cape31_backup.py [optional label]
"""
import shutil, os, re, sys
from datetime import datetime

SRC   = '/mnt/user-data/outputs/cape31-class-management.html'
BKDIR = '/mnt/user-data/outputs/backups'
os.makedirs(BKDIR, exist_ok=True)

label = sys.argv[1].replace(' ','_') if len(sys.argv) > 1 else 'auto'
stamp = datetime.now().strftime('%Y%m%d_%H%M')
tag   = f'{stamp}_{label}'

with open(SRC) as f:
    cm = f.read()

# HTML snapshot
html_bk = f'{BKDIR}/cape31_{tag}_clean.html'
shutil.copy(SRC, html_bk)

# Seed data extraction
js = cm[cm.find('<script>')+8:cm.rfind('</script>')]

def grab(pattern, text):
    m = re.search(pattern, text, re.DOTALL)
    return m.group(1) if m else '// Not found'

blocks = {
    'BOATS':    grab(r'(S\.boats\s*=\s*\[[\s\S]{50,}?\];)', js),
    'USERS':    grab(r'(S\.users\s*=\s*\[[\s\S]{50,}?\];)', js),
    'REGATTAS': grab(r'(S\.regattas\s*=\s*\[[\s\S]{50,}?\];)', js),
    'SPONSORS': grab(r'(S\.sponsors\s*=\s*\[[\s\S]{10,}?\];)', js),
}

bi = js.find('var SR_BOAT_BUTTONS')
bj = js.find('\nfunction ', bi+1) if bi >= 0 else -1
blocks['BUTTONS'] = js[bi:bj].strip() if bi >= 0 and bj > bi else '// Not found'

lines = [f'// Cape 31 CMS Seed Data — {datetime.now().strftime("%Y-%m-%d %H:%M")} [{label}]']
for k, v in blocks.items():
    lines.append(f'\n// ── {k} {"─"*(60-len(k))}')
    lines.append(v)

js_bk = f'{BKDIR}/cape31_{tag}_seeddata.js'
with open(js_bk, 'w') as f:
    f.write('\n'.join(lines))

# Update LATEST
shutil.copy(SRC,   f'{BKDIR}/cape31_LATEST_clean.html')
shutil.copy(js_bk, f'{BKDIR}/cape31_LATEST_seeddata.js')

# Keep only 10 most recent HTML backups
html_bks = sorted([x for x in os.listdir(BKDIR)
                   if x.startswith('cape31_2') and x.endswith('_clean.html')])
for old in html_bks[:-10]:
    os.remove(f'{BKDIR}/{old}')
    print(f'  Pruned old backup: {old}')

print(f'✓ HTML:  {html_bk}  ({os.path.getsize(html_bk)//1024}KB)')
print(f'✓ Data:  {js_bk}  ({os.path.getsize(js_bk)//1024}KB)')
print(f'✓ LATEST updated')
print(f'Backups kept: {len([x for x in os.listdir(BKDIR) if x.endswith("_clean.html") and "LATEST" not in x])}')
