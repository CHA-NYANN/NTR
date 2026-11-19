"""Reflow the approved SVG geometry. Never vertically squash its ornaments."""
from pathlib import Path
import copy,math,re,sys,xml.etree.ElementTree as ET
import resvg_py
root=Path(__file__).resolve().parents[1]/'game/gui/kouseikan'
out=root/'adaptive'
out.mkdir(exist_ok=True)
NS='http://www.w3.org/2000/svg'
ET.register_namespace('',NS)
def tag(name): return '{'+NS+'}'+name
def path_y(data,delta):
    tokens=re.findall(r'[A-Za-z]|[-+]?(?:\d*\.\d+|\d+)(?:[eE][-+]?\d+)?',data)
    result=[]; command=None; index=0; last_y=0
    lengths={'M':2,'L':2,'H':1,'V':1,'C':6,'S':4,'Q':4,'T':2,'A':7,'Z':0}
    for token in tokens:
        if token.isalpha():
            command=token; index=0; result.append(token); continue
        value=float(token)
        n=lengths[command.upper()]
        axis=index%n
        is_y=(command in ('M','L','C','S','Q','T') and axis%2==1) or command=='V' or (command=='A' and axis==6)
        if command=='H' and last_y>=300: value-=delta*.215
        if is_y: last_y=value
        if is_y and value>=300:
            value+=delta
            if command not in ('V','A'):
                result[-1]=format(float(result[-1])-delta*.215,'.5g')
        result.append(format(value,'.5g')); index+=1
    return ' '.join(result)
def write(name,tree):
    svg=ET.tostring(tree,encoding='unicode')
    (out/(name+'.svg')).write_text(svg,encoding='utf8')
    (out/(name+'.png')).write_bytes(resvg_py.svg_to_bytes(svg_string=svg))
for skin in ('dialogue-yutaka','dialogue-chiasa','dialogue-dark','dialogue-neutral','system-dialogue'):
    if '--system-only' in sys.argv and skin!='system-dialogue': continue
    original=ET.fromstring((root/(skin+'.svg')).read_text(encoding='utf-8-sig'))
    system=skin=='system-dialogue'
    width=1472 if system else 1596
    native_width=float(original.get('width'))
    ratio=width/native_width
    old_h=float(original.get('height'))
    for lines in range(1,12 if system else 15):
        display_h=(320+lines*60) if system else max(250,190+lines*52)
        h=math.ceil(display_h/ratio); delta=h-old_h
        tree=copy.deepcopy(original)
        tree.set('height',str(h)); tree.set('viewBox',f'0 0 {native_width:g} {h}')
        for group in tree:
            for nested in group.findall(tag('svg')):
                nested.set('height',str(h)); nested.set('viewBox',f'0 0 {nested.get("width")} {h}')
        if system:
            for group in list(tree)[:5]:
                for node in group.iter():
                    if node.tag==tag('path'):
                        node.set('d',path_y(node.get('d'),delta))
                    if node.tag==tag('filter'):
                        node.set('height',str(float(node.get('height'))+max(0,delta)))
                    for key in ('y1','y2'):
                        if node.get(key) and float(node.get(key))>=300:
                            node.set(key,str(float(node.get(key))+delta))
            list(tree)[2].set('transform',f'translate(0 {delta:g})')
            # Rear tab follows the lower edge as one intact object.
            original_tab=list(original)[2]
            list(tree)[2].clear()
            list(tree)[2].attrib.update(original_tab.attrib)
            list(tree)[2].set('transform',f'translate(0 {delta:g})')
            for child in original_tab: list(tree)[2].append(copy.deepcopy(child))
        else:
            groups=list(tree)
            next(groups[0].iter(tag('path'))).set('d',f'M34 76L1180 114L1155 {h-16}L67 {h-5}L34 76Z')
            cuts=[cy for cy in (123,189,255,321,387,453,519,585,651) if cy+18<h-36]
            outline=f'M8 56L1115 46L1164 53L1165 111L1144 {h-37}L18 {h-26}L3 {h-36}'
            for cy in reversed(cuts): outline+=f'L4 {cy+17}C24 {cy+8} 24 {cy-8} 4 {cy-17}'
            outline+='L8 56Z'
            next(groups[1].iter(tag('path'))).set('d',outline)
            groups[6].set('transform',f'translate(0 {delta:g})')
            for group in groups[7:]: tree.remove(group)
            for y in range(74,h-48,31):
                hole=copy.deepcopy(groups[7]); hole.set('transform',f'translate(30 {y})'); tree.append(hole)
        write(skin+'-'+str(lines),tree)
print('Built adaptive variants; original SVG/PNG sources unchanged.')
