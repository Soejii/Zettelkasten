// Runs inside the page. Rebuilds #src (marked output of the canonical .md) into designed print pages.
(function(){
const src=document.getElementById('src');
const doc=document.getElementById('doc');
const T=(e)=>(e.textContent||'').replace(/\s+/g,' ').trim();
const el=(tag,cls,html)=>{const e=document.createElement(tag);if(cls)e.className=cls;if(html!=null)e.innerHTML=html;return e;};
const HEART='<svg viewBox="0 0 24 24"><path d="M19.5 12.572 12 20l-7.5-7.428a5 5 0 1 1 7.5-6.566 5 5 0 1 1 7.5 6.572"/></svg>';
const PHONE='<svg viewBox="0 0 24 24"><rect x="7" y="2.5" width="10" height="19" rx="2.2"/><path d="M11 18h2"/></svg>';
const TOC=window.__TOC||{};

const nodes=[...src.children];
let title='', cover=[], part=0, cur=null, sec=null, sub=null, secType='', tocItems=[];

function newSection(h3){
  const t=T(h3);
  sec=el('section','sec part'+part);
  const m=t.match(/^(\d+)\.\s*(.*)$/);
  const kick=part===1?'Bagian 1 · Panduan Fasilitator':part===2?'Bagian 2 · Materi Peserta':'';
  const head=el('div','sec-head');
  head.appendChild(el('div','kick',kick+(m?' · '+m[1]:'')));
  const h=el('h3',null,h3.innerHTML.replace(/^\d+\.\s*/,''));h.dataset.toc=t;head.appendChild(h);
  head.appendChild(el('div','bar'));
  sec.appendChild(head);
  doc.appendChild(sec);
  cur=sec; sub=null;
  secType = /Latar Belakang|Profil Peserta/.test(t)?'prose':
            /^2\. Tujuan/.test(t)?'tujuan':
            /Rincian Sesi/.test(t)?'rincian':
            /Panduan Teknis/.test(t)?'panduan':
            /Evaluasi/.test(t)?'evaluasi':
            /Buku Pegangan/.test(t)?'buku':
            /Konten Psikoedukasi/.test(t)?'konten':
            /Lembar Kerja/.test(t)?'lembar':
            /Refleksi/.test(t)?'refleksi':
            /Bacaan Lanjutan/.test(t)?'bacaan':'other';
  sec.classList.add(secType);
  if(secType==='prose') sec.classList.add('prose');
  tocItems.push({t, part, label:h.textContent});
}

function h4Handler(h4){
  const t=T(h4);
  if(secType==='rincian'||secType==='panduan'){
    const m=t.match(/^Sesi (\d+):\s*(.*)$/);
    const b=el('div','band'+(m?'':' soft'));
    if(secType==='panduan'&&(m||/Manajemen|Alat Fasilitator/.test(t))) { b.classList.add('newpage'); }
    b.innerHTML=m?`<span class="no">${m[1]}</span><span class="tt"><small>Sesi ${m[1]}</small>${h4.innerHTML.replace(/^Sesi \d+:\s*/,'')}</span>`
                 :`<span class="no">${/Jeda/.test(t)?'⏸':'•'}</span><span class="tt">${h4.innerHTML}</span>`;
    if(/Jeda/.test(t)) b.querySelector('.no').innerHTML='14';
    if(/Persiapan/.test(t)) b.querySelector('.no').innerHTML='P'; if(/Manajemen/.test(t)) b.querySelector('.no').innerHTML='M'; if(/Alat/.test(t)) b.querySelector('.no').innerHTML='A';
    sec.appendChild(b); cur=sec; return;
  }
  if(secType==='konten'){
    const m=t.match(/^Materi (\d+):\s*(.*)$/);
    sub=el('div','materi');
    const o=el('div','mopen');
    o.innerHTML=`<div class="big">0${m[1]}</div><div><div class="mk">Materi ${m[1]}</div><h4>${h4.innerHTML.replace(/^Materi \d+:\s*/,'')}</h4></div>`;
    sub.appendChild(o); sec.appendChild(sub); cur=sub; tocItems.push({t,part,label:T(h4).replace(/^Materi \d+:\s*/,''),sub:true,id:'Materi '+m[1]}); o.querySelector('h4').dataset.toc=t; return;
  }
  if(secType==='lembar'){
    let pill='Aktivitas', name=h4.innerHTML;
    let m=t.match(/^Lembar Kerja (\d+):\s*(.*)$/);
    if(m){pill='Lembar Kerja '+m[1];name=h4.innerHTML.replace(/^Lembar Kerja \d+:\s*/,'');}
    else if(/Pemantauan/.test(t)){pill='Lembar Pemantauan';}
    sub=el('div','ws');
    if(/Pemantauan/.test(t)) sub.classList.add('wide2');
    sub.innerHTML=`<div class="wsh"><span class="wp">${pill}</span><span class="pill">Bicara Dulu, Baru Sepakat</span></div>`;
    const h=el('h4',null,name);h.dataset.toc=t;sub.appendChild(h);
    sec.appendChild(sub); cur=sub; tocItems.push({t,part,label:pill+(m||/Pemantauan/.test(t)?'':'')+(m?': '+T(h):/Pemantauan/.test(t)?'':': '+T(h)),sub:true}); return;
  }
  if(secType==='evaluasi'){
    const b=el('div','band soft');b.innerHTML=`<span class="no">${/Hasil/.test(t)?'A':'B'}</span><span class="tt">${h4.innerHTML}</span>`;
    sec.appendChild(b);cur=sec;return;
  }
  const h=el('h4',null,h4.innerHTML); cur.appendChild(h);
}

// ---------- pass 1: distribute nodes ----------
let inCover=false;
for(const n of nodes){
  const tag=n.tagName;
  if(tag==='H1'){title=n.innerHTML;continue;}
  if(tag==='H2'){
    inCover=false;
    const t=T(n);
    if(/^Bagian 1/.test(t)){part=1;doc.appendChild(divider(1,n));continue;}
    if(/^Bagian 2/.test(t)){part=2;doc.appendChild(divider(2,n));continue;}
    if(/Daftar Pustaka/.test(t)){part=3;sec=el('section','sec refs part3');sec.innerHTML=`<div class="sec-head"><div class="kick">Rujukan</div><h3 data-toc="Daftar Pustaka">Daftar Pustaka</h3><div class="bar"></div></div>`;doc.appendChild(sec);cur=sec;secType='refs';tocItems.push({t:'Daftar Pustaka',part:3,label:'Daftar Pustaka'});continue;}
  }
  if(tag==='H3'){
    if(/Halaman Sampul/.test(T(n))){inCover=true;continue;}
    inCover=false; newSection(n); continue;
  }
  if(inCover){cover.push(n);continue;}
  if(tag==='H4'){h4Handler(n);continue;}
  if(cur) cur.appendChild(n);
}

function divider(k,h2){
  const d=el('section','full divider d'+k);
  const name=T(h2).replace(/^Bagian \d+:\s*/,'');
  d.innerHTML=`<div class="num">0${k}</div><div class="kick">Bagian ${k}</div><h2 data-toc="${T(h2)}">${name}</h2>`;
  d.dataset.part=k;
  tocItems.push({t:T(h2),part:k,label:'Bagian '+k+': '+name,isPart:true});
  return d;
}

// fill divider lists after sections known
function fillDividers(){
  document.querySelectorAll('.divider').forEach(d=>{
    const k=+d.dataset.part; const ul=el('ul');
    tocItems.filter(i=>i.part===k&&!i.isPart&&!i.sub).forEach(i=>ul.appendChild(el('li',null,i.label)));
    d.appendChild(ul);
  });
}

// ---------- cover ----------
function buildCover(){
  const c=el('section','full cover');
  const tbl=cover.filter(n=>n.tagName==='TABLE');
  const meta=tbl[0]?[...tbl[0].querySelectorAll('tbody tr')].map(r=>[T(r.cells[0]),r.cells[1].innerHTML]):[];
  const nrows=tbl[1]?[...tbl[1].querySelectorAll('tbody tr')].map(r=>[T(r.cells[1]),T(r.cells[2])]):[['',''],['',''],['',''],['',''],['','']];
  window.__meta=Object.fromEntries(meta.map(([k,v])=>[k,v.replace(/<[^>]+>/g,'')]));
  const tt=title.replace(/^Modul Psikoedukasi\s*/,'');
  const mm=tt.match(/^"?(.*?)"?:\s*(.*)$/)||tt.match(/^&quot;(.*?)&quot;:\s*(.*)$/);
  let q=tt,s='';
  const raw=tt.replace(/&quot;/g,'"');const m2=raw.match(/^"([^"]+)":\s*(.*)$/);
  if(m2){q=m2[1];s=m2[2];}
  c.innerHTML=`<div class="top"><div class="dots"><i style="background:var(--sec)"></i><i style="background:var(--acc)"></i><i style="background:var(--bg)"></i></div>
   <div class="kick">Modul Psikoedukasi</div><h1 class="quote">${q}</h1><p class="sub">${s}</p></div>
   <div class="low"><div class="badge">${HEART}</div><div class="bar"></div>
   <div class="meta">${meta.map(([k,v])=>`<b>${k}</b><div>${v}</div>`).join('')}</div>
   <div class="names"><div class="h">Nama anggota</div><div class="h">NIM</div>${nrows.map(([n,m])=>`<div class="l">${n}</div><div class="l">${m}</div>`).join('')}</div></div>`;
  doc.insertBefore(c,doc.firstChild);
}

// ---------- TOC ----------
function buildTOC(){
  const t=el('section','toc');
  t.innerHTML='<h2>Daftar Isi</h2><div class="bar"></div>';
  for(const i of tocItems){
    if(i.isPart){t.appendChild(el('div','part',i.label));continue;}
    const r=el('div','row'+(i.sub?' sub':''));
    const n=TOC[i.t]||'';
    r.innerHTML=`<span class="t">${i.label}</span><span class="d"></span><span class="n">${n}</span>`;
    if(i.t==='Daftar Pustaka'){t.appendChild(el('div','part','Rujukan'));}
    t.appendChild(r);
  }
  doc.insertBefore(t,doc.children[1]);
}

// ---------- generic helpers ----------
function boxify(first,kind,label,icon,extra){
  const b=el('div','box '+kind);
  b.innerHTML=`<div class="bh"><i>${icon}</i>${label}</div>`;
  first.parentNode.insertBefore(b,first);
  if(extra!==undefined){ // first is a label paragraph, move following element(s)
    first.remove();
    for(const x of extra) b.appendChild(x);
  } else b.appendChild(first);
  return b;
}
function stripLead(p,re){ // remove leading label text from paragraph
  p.innerHTML=p.innerHTML.replace(re,'');
}

function processBoxes(root){
  [...root.querySelectorAll('p')].forEach(p=>{
    if(!p.isConnected) return;
    const t=T(p);
    // activity header
    const st=p.firstElementChild;
    if(st&&st.tagName==='STRONG'&&p.childNodes.length===1){
      const ka=T(st).match(/^Kegiatan (\d+)\.\s*(.*)\((\d+ menit)\)$/);
      if(ka){
        const h=el('div','act');
        const inner=st.innerHTML.replace(/^Kegiatan \d+\.\s*/,'').replace(/\s*\(\d+ menit\)\s*$/,'');
        h.innerHTML=`<span class="an">${ka[1]}</span><span class="at">${inner}</span><span class="pill">${ka[3]}</span>`;
        p.replaceWith(h);return;
      }
    }
    if(t==='Naskah pembuka:'){const bq=p.nextElementSibling;boxify(p,'naskah','Naskah pembuka','“',[...bq.children]);bq.remove();return;}
    if(/^Pertanyaan pemantik/.test(t)){const ul=p.nextElementSibling;const lab=t.replace(/:$/,'');boxify(p,'pemantik',lab,'?',[ul]);return;}
    if(t==='Langkah:'){p.className='lbl';p.textContent='Langkah';const ol=p.nextElementSibling;if(ol&&ol.tagName==='OL')ol.classList.add('steps');return;}
    if(/^Pembukaan singkat:/.test(t)){stripLead(p,/^Pembukaan singkat:\s*/);boxify(p,'naskah','Pembukaan singkat','“');return;}
    if(/^Catatan untuk fasilitator:/.test(t)){stripLead(p,/^Catatan untuk fasilitator:\s*/);p.innerHTML=p.innerHTML.charAt(0).toUpperCase()+p.innerHTML.slice(1);boxify(p,'catatan','Catatan untuk fasilitator','i');return;}
    const km=t.match(/^(Kunci diskusi|Kunci penilaian|Poin yang diharapkan muncul):/);
    if(km){stripLead(p,new RegExp('^'+km[1]+':\\s*'));p.innerHTML=p.innerHTML.charAt(0).toUpperCase()+p.innerHTML.slice(1);boxify(p,'kunci',km[1],'✓');return;}
  });
  // ordered lists right after an activity header become step lists
  root.querySelectorAll('.act + ol, .act + p + ol').forEach(o=>o.classList.add('steps'));
}

function processChats(root){
  root.querySelectorAll('blockquote').forEach(bq=>{
    const ps=[...bq.children].filter(x=>x.tagName==='P');
    if(ps.length&&ps.every(p=>p.firstElementChild&&/^(Istri|Suami):$/.test(T(p.firstElementChild)))){
      const c=el('div','chat');
      ps.forEach(p=>{const who=T(p.firstElementChild).replace(':','');p.firstElementChild.remove();
        const b=el('div','b '+(who==='Istri'?'l':'r'));b.innerHTML=`<span class="who">${who}</span>${p.innerHTML.trim()}`;c.appendChild(b);});
      bq.replaceWith(c);
    }
  });
}

function processFormula(root){
  root.querySelectorAll('blockquote').forEach(bq=>{
    if(bq.children.length===1&&bq.children[0].tagName==='P'&&/\[/.test(T(bq))&&T(bq).length<140){
      const f=el('div','formula');f.innerHTML=`<span class="fx">RUMUS</span><span>${bq.children[0].innerHTML}</span>`;bq.replaceWith(f);
    }
  });
}

function processFills(root){
  const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);const list=[];
  while(w.nextNode()) if(/\.{6,}/.test(w.currentNode.nodeValue)) list.push(w.currentNode);
  list.forEach(tn=>{
    const p=tn.parentNode;
    if(p.tagName==='P'&&T(p).replace(/\.{6,}/g,'').trim()===''){p.replaceWith(el('div','ruled'));return;}
    const span=document.createElement('span');
    span.innerHTML=tn.nodeValue.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/\.{6,}/g,'<span class="fill"></span>');
    tn.replaceWith(...span.childNodes);
  });
}

function processTables(root){
  root.querySelectorAll('td').forEach(td=>{if(T(td)==='')td.classList.add('empty');});
  root.querySelectorAll('table').forEach(tb=>{
    const ths=[...tb.querySelectorAll('thead th')].map(T);
    if(ths.length===2&&/^(Bagian|Keterangan|Hal)$/.test(ths[0])) tb.classList.add('kv');
  });
}

// ---------- section specific ----------
function doTujuan(s){
  const h=[...s.querySelectorAll('h4')].find(x=>/Tujuan Umum/.test(T(x)));
  if(h){const p=h.nextElementSibling;const b=el('div','box goal');b.appendChild(p);h.after(b);}
}
function doPanduan(s){
  // Alat Fasilitator: bold-title paragraphs become labels; checklist goes landscape
  [...s.querySelectorAll('p')].forEach(p=>{
    if(p.children.length===1&&p.firstElementChild.tagName==='STRONG'&&T(p)===T(p.firstElementChild)){
      const t=T(p);
      if(/^(Naskah contoh|Kunci Jawaban|Daftar Periksa|Pesan Pengingat)/.test(t)){
        const h=el('h4',null,p.firstElementChild.innerHTML);p.replaceWith(h);
        if(/Daftar Periksa/.test(t)){
          const w=el('div','wide1');h.before(w);w.appendChild(h);
          let n=w.nextElementSibling; while(n&&n.tagName!=='TABLE'){const nx=n.nextElementSibling;w.appendChild(n);n=nx;} if(n)w.appendChild(n);
        }
        if(/Pesan Pengingat/.test(t)){const bq=h.nextElementSibling;if(bq&&bq.tagName==='BLOCKQUOTE'){const b=el('div','box msg');b.innerHTML=`<div class="bh"><i>i</i>Pesan singkat</div>`;b.append(...bq.children);bq.replaceWith(b);}}
      }
    }
    if(/^Versi (agresif|asertif):$/.test(T(p))){p.className='lbl';p.textContent=T(p).replace(':','');}
  });
}
function doEvaluasi(s){
  s.querySelectorAll('blockquote').forEach(bq=>{
    const first=T(bq.children[0]||bq);
    const f=el('div','form');
    if(/Kuesioner/.test(first)) f.dataset.tag='Kuesioner pra dan pasca';
    else if(/Formulir/.test(first)) f.dataset.tag='Formulir umpan balik';
    else return;
    const h=el('h5',null,bq.children[0].innerHTML.replace(/<\/?strong>/g,''));
    bq.children[0].remove();
    f.appendChild(h);f.append(...bq.children);bq.replaceWith(f);
  });
  [...s.querySelectorAll('p')].forEach(p=>{
    if(p.children.length===1&&p.firstElementChild.tagName==='STRONG'&&T(p)===T(p.firstElementChild)){
      const h=el('h4',null,p.firstElementChild.innerHTML);p.replaceWith(h);
      if(/Kunci jawaban kuesioner/i.test(T(h))) h.classList.add('newpage');
    }
    if(/^Rekap per (orang|pasangan):$/.test(T(p))){p.className='lbl';p.textContent=T(p).replace(':','');const t=p.nextElementSibling;if(t&&t.tagName==='TABLE'){const k=el('div','keep');p.before(k);k.append(p,t);}}
    if(/^Penilaian:/.test(T(p))){stripLead(p,/^Penilaian:\s*/);p.innerHTML=p.innerHTML.charAt(0).toUpperCase()+p.innerHTML.slice(1);boxify(p,'kunci','Penilaian','✓');}
  });
  // give rekap tables extra blank rows
  s.querySelectorAll('table').forEach(tb=>{
    const rows=tb.querySelectorAll('tbody tr');
    if(rows.length===1&&[...rows[0].cells].every(c=>c.classList.contains('empty'))){for(let i=0;i<5;i++)tb.tBodies[0].appendChild(rows[0].cloneNode(true));}
  });
}
function doBuku(s){
  [...s.querySelectorAll('p')].forEach(p=>{
    const st=p.firstElementChild;
    if(st&&st.tagName==='STRONG'&&/Buku ini milik/.test(T(st))){
      const o=el('div','owner');o.innerHTML=`<span>Buku ini milik</span><span class="fill"></span><span>dan</span><span class="fill"></span>`;p.replaceWith(o);return;}
    if(p.children.length===1&&st&&st.tagName==='STRONG'&&T(p)===T(st)){
      const q=el('div','q',st.innerHTML);p.replaceWith(q);
      if(/Cara memakai/.test(T(q))){const ol=q.nextElementSibling;if(ol&&ol.tagName==='OL')ol.classList.add('steps');}
      if(/^Catatan$/.test(T(q))){q.classList.add('newpage');}
    }
  });
}
function doKonten(s){
  s.querySelectorAll('.materi').forEach(m=>{
    [...m.querySelectorAll(':scope > p')].forEach(p=>{
      const st=p.firstElementChild;
      if(p.children.length===1&&st&&st.tagName==='STRONG'&&/^(Inti|Contoh|Ingat)$/.test(T(p))){
        const lab=T(p);
        if(lab==='Ingat'){const ul=p.nextElementSibling;const b=el('div','ingat');b.innerHTML='<div class="bh"><i>!</i>Ingat</div>';p.replaceWith(b);b.appendChild(ul);}
        else p.replaceWith(el('div','mlab',lab));
      }
    });
    // simple situation list in Materi 1 becomes chips
    m.querySelectorAll(':scope > ul').forEach(u=>{if([...u.children].every(li=>T(li).length<70)&&!u.closest('.ingat'))u.className='chips-row';});
    m.querySelectorAll(':scope > ol').forEach(o=>o.classList.add('steps'));
  });
  s.querySelectorAll('.mlab').forEach(m=>{if(T(m)!=='Contoh')return;const a=m.nextElementSibling,b=a&&a.nextElementSibling;
    if(a&&a.tagName==='TABLE'){const k=el('div','keep');m.before(k);k.append(m,a);}
    else if(a&&a.tagName==='P'&&b&&b.tagName==='TABLE'){const k=el('div','keep');m.before(k);k.append(m,a,b);}});
  // contoh percakapan label
  [...s.querySelectorAll('p')].forEach(p=>{if(T(p)==='Contoh percakapan:'){p.className='lbl';p.textContent='Contoh percakapan';}});
}
function doLembar(s){
  s.querySelectorAll('.ws').forEach(ws=>{
    // meta rows
    const metas=[...ws.querySelectorAll(':scope > p')].filter(p=>{const st=p.firstElementChild;return st&&st.tagName==='STRONG'&&/^(Diisi oleh|Petunjuk|Nama):$/.test(T(st));});
    if(metas.length){
      const g=el('div','wsmeta');metas[0].before(g);
      metas.forEach(p=>{const k=T(p.firstElementChild).replace(':','');p.firstElementChild.remove();const v=el('div',null,p.innerHTML.trim());g.append(el('b',null,k),v);p.remove();});
    }
    // situation cards
    const tb=ws.querySelector('table');
    if(tb&&[...tb.querySelectorAll('thead th')].map(T).join('|')==='No.|Situasi'){
      const g=el('div','cards');
      tb.querySelectorAll('tbody tr').forEach(r=>{const c=el('div','card');c.innerHTML=`<span class="cn">${T(r.cells[0])}</span><p>${r.cells[1].innerHTML}</p>`;g.appendChild(c);});
      tb.replaceWith(g);
    }
    // bold sub labels (Rencana 1, Revisi, Ringkasan)
    [...ws.querySelectorAll(':scope > p')].forEach(p=>{
      const st=p.firstElementChild;
      if(p.children.length===1&&st&&st.tagName==='STRONG'&&T(p)===T(st)){
        const b=el('div','band soft');b.innerHTML=`<span class="no">${/Rencana (\d)/.test(T(p))?T(p).match(/(\d)/)[1]:/Revisi/.test(T(p))?'R':'✓'}</span><span class="tt">${st.innerHTML}</span>`;
        if(/Revisi/.test(T(p))) b.classList.add('newpage');
        p.replaceWith(b);
      }
    });
    // signature tables
    ws.querySelectorAll('table').forEach(t=>{if(/Suami.*Istri/.test([...t.querySelectorAll('thead th')].map(T).join(' '))&&/Tanda tangan/.test(T(t)))t.parentNode.insertBefore(el('div','sigs'),t).appendChild(t);});
    ws.querySelectorAll('table').forEach(t=>{const h=[...t.querySelectorAll('thead th')].map(T).join('|');if(/Situasi \(kapan/.test(h))t.classList.add('tall');});
  });
}
function doRefleksi(s){
  const g=el('div','rgrid');let first=null;
  [...s.querySelectorAll(':scope > p')].forEach(p=>{
    const st=p.firstElementChild;
    if(p.children.length===1&&st&&st.tagName==='STRONG'&&T(p)===T(st)){
      const c=el('div','rcard'+(/akhir/i.test(T(p))?' final':''));c.appendChild(el('div','rh',st.innerHTML));
      const ol=p.nextElementSibling;if(!first){first=p;p.before(g);}
      g.appendChild(c);if(ol&&ol.tagName==='OL')c.appendChild(ol);p.remove();
    }
  });
}
function doBacaan(s){s.querySelectorAll('ol').forEach(o=>o.className='reads');}

// ---------- run ----------
buildCover();
fillDividers();
document.querySelectorAll('.sec').forEach(s=>{
  processTables(s);
  if(s.classList.contains('tujuan'))doTujuan(s);
  if(s.classList.contains('panduan'))doPanduan(s);
  processBoxes(s);
  processChats(s);
  processFormula(s);
  if(s.classList.contains('evaluasi'))doEvaluasi(s);
  if(s.classList.contains('buku'))doBuku(s);
  if(s.classList.contains('konten'))doKonten(s);
  if(s.classList.contains('lembar'))doLembar(s);
  if(s.classList.contains('refleksi'))doRefleksi(s);
  if(s.classList.contains('bacaan'))doBacaan(s);
  processFills(s);
});
// first materi / worksheet directly after the section intro shares the page
document.querySelectorAll('.konten, .lembar').forEach(sc=>{const f=sc.querySelector(':scope > .materi, :scope > .ws');if(f)f.classList.add('first');});
// keep each Rencana band with its table
document.querySelectorAll('.ws .band.soft').forEach(b=>{const t=b.nextElementSibling;if(t&&t.tagName==='TABLE'){const k=el('div','keep');b.before(k);k.append(b,t);if(b.classList.contains('newpage')){b.classList.remove('newpage');k.classList.add('newpage');}}});
// buku pegangan notes: extra ruled lines
document.querySelectorAll('.buku').forEach(s=>{const r=[...s.querySelectorAll('.ruled')];if(r.length){const wrap=el('div','notes');r[0].before(wrap);r.forEach(x=>wrap.appendChild(x));for(let i=0;i<14;i++)wrap.appendChild(el('div','ruled'));}});
(function(){const w=document.createTreeWalker(doc,NodeFilter.SHOW_TEXT);const L=[];while(w.nextNode())if(/I-[Ss]tatement/.test(w.currentNode.nodeValue))L.push(w.currentNode);
L.forEach(tn=>{const sp=document.createElement('span');sp.innerHTML=tn.nodeValue.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/(I-[Ss]tatement)/g,'<span style="white-space:nowrap">$1</span>');tn.replaceWith(...sp.childNodes);});
// also italic wrappers: <em>I-statement</em> handled above since text node inside em
})();
const V=window.__VARIANT||'';
if(V){const drop=V==='fasilitator'?['.divider.d2','.part2']:['.divider.d1','.part1','.part3'];
  drop.forEach(q=>document.querySelectorAll('#doc '+q).forEach(x=>x.remove()));
  tocItems=tocItems.filter(i=>V==='fasilitator'?(i.part===1||i.part===3):i.part===2);
  const k=document.querySelector('.cover .kick');if(k)k.textContent=V==='fasilitator'?'Modul Psikoedukasi · Panduan Fasilitator':'Modul Psikoedukasi · Materi Peserta';}
document.querySelectorAll('#doc table').forEach(t=>{if(t.querySelectorAll('tbody tr').length<=8&&!t.closest('.wide1,.wide2'))t.classList.add('nb');});
buildTOC();
// back cover
const back=el('section','full back');
back.innerHTML=`<div class="badge">${HEART}</div><p class="t">${title.replace(/^Modul Psikoedukasi\s*/,'').replace(/&quot;/g,'"').replace(/^"([^"]+)":.*/,'$1')}</p><p class="s">Modul Psikoedukasi · ${(window.__meta||{})['Mata kuliah']||''} · ${(window.__meta||{})['Kelompok']||''}</p>`;
doc.appendChild(back);
window.__tocKeys=[...document.querySelectorAll('[data-toc]')].map(e=>e.dataset.toc);
if(window.__MARK){document.querySelectorAll('[data-toc]').forEach((e,i)=>{e.style.position='relative';const m=el('span',null,'@@T'+i+'@@');m.style.cssText='position:absolute;left:0;top:0;font-size:2px;color:#F6F1E7;line-height:1';e.appendChild(m);});}
document.body.dataset.ready='1';
})();
