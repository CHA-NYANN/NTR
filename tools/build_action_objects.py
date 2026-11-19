"""Object buttons for existing world actions, matching the native vector GUI."""
from pathlib import Path
import resvg_py
root=Path(__file__).resolve().parents[1]/'game/gui/kouseikan/actions'
defs='<defs><linearGradient id="paper" x2=".2" y2="1"><stop stop-color="#FFF2DD"/><stop offset="1" stop-color="#C5BBD8"/></linearGradient><linearGradient id="blue" x2=".7" y2="1"><stop stop-color="#9DCCDF"/><stop offset="1" stop-color="#63527D"/></linearGradient></defs>'
drawings={
'book':'<path d="M57 95 186 65 295 82 187 111Z" fill="#CBAFC9"/><path d="M57 95v184l129 39 109-48V82L186 111Z" fill="url(#paper)"/><path d="M186 111v207M68 102v167l108 33M196 116l86-27v170l-86 42" fill="none" stroke="#9C85AB"/><path d="m88 131 64 14m-64 10 64 14m-64 10 64 14m-64 10 64 14m67-68 42-14m-42 33 42-14m-42 33 42-14" stroke="#B29AAF" stroke-width="3"/><path d="m113 278 126-158 14 11-126 158-21 8Z" fill="#687996"/><path d="m113 278-7 19 21-8" fill="#E2B896"/>',
'meal':'<ellipse cx="180" cy="279" rx="143" ry="35" fill="#716087" opacity=".25"/><ellipse cx="180" cy="234" rx="141" ry="68" fill="url(#paper)"/><ellipse cx="180" cy="224" rx="120" ry="49" fill="#FFF4E8"/><path d="M76 223c0-51 200-72 204 0Z" fill="#EBD8AB"/><path d="M89 206c15-75 66-30 68-8m12 6c9-54 53-63 65-6" fill="#8FA873"/><ellipse cx="191" cy="220" rx="62" ry="31" fill="#FFF9E4"/><ellipse cx="191" cy="218" rx="24" ry="19" fill="#EDBE61"/><path d="m65 116 242 48m-242-38 242 48" stroke="#9E7A79" stroke-width="7"/>',
'work':'<path d="m125 73 16-34h78l16 34-27 44h-56Z" fill="#B4C2D3"/><path d="M135 80c-14 30-36 31-51 44l-21 169c71 29 147 29 234 0l-21-169c-25-10-37-21-49-44-16 34-76 39-92 0Z" fill="url(#blue)"/><path d="M119 177h123v66c-38 20-79 20-123 0Z" fill="#E4D4DE"/><path d="M143 187v47m27-47v47m27-47v47m27-47v47" stroke="#A8A0B5" stroke-width="2"/><path d="m94 130-33-17m205 17 33-17" stroke="#D3BED4" stroke-width="13"/>',
'bed':'<path d="M45 114h267v139H45Z" fill="#776982"/><path d="M57 98c13-40 230-39 242 0v92H57Z" fill="url(#blue)"/><path d="m45 183 267-2 19 91H28Z" fill="url(#paper)"/><path d="m28 272 19-33h265l19 33v33H28Z" fill="#C4B1D0"/><path d="M79 156h79v42H68Zm122 0h77l14 42h-91Z" fill="#FFF2E7"/><path d="M46 305v24m266-24v24" stroke="#776982" stroke-width="12"/>',
'train':'<path d="M94 75c0-48 173-48 173 0v198H94Z" fill="url(#paper)"/><path d="M108 87h145v90H108Z" fill="url(#blue)"/><path d="M180 87v90" stroke="#D1DDE5"/><path d="M94 210h173v24H94Z" fill="#AA82BF"/><circle cx="127" cy="252" r="10" fill="#E6BE6D"/><circle cx="236" cy="252" r="10" fill="#E6BE6D"/><path d="m129 281-55 51m157-51 55 51m-153-20h94m-117 14h139" fill="none" stroke="#7B6A91" stroke-width="8"/>',
'chess':'<path d="m38 253 190-58 108 58-194 72Z" fill="url(#paper)"/><path d="m38 253 104 72 194-72v17l-194 72-104-72Z" fill="#96809E"/><path d="m75 241 103 71m3-104 107 63m-167-42 107 69m-117 4 196-66m-165 87 194-70" stroke="#AA92B2" stroke-width="15"/><path d="M145 222c29-6 39-1 66 1l-5-16-13-11-4-49h-22l-4 49-14 11Z" fill="#645475"/><circle cx="178" cy="130" r="23" fill="#77658A"/><path d="M244 220h60l-8-17-11-9-5-43h-15l-6 43-9 9Z" fill="#F8E9DA"/><circle cx="273" cy="139" r="17" fill="#F8E9DA"/>'
}
for name,body in drawings.items():
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="360" viewBox="0 0 360 360">{defs}<g stroke="#65556F" stroke-width="2.4" stroke-linejoin="round">{body}</g></svg>'
    (root/(name+'.svg')).write_text(svg,encoding='utf8')
    (root/(name+'.png')).write_bytes(resvg_py.svg_to_bytes(svg_string=svg))
print('Rendered',len(drawings),'native action objects.')
