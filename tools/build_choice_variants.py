"""Grow approved choice paper edges; keep the circular perforations intact."""
from pathlib import Path
import copy,math,xml.etree.ElementTree as ET
import resvg_py
root=Path(__file__).resolve().parents[1]/'game/gui/kouseikan'
out=root/'adaptive'; out.mkdir(exist_ok=True)
NS='http://www.w3.org/2000/svg'; ET.register_namespace('',NS)
def tag(n): return '{'+NS+'}'+n
for skin in ('choice-idle','choice-hover'):
    original=ET.fromstring((root/(skin+'.svg')).read_text(encoding='utf-8-sig'))
    for lines in range(1,7):
        h=math.ceil(max(84,36+lines*44)*650/740)
        tree=copy.deepcopy(original)
        tree.set('height',str(h)); tree.set('viewBox',f'0 0 650 {h}')
        groups=list(tree)
        for group in groups:
            nested=group.find(tag('svg'))
            if nested is not None and nested.get('width')=='650':
                nested.set('height',str(h)); nested.set('viewBox',f'0 0 650 {h}')
        next(groups[0].iter(tag('path'))).set('d',f'M10 4H618L643 7L627 {h-6}H2L10 4Z')
        for group in groups[2:5]: tree.remove(group)
        for y in range(13,h-13,14):
            hole=copy.deepcopy(groups[2]);hole.set('transform',f'translate({13-(y-13)*.12:g} {y})');tree.append(hole)
        svg=ET.tostring(tree,encoding='unicode')
        (out/(skin+'-'+str(lines)+'.svg')).write_text(svg,encoding='utf8')
        (out/(skin+'-'+str(lines)+'.png')).write_bytes(resvg_py.svg_to_bytes(svg_string=svg))
print('Built 12 choice variants from the approved source art.')
