"""Check a save made by an earlier Windows playtest ZIP. Use trusted local builds only."""
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

project = Path(__file__).resolve().parents[1]
sdk = Path(sys.argv[1]).resolve()
old_zip = Path(sys.argv[2]).resolve()
runtime = sdk / ("lib/py3-windows-x86_64/python.exe" if os.name == "nt" else "lib/py3-linux-x86_64/python")

with tempfile.TemporaryDirectory(prefix="kk-save-upgrade-") as temp:
    work = Path(temp)
    with zipfile.ZipFile(old_zip) as archive:
        for name in archive.namelist():
            parts = Path(name).parts
            if len(parts) < 3 or parts[1] != "game" or archive.getinfo(name).is_dir():
                continue
            if any(part in ("..", "saves", "cache") or ":" in part for part in parts):
                continue
            target = work / "before" / Path(*parts[1:])
            if target.suffix in (".rpyc", ".rpymc"):
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(archive.read(name))
    shutil.copytree(project / "game", work/"after"/"game", ignore=shutil.ignore_patterns("saves","cache","*.rpyc","*.rpymc"))
    for phase in ("before", "after"):
        base = work / phase
        game = base / "game"
        for filename, names in (("screens.rpy",("main_menu","kk_route_select","say","kk_titlecard","kk_choice_panel")),("kk_world.rpy",("kk_world_district",))):
            p = game / filename
            src = p.read_text(encoding="utf-8-sig")
            for name in names:
                src = re.sub(r"(^screen "+name+r"\([^\n]*\):\n(?:    (?:tag menu|tag kk_world|modal True)\n)*)",
                             lambda m:m[0]+'    timer .15 repeat True action Function(kk_upgrade_check, "'+name+'", _update_screens=False)\n',src,flags=re.M)
            p.write_text(src,encoding="utf8")
        (game/"zz_migration.rpy").write_text("""
init 999 python:
    import os
    config.savedir = os.environ["KK_MIGRATION_SAVE"]
    def kk_upgrade_check(name):
        phase = os.environ["KK_PHASE"]
        if name == "main_menu":
            if phase == "before":
                return renpy.run(Start())
            renpy.load("migration-1")
        elif name == "kk_titlecard":
            return renpy.run(Return())
        elif name == "kk_route_select":
            return renpy.run(Return("yutaka"))
        elif name == "kk_choice_panel":
            screen = renpy.get_screen(name)
            if screen:
                return renpy.run(screen.scope["rows"][0][1])
        elif name == "say":
            renpy.queue_event("dismiss")
        elif name == "kk_world_district":
            assert kk_host == "yutaka" and kk_done("Y01") and saldo == 500000
            if phase == "before":
                renpy.save("migration-1")
            else:
                assert kk_phone_mode == "normal" and not kk_priority_contacts
                assert kk_rest_energy_minutes == 0 and kk_harumi_ending() is None
            with open(os.path.join(config.basedir, "verified"), "w") as out:
                out.write(repr((kk_host, saldo, kk_bulan, kk_hari_n, list(choices_log))))
            renpy.quit()
""",encoding="utf8")
        env = dict(os.environ, KK_PHASE=phase, KK_MIGRATION_SAVE=str(work/"save"), RENPY_PATH_TO_SAVES=str(work/"userdata"),
                   RENPY_SIMPLE_EXCEPTIONS="1", SDL_AUDIODRIVER="dummy", RENPY_PERFORMANCE_TEST="0")
        try:
            subprocess.run([str(runtime),str(sdk/"renpy.py"),str(base)],env=env,timeout=90,check=True)
            assert (base/"verified").is_file()
        except Exception:
            for name in ("traceback.txt","errors.txt"):
                if (base/name).exists():
                    print((base/name).read_text(errors="replace")[-1600:])
            raise
    assert (work/"before"/"verified").read_bytes() == (work/"after"/"verified").read_bytes()
    print("Save upgrade OK: host, balance, date and opening choice restored at district screen")

