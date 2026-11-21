"""Check icon-only controls and main-menu navigation in an isolated game copy."""
from pathlib import Path
import os,re,shutil,subprocess,sys
project=Path(__file__).resolve().parents[1]
sdk=Path(sys.argv[1]).resolve(); root=Path(sys.argv[2]).resolve()
game=root/'game'
shutil.copytree(project/'game',game,ignore=shutil.ignore_patterns('saves','cache','*.rpyc','*.rpymc','*.log'))
(root/'captures').mkdir()
env=dict(os.environ,RENPY_PATH_TO_SAVES=str(root/'isolated-saves'),SDL_AUDIODRIVER='dummy',RENPY_SIMPLE_EXCEPTIONS='1')
exe=sdk/('lib/py3-windows-x86_64/python.exe' if os.name=='nt' else 'lib/py3-linux-x86_64/python')
cmd=[str(exe),str(sdk/'renpy.py'),str(root)]
options={'creationflags':subprocess.CREATE_NO_WINDOW} if os.name=='nt' else {}
subprocess.run(cmd+['lint',str(root/'lint.txt')],env=env,check=True,timeout=150,**options)
report=(root/'lint.txt').read_text(encoding='utf-8-sig')
assert 'Statistics:' in report and 'game/' not in report.split('Statistics:')[0],report
for filename in ('zz_kk_gui.rpy','zzz_kk_secondary.rpy'):
    source=(game/filename).read_text(encoding='utf-8-sig')
    assert 'GetTooltip' not in source and not re.search(r'^\s*tooltip\s+',source,re.M)
    for name in ('main_menu','preferences','load','kk_cutscene_gallery','kk_system_menu','confirm','kg_pause_menu'):
        source=re.sub(r'(^screen '+name+r'\([^\n]*\):\n)',lambda m:m[0]+'    timer .5 repeat True action Function(ks_icon_qa,"'+name+'",_update_screens=False)\n',source,flags=re.M)
    (game/filename).write_text(source,encoding='utf8')
(game/'zzzz_icon_qa.rpy').write_text(r'''
init 100 python:
    import os
    ks_icon_stage=0
    ks_icon_case=0
    ks_icon_expect=None
    ks_icon_pages=[("settings","preferences"),("gallery","kk_cutscene_gallery"),("bookmark","load"),("system","kk_system_menu"),("exit","confirm")]
    def ks_icon_texts(displayable):
        if isinstance(displayable,renpy.text.text.Text):return [displayable]
        result=[]
        for child in displayable.visit():result.extend(ks_icon_texts(child))
        return result
    def ks_icon_qa(name):
        global ks_icon_stage,ks_icon_case,ks_icon_expect
        if name=="main_menu":
            if renpy.get_screen("confirm"):return
            row=renpy.get_displayable(name,"kg_main_icon_row")
            x,y=row.get_placement()[:2]; w,h=renpy.render(row,1920,1080,0,0).get_size()
            assert (x,y,w,h)==(1238,710,576,104),(x,y,w,h)
            assert x+w<=1814 and y+h<1080,"Menu row clipped"
            assert not ks_icon_texts(row),"Visible text inside the icon row"
            for icon,page in ks_icon_pages:
                button=renpy.get_displayable(name,"kg_main_"+icon)
                assert not ks_icon_texts(button),icon+" contains a visible label"
                assert button.style.focus_mask is True
                if icon!="exit":assert button.action.screen==page
                else:assert button.action.confirm is True
            assert GetTooltip() is None,"Hover function label still present"
            if ks_icon_stage<6:
                sizes=[(1280,720),(1366,768),(1920,1080)]
                if ks_icon_stage%2==0:
                    renpy.set_physical_size(sizes[ks_icon_stage//2])
                    renpy.set_focus(name,"kg_main_exit")
                else:
                    renpy.screenshot(os.path.join(config.basedir,"captures","main-"+str(ks_icon_stage//2)+".png"))
                ks_icon_stage+=1;return
            if ks_icon_case<len(ks_icon_pages):
                icon,ks_icon_expect=ks_icon_pages[ks_icon_case]
                return renpy.run(renpy.get_displayable(name,"kg_main_"+icon).action)
            return renpy.run(Start("ks_icon_review"))
        if name=="kg_pause_menu":
            button=renpy.get_displayable(name,"ks_pause_save")
            assert not ks_icon_texts(button),"Pause object still contains function text"
            resume=renpy.get_displayable(name,"kg_resume")
            assert len(ks_icon_texts(resume))==1,"Resume phone contains text beyond its clock"
            renpy.set_focus(name,"ks_pause_save")
            assert GetTooltip() is None
            renpy.screenshot(os.path.join(config.basedir,"captures","pause.png"))
            return renpy.run(Return())
        assert name==ks_icon_expect,(name,ks_icon_expect)
        renpy.screenshot(os.path.join(config.basedir,"captures",name+".png"))
        ks_icon_case+=1
        if name=="confirm":return renpy.run(renpy.get_screen(name).scope["no_action"])
        return renpy.run(Return())

label ks_icon_review:
    $ kk_host="yutaka"
    $ kk_setup_state()
    call screen kg_pause_menu
    $ open(os.path.join(config.basedir,"icons.ok"),"w").write("PASS: icon-only row and pause objects; 3 viewport sizes; complete Quit; Settings/Gallery/Load/System/quit-cancel native actions; no hover labels")
    $ renpy.quit()
''',encoding='utf8')
try:
    subprocess.run(cmd,env=env,check=True,timeout=100,**options)
    assert (root/'icons.ok').exists(),'UI test did not finish'
    print((root/'icons.ok').read_text(),flush=True)
    print(root,flush=True)
except Exception:
    for name in ('errors.txt','traceback.txt','log.txt'):
        if (root/name).exists():print((root/name).read_text(encoding='utf-8-sig',errors='replace')[-4500:],flush=True)
    raise
