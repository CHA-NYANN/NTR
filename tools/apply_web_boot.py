"""Apply Kouseikan's startup shell AFTER exporting a Ren'Py web build.

Usage: python tools/apply_web_boot.py path/to/exported-web-directory
No engine, game archive, service worker, or browser save data is modified.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil


SOURCE = Path(__file__).resolve().parent / "web_boot"
REQUIRED_IDS = (
    "canvas", "overlayDiv", "presplash", "statusDiv", "statusTextDiv",
    "statusProgress", "inputDiv", "inputForm", "inputPrompt", "inputText",
    "ContextContainer", "ContextButton", "ContextMenu", "ID_SavegamesImport",
)


def block(name: str, contents: str) -> str:
    return f"<!-- KK_{name}_START -->\n{contents}\n<!-- KK_{name}_END -->"


def replace_block(html: str, name: str, contents: str) -> tuple[str, bool]:
    pattern = rf"<!-- KK_{name}_START -->.*?<!-- KK_{name}_END -->"
    updated, count = re.subn(pattern, lambda _: block(name, contents), html, flags=re.S)
    if count > 1:
        raise ValueError(f"Duplicate Kouseikan {name} blocks; index.html was not modified")
    return updated, bool(count)


def apply(export: Path) -> str:
    export = export.resolve(strict=True)
    index = export / "index.html"
    html = index.read_text(encoding="utf-8")
    originals = {name: html.count(f'id="{name}"') for name in REQUIRED_IDS}
    if any(value != 1 for value in originals.values()):
        raise ValueError("Expected one of each Ren'Py DOM hook; refusing an incompatible export")
    if not re.search(r'<script\b[^>]*src=[\"\']renpy-pre\.js[\"\']', html):
        raise ValueError("renpy-pre.js must remain before the branded loader")

    files = sorted(path for path in SOURCE.rglob("*") if path.is_file())
    for required in ("boot.html", "boot.css", "boot.js", "assets/studio-logo.jpg",
                     "assets/Tinos-Italic.ttf", "assets/Nunito.ttf"):
        if not (SOURCE / required).is_file():
            raise ValueError(f"Missing startup source: {required}")
    digest = hashlib.sha256()
    for path in files:
        digest.update(path.relative_to(SOURCE).as_posix().encode())
        digest.update(path.read_bytes())
    version = digest.hexdigest()[:12]

    existing_config = re.search(r'<script id="kkBootConfig"[^>]*>(.*?)</script>', html, re.S)
    if existing_config:
        engine = json.loads(existing_config[1])["engine"]
    else:
        engine_match = re.search(r'<script\b(?=[^>]*\bsrc=[\"\'](renpy\.js(?:\?[^\"\']*)?)[\"\'])[^>]*>\s*</script>', html)
        if not engine_match:
            raise ValueError("Could not locate the Ren'Py engine script; export was not modified")
        engine = engine_match[1]
    config = json.dumps({"engine": engine}, ensure_ascii=True).replace("<", "\\u003c")
    head = f'<link rel="stylesheet" href="boot/boot.css?v={version}">\n<link rel="preload" href="{engine}" as="script">'
    html, found = replace_block(html, "HEAD", head)
    if not found:
        html = html.replace("</head>", block("HEAD", head) + "\n</head>", 1)
    markup = '<div id="presplash" hidden></div>\n' + (SOURCE / "boot.html").read_text(encoding="utf-8")
    html, found = replace_block(html, "VIEW", markup)
    if not found:
        html, count = re.subn(r'<img\b(?=[^>]*\bid=[\"\']presplash[\"\'])[^>]*>', lambda _: block("VIEW", markup), html)
        if count != 1:
            raise ValueError("Unsupported presplash element; export was not modified")
    scripts = f'<script id="kkBootConfig" type="application/json">{config}</script>\n<script src="boot/boot.js?v={version}"></script>'
    html, found = replace_block(html, "ENGINE", scripts)
    if not found:
        html, count = re.subn(r'<script\b(?=[^>]*\bsrc=[\"\']renpy\.js(?:\?[^\"\']*)?[\"\'])[^>]*>\s*</script>', lambda _: block("ENGINE", scripts), html)
        if count != 1:
            raise ValueError("Unexpected engine script count; export was not modified")
    if any(html.count(f'id="{name}"') != 1 for name in REQUIRED_IDS):
        raise ValueError("A Ren'Py DOM hook would be lost; export was not modified")
    if html.index('src="renpy-pre.js"') > html.index('id="kkBootConfig"'):
        raise ValueError("renpy-pre.js must load before boot.js")

    catalog_path = export / "pwa_catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8")) if catalog_path.exists() else None
    assets = [path for path in files if path.name in ("boot.css", "boot.js")
              or path.relative_to(SOURCE).parts[0] == "assets"]
    if catalog is not None:
        catalog["files"] = list(dict.fromkeys(catalog["files"] + ["boot/" + p.relative_to(SOURCE).as_posix() for p in assets]))
        catalog["version"] = int(version[:10], 16)
    # Validate everything before writing. Keep unrelated files and engine binaries intact.
    for path in assets:
        target = export / "boot" / path.relative_to(SOURCE)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
    index.write_text(html, encoding="utf-8", newline="\n")
    if catalog is not None:
        catalog_path.write_text(json.dumps(catalog, ensure_ascii=False) + "\n", encoding="utf-8")
    return version


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("export", type=Path, help="Ren'Py web export containing index.html")
    args = parser.parse_args()
    print(f"Applied Kouseikan startup {apply(args.export)} to {args.export.resolve()}")
