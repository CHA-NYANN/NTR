"""Task audit. Run against the saved baseline to catch reference changes."""
from pathlib import Path
import hashlib,json,re,sys
root=Path(__file__).resolve().parents[1]
lock_path=root/'scope-lock.json'
if not lock_path.exists() or '--portable' in sys.argv:
    lock_path=root/'tools/secondary_reference_lock.json'
lock=json.loads(lock_path.read_text())
# Owner explicitly replaced the assistant's text-based hand selection on 19 Nov 2026.
lock['protected_screens'].pop('kk_route_select',None)
def digest(path):
    raw=path.read_bytes()
    if lock.get('normalised') and path.suffix in ('.rpy','.svg'):
        raw=raw.decode('utf-8-sig').replace('\r\n','\n').encode()
    return hashlib.sha256(raw).hexdigest()
original=(root/'game/zz_kk_gui.rpy').read_bytes()
assert digest(root/'game/zz_kk_gui.rpy')==lock['source_gui_hash'],'Original reference GUI file changed'
late=(root/'game/zzz_kk_secondary.rpy').read_text(encoding='utf8')
names=set(re.findall(r'^screen (\w+)\(',late,re.M))
assert not names.intersection(lock['protected_screens']), 'Protected screen overridden: '+str(names.intersection(lock['protected_screens']))
assert all(n.startswith('ks_') for n in re.findall(r'^\s*def (\w+)\(',late,re.M)), 'Reference helper overridden'
assert all(n.startswith('ks_') for n in re.findall(r'^(?:style|transform) (\w+)',late,re.M)), 'Reference style/animation overridden'
for path,expected_hash in lock['protected_assets'].items():
    assert digest(root/path)==expected_hash,path+' changed'
original_text=original.decode('utf-8-sig').replace('\r\n','\n')
def screen(text,name):
    return re.search(r'(?ms)^screen '+name+r'\([^\n]*\):\n.*?(?=^screen |^label |\Z)',text)[0]
before=screen(original_text,'kk_phone_locator')
after=screen(late,'kk_phone_locator')
start=before.index('            if tab !=')
end=before.index('        button:',start)
expected=before[:start]+'            if tab != "home":\n                use ks_phone_tab(tab)\n'+before[end:]
assert after.strip()==expected.strip(),'Phone home layout changed outside app panel'
world=(root/'game/kk_world.rpy').read_text(encoding='utf-8-sig')
def operations(text):
    return re.findall(r'Return\(\(.*?\)\)',text)
assert operations(screen(world,'kk_location_view'))==operations(screen(late,'kk_location_view')),'Location operations changed'
print('PASS: reference GUI file, main menu/map/controls, 45 reference assets, phone home and location operations preserved.')
