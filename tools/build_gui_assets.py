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

# A neutral opening identity, before the player has chosen a host.
neutral_colors = {
    "#A7A1DE":"#ACADB0", "#827FC9":"#797B82", "#66A2E2":"#B89B35",
    "#379FED":"#E0BB45", "#8A39D5":"#989BA2", "#E8D7F0":"#D4D4D1",
    "#FFF7FE":"#F4F4EF", "#F4E9FF":"#E8E8E3", "#CDB2EB":"#BCBDB8",
    "#F1DDFF":"#E8E2BD", "#B98AE8":"#D7BE63", "#D8BAEC":"#D9D1AC",
    "#58B2F5":"#E5C74F", "#FFF0FD":"#FFF8DA", "#343485":"#53565E",
    "#EFE8FF":"#F5F2DF",
}
neutral = (OUT / "dialogue-yutaka.svg").read_text(encoding="utf8")
neutral = re.sub(r"#[0-9A-Fa-f]{6}", lambda m: neutral_colors.get(m[0].upper(),m[0]), neutral)
(OUT / "dialogue-neutral.svg").write_text(neutral, encoding="utf8")
(OUT / "dialogue-neutral.png").write_bytes(resvg_py.svg_to_bytes(svg_string=neutral))
tag = (OUT / "tool-tag.svg").read_text(encoding="utf8")
for old, new in {"#5B3D85":"#5B5E66", "#C4A7EB":"#CFCFD2", "#DCC4FF":"#EFEDE6", "#D8B6E9":"#E7C963"}.items():
    tag = tag.replace(old,new)
(OUT / "tool-tag-neutral.svg").write_text(tag,encoding="utf8")
(OUT / "tool-tag-neutral.png").write_bytes(resvg_py.svg_to_bytes(svg_string=tag))

# The original map decoration was a cropped phone peek. These complete vector
# handsets include safe margins so the whole shape fits inside a clickable area.
phone_icon = next(item["svg"] for item in json.loads((ROOT / "tools/icons.json").read_text(encoding="utf8")) if item["name"] == "phone")
icon = ET.fromstring(phone_icon)
icon.set("x","53")
icon.set("y","101")
icon.set("width","76")
icon.set("height","76")
symbol = ET.tostring(icon,encoding="unicode")
for name,side,rim,screen,line,notch in [
    ("phone-launch-full","#DB87D5","#CEB7F9","#59469B","#F8F2FF","#201844"),
    ("phone-launch-neutral","#D9BB54","#E5E3D6","#5A5D64","#FFF5CB","#303238"),
]:
    body = f'''<path d="m196 18 7-9m-2 27 13-2" stroke="{line}" stroke-width="5" stroke-linecap="round"/>
    <g transform="translate(37 17) rotate(7 78 136)">
    <rect x="12" y="10" width="156" height="270" rx="28" fill="{side}"/>
    <rect x="0" y="0" width="156" height="270" rx="28" fill="{rim}" stroke="{line}" stroke-width="3"/>
    <rect x="9" y="10" width="138" height="250" rx="21" fill="{screen}"/>
    <path d="M47 10h64v9q0 9-10 9H57q-10 0-10-9Z" fill="{notch}"/>
    <path d="M20 58V40q0-16 16-16" fill="none" stroke="{line}" stroke-width="4" stroke-linecap="round" opacity=".7"/>
    <circle cx="78" cy="140" r="49" fill="none" stroke="{line}" stroke-width="2" opacity=".55"/>
    {re.sub(r'#[0-9A-Fa-f]{6}',lambda m:line,symbol) if name.endswith('neutral') else symbol}<path d="M56 247h45" stroke="{line}" stroke-width="4" stroke-linecap="round"/>
    </g>'''
    render(name,body,240,320)
render("phone-neutral", '<defs><linearGradient id="wall" x2=".8" y2="1"><stop stop-color="#F1F0E8"/><stop offset="1" stop-color="#C8CACE"/></linearGradient></defs><rect width="501" height="875" fill="url(#wall)"/><circle cx="430" cy="690" r="214" fill="#DBC45E" opacity=".45"/><circle cx="63" cy="808" r="140" fill="#E8E1B8"/><path d="m403 495 10 29 29 10-29 10-10 29-10-29-29-10 29-10Z" fill="#FFF7D8"/><path d="M-45 580Q240 440 540 635" fill="none" stroke="#FFFFFF" stroke-width="3" opacity=".5"/>',501,875)

for path in OUT.glob("*.png"):
    with Image.open(path) as im:
        im.verify()
manifest = {"source": "Editable Figma decorations and native SVG variants, without game text", "variants": {"dialogue-neutral":"Gray/yellow palette of dialogue-yutaka before host selection", "phone-launch-full":"Complete native SVG handset using the Figma phone symbol", "phone-launch-neutral":"Gray/yellow complete handset", "tool-tag-neutral":"Gray/yellow controls before host selection", "phone-neutral":"Neutral vector wallpaper before host selection"}, "assets": sorted(p.name for p in OUT.glob("*.png")), "runtime_canvas": [1920, 1080], "fonts": [p.name for p in (OUT / "fonts").glob("*.ttf")]}
(OUT / "provenance.json").write_text(json.dumps(manifest, indent=2), encoding="utf8")
print(f"Rendered {len(manifest['assets'])} GUI assets")
