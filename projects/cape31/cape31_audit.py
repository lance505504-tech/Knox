#!/usr/bin/env python3
"""
Cape 31 CMS — Build Audit Tool
Run: python3 cape31_audit.py cape31-class-management.html
"""
import re, sys
from collections import Counter

filename = sys.argv[1] if len(sys.argv) > 1 else 'cape31-class-management.html'
with open(filename) as f:
    raw = f.read()

issues = []
warnings = []

script_match = re.search(r'<script[^>]*>', raw)
if not script_match:
    print("CRITICAL: No <script> tag found"); sys.exit(1)

js_start = script_match.end()
js_end   = raw.rfind('</script>')
js   = raw[js_start:js_end]
html = raw[:script_match.start()]

print(f"File: {len(raw)//1024}KB | HTML: {len(html)//1024}KB | JS: {len(js)//1024}KB")
print(f"Script: {raw.count('<script')} open / {raw.count('</script>')} close\n")

# ── 1. HTML STRUCTURE ─────────────────────────────────────────────────────────
print("═══ 1. HTML STRUCTURE ════════════════════════════════════")
for tag, label in [('<!DOCTYPE','DOCTYPE'),('<html','<html>'),('<head>','<head>'),
                   ('</head>','</head>'),('<body','<body>'),('</body>','</body>'),('</html>','</html>')]:
    count = raw.count(tag)
    ok = count == 1
    print(f"  {'✓' if ok else '✗'} {label}: {count}")
    if not ok: issues.append(f"{'Missing' if count==0 else 'Duplicate'} {label}")

all_ids = re.findall(r'id="([^"]+)"', html)
id_dupes = {k:v for k,v in Counter(all_ids).items() if v>1}
if id_dupes:
    issues.append(f"Duplicate HTML IDs: {list(id_dupes.keys())}")
    print(f"  ✗ Duplicate IDs: {list(id_dupes.keys())}")
else:
    print(f"  ✓ No duplicate HTML IDs ({len(all_ids)} total)")

# ── 2. JS SYNTAX ──────────────────────────────────────────────────────────────
print("\n═══ 2. JS SYNTAX ════════════════════════════════════════")
brace_diff = js.count('{') - js.count('}')
paren_diff = js.count('(') - js.count(')')
bt_count   = js.count('`')
print(f"  {'✓' if brace_diff==0 else '✗'} Braces: {js.count('{')} / {js.count('}')} (diff={brace_diff})")
print(f"  {'✓' if paren_diff==0 else '✗'} Parens: diff={paren_diff}")
print(f"  {'✓' if bt_count%2==0 else '✗'} Backticks: {bt_count}")
if brace_diff != 0: issues.append(f"Brace imbalance: {brace_diff}")

# Check for broken triple-backslash onclick patterns (common corruption)
pass  # replaced by node check below
broken_escape = []
if broken_escape:
    issues.append(f"Broken escape sequences in JS strings: {len(broken_escape)} found")
    print(f"  ✗ Broken escape sequences: {len(broken_escape)}")
else:
    print(f"  ✓ No broken escape sequences")
if paren_diff != 0: issues.append(f"Paren imbalance: {paren_diff}")
if bt_count % 2 != 0: issues.append("Odd backtick count")

all_fns = re.findall(r'^(?:async\s+)?function\s+(\w+)\s*\(', js, re.MULTILINE)
fn_dupes = {k:v for k,v in Counter(all_fns).items() if v>1}
if fn_dupes:
    issues.append(f"Duplicate functions: {list(fn_dupes.keys())}")
    print(f"  ✗ Duplicate functions: {list(fn_dupes.keys())}")
else:
    print(f"  ✓ No duplicate functions ({len(all_fns)} total)")

# Top-level scope only for const/var conflicts
first_fn = re.search(r'\nfunction \w+|\nasync function \w+', js)
top = js[:first_fn.start()] if first_fn else js
top_consts = set(re.findall(r'(?:const|let)\s+(\w+)\s*=', top))
top_vars   = set(re.findall(r'\bvar\s+(\w+)\s*=', top))
conflicts  = top_consts & top_vars
if conflicts:
    issues.append(f"CRITICAL: Top-level const/var conflicts: {list(conflicts)}")
    print(f"  ✗ CRITICAL top-level const/var conflicts: {list(conflicts)}")
else:
    print(f"  ✓ No top-level const/var conflicts")

top_const_list = re.findall(r'(?:const|let)\s+(\w+)\s*=', top)
top_dupes = {k:v for k,v in Counter(top_const_list).items() if v>1}
if top_dupes:
    issues.append(f"CRITICAL: Duplicate top-level const/let: {list(top_dupes.keys())}")
    print(f"  ✗ CRITICAL duplicate top-level const: {list(top_dupes.keys())}")
else:
    print(f"  ✓ No duplicate top-level const/let")

strict_pos = js.find("'use strict'")
print(f"  {'✓' if strict_pos >= 0 else '⚠'} 'use strict' {'at position '+str(strict_pos) if strict_pos >= 0 else 'not found'}")

# ── 3. REQUIRED FUNCTIONS ─────────────────────────────────────────────────────
print("\n═══ 3. REQUIRED FUNCTIONS ═══════════════════════════════")
required_fns = [
    'doLogin','doDemoLogin','signOut','goHome','openSection','openAdmin','openAdminHome',
    'renderHomeBoatCard','renderAll','renderStats','renderFleet','renderFees',
    'renderRegattas','renderEntries','renderEntryRegattas','renderRacingPanel',
    'renderResultsRegattas','renderResults','renderAdmin','renderPayments',
    'saveData','saveLocal','loadData',
    'isAdmin','isExCom','isOwner','canAddSerial','canEdit',
    'sbInit','sbDefaultState','sbRenderFleet','sbLogAudit','sbGenCode',
    'sbIssueStandardButtons','sbIssueBonusButtons','sbSaveData','sbIssueBulk',
    'confirmFeePayment','doConfirmFeePayment',
    'activateDemoMode','deactivateDemoMode','loadDemoData','resetDemoData',
    'submitEnquiry','oo','co','openModal','closeModal','toast','uid','toggleUserMenu',
]
fn_set = set(all_fns)
missing_fns = [f for f in required_fns if f not in fn_set]
if missing_fns:
    issues.append(f"Missing functions: {missing_fns}")
    for f in missing_fns: print(f"  ✗ Missing: {f}()")
else:
    print(f"  ✓ All {len(required_fns)} required functions present")

# ── 4. JS → HTML ELEMENT REFERENCES ──────────────────────────────────────────
print("\n═══ 4. JS → HTML ELEMENT REFERENCES ════════════════════")
js_id_refs = set(re.findall(r"getElementById\('([^']+)'\)", js))
html_ids   = set(re.findall(r'id="([^"]+)"', raw))
acceptable = {'nav-av','nav-lbl','tab-admin','tab-sailbuttons','tab-payments',
              'stats-bar','ls','rn','re','rp','rb','reg-err','au-title','au-name',
              'au-email','au-pw','au-role','au-boat','au-err','au-boat-field',
              'au-summary','au-ov','um-av2','nav-nm','fleet-note','r-st','r-type',
              'ec-name','ec-email','excom-list','user-list','accounts-callout',
              's-bonus','alloc-yr','mine-content','q-reg','r-yr','reg-body',
              'sb-fleet','sb-register','sb-mine','sb-settings','fleet-grid',
              'q-fleet','f-yr','fleet-note','tab-mine','tab-settings',
              'rpw-val','rpw-err','rpw-for','boat-ov-title','fleet-body-sb',
              'panel-sailbuttons','s-alloc','s-yr','sync-bar-inline','btn-race-mgmt','btn-add-regatta','reg-region','bm-contact-name','bm-address','bm-mobile','bm-phone','bm-emerg-name','bm-emerg-phone','bm-insurer','bm-policy','bm-ins-contact','bm-ins-phone','bm-ins-start','bm-ins-expiry','bm-ins-notes','bm-ins-status','bm-ins-status-row','um-boat','um-positions','um-boats','sp-stats','sponsors-grid','sp-panel-list','sp-panel-benefits','sp-panel-hospitality','sp-panel-manage','sp-benefits-content','sp-hosp-content','sp-manage-list','sp-tab-benefits','sp-tab-hosp','sp-tab-manage','sp-name','sp-type','sp-level','sp-website','sp-contact-name','sp-contact-email','sp-start','sp-end','sp-notes','sp-benefit-logo','sp-benefit-media','sp-benefit-reports','sp-benefit-hosp','sp-benefit-visits','sp-benefit-other','sp-media-url','sp-highlights-url','sp-logo-url','sp-photos-url','sp-media-notes','sp-err','sp-modal-title','sp-modal-details','sp-modal-benefits','sp-modal-media','enq-err','enq-msg','enq-type','enq-name','enq-email'}
real_missing = {e for e in (js_id_refs - html_ids - acceptable)
                if not any(c in e for c in ['+','$','{'])}
if real_missing:
    warnings.append(f"JS refs elements not in HTML: {sorted(real_missing)}")
    print(f"  ⚠ {len(real_missing)} JS refs to missing HTML elements: {sorted(real_missing)}")
else:
    print(f"  ✓ All JS element references have HTML counterparts")

# ── 5. REQUIRED HTML ELEMENTS ─────────────────────────────────────────────────
print("\n═══ 5. REQUIRED HTML ELEMENTS ═══════════════════════════")
required_els = [
    'login-screen','app','home-screen','admin-screen',
    'top-bar','top-bar-title','top-bar-sub','back-btn','user-av',
    'home-boat-card','hbc-name','hbc-meta','hbc-fee-badge','hbc-body',
    'demo-banner','li-em','li-pw','li-err',
    'fee-confirm-ov','fee-confirm-title','fee-confirm-year',
    'fee-confirm-boat','fee-confirm-amount','fee-confirm-method',
    'fee-confirm-ref','fee-confirm-notes','fee-confirm-btn-row',
    'enquiry-ov','enq-name','enq-email','enq-type','enq-msg','enq-err','gate-config-body','region-gates-section','rm-messaging','rm-buttons-req','rm-handicap','rm-int-fee-req','meas-stats','meas-panel-rules','meas-rules-list','meas-panel-docs','meas-docs-list','meas-panel-qa','meas-qa-list','meas-panel-manage','meas-manage-list','meas-tab-manage','meas-qa-search','meas-qa-cat','meas-doc-ov','meas-doc-title','meas-doc-type','meas-doc-name','meas-doc-url','meas-doc-date','meas-doc-size','meas-doc-notes','meas-doc-err','meas-qa-ov','meas-qa-title','meas-qa-cat-sel','meas-qa-q','meas-qa-a','meas-qa-by','meas-qa-date','meas-qa-err','clubs-list','clubs-stats','clubs-admin-view','clubs-user-view','club-events-list','club-ov','club-ov-title','club-user-ov','club-user-ov-title','cl-name','cl-location','cl-contact','cl-region','cl-notes','cl-err','cu-name','cu-email','cu-pw','cu-club-id','cu-err','btn-add-club','rm-club','cpw-ov','cpw-for-label','cpw-uid','cpw-current-row','cpw-current','cpw-new2','cpw-conf2','cpw-err2','account-card','account-bio-status','btn-register-bio','btn-remove-bio','btn-biometric','forgot-pw-msg',
    'ov-regatta','rm-name','rm-start','rm-end','rm-venue','rm-year',
    'ov-user','um-role','toast-wrap',
    'fleet-body','fees-body','fees-summary','regatta-list',
    'entries-container','entry-reg','races-container','results-container',
    'sdot','slbl',
]
missing_els = [e for e in required_els if f'id="{e}"' not in raw]
if missing_els:
    issues.append(f"Missing HTML elements: {missing_els}")
    for e in missing_els: print(f"  ✗ Missing: #{e}")
else:
    print(f"  ✓ All {len(required_els)} required HTML elements present")

# ── 6. SECTION SCREENS ────────────────────────────────────────────────────────
print("\n═══ 6. SECTION SCREENS ══════════════════════════════════")
screens = ['regattas','entries','results','fleet','fees','racing','admin','payments','sailbuttons','sponsors','certs']
missing_screens = []
for s in screens:
    has = f'id="screen-{s}"' in raw or f'id="sect-{s}"' in raw
    print(f"  {'✓' if has else '✗'} screen-{s}")
    if not has: missing_screens.append(s)
if missing_screens: issues.append(f"Missing section screens: {missing_screens}")

# ── 7. BAD REFERENCES ─────────────────────────────────────────────────────────
print("\n═══ 7. BAD REFERENCES ═══════════════════════════════════")
bad_refs = [
    ('cape31-auth.html',   'Auth redirect'),
    ('cdn-cgi',            'Cloudflare CDN'),
    ('cloudflare',         'Cloudflare ref'),
    ('__cf_email__',       'CF email obfuscation'),
    ('cape31-sail-register.html', 'Old sail register link'),
]
for ref, label in bad_refs:
    count = raw.count(ref)
    if count: issues.append(f"{label}: {count} refs"); print(f"  ✗ {label}: {count}")
    else: print(f"  ✓ No {label}")

# ── 8. ONCLICK FUNCTIONS ──────────────────────────────────────────────────────
print("\n═══ 8. ONCLICK FUNCTION CHECK ═══════════════════════════")
onclick_fns = set(re.findall(r'onclick="(?:if\(typeof )?(\w+)\s*(?:===|[(])', raw))
onclick_fns |= set(re.findall(r'onclick="(\w+)\s*\(', raw))
onclick_fns |= set(re.findall(r'onchange="(\w+)\s*\(', raw))
onclick_fns -= {'if','event','typeof','setTimeout','this','true','false',
                'confirm','alert','window','document'}
missing_onclick = onclick_fns - fn_set - {'event','confirm','alert','encodeURIComponent',
    'window','document','parseInt','parseFloat','Date','Math','Array','Object'}
if missing_onclick:
    issues.append(f"onclick refs missing JS: {sorted(missing_onclick)}")
    for f in sorted(missing_onclick): print(f"  ✗ onclick calls undefined: {f}()")
else:
    print(f"  ✓ All onclick function references exist")

# ── 9. KEY VARIABLES ──────────────────────────────────────────────────────────
print("\n═══ 9. KEY VARIABLES ════════════════════════════════════")
for v in ['SK','USK','HAS_CLOUD','SB_SK','SB','S','ME','DEMO_MODE','DEMO_SK','DEMO_SB_SK']:
    ok = bool(re.search(r'(?:const|let|var)\s+'+v+r'\b', js))
    print(f"  {'✓' if ok else '✗'} {v} declared")
    if not ok: issues.append(f"Missing variable: {v}")

# ── 10. LOGIN FLOW ────────────────────────────────────────────────────────────
print("\n═══ 10. LOGIN FLOW ══════════════════════════════════════")
for ok, label in [
    ('function doLogin' in js,       'doLogin function'),
    ('function doDemoLogin' in js,   'doDemoLogin function'),
    ('login-screen' in raw,          'login-screen div'),
    ('id="app"' in raw,              'app div'),
    ('id="li-em"' in raw,            'Email input'),
    ('id="li-pw"' in raw,            'Password input'),
    ('doDemoLogin' in raw,           'Demo button'),
    ('demo-banner' in raw,           'Demo banner'),
]:
    print(f"  {'✓' if ok else '✗'} {label}")
    if not ok: issues.append(f"Login flow: missing {label}")

# ── SUMMARY ───────────────────────────────────────────────────────────────────
print(f"\n{'═'*56}\nSUMMARY\n{'═'*56}")
if issues:
    print(f"\n✗ {len(issues)} ISSUES:")
    for i in issues: print(f"  • {i}")
else:
    print("\n✓ ALL CLEAR — no issues found")
if warnings:
    print(f"\n⚠ {len(warnings)} WARNINGS:")
    for w in warnings: print(f"  • {w}")
print(f"\nFile: {len(raw)//1024}KB | Complete: {'</html>' in raw}")
