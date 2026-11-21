"""Render the owner's icon-only main-menu row from existing vector symbols."""
from pathlib import Path
import json,math,xml.etree.ElementTree as ET
import resvg_py
root=Path(__file__).resolve().parents[1]
out=root/'game/gui/kouseikan/main-icons';out.mkdir(parents=True,exist_ok=True)
symbols={item['name']:item['svg'] for item in json.loads((root/'tools/icons.json').read_text(encoding='utf8'))}
def symbol(name,color):
    icon=ET.fromstring(symbols[name]);icon.set('x','28');icon.set('y','28');icon.set('width','48');icon.set('height','48')
    for node in icon.iter():
        for prop in ('stroke','fill'):
            if node.get(prop) and node.get(prop)!='none':node.set(prop,color)
    return ET.tostring(icon,encoding='unicode')
def seal():
    points=[]
    for i in range(24):
        angle=math.tau*i/24-math.pi/2
        radius=46 if i%2==0 else 41
        points.append((52+radius*math.cos(angle),52+radius*math.sin(angle)))
    mid=lambda a,b:((a[0]+b[0])/2,(a[1]+b[1])/2)
    start=mid(points[-1],points[0]);d='M%.3f %.3f'%start
    for i,p in enumerate(points):
        end=mid(p,points[(i+1)%len(points)])
        d+='Q%.3f %.3f %.3f %.3f'%(*p,*end)
    return '<path d="'+d+'Z" fill="#70568E" stroke="#FFF0FE" stroke-width="2.4"/>'
paper='M19 18 31 13 42 16 52 11 64 15 77 12 88 19 95 25 91 37 96 47 91 59 95 71 89 82 93 94 80 98 68 94 57 100 45 96 33 99 22 94 25 84 19 74 23 64 18 53 22 43 17 31Z'
tape='<path d="m42 4 20 7-5 13-20-7Z" fill="#D991BC"/><path d="m40 7 17 9m-19-5 17 9m-10-13-7 12m13-10-7 12m12-9-7 12" stroke="#FFF2FF" stroke-width=".65" opacity=".9"/>'
frames={
 'settings':seal(),
 'gallery':'<path d="'+paper+'" fill="#F2E2F0" stroke="#EDDBED" stroke-width="1.1"/>'+tape,
 'bookmark':'<path d="'+paper+'" fill="#F7E8F2" stroke="#EDDBED" stroke-width="1.1"/>'+tape,
 'system':'<defs><linearGradient id="blue" x1="14" y1="13" x2="85" y2="98" gradientUnits="userSpaceOnUse"><stop stop-color="#A9BDD1"/><stop offset="1" stop-color="#625A7E"/></linearGradient></defs><path d="M31 13Q40 8 53 12L86 16Q101 18 97 35L89 82Q86 99 68 96L24 92Q9 91 13 74L20 31Q22 18 31 13Z" fill="url(#blue)" stroke="#D5D0EB" stroke-width="1.6"/><path d="m24 28-7 45q-3 14 11 15l38 4" fill="none" stroke="#EEE5FA" stroke-width=".8" stroke-dasharray="2.5 3" opacity=".7"/>',
 'exit':'<circle cx="52" cy="52" r="44" fill="#EEE1F5" stroke="#D7C5E8" stroke-width="1.8"/>'
}
for name,frame in frames.items():
    color='#8C566B' if name in ('gallery','bookmark') else '#3E2C60' if name=='exit' else '#FFF2FF'
    svg='<svg xmlns="http://www.w3.org/2000/svg" width="104" height="104" viewBox="0 0 104 104">'+frame+symbol(name,color)+'</svg>'
    (out/(name+'.svg')).write_text(svg,encoding='utf8')
    (out/(name+'.png')).write_bytes(resvg_py.svg_to_bytes(svg_string=svg))
print('Rendered five complete 104px menu icons. Quit circle fits inside its transparent margins.')
