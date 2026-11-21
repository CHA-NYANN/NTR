"""Run reference reflow and illustrated action QA in a disposable copy."""
from pathlib import Path
import os,re,shutil,subprocess,sys,time
project=Path(__file__).resolve().parents[1]
panels_only='--panels-only' in sys.argv
if panels_only: sys.argv.remove('--panels-only')
sdk=Path(sys.argv[1]).resolve()
root=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else project/('qa-dialogue-'+time.strftime('%H%M%S'))
game=root/'game'
shutil.copytree(project/'game',game,ignore=shutil.ignore_patterns('saves','cache','*.rpyc','*.rpymc','*.log'))
(root/'captures').mkdir()
exe=sdk/('lib/py3-windows-x86_64/python.exe' if os.name=='nt' else 'lib/py3-linux-x86_64/python')
cmd=[str(exe),str(sdk/'renpy.py'),str(root)]
env=dict(os.environ,RENPY_PATH_TO_SAVES=str(root/'isolated-saves'),SDL_AUDIODRIVER='dummy',RENPY_SIMPLE_EXCEPTIONS='1')
options={'creationflags':subprocess.CREATE_NO_WINDOW} if os.name=='nt' else {}
subprocess.run(cmd+['lint',str(root/'lint.txt')],env=env,check=True,timeout=120,**options)
report=(root/'lint.txt').read_text(encoding='utf-8-sig')
assert 'Statistics:' in report and 'game/' not in report.split('Statistics:')[0],report
for filename,names in (('zz_kk_gui.rpy',('main_menu',)),('zzz_kk_secondary.rpy',('say','kk_choice_panel','kk_route_select','kk_location_view'))):
    path=game/filename
    text=path.read_text(encoding='utf-8-sig')
    for name in names:
        text=re.sub(r'(^screen '+name+r'\([^\n]*\):\n)',lambda m:m[0]+'    timer .65 repeat True action Function(ks_review_input,"'+name+'",_update_screens=False)\n',text,flags=re.M)
    path.write_text(text,encoding='utf8')
(game/'zzzz_review.rpy').write_text(r'''
init 100 python:
    import os
    ks_review_count={}
    def ks_review_input(name):
        count=ks_review_count.get(name,0)
        ks_review_count[name]=count+1
        if name=="main_menu": return renpy.run(Start("ks_review"))
        renpy.screenshot(os.path.join(config.basedir,"captures",name+"-%02d.png"%count))
        if name=="say":
            screen=renpy.get_screen(name)
            scope=screen.scope
            lines,height,th=ks_dialog_metrics(scope['who'],scope['what'])
            window=renpy.get_displayable(name,"window")
            x,y=window.get_placement()[:2]
            w,h=renpy.render(window,1920,1080,0,0).get_size()
            text=renpy.get_displayable(name,"what")
            system=kg_dialogue_skin(scope['who'],scope['what'])=='system-dialogue'
            tw,actual=renpy.render(text,824 if system else 1360,4096,0,0).get_size()
            room=h-(244 if system else 190)
            if system:
                assert w==1120 and h<=430,(w,h)
                assert text.style.font==kg_system_dialogue,text.style.font
                viewport=renpy.get_displayable(name,"ks_system_body")
                vw,vh=renpy.render(viewport,844,room,0,0).get_size()
                assert vw<=844 and vh==room,(vw,vh,room)
                assert actual<=room or lines==4,(lines,actual,room)
            else:
                assert text.style.font==kg_dialogue,text.style.font
                assert actual<=room,(lines,actual,room,scope['what'])
            assert x>=0 and x+w<1758 and y+h<=1036,(x,y,w,h)
            with open(os.path.join(config.basedir,"layout.txt"),"a") as f:f.write(str((scope['who'],lines,h,actual,room))+"\n")
            return renpy.queue_event("dismiss")
        if name=="kk_route_select":
            scope=renpy.get_screen(name).scope
            button=renpy.get_displayable(name,"ks_hand_"+ks_review_host)
            assert button.style.focus_mask is True
            art="hand-male" if ks_review_host=="yutaka" else "hand-female"
            rendered=renpy.render(ks_action_image(art,780,780),780,780,0,0)
            assert not rendered.is_pixel_opaque(779,0)
            assert rendered.is_pixel_opaque(390,390)
            if scope['selected'] is None:
                renpy.set_focus(name,"ks_hand_"+ks_review_host)
                return renpy.run(button.action)
            return
        if name=="kk_choice_panel":
            scope=renpy.get_screen(name).scope
            rows=scope['rows']
            art=ks_action_set(rows,scope['heading'])
            if art:
                button=renpy.get_displayable(name,"ks_action_"+str(ks_review_index))
                assert button.style.focus_mask is True
                return renpy.run(button.action)
            return renpy.run(rows[ks_review_index][1])
        if name=="kk_location_view":
            button=renpy.get_displayable(name,"ks_act_"+ks_review_activity)
            assert button.style.focus_mask is True
            return renpy.run(button.action)

label ks_review:
    $ _preferences.text_cps=0
    $ quick_menu=True
    $ kk_host=None
    nar "Tidak ada lagi raungan klakson atau teriakan penumpang. Tidak ada rasa sakit, tidak ada dinginnya lantai peron, bahkan tidak ada detak waktu. Kesadaranmu hanya mengapung tanpa bobot di dalam keheningan alam bawah sadar yang gelap gulita."
    $ ks_review_host="yutaka"
    call screen kk_route_select
    $ assert _return=="yutaka"
    $ ks_review_host="chiasa"
    call screen kk_route_select
    $ assert _return=="chiasa"
    $ kk_host="chiasa"
    $ kk_setup_state()
    nar "Kau tersentak bangun dengan napas memburu. Kedua tanganmu refleks mencengkeram dada, bersiap merasakan tulang rusuk yang remuk dihantam baja kereta."
    chiasa "Kamu pilih: masuk sekarang?\nKelasnya bahkan belum dimulai."
    sistem "Bangun juga akhirnya. Kukira jiwamu ikut penyok tertabrak kereta tadi, Sampah Peron."
    sistem "Aturannya sangat sederhana: kau punya waktu tiga tahun sampai Amamiya Koita lulus kuliah untuk menyimpangkan takdir romantisnya sejauh mungkin dari jalur asli. Evaluasinya hanya dilakukan satu kali, tepat saat ia menerima ijazah wisuda. Kalau sampai hari itu skenario romansa sang protagonis masih berjalan mulus... jantung barumu akan kubuat berhenti berdetak di tempat."
    $ persistent.kk_gui_dark=True
    chiasa "Kamu pilih: masuk sekarang?\nKelasnya bahkan belum dimulai."
    $ persistent.kk_gui_dark=False
    $ kk_host="yutaka"
    $ kk_setup_state()
    yutaka "Kamu pilih: masuk sekarang?\nKelasnya bahkan belum dimulai."
    $ ks_review_round=0
    while ks_review_round<2:
        $ kk_host="yutaka" if ks_review_round==0 else "chiasa"
        $ ks_review_actions=(["Bongkar isi dompet dan ponselnya.","Hampiri cermin kamar mandi untuk memastikan.","Langsung telepon Koita sekarang juga.","Duduk membisu menuntut penjelasan."] if kk_host=="yutaka" else ["Hampiri cermin dan periksa meja belajarnya.","Bongkar isi ponsel di sebelah kasur.","Nekat keluar kamar dan turun ke bawah.","Duduk membisu menuntut penjelasan."])
        $ ks_review_index=0
        while ks_review_index<4:
            $ ks_review_rows=[(caption,Return(key),False) for key,caption in zip("ABCD",ks_review_actions)]
            call screen kk_choice_panel(ks_review_rows,"Di situasi gila ini, apa langkah pertamamu?")
            $ assert _return=="ABCD"[ks_review_index]
            $ ks_review_index+=1
        $ ks_review_round+=1
    $ kk_host="chiasa"
    $ kk_setup_state()
    $ ks_review_activity="belajar"
    call screen kk_location_view("d1","Perpustakaan Pusat")
    $ assert _return==("act","belajar")
    $ ks_review_activity="makan"
    call screen kk_location_view("d4","Kafe Komorebi")
    $ assert _return==("act","makan")
    $ ks_review_activity="kerja"
    call screen kk_location_view("d4","Kafe Komorebi")
    $ assert _return==("act","kerja")
    $ ks_review_activity="santai"
    call screen kk_location_view("d1","Taman Kampus")
    $ assert _return==("act","santai")
    $ ks_review_index=0
    while ks_review_index<3:
        $ kk_setup_state()
        call kkscene_C02
        $ assert kk_done("C02")
        $ assert choices_log[-1]["key"]=="ABC"[ks_review_index]
        $ ks_review_index+=1
    $ open(os.path.join(config.basedir,"review.ok"),"w").write("PASS: reference reflow; both hand returns and alpha masks; 8 opening actions; location; C02 ABC")
    $ renpy.quit()
''',encoding='utf8')
if panels_only:
    driver=game/'zzzz_review.rpy'
    text=driver.read_text(encoding='utf8')
    point=text.index('    $ ks_review_round=0')
    text=text[:point]+'''    $ open(os.path.join(config.basedir,"review.ok"),"w").write("PASS: final reference panel geometry and text bounds")
    $ renpy.quit()
'''
    driver.write_text(text,encoding='utf8')
try:
    subprocess.run(cmd,env=env,check=True,timeout=240,**options)
    assert (root/'review.ok').exists(),'QA did not complete'
    print((root/'review.ok').read_text(),flush=True)
    print(root,flush=True)
finally:
    for name in ('traceback.txt','errors.txt'):
        if (root/name).exists(): print((root/name).read_text(errors='replace')[-6000:],flush=True)
