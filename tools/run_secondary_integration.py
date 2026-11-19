"""Existing story suite with isolated hooks for secondary screen overrides."""
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
quick='--quick' in sys.argv
if quick:
    sys.argv.remove('--quick')
code=(root/'tests/run_living.py').read_text(encoding='utf-8-sig')
if quick:
    code=code.replace('    for seq,(host,size,case) in enumerate(runs):','    for seq,(host,size,case) in enumerate(runs[:2]):')
extra='''
            for filename in ("zz_kk_gui.rpy","zzz_kk_secondary.rpy"):
                gui=game/filename
                src=gui.read_text(encoding="utf-8-sig")
                for name in ("main_menu","say","choice","kk_route_select","kk_choice_panel","kk_world_district","kk_world_location","kg_travel_confirm","kk_wallet","kk_location_view","kk_titlecard","kk_ending_card"):
                    src=re.sub(r"(^screen "+name+r"\\([^\\n]*\\):\\n)",lambda m:m[0]+'    timer .03 repeat True action Function(kk_test_input, "'+name+'", _update_screens=False)\\n',src,flags=re.M)
                gui.write_text(src,encoding="utf8")
            driver=game/"zz_sandbox_test.rpy"
            src=driver.read_text(encoding="utf-8-sig")
            src=src.replace('        if name == "kk_world_location":','        if name == "kg_travel_confirm":\\n            return renpy.run([Hide("kg_travel_confirm"),Return("Gedung Arsitektur")])\\n        if name == "kk_world_location":')
            driver.write_text(src,encoding="utf8")
'''
code=code.replace('            world.write_text(src,encoding="utf8")','            world.write_text(src,encoding="utf8")\n'+extra)
exec(compile(code,str(root/'tests/run_living.py'),'exec'))
