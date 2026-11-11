"""Cross-check the hand-authored scheduler against the generated catalogue and audit."""
import ast
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
game = root / "game"


def source(name):
    return (game / name).read_text(encoding="utf-8-sig")


def audit(name, key, connected, coverage):
    script = source("kk_data_kk_" + name + ".rpy")
    rows = ast.literal_eval(script.split(" = ", 1)[1].strip())
    ids = [entry[key] for entry in rows]
    assert len(set(ids)) == len(ids), "Duplicate catalogue ID in " + name
    assert connected <= set(ids), "Unknown scheduled IDs: " + str(connected - set(ids))
    for eid in ids:
        matches = re.findall(r"^\| " + re.escape(eid) + r" \| ([^|]+) \|", coverage, re.M)
        assert len(matches) == 1, "Missing or duplicate coverage row: " + eid
        if eid in connected:
            assert matches[0].strip() in ("implemented", "partial"), eid
    assert f"{len(connected)} dari {len(ids)} ID" in coverage, "Coverage count: " + name
    print(f"{name}: {len(connected)}/{len(ids)}")


def verify():
    coverage = (root / "docs/Sandbox_Coverage.md").read_text(encoding="utf-8-sig")
    world = source("kk_world.rpy")
    assignment = re.search(r"^    KK_MILESTONE_MAP = (\[.*?^    \])", world, re.M | re.S)
    assert assignment, "Missing world milestone map"
    entries = ast.literal_eval(assignment[1])
    scheduled = {row[0] for row in entries}
    assert len(entries) == len(scheduled), "Duplicate world milestone"
    scenes = set()
    for script in game.glob("*.rpy"):
        scenes.update(re.findall(r"^label kkscene_(\w+):", source(script.name), re.M))
    assert scheduled <= scenes, "No cinematic scene: " + str(scheduled - scenes)
    audit("events_main", "id", scheduled | {"C01", "Y01"}, coverage)
    dynamic = set(re.findall(r'"([A-Za-z]+-D\d+)"', source("kk_life_events.rpy")))
    audit("events_dyn", "id", dynamic, coverage)
    resolvers = ("kk_engine.rpy", "kk_family.rpy", "kk_life_events.rpy", "kk_harumi.rpy")
    endings = set(re.findall(r'"(E-[A-Z]+-\d+)"', "\n".join(source(n) for n in resolvers)))
    audit("endings", "code", endings, coverage)


if __name__ == "__main__":
    verify()

