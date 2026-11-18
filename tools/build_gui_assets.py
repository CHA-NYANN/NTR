"""Render the original Figma vector decorations; keep all game text native."""
from pathlib import Path
import copy
import io
import json
import math
import re
import shutil
import xml.etree.ElementTree as ET

from PIL import Image
import resvg_py

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "game/gui/kouseikan"
SOURCE = ROOT.parent / "fixed-gui-assets"
OUT.mkdir(parents=True, exist_ok=True)

def render(name, body, width, height):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">{body}</svg>'
    (OUT / (name + ".svg")).write_text(svg, encoding="utf8")
    (OUT / (name + ".png")).write_bytes(resvg_py.svg_to_bytes(svg_string=svg))

for file in (ROOT / "tools/figma-art").glob("*.json"):
    data = json.loads(file.read_text(encoding="utf8"))
    parts = []
    extent_x, extent_y = data["width"], data["height"]
    for index, layer in enumerate(data["layers"]):
        svg = layer["svg"]
        svg_root = ET.fromstring(svg)
        extent_x = max(extent_x, layer["x"] + float(svg_root.attrib.get("width", 0)))
        extent_y = max(extent_y, layer["y"] + float(svg_root.attrib.get("height", 0)))
        ids = re.findall(r'\bid="([^"]+)"', svg)
        for ident in sorted(set(ids), key=len, reverse=True):
            new = f"a{index}_{ident}"
            svg = svg.replace(f'id="{ident}"', f'id="{new}"').replace(f"#{ident})", f"#{new})").replace(f'href="#{ident}"', f'href="#{new}"')
        parts.append(f'<g transform="translate({layer["x"]} {layer["y"]})">{svg}</g>')
    # Figma effects can extend the exported child beyond the parent's bounds.
    render(data["name"], "".join(parts), math.ceil(extent_x), math.ceil(extent_y))

for item in json.loads((ROOT / "tools/icons.json").read_text(encoding="utf8")):
    png = resvg_py.svg_to_bytes(svg_string=item["svg"], width=80, height=80)
    (OUT / ("icon-" + item["name"] + ".png")).write_bytes(png)

for src, dest in [(SOURCE / "main-art-clean.png", "main-art.png"),
                  (SOURCE / "yutaka-wallpaper-clean.png", "phone-yutaka.png"),
                  (SOURCE / "map/city-illustration-v2.png", "city.png")]:
    if src.exists():
        shutil.copy2(src, OUT / dest)
    elif not (OUT / dest).exists():
        raise FileNotFoundError(f"Missing illustration: {src}. Restore {dest} from version control.")

paper = '<path d="M7 13 82 3 270 9 470 2 690 10 896 3 994 11 998 170 990 340 997 500 989 592 764 598 570 591 348 599 107 592 3 597 10 400 1 205Z" fill="#FFF2FA" stroke="#D5BDD8" stroke-width="2"/><path d="M33 29v540" stroke="#E7B5D5" stroke-width="1.5"/>'
render("paper-panel", paper, 1000, 600)
for name, fill in [("ribbon", "#F5E6F2"), ("ribbon-hover", "#E8C5EA"), ("ribbon-selected", "#C3ACDF"), ("ribbon-disabled", "#D9D0DF")]:
    render(name, f'<path d="M14 5 586 1 598 17 578 84 3 89 12 50 5 29Z" fill="{fill}" stroke="#BBA0CC" stroke-width="2"/><path d="M22 13v58" stroke="#FFF9FF" stroke-width="2" stroke-dasharray="4 5"/>', 600, 94)
render("tool-tag", '<path d="M8 8 87 1 98 20 88 77 2 84 7 46 2 27Z" fill="#5B3D85" stroke="#C4A7EB" stroke-width="2"/><path d="M16 17v50" stroke="#DCC4FF" stroke-dasharray="3 4"/><path d="m26 2 18-2 15 13-22 4Z" fill="#D8B6E9"/>', 100, 86)
render("star-thumb", '<path d="M21 2 34 8 40 23 32 39 14 42 3 24 8 8Z" fill="#FFF5FC" stroke="#B685BC" stroke-width="2"/><path d="M21 12q-1 9-9 11 9 1 10 10 1-9 9-11-9-1-10-10Z" fill="#D387BE"/>', 44, 44)
render("map-label", '<path d="M22 3H430q20 0 12 23l-15 49q-4 13-20 13H17Q1 88 8 67l10-48q3-16 4-16Z" fill="#FFF3F7" stroke="#AD8DC5" stroke-width="2"/><circle cx="48" cy="45" r="27" fill="#9470B5"/>', 450, 92)
render("phone-frame", '<defs><linearGradient id="rim" x2="1" y2="1"><stop stop-color="#B8DFFF"/><stop offset=".45" stop-color="#F7F2FF"/><stop offset="1" stop-color="#A27BCF"/></linearGradient></defs><rect x="27" y="5" width="526" height="934" rx="79" fill="url(#rim)" stroke="#9AB2D1" stroke-width="4"/><rect x="40" y="18" width="500" height="910" rx="66" fill="#2E2549"/><path d="M206 38h164v16q0 22-21 22H228q-22 0-22-22Z" fill="#201B31"/>', 580, 950)

for path in OUT.glob("*.png"):
    with Image.open(path) as im:
        im.verify()
manifest = {"source": "Original editable Figma decorations exported without text", "assets": sorted(p.name for p in OUT.glob("*.png")), "runtime_canvas": [1920, 1080], "fonts": [p.name for p in (OUT / "fonts").glob("*.ttf")]}
(OUT / "provenance.json").write_text(json.dumps(manifest, indent=2), encoding="utf8")
print(f"Rendered {len(manifest['assets'])} GUI assets")
