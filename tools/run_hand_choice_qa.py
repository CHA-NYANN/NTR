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
def qa_ignore(directory, names):
    ignored = set(shutil.ignore_patterns("saves", "cache", "*.rpyc", "*.rpymc", "*.log")(directory,names))
    if Path(directory).resolve() == (project/"game/gui/kouseikan/hand-choice").resolve():
        ignored.add("animation")  # Prove the new implementation runs without the old frames.
    return ignored
shutil.copytree(project / "game", game, ignore=qa_ignore)
if args.overlay:
    shutil.copytree(args.overlay.resolve(), game, dirs_exist_ok=True)
(output / "captures").mkdir()
assert not (game / "gui/kouseikan/hand-choice/animation").exists()
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
    kh_positions = []
    kh_case = 0
    kh_cases = [("yutaka",True,(1920,1080)),("chiasa",True,(1280,720)),("yutaka",False,(1366,768)),("chiasa",False,(1366,768)),("yutaka",True,(1280,720))]

    def kh_motion_wrapper(host):
        base = renpy.get_displayable("kk_route_select","ks_player_reach_"+host)
        pending = [renpy.get_screen("kk_route_select").child]
        seen = set()
        while pending:
            item = pending.pop()
            if id(item) in seen: continue
            seen.add(id(item))
            if getattr(item,"child",None) is base and item.get_placement()[1] is not None:
                return item
            pending.extend(item.visit())
        raise AssertionError("No positioned ATL wrapper for player hand")

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
                assert ("game/gui/kouseikan/hand-choice/animation/**",None) in build.base_patterns
            # Waiting longer than the animation tests that its clock starts at click.
            if now-kh_started > (2.1 if kh_case==4 else .35) and kh_clicked is None:
                kh_clicked = now
                renpy.set_focus("kk_route_select","ks_hand_"+host)
                renpy.queue_event("button_select")
            return
        assert selected == host, (selected,host)
        overlay = kh_motion_wrapper(host)
        x,y = overlay.get_placement()[:2]
        x = absolute.compute_raw(x,1920)
        y = absolute.compute_raw(y,1080)
        final_x,final_y,w,h,start_x = KS_PLAYER_HANDS[host]
        if not kh_positions and motion:
            assert y>final_y+100, ("Movement must start after click",x,y)
        if kh_positions and motion:
            assert y<=kh_positions[-1][1]+1, ("Reach must move upward",kh_positions[-1],(x,y))
        kh_positions.append((x,y))
        assert kk_host is None, "Host state must remain unchanged until the screen returns"
        for target in ("yutaka","chiasa"):
            assert not renpy.get_displayable("kk_route_select","ks_hand_"+target).is_sensitive(), "Both choices must lock after selection"
        elapsed = now-kh_clicked
        final_pose = abs(x-final_x)<1 and abs(y-final_y)<1
        tag = "final" if final_pose else "mid"
        capture_ready = final_pose or (motion and final_y+60<y<1040)
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
        $ kh_positions = []
        $ persistent.kk_secondary_motion = kh_cases[kh_case][1]
        $ renpy.set_physical_size(kh_cases[kh_case][2])
        call screen kk_route_select
        $ assert _return == kh_cases[kh_case][0], (_return,kh_case)
        $ elapsed = time.monotonic()-kh_clicked
        $ minimum = KS_HAND_DURATION if persistent.kk_secondary_motion else .25
        $ assert elapsed >= minimum-.07, (elapsed,minimum)
        $ assert "final" in kh_captures, kh_captures
        if persistent.kk_secondary_motion:
            $ assert len(set(kh_positions))>=8, kh_positions
        $ open(os.path.join(config.basedir,"timing.txt"),"a").write(str((kh_cases[kh_case],elapsed,renpy.get_physical_size()))+"\n")
        $ kh_case += 1
    $ open(os.path.join(config.basedir,"review.ok"),"w").write("PASS: both host returns, real button selection, contour masks, locked choices, PNG position tween and final pose, reduced motion, delayed selection, repeat visit, three viewport requests; old animation frames absent")
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
