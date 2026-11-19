"""Isolated runtime UI smoke test. Never writes to player saves."""
from pathlib import Path
import os
import re
import shutil
import subprocess
import sys
import time

project = Path(__file__).resolve().parents[1]
sdk = Path(sys.argv[1]).resolve()
capture_motion='--motion' in sys.argv
root = project / ("qa-runtime-" + time.strftime("%H%M%S"))
game = root / "game"
shutil.copytree(project / "game", game, ignore=shutil.ignore_patterns("saves", "cache", "*.rpyc", "*.rpymc", "*.log"))
(root / "captures").mkdir()
if capture_motion:
    (root/'motion').mkdir()
src = (game / "zz_kk_gui.rpy").read_text(encoding="utf-8-sig")
names = ("main_menu", "say", "kk_world_district", "kk_world_location", "kg_travel_confirm", "preferences", "save", "load", "history", "kk_cutscene_gallery", "kk_system_menu", "kk_phone_locator", "kg_map_viewer", "kk_choice_panel", "kg_pause_menu", "kk_status", "kk_wallet", "kk_titlecard", "kk_ending_card", "confirm")
for filename in ("zz_kk_gui.rpy","zzz_kk_secondary.rpy"):
    src=(game/filename).read_text(encoding="utf-8-sig")
    for name in names:
        interval=3.5 if capture_motion and name == 'kg_pause_menu' else .7
        src = re.sub(r"(^screen " + name + r"\([^\n]*\):\n)", lambda m: m[0] + '    timer '+str(interval)+' repeat True action Function(kg_qa_input, "' + name + '", _update_screens=False)\n', src, flags=re.M)
    if capture_motion and filename == 'zzz_kk_secondary.rpy':
        src=src.replace('screen kg_pause_menu():\n','screen kg_pause_menu():\n    timer .09 repeat True action Function(ks_qa_motion, _update_screens=False)\n')
    (game / filename).write_text(src, encoding="utf-8")
(game / "zzz_gui_test.rpy").write_text(r'''
init 100 python:
    import os
    _kg_qa_counts = {}
    _ks_motion_frame = 0
    def ks_qa_motion():
        global _ks_motion_frame
        i=_ks_motion_frame
        _ks_motion_frame += 1
        if i == 0:
            renpy.set_physical_size((1280,720))
        if i == 8:
            renpy.set_focus("kg_pause_menu","ks_pause_save")
        if i == 16:
            renpy.set_focus("kg_pause_menu","kg_resume")
        if i == 20:
            renpy.get_displayable("kg_pause_menu","kg_resume_drag").snap(790,80,.6)
        if i == 29:
            store.kg_qa_menu_returned=True
            return ks_resume_drag([renpy.get_displayable("kg_pause_menu","kg_resume_drag")],None)
        renpy.screenshot(os.path.join(config.basedir,"motion","frame-%03d.png"%i))
    def kg_qa_input(name):
        count = _kg_qa_counts.get(name, 0)
        _kg_qa_counts[name] = count + 1
        suffix = str(count)
        renpy.screenshot(os.path.join(config.basedir,"captures",name+"-"+suffix+".png"))
        with open(os.path.join(config.basedir,"progress.txt"),"a") as out:
            out.write(name+" "+suffix+"\n")
        if name == "main_menu":
            return renpy.run(Start("kk_gui_qa"))
        if name == "say":
            scope=renpy.get_screen(name).scope
            skin=kg_dialogue_skin(scope["who"],scope["what"])
            expected="#29165F" if skin == "system-dialogue" else "#3E4047" if skin == "dialogue-neutral" else "#F8EDFF" if skin == "dialogue-dark" else kg_ink
            assert tuple(renpy.get_displayable(name,"what").style.color) == tuple(Color(expected)), "Incorrect dialogue contrast"
            launcher=renpy.get_displayable(name,"kg_phone_launcher")
            x,y=launcher.get_placement()[:2]
            w,h=renpy.render(launcher,1920,1080,0,0).get_size()
            assert x >= 0 and y >= 0 and x+w <= 1920 and y+h <= 1080, "Phone launcher exceeds the viewport"
            if not kk_host and skin != "system-dialogue":
                assert skin == "dialogue-neutral", "Opening inherited a host color"
            return renpy.queue_event("dismiss")
        if name == "kk_world_district":
            launcher=renpy.get_displayable(name,"kg_map_phone_launcher")
            x,y=launcher.get_placement()[:2]
            w,h=renpy.render(launcher,1920,1080,0,0).get_size()
            assert x >= 0 and y >= 0 and x+w <= 1920 and y+h <= 1080, "Map phone launcher exceeds the viewport"
            if not getattr(store,"kg_qa_menu_returned",False):
                if not renpy.get_screen("kk_phone_locator"):
                    return renpy.run(Show("kk_phone_locator"))
                return
            assert not renpy.get_screen("kk_phone_locator"), "Phone blocked the game after resuming"
            assert not renpy.get_screen("kg_pause_menu")
            assert sum(len(p) for d,n,p in KK_DISTRICTS) == 37
            for did, people in kg_map_people().items():
                for cid, place in people:
                    assert kk_daily_place(cid) == place
                    assert place in KK_DISTRICT_LOCS[did]
            return renpy.run(renpy.get_displayable(name,"qa_d1").action)
        if name == "kk_world_location":
            return renpy.run(renpy.get_displayable(name,"qa_Gedung Arsitektur").action)
        if name == "kg_travel_confirm":
            if count == 0:
                return renpy.run(Hide(name))
            return renpy.run([Hide(name), Return("Gedung Arsitektur")])
        if name == "kk_phone_locator":
            if not getattr(store,"kg_qa_menu_returned",False):
                return renpy.run(renpy.get_displayable(name,"kg_phone_menu").action)
            if count == 1:
                return renpy.run(SetScreenVariable("tab","location"))
            if count == 2:
                return renpy.run(SetScreenVariable("tab","messages"))
            return renpy.run(Return())
        if name == "kg_pause_menu":
            assert not main_menu, "Home left the active game instead of opening its menu"
            assert not renpy.get_screen("kk_phone_locator"), "Phone still blocks menu input"
            store.kg_qa_menu_returned = True
            if count == 0:
                drag=renpy.get_displayable(name,"kg_resume_drag")
                drag.y=80
                return ks_resume_drag([drag],None)
            return renpy.run(renpy.get_displayable(name,"kg_resume").action)
        if name == "kg_map_viewer":
            if count == 0:
                return renpy.run(renpy.get_displayable(name,"qa_d1").action)
            if count == 1:
                assert renpy.get_screen(name).scope["district"] == "d1"
                return renpy.run(SetScreenVariable("district",None))
            return renpy.run(Return())
        if name == "kk_choice_panel":
            rows=renpy.get_screen(name).scope["rows"]
            return renpy.run(rows[1][1])
        if name == "save":
            scope=renpy.get_screen(name).scope
            if not getattr(persistent,"ks_album_checked",False):
                if scope["active_slot"] == 1:
                    return renpy.run(renpy.get_displayable(name,"kg_thumb_slot_2").action)
                assert scope["active_slot"] == 2
                persistent.ks_album_checked=True
                return renpy.run(renpy.get_displayable(name,"kg_thumb_slot_1").action)
            if not FileLoadable(1):
                return renpy.run(renpy.get_displayable(name,"kg_slot_1").action)
            assert FileLoadable(1)
            return renpy.run(Return())
        if name == "load":
            assert FileLoadable(1)
            persistent.kg_qa_loaded = True
            return renpy.run(FileLoad(1,confirm=False))
        if name == "kk_cutscene_gallery":
            assert any(e["id"] == "N01" for e in kg_replays())
            if count == 0:
                return renpy.run(renpy.get_displayable(name,"kg_replay_N01").action)
        if name == "kk_status":
            if not getattr(store,"ks_wallet_tested",False):
                if renpy.get_screen("kk_wallet"):
                    return
                if count == 0:
                    return renpy.run(renpy.get_displayable(name,"ks_contact_koita").action)
                assert renpy.get_screen(name).scope["contact"] == "koita"
                return renpy.run(renpy.get_displayable(name,"ks_open_wallet").action)
            return renpy.run(Return())
        if name == "kk_wallet":
            scope=renpy.get_screen(name).scope
            if scope["page"] == 0:
                assert len(scope["entries"]) == 7
                return renpy.run(renpy.get_displayable(name,"ks_wallet_older").action)
            assert len(scope["entries"]) == 2
            store.ks_wallet_tested=True
            return renpy.run(Hide("kk_wallet"))
        if name == "preferences":
            if count == 0:
                bar=renpy.get_displayable(name,"ks_music_volume")
                bar.adjustment.change(bar.adjustment.range*.35)
                assert 0 < _preferences.get_volume("music") < 1
                assert abs(bar.adjustment.value/bar.adjustment.range-.35) < .01
                return renpy.run(renpy.get_displayable(name,"ks_motion_toggle").action)
            assert not persistent.kk_secondary_motion
            return renpy.run(Return())
        if name == "confirm":
            return renpy.run(renpy.get_displayable(name,"ks_confirm_yes").action)
        return renpy.run(Return())

label kk_gui_qa:
    $ kk_host = ""
    $ _preferences.text_cps = 0
    scene black
    $ assert kg_dialogue_skin(None,"Prolog") == "dialogue-neutral"
    nar "Di ujung terowongan yang gelap, dua sorot lampu kereta ekspres sudah menyala menyilaukan. Klakson panjang meraung memekakkan telinga, disusul gemuruh roda besi yang membelah rel dengan kecepatan penuh."
    $ persistent.kk_gui_dark = True
    $ assert kg_dialogue_skin(None,"Prolog") == "dialogue-neutral"
    nar "Aku belum menjadi Yutaka atau Chiasa. Warna pembuka tetap netral sampai tubuh dipilih."
    $ persistent.kk_gui_dark = False
    $ kk_host = "yutaka"
    $ kk_setup_state()
    $ kk_transactions=[(1,i+1,"Keperluan harian",-1000,500000-1000*(i+1)) for i in range(9)]
    $ saldo=491000
    scene expression Transform("gui/kouseikan/main-art.png",xysize=(1920,1080))
    $ _preferences.text_cps = 0
    call screen kk_titlecard("Sebuah hari di Kouseikan","Catatan yang baru dimulai.")
    call screen kk_status
    call screen kk_world_district
    $ assert _return == ("go","d1")
    call screen kk_world_location("d1")
    $ assert _return == "Gedung Arsitektur"
    call screen kk_phone_locator
    call screen kg_map_viewer
    yutaka "Aku tahu ini kedengarannya sepele… tapi akhir-akhir ini semuanya terasa aneh."
    sistem "Bangun juga akhirnya. Kukira jiwamu ikut penyok tertabrak kereta tadi, Sampah Peron."
    call screen kk_choice_panel([("Ya, kamu kelihatan lelah.", Return("one"), False), ("Ada sesuatu yang mengganggumu?", Return("two"), False), ("Atau, lebih baik kita ganti topik?", Return("three"), False)], "Pilihanmu")
    $ assert _return == "two"
    $ kk_host = "chiasa"
    chiasa "Kalau belum siap cerita sekarang, aku akan menunggumu di sini."
    $ persistent.kk_gui_dark = True
    chiasa "Bahkan ketika hari sudah berganti malam."
    $ persistent.kk_gui_dark = False
    call screen preferences
    $ persistent.kk_secondary_motion = True
    $ kg_qa_token = "saved"
    call screen save
    if not getattr(persistent,"kg_qa_loaded",False):
        $ kg_qa_token = "changed"
        call screen load
    $ assert kg_qa_token == "saved", "Load did not restore game state"
    call screen history
    $ renpy.mark_label_seen("kkscene_N01")
    $ kg_qa_before_replay = (kk_host,kk_bulan,saldo,list(choices_log))
    call screen kk_cutscene_gallery
    $ assert (kk_host,kk_bulan,saldo,list(choices_log)) == kg_qa_before_replay, "Replay changed active game state"
    call screen kk_system_menu
    call screen confirm("Lanjutkan catatan ini?",Return(True),Return(False))
    $ assert _return is True
    call screen kk_ending_card({"name":"Catatan pengujian","body":"Isi kartu tetap dapat dibaca dan dinavigasi."})
    $ open(os.path.join(config.basedir,"gui.ok"),"w").write("PASS: protected reference screens retained; secondary contact/wallet paging, real sound fader, motion toggle, album selection/save/load, swipe resume, history, gallery replay, ending and confirmation.")
    $ renpy.quit()
''', encoding="utf-8")
env = dict(os.environ, RENPY_PATH_TO_SAVES=str(root / "isolated-saves"), RENPY_SIMPLE_EXCEPTIONS="1", SDL_AUDIODRIVER="dummy")
command = [str(sdk / "lib/py3-windows-x86_64/python.exe"), str(sdk / "renpy.py"), str(root)]
print(root, flush=True)
try:
    subprocess.run(command, env=env, check=True, timeout=180, creationflags=subprocess.CREATE_NO_WINDOW)
    assert (root / "gui.ok").is_file(), "GUI test did not complete"
    print((root / "gui.ok").read_text(), flush=True)
    if capture_motion:
        from PIL import Image
        frames=[Image.open(p).convert('RGB').resize((1024,576)) for p in sorted((root/'motion').glob('frame-*.png'))[2:]]
        frames[0].save(root/'secondary-motion.gif',save_all=True,append_images=frames[1:],duration=90,loop=0,optimize=True)
        print(root/'secondary-motion.gif',flush=True)
finally:
    for name in ("traceback.txt", "errors.txt", "progress.txt"):
        if (root / name).exists():
            print((root / name).read_text(errors="replace")[-6000:], flush=True)
