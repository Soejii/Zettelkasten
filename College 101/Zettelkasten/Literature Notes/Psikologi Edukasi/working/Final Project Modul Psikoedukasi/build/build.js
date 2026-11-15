// node build.js  -> builds HTML + PDF from the canonical .md (two passes for TOC page numbers)
const fs=require('fs'),path=require('path'),{execFileSync}=require('child_process');
const NM='/home/suji/.npm-global/lib/node_modules/md-to-pdf/node_modules/';
const {marked}=require(NM+'marked');const puppeteer=require(NM+'puppeteer');
const B=__dirname, MD=path.resolve(B,'../../../Final Project Modul Psikoedukasi.md');
const VAR=process.argv[2]||'';
const DEST='/home/suji/Documents/Modul Psikoedukasi Technoference';
const OUT=process.argv[3]?path.resolve(process.argv[3]):path.join(DEST,(VAR==='peserta'?'Materi Peserta':VAR==='fasilitator'?'Panduan Fasilitator':'Modul Lengkap')+' - Bicara Dulu, Baru Sepakat.pdf');
fs.mkdirSync(DEST,{recursive:true});
const md=fs.readFileSync(MD,'utf8');
const body=marked.parse(md,{gfm:true});
function page(toc,mark){return `<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Bicara Dulu, Baru Sepakat</title>
<link rel="stylesheet" href="style.css"></head><body><div id="src">${body}</div><div id="doc"></div>
<script>window.__TOC=${JSON.stringify(toc)};window.__MARK=${mark};window.__VARIANT=${JSON.stringify(VAR)};</script><script src="transform.js"></script></body></html>`;}
(async()=>{
 const b=await puppeteer.launch({args:['--no-sandbox']});
 async function render(html,pdf){const f=path.join(B,'modul.html');fs.writeFileSync(f,html);const p=await b.newPage();
   await p.goto('file://'+f,{waitUntil:'networkidle0'});await p.evaluate(()=>document.fonts.ready);
   const keys=await p.evaluate(()=>window.__tocKeys);
   await p.pdf({path:pdf,preferCSSPageSize:true,printBackground:true});await p.close();return keys;}
 const tmp=path.join(B,'pass1-'+(VAR||'all')+'.pdf');
 const keys=await render(page({},true),tmp);
 const n=+execFileSync('pdfinfo',[tmp]).toString().match(/Pages:\s+(\d+)/)[1];
 const toc={};
 for(let i=1;i<=n;i++){const t=execFileSync('pdftotext',['-f',String(i),'-l',String(i),tmp,'-']).toString();
   for(const m of t.matchAll(/@@T(\d+)@@/g)){const k=keys[+m[1]];if(!(k in toc))toc[k]=i;}}
 await render(page(toc,false),OUT);
 const n2=+execFileSync('pdfinfo',[OUT]).toString().match(/Pages:\s+(\d+)/)[1];
 console.log(VAR||'all','pages',n2);fs.unlinkSync(tmp);console.log(JSON.stringify(toc));
 await b.close();})();
