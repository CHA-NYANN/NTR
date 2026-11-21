/* Branded shell around the existing Ren'Py startup; engine and saves are intact. */
(() => {
  'use strict';
  const root=document.getElementById('kkBoot');
  if(!root)return;
  const studio=document.getElementById('kkStudioIntro');
  const caption=document.getElementById('kkLoadingCaption');
  const hint=document.getElementById('kkLoadingHint');
  const progress=document.getElementById('kkProgress');
  const fill=document.getElementById('kkProgressFill');
  const star=progress.querySelector('.kk-progress-star');
  const percent=document.getElementById('kkPercent');
  const nativeText=document.getElementById('statusTextDiv');
  const nativeProgress=document.getElementById('statusProgress');
  const reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const config=JSON.parse(document.getElementById('kkBootConfig').textContent);
  let state='studio', started=false, finished=false, observer, framePending=false;
  document.body.classList.add('kk-is-booting');
  const fatalPattern=/could not (?:load|download|create)|does not support|requires the game to be run|aborted unexpectedly|exited unexpectedly|more information may be available in the browser console/i;
  function setState(value){state=value;root.dataset.state=value;}
  function setProgress(done,total,message){
    if(finished||state==='error')return;
    const known=Number.isFinite(done)&&Number.isFinite(total)&&total>0;
    progress.classList.toggle('is-indeterminate',!known);
    if(known){
      const value=Math.max(0,Math.min(100,done/total*100));
      fill.style.transform=`scaleX(${value/100})`;star.style.left=`${value}%`;
      progress.setAttribute('aria-valuenow',String(Math.round(value)));
      percent.textContent=`${Math.floor(value)}%`;
    }else{fill.style.removeProperty('transform');star.style.removeProperty('left');progress.removeAttribute('aria-valuenow');percent.textContent='';}
    if(message&&caption.textContent!==message)caption.textContent=message;
  }
  function syncStatus(){
    framePending=false;
    if(finished)return;
    const text=(nativeText.innerText||nativeText.textContent).trim();
    if(fatalPattern.test(text)){fail(text);return;}
    const last=text.split(/\n/).filter(Boolean).at(-1)||text;
    let label='Menyiapkan panggung cerita…';
    if(/loading script|compiling|initializ/i.test(last)){label='Menyusun cerita Kouseikan…';}
    else if(/game data|game files|preloading/i.test(last)){label='Mengumpulkan halaman cerita…';}
    else if(/engine|download|fetch/i.test(last)){label='Menyiapkan dunia Kouseikan…';}
    const known=nativeProgress.style.display==='block';
    setProgress(known?Number(nativeProgress.value):NaN,known?Number(nativeProgress.max):NaN,label);
    hint.textContent=/loading script/i.test(last)?'Merangkai pilihan dan pertemuan.':'Sebentar. Ceritamu sedang disiapkan.';
  }
  function queueSync(){if(!framePending){framePending=true;requestAnimationFrame(syncStatus);}}
  function fail(message){
    if(finished||state==='error')return;
    setState('error');document.body.classList.add('kk-boot-error');
    caption.textContent='Ada halaman yang belum berhasil dimuat.';
    document.getElementById('kkBootError').hidden=false;
    document.getElementById('kkErrorDetail').textContent=String(message||'Koneksi terputus saat menyiapkan game.');
    progress.hidden=true;percent.textContent='';hint.textContent='Periksa koneksi, lalu coba sekali lagi.';
    document.getElementById('kkRetry').focus({preventScroll:true});
  }
  function ready(){
    if(finished||state==='error')return;
    finished=true;setState('ready');
    caption.textContent='Ceritamu siap.';fill.style.transform='scaleX(1)';star.style.left='100%';
    progress.classList.remove('is-indeterminate');progress.setAttribute('aria-valuenow','100');percent.textContent='100%';
    observer.disconnect();root.classList.add('is-finished');document.body.classList.remove('kk-is-booting');
    document.getElementById('canvas')?.focus({preventScroll:true});
    setTimeout(()=>root.remove(),reduce?0:470);
  }
  function startEngine(){
    if(started||state==='error')return;
    started=true;setState('loading');studio.disabled=true;
    // Give the loading view a painted frame before executing the WebAssembly loader.
    requestAnimationFrame(()=>requestAnimationFrame(()=>{
      const script=document.createElement('script');script.src=config.engine;script.async=true;
      script.addEventListener('error',()=>fail('Berkas mesin game gagal diunduh.'));
      document.body.appendChild(script);
    }));
  }
  const originalEnd=window.presplashEnd;
  window.presplashEnd=()=>{if(originalEnd)originalEnd();ready();};
  for(const name of ['onAbort']){
    const original=Module[name];
    Module[name]=(...args)=>{fail(args[0]||'Mesin game berhenti saat memuat.');if(original)original(...args);};
  }
  observer=new MutationObserver(queueSync);
  observer.observe(nativeText,{childList:true,subtree:true,characterData:true});
  observer.observe(nativeProgress,{attributes:true,attributeFilter:['value','max','style']});
  document.getElementById('kkRetry').addEventListener('click',()=>location.reload());
  studio.addEventListener('click',startEngine);
  window.addEventListener('error',event=>{
    if(!finished&&event.error&&/renpy(?:-pre)?\.js|boot\/boot\.js/.test(event.filename||''))fail(event.message);
  });
  // Optional service-worker/extension failures must not interrupt a playable game.
  // The engine reports download failures through statusTextDiv and onAbort.
  window.KouseikanBoot=Object.freeze({ready,fail,progress:setProgress,skipStudio:startEngine,get state(){return state;}});
  syncStatus();
  setTimeout(startEngine,reduce?650:2500);
})();
