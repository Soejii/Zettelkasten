// usage: node sheet.js out.png cols widthPx img1 img2 ... [--gray]
const puppeteer=require('/home/suji/.npm-global/lib/node_modules/md-to-pdf/node_modules/puppeteer');
const path=require('path');
(async()=>{const a=process.argv.slice(2);const gray=a.includes('--gray');const [out,cols,w,...imgs]=a.filter(x=>x!=='--gray');
const html=`<html><body style="margin:0;background:#999;display:grid;grid-template-columns:repeat(${cols},${w}px);gap:8px;padding:8px;width:max-content;${gray?'filter:grayscale(1)':''}">${imgs.map(i=>`<img src="file://${path.resolve(i)}" style="width:${w}px;border:1px solid #333">`).join('')}</body></html>`;
const b=await puppeteer.launch({args:['--no-sandbox']});const p=await b.newPage();await p.setViewport({width:100,height:100});
const fs=require('fs');const tmp=path.resolve(out+'.html');fs.writeFileSync(tmp,html);await p.goto('file://'+tmp,{waitUntil:'load'});const el=await p.$('body');await el.screenshot({path:out});await b.close();})();
