// Dependency-free startup contract tests. Run: node tools/test_web_boot.mjs
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
const source=fs.readFileSync(new URL('./web_boot/boot.js',import.meta.url),'utf8');
function setup(reduced=false){
  const elements=new Map(),timers=[],frames=[],scripts=[],events={};
  let observer,ended=0,reloaded=0;
  function element(id){
    const classes=new Set(),attrs=new Map();
    const result={id,textContent:'',dataset:{},hidden:false,removed:false,focused:false,value:0,max:100,
      style:{display:'none',removeProperty(key){delete this[key];}},
      classList:{add:(v)=>classes.add(v),remove:(v)=>classes.delete(v),contains:(v)=>classes.has(v),toggle(v,on){on?classes.add(v):classes.delete(v);}},
      handlers:{},addEventListener(type,fn){this.handlers[type]=fn;},
      setAttribute:(k,v)=>attrs.set(k,v),removeAttribute:(k)=>attrs.delete(k),getAttribute:(k)=>attrs.get(k),
      focus(){this.focused=true;},remove(){this.removed=true;},querySelector:()=>element('star')};
    elements.set(id,result);return result;
  }
  for(const id of ['kkBoot','kkStudioIntro','kkLoadingCaption','kkLoadingHint','kkProgress','kkProgressFill','kkPercent','statusTextDiv','statusProgress','kkBootError','kkErrorDetail','kkRetry','canvas','kkBootConfig'])element(id);
  elements.get('kkBootConfig').textContent='{"engine":"renpy.js"}';
  const document={getElementById:id=>elements.get(id),createElement:()=>element('script'),body:element('body')};
  document.body.appendChild=script=>scripts.push(script);
  const context={document,Module:{onAbort:()=>ended++},MutationObserver:class{
    constructor(fn){this.callback=fn;this.disconnected=false;observer=this;}observe(){}disconnect(){this.disconnected=true;}
  },requestAnimationFrame:fn=>frames.push(fn),setTimeout:(fn,ms)=>timers.push({fn,ms}),location:{reload:()=>reloaded++}};
  context.window={matchMedia:()=>({matches:reduced}),presplashEnd:()=>ended++,addEventListener:(type,fn)=>events[type]=fn};
  vm.runInNewContext(source,context);
  return {context,api:context.window.KouseikanBoot,elements,timers,frames,scripts,events,
    get observer(){return observer;},get ended(){return ended;},get reloaded(){return reloaded;},
    flush(){while(frames.length)frames.shift()();},notify(){observer.callback();this.flush();}};
}
const a=setup();
assert.equal(a.api.state,'studio');assert.equal(a.scripts.length,0);
assert.equal(a.timers[0].ms,2500);a.timers[0].fn();
assert.equal(a.api.state,'loading');assert.equal(a.scripts.length,0);a.flush();
assert.equal(a.scripts.length,1);assert.equal(a.scripts[0].src,'renpy.js');
a.api.skipStudio();a.flush();assert.equal(a.scripts.length,1,'skip/timer must not boot twice');
const p=a.elements.get('statusProgress');p.value=25;p.max=200;p.style.display='block';
a.elements.get('statusTextDiv').textContent='Downloading game data...';a.notify();
assert.equal(a.elements.get('kkProgress').getAttribute('aria-valuenow'),'13');
assert.equal(a.elements.get('kkPercent').textContent,'12%');
assert.match(a.elements.get('kkLoadingCaption').textContent,/halaman cerita/);
p.style.display='none';a.elements.get('statusTextDiv').textContent='Loading script...';a.notify();
assert.equal(a.elements.get('kkProgress').getAttribute('aria-valuenow'),undefined);
assert.equal(a.elements.get('kkPercent').textContent,'');
assert.equal(a.api.state,'loading','download completion must not dismiss the shell');
a.context.window.presplashEnd();assert.equal(a.api.state,'ready');assert.equal(a.ended,1);
assert.equal(a.observer.disconnected,true);assert.equal(a.elements.get('canvas').focused,true);
a.timers.at(-1).fn();assert.equal(a.elements.get('kkBoot').removed,true);
const b=setup(true);assert.equal(b.timers[0].ms,650);
b.elements.get('kkStudioIntro').handlers.click();b.flush();
b.scripts[0].handlers.error();assert.equal(b.api.state,'error');
assert.equal(b.elements.get('kkBootError').hidden,false);
assert.equal(b.elements.get('kkRetry').focused,true);
b.context.window.presplashEnd();assert.equal(b.api.state,'error','failed startup must not reveal a blank canvas');
b.elements.get('kkRetry').handlers.click();assert.equal(b.reloaded,1);
const c=setup();c.elements.get('statusTextDiv').textContent='Could not download game.zip';c.notify();
assert.equal(c.api.state,'error');assert.match(c.elements.get('kkErrorDetail').textContent,/game.zip/);
const d=setup();d.context.Module.onAbort('WASM failed');assert.equal(d.api.state,'error');assert.equal(d.ended,1);
console.log('PASS: studio order, skip, real/unknown progress, first-frame handoff, reduced motion, retry and engine failures');
