"""Run isolated desktop integration tests: python tests/run_living.py <renpy-sdk>."""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

project = Path(__file__).resolve().parents[1]
sdk = Path(sys.argv[1]).resolve()
exe = sdk / ("lib/py3-windows-x86_64/python.exe" if os.name == "nt" else "lib/py3-linux-x86_64/python")
with tempfile.TemporaryDirectory(prefix="kouseikan-playtest-") as temp:
    root = Path(temp)
    game = root / "game"
    shutil.copytree(project/"game", game, ignore=shutil.ignore_patterns("saves","cache","*.rpyc","*.rpymc","*.log"))
    capture = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else None
    sizes = ("1280x720","1366x768","1920x1080") if capture else ()
    if capture:
        capture.mkdir(parents=True,exist_ok=True)
    runs = [("chiasa", size) for size in sizes] if capture else [("yutaka",None),("chiasa",None),("chiasa",None)]
    for seq,(host,size) in enumerate(runs):
        env = dict(os.environ, RENPY_PATH_TO_SAVES=str(root/(host+"-"+str(seq))), KK_HOST=host,
                   RENPY_SIMPLE_EXCEPTIONS="1", RENPY_PERFORMANCE_TEST="0", SDL_AUDIODRIVER="dummy")
        if not size and seq == 2:
            env["KK_ART_WIN"] = "1"
        if size:
            env.update(KK_CAPTURE=str(capture), KK_SIZE=size, RENPY_HIGHDPI="1")
        command = [str(exe),str(sdk/"renpy.py"),str(root)]
        if seq == 0:
            report = root/"lint.txt"
            subprocess.run(command+["lint",str(report)],env=env,check=True,timeout=120)
            lint=report.read_text(encoding="utf-8-sig")
            if "Statistics:" not in lint or "game/" in lint.split("Statistics:")[0]:
                raise AssertionError(lint)
            print(lint, flush=True)
            shutil.copy(project/"tests/sandbox_scenario.rpy",game/"zz_sandbox_test.rpy")
            # Drive real interactions in the temporary project only.
            screens = game/"screens.rpy"
            src = screens.read_text(encoding="utf-8-sig")
            for name in ("main_menu","say","choice","kk_route_select","kk_choice_panel","kk_ending_card","kk_titlecard","kk_wallet"):
                import re
                src = re.sub(r"(^screen "+name+r"\([^\n]*\):\n(?:    (?:tag menu|modal True)\n)*)",
                             lambda m:m[0]+'    timer .12 repeat True action Function(kk_test_input, "'+name+'", _update_screens=False)\n',src,flags=re.M)
            screens.write_text(src,encoding="utf8")
            world = game/"kk_world.rpy"
            src = world.read_text(encoding="utf-8-sig")
            for name in ("kk_world_district","kk_world_location","kk_location_view"):
                src = re.sub(r"(^screen "+name+r"\([^\n]*\):\n    tag kk_world\n)",
                             lambda m:m[0]+'    timer .12 repeat True action Function(kk_test_input, "'+name+'", _update_screens=False)\n',src,flags=re.M)
            for token, variable in (('Return(("go", did))','did'),('Return(lokasi)','lokasi'),('Return(("talk", cid))','cid')):
                src = src.replace("action "+token,'id ("qa_" + '+variable+') action '+token)
            world.write_text(src,encoding="utf8")
        try:
            subprocess.run(command,env=env,check=True,timeout=120)
            result=root/((size or ("artist" if seq == 2 else host))+".ok")
            assert result.is_file(), "Game exited before test completion"
            print(result.read_text(),flush=True)
        except Exception:
            for file in ("traceback.txt","errors.txt","log.txt","progress.txt"):
                if (root/file).exists(): print((root/file).read_text(errors="replace")[-5500:],flush=True)
            raise

