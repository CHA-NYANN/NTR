"""Run the hand selection in an isolated Ren'Py copy; preserve player saves/drafts."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("sdk", type=Path)
parser.add_argument("output", type=Path, help="New directory for isolated game, saves, captures and reports")
parser.add_argument("--project", type=Path, default=Path(__file__).resolve().parents[1])
parser.add_argument("--overlay", type=Path, help="Optional staged game/ directory to test before installation")
args = parser.parse_args()
sdk, output, project = args.sdk.resolve(), args.output.resolve(), args.project.resolve()
if output.exists():
    raise SystemExit("Choose a new output directory; existing QA data is never overwritten")
game = output / "game"
shutil.copytree(project / "game", game, ignore=shutil.ignore_patterns("saves", "cache", "*.rpyc", "*.rpymc", "*.log"))
if args.overlay:
    shutil.copytree(args.overlay.resolve(), game, dirs_exist_ok=True)
(output / "captures").mkdir()
runtime = sdk / ("lib/py3-windows-x86_64/python.exe" if os.name == "nt" else "lib/py3-linux-x86_64/python")
command = [str(runtime), str(sdk / "renpy.py"), str(output)]
env = dict(os.environ, RENPY_PATH_TO_SAVES=str(output / "isolated-saves"), SDL_AUDIODRIVER="dummy", RENPY_SIMPLE_EXCEPTIONS="1")
options = {"creationflags": subprocess.CREATE_NO_WINDOW} if os.name == "nt" else {}
subprocess.run(command + ["lint", str(output / "lint.txt")], env=env, check=True, timeout=180, **options)
report = (output / "lint.txt").read_text(encoding="utf-8-sig")
if "Statistics:" not in report or "game/" in report.split("Statistics:")[0]:
    raise SystemExit("Ren'Py lint reported issues; inspect " + str(output / "lint.txt"))

source = game / "zzz_kk_secondary.rpy"
text = source.read_text(encoding="utf-8-sig")
needle = "screen kk_route_select():\n"
assert text.count(needle) == 1
source.write_text(text.replace(needle, needle + '    timer .05 repeat True action Function(kh_tick, _update_screens=False)\n'), encoding="utf-8")
(game / "zzzzz_hand_qa.rpy").write_text(r'''
init offset = 100
init 100 python:
    import os
    import time
    kh_started = None
    kh_clicked = None
    kh_captures = set()
    kh_frames = set()
    kh_case = 0
    kh_cases = [("yutaka",True,(1920,1080)),("chiasa",True,(1280,720)),("yutaka",False,(1366,768)),("chiasa",False,(1366,768)),("yutaka",True,(1280,720))]

    def kh_tick():
        global kh_started, kh_clicked
        now = time.monotonic()
        if kh_started is None: kh_started = now
        scope = renpy.get_screen("kk_route_select").scope
        selected = scope["selected"]
        host, motion, requested_size = kh_cases[kh_case]
        stem = "%02d-%s-%s" % (kh_case,host,"motion" if motion else "still")
        if selected is None:
            if "idle" not in kh_captures and now-kh_started > .15:
                kh_captures.add("idle")
                renpy.screenshot(os.path.join(config.basedir,"captures",stem+"-idle.png"))
                scene = renpy.get_displayable("kk_route_select","ks_hand_scene")
                assert renpy.render(scene,1920,1080,0,0).get_size() == (1920,1080)
                for target in ("yutaka","chiasa"):
                    button = renpy.get_displayable("kk_route_select","ks_hand_"+target)
                    assert button.is_sensitive(), target
                    assert button.style.focus_mask not in (True,None), "Explicit alpha mask required"
                    x,y,w,h,_ = KS_HAND_BOUNDS[target]
                    assert x>=0 and x+w<=1920 and y+h<=1080
                    mask = renpy.render(button.style.focus_mask,w,h,0,0)
                    assert mask.get_size()==(w,h), mask.get_size()
                    assert not mask.is_pixel_opaque(w-1,h-1), "Background must not be clickable"
                    assert any(mask.is_pixel_opaque(px,py) for px in range(w//3,2*w//3,15) for py in range(h//3,2*h//3,15)), "Hand must be clickable"
            # Waiting longer than the animation tests that its clock starts at click.
            if now-kh_started > (2.1 if kh_case==4 else .35) and kh_clicked is None:
                kh_clicked = now
                renpy.set_focus("kk_route_select","ks_hand_"+host)
                renpy.queue_event("button_select")
            return
        assert selected == host, (selected,host)
        frame = scope["selected_frame"]
        if not kh_frames:
            assert frame < 4, "Animation must start from the beginning after click"
        kh_frames.add(frame)
        assert kk_host is None, "Host state must remain unchanged until the screen returns"
        for target in ("yutaka","chiasa"):
            assert not renpy.get_displayable("kk_route_select","ks_hand_"+target).is_sensitive(), "Both choices must lock after selection"
        elapsed = now-kh_clicked
        tag = "mid" if motion and frame<16 else "final"
        capture_ready = frame>=8 if tag=="mid" else frame>=16 if motion else elapsed>=.1
        if capture_ready and tag not in kh_captures:
            kh_captures.add(tag)
            renpy.screenshot(os.path.join(config.basedir,"captures",stem+"-"+tag+".png"))

screen main_menu():
    timer .1 action Start("kh_review")

label kh_review:
    $ _preferences.text_cps = 0
    $ kk_host = None
    while kh_case < len(kh_cases):
        $ kh_started = None
        $ kh_clicked = None
        $ kh_captures = set()
        $ kh_frames = set()
        $ persistent.kk_secondary_motion = kh_cases[kh_case][1]
        $ renpy.set_physical_size(kh_cases[kh_case][2])
        call screen kk_route_select
        $ assert _return == kh_cases[kh_case][0], (_return,kh_case)
        $ elapsed = time.monotonic()-kh_clicked
        $ minimum = KS_HAND_DURATION if persistent.kk_secondary_motion else .25
        $ assert elapsed >= minimum-.07, (elapsed,minimum)
        $ assert "final" in kh_captures, kh_captures
        if persistent.kk_secondary_motion:
            $ assert max(kh_frames)==19, kh_frames
            $ assert len(kh_frames)>=16, kh_frames
        $ open(os.path.join(config.basedir,"timing.txt"),"a").write(str((kh_cases[kh_case],elapsed,renpy.get_physical_size()))+"\n")
        $ kh_case += 1
    $ open(os.path.join(config.basedir,"review.ok"),"w").write("PASS: both host returns, real button selection, contour masks, locked choices, 20 frames/12 FPS, last-pose hold, reduced motion, repeat visit and three viewport requests")
    $ renpy.quit()
''', encoding="utf-8")
try:
    subprocess.run(command, env=env, check=True, timeout=180, **options)
    assert (output / "review.ok").exists(), "Hand selection QA did not finish"
    print((output / "review.ok").read_text(), flush=True)
    print(output, flush=True)
finally:
    for name in ("traceback.txt", "errors.txt"):
        if (output / name).exists():
            print((output / name).read_text(errors="replace")[-6000:], flush=True)
