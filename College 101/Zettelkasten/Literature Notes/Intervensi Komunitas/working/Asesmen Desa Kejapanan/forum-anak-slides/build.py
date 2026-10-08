"""Build the Forum Anak assessment slides (APKL, USG, Fishbone) as 1920x1080 HTML pages.

Content is copied from "Laporan Asesmen APKL, USG, dan Fishbone - Forum Anak Desa Kejapanan.md".
Run: python3 build.py  (writes s01.html ... s10.html next to this file)
"""
from pathlib import Path

OUT = Path(__file__).parent

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
:root { --navy:#254671; --ink:#1d2f47; --muted:#5d6f85; --yellow:#ffde59; --line:#dfe5ec; --soft:#f5f7fa; --pass:#2f7d4f; --fail:#b4532f; }
body { width:1920px; height:1080px; background:#fff; font-family:Montserrat,sans-serif; color:var(--ink); position:relative; overflow:hidden; }
.kick { position:absolute; left:112px; top:52px; font-family:"League Spartan"; font-weight:800; font-size:20px; letter-spacing:3px; color:var(--muted); }
h1 { position:absolute; left:108px; top:80px; font-family:"League Spartan"; font-weight:800; font-size:84px; letter-spacing:-3px; color:var(--navy); line-height:1; }
.page { position:absolute; right:108px; top:96px; font-family:"League Spartan"; font-weight:800; font-size:22px; color:var(--navy); background:var(--yellow); border-radius:10px; padding:8px 14px; }
.body { position:absolute; left:108px; right:108px; top:200px; bottom:70px; display:flex; flex-direction:column; gap:18px; }
.foot { position:absolute; left:108px; right:108px; bottom:24px; font-size:14px; color:#7a8899; }
p.lead { font-size:21px; line-height:1.45; color:#2b3d53; max-width:1600px; }
p.lead b { color:var(--ink); }
table { border-collapse:separate; border-spacing:0; width:100%; border:2px solid var(--line); border-radius:14px; overflow:hidden; }
th { background:var(--navy); color:#fff; text-align:left; font-weight:700; padding:10px 14px; font-size:var(--fs,18px); }
td { padding:9px 14px; font-size:var(--fs,18px); line-height:1.35; border-top:1.5px solid var(--line); vertical-align:top; color:#2b3d53; }
tr:nth-child(even) td { background:var(--soft); }
td.c, th.c { text-align:center; }
td.n { font-weight:800; color:var(--navy); text-align:center; font-variant-numeric:tabular-nums; }
tr.tot td { background:#fff8dc !important; font-weight:700; color:var(--ink); }
.pass { color:var(--pass); font-weight:800; }
.fail { color:var(--fail); font-weight:800; }
.cols { display:grid; gap:24px; align-items:start; }
.cap { font-family:"League Spartan"; font-weight:800; font-size:22px; color:var(--navy); margin-bottom:8px; }
.note { background:var(--soft); border-left:6px solid var(--navy); border-radius:0 12px 12px 0; padding:14px 18px; font-size:18px; line-height:1.45; color:#2b3d53; }
.note b { color:var(--ink); }
.key { background:var(--navy); color:#fff; border-radius:16px; padding:20px 26px; font-size:22px; line-height:1.45; }
.key b { color:var(--yellow); }
.flow { display:flex; gap:10px; align-items:center; flex-wrap:wrap; }
.flow span { background:var(--navy); color:#fff; font-weight:700; border-radius:10px; padding:8px 16px; font-size:18px; }
.flow span.on { background:var(--yellow); color:var(--navy); }
.flow i { color:var(--navy); font-style:normal; font-weight:800; }
sup { font-size:.65em; }
"""

HEAD = ('<!doctype html><html lang="id"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=League+Spartan:wght@700;800'
        '&family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap" rel="stylesheet">'
        '<style>' + CSS + '</style></head><body>')


def flow(active):
    steps = ["MAP", "APKL", "USG", "Fishbone"]
    parts = []
    for i, s in enumerate(steps):
        parts.append(f'<span class="{"on" if s == active else ""}">{s}</span>')
        if i < len(steps) - 1:
            parts.append("<i>→</i>")
    return '<div class="flow">' + "".join(parts) + "</div>"


def page(kick, title, body, foot, num):
    return (HEAD + f'<div class="kick">{kick}</div><h1>{title}</h1><div class="page">{num}</div>'
            f'<div class="body">{body}</div><div class="foot">{foot}</div></body></html>')


def table(headers, rows, fs=18, widths=None, total=True, center_cols=()):
    cols = ""
    if widths:
        cols = "<colgroup>" + "".join(f'<col style="width:{w}">' for w in widths) + "</colgroup>"
    h = "".join(f'<th class="{"c" if i in center_cols else ""}">{x}</th>' for i, x in enumerate(headers))
    body = []
    for ri, r in enumerate(rows):
        cls = ' class="tot"' if total and ri == len(rows) - 1 else ""
        cells = []
        for ci, x in enumerate(r):
            klass = "n" if ci in center_cols else ""
            cells.append(f'<td class="{klass}">{x}</td>')
        body.append(f"<tr{cls}>" + "".join(cells) + "</tr>")
    return f'<table style="--fs:{fs}px">{cols}<thead><tr>{h}</tr></thead><tbody>{"".join(body)}</tbody></table>'


def apkl(rows, total, status, fs):
    r = [[k, v, t] for k, v, t in rows]
    r.append(["<b>Total</b>", f"<b>{total}</b>", status])
    return table(["Indikator", "Skor", "Keterangan"], r, fs=fs, widths=["13%", "10%", "77%"], center_cols=(0, 1))


def usg(rows, total, status, fs):
    r = [[k, v, t] for k, v, t in rows]
    r.append(["<b>Total</b>", f"<b>{total}</b>", status])
    return table(["Kriteria", "Nilai", "Keterangan"], r, fs=fs, widths=["22%", "11%", "67%"], center_cols=(1,))


LOLOS = '<span class="pass">Lolos.</span>'
TIDAK = '<span class="fail">Tidak lolos</span> (L di bawah 3).'
SRC_P = "Sumber: Pambudi, K. S. (2026). <i>Asesmen dan analisis urgensi masalah</i> [PowerPoint slides]."
SRC_JP = "Sumber: wawancara dan observasi Kelompok 1; Jatimsatunews (2025); Pambudi (2026)."

slides = {}

# 1. Rumusan masalah
slides["s01"] = page(
    "ASESMEN FORUM ANAK DESA KEJAPANAN", "RUMUSAN MASALAH HASIL MAP",
    flow("MAP")
    + '<p class="lead"><b>Fokus intervensi:</b> Forum Anak Desa Kejapanan, Kecamatan Gempol, Kabupaten Pasuruan. '
      'Alur asesmen: MAP menggali masalah, APKL menyaring masalah, USG menentukan prioritas, dan Fishbone menelusuri akar masalah (Pambudi, 2026). '
      'Metode Asesmen Partisipatif (MAP) melalui wawancara dan observasi lapangan menghasilkan lima masalah.</p>'.replace('<p class="lead">','<p class="lead" style="font-size:24px">')
    + table(["No", "Rumusan masalah"], [
        ["M1", "Rendahnya keaktifan dan keberfungsian Forum Anak sebagai wadah partisipasi anak, meskipun secara kelembagaan sudah terbentuk"],
        ["M2", "Belum meratanya jangkauan partisipasi dan kegiatan lintas dusun, sehingga aktivitas desa terpusat pada wilayah tertentu"],
        ["M3", "Dominasi partisipasi segelintir pihak dalam forum musyawarah desa (partisipasi deliberatif belum merata)"],
        ["M4", "Stagnasi peran Karang Taruna sebagai organisasi kepemudaan desa"],
        ["M5", "Terbatasnya kapasitas sumber daya pengelola dalam mengoptimalkan peluang baru desa (kafe desa, hidroponik, dan lainnya)"],
    ], fs=25, widths=["8%", "92%"], total=False, center_cols=(0,))
    + '<div class="note" style="font-size:21px"><b>Catatan:</b> isu relasi pondok pesantren dan warga juga muncul dalam wawancara, tetapi tidak dianalisis karena data pendukungnya belum memadai dan isunya sensitif.</div>',
    "Disiapkan oleh Kelompok 1, Universitas Negeri Malang. " + SRC_P, "1/10")

# 2. APKL M1, M2
m1 = apkl([
    ["A", "5", "Forum Anak sudah terbentuk, tetapi kegiatannya tidak berjalan rutin. Kondisi ini sedang terjadi dan ditemukan melalui wawancara dan observasi. Kesenjangan ini menonjol karena, menurut pernyataan Kepala Desa dalam pemberitaan, Kejapanan berstatus Desa Ramah Anak sejak Juli 2025 (Jatimsatunews, 2025)."],
    ["P", "4", "Forum ada secara struktural, tetapi belum berfungsi sebagai wadah partisipasi dan suara anak. Penyebabnya berlapis (lihat Fishbone), meskipun belum menimbulkan kerugian akut."],
    ["K", "3", "Sasaran langsung adalah sekitar 4.142 anak usia 8 sampai 18 tahun<sup>1</sup>, atau sekitar 19% penduduk. Dampaknya nyata bagi kelompok usia ini dan keluarganya, tetapi tidak menyangkut hajat hidup seluruh warga secara langsung."],
    ["L", "5", "Kelembagaan sudah ada dan terdapat pendamping dari pemerintah desa dan sekolah (SDN Kejapanan V). Intervensi sesuai dengan peran mahasiswa psikologi dan tidak perlu membangun dari nol."],
], "17", LOLOS, 17)
m2 = apkl([
    ["A", "4", "Pemerintah desa merasakan langsung kesulitan merangkul seluruh dusun, dan kegiatan berputar di wilayah yang sama. Keterangan ini sejalan dengan wawancara Pak Eki tentang ego wilayah dan sulitnya kegiatan gabungan tingkat desa."],
    ["P", "4", "Desa terbagi atas 12 dusun dengan karakter berbeda. Ketimpangan akses kegiatan menyimpang dari prinsip pembangunan inklusif dan penyebabnya bersifat struktural."],
    ["K", "5", "Menyangkut seluruh warga di 12 dusun (sekitar 21.545 jiwa)."],
    ["L", "2", "Penyelesaiannya menuntut koordinasi 12 dusun, 27 RW, dan 152 RT yang masing-masing memiliki agenda sendiri. Hal ini berada di luar kewenangan dan rentang waktu kelompok."],
], "15", TIDAK, 17)
slides["s02"] = page(
    "ASESMEN FORUM ANAK · APKL 1/3", "ANALISIS APKL",
    flow("APKL")
    + '<p class="lead" style="font-size:18px">Setiap indikator dinilai dengan skala 1 sampai 5 (skor maksimal 20). Dalam rangkaian asesmen, APKL berfungsi untuk <b>menyaring</b> masalah (Pambudi, 2026). '
      'Kriteria lolos yang digunakan adalah <b>Kelayakan (L) minimal 3</b>. Indikator L menilai apakah isu realistis dan relevan untuk ditangani sesuai tugas dan tanggung jawab pelaksana. '
      'Isu dengan skor total tinggi tetapi tidak layak ditangani kelompok tetap penting, tetapi tidak dapat menjadi fokus intervensi kelompok.</p>'
    + f'<div class="cols" style="grid-template-columns:1fr 1fr"><div><div class="cap">Tabel APKL 1: M1, rendahnya keaktifan Forum Anak</div>{m1}</div>'
      f'<div><div class="cap">Tabel APKL 2: M2, jangkauan partisipasi lintas dusun belum merata</div>{m2}</div></div>',
    "<sup>1</sup> Dihitung dari tabel demografi desa: 2.063 laki-laki dan 2.079 perempuan usia 8 sampai 18 tahun. Persentase dihitung terhadap 21.545 jiwa. "
    "Sumber: Jatimsatunews (2025); Pambudi (2026); wawancara dan observasi Kelompok 1.", "2/10")

# 3. APKL M3, M4, M5
m3 = apkl([
    ["A", "4", "Pada rapat besar bersama Kepala Desa, pendapat hanya disampaikan oleh beberapa orang. Menurut Pak Eki, yang aktif bersuara hanya tiga orang: Pak Eki sendiri, Pak Toni, dan Pak Putut."],
    ["P", "3", "Musyawarah tetap berjalan dan menghasilkan keputusan, tetapi kualitas partisipasi belum ideal. Masalahnya laten dan belum menimbulkan konflik."],
    ["K", "3", "Berdampak pada keterwakilan aspirasi warga, tetapi terbatas pada peserta forum musyawarah."],
    ["L", "3", "Dapat dibantu dengan teknik fasilitasi, seperti diskusi kelompok kecil atau pengumpulan aspirasi tertulis. Namun, penerapannya bergantung pada persetujuan pemimpin rapat karena kelompok tidak memimpin musyawarah."],
], "13", LOLOS, 17.5)
m4 = apkl([
    ["A", "4", "Karang Taruna kurang aktif dan program kerjanya tidak berjalan, berdasarkan wawancara dan observasi."],
    ["P", "4", "Karang Taruna seharusnya menjadi penggerak kegiatan kepemudaan desa. Pemberitaan menyebut kegiatan seperti bimbingan belajar gratis oleh Karang Taruna (Jatimsatunews, 2025), tetapi temuan lapangan menunjukkan program kerjanya tidak berjalan. Kesenjangan antara citra resmi dan kondisi lapangan ini memperjelas masalahnya."],
    ["K", "4", "Berdampak pada kelompok pemuda dan menghambat regenerasi kepemimpinan desa."],
    ["L", "3", "Pembenahan memerlukan perbaikan struktur dan regenerasi pengurus yang bergantung pada dinamika internal organisasi. Kelompok hanya dapat berperan sebagai fasilitator."],
], "15", LOLOS, 17.5)
m5 = apkl([
    ["A", "4", "Peluang seperti kafe desa dan hidroponik sudah ada, tetapi belum terkelola secara optimal."],
    ["P", "3", "Terdapat kesenjangan antara potensi dan kapasitas pengelolaan (SDM, waktu, pendanaan). Masalahnya berupa peluang yang belum tergarap, bukan penyimpangan dari standar yang berlaku."],
    ["K", "4", "Berpotensi meningkatkan ekonomi dan lapangan kerja warga apabila dikelola dengan baik."],
    ["L", "2", "Membutuhkan modal, keahlian teknis, dan jangka waktu panjang di luar kapasitas intervensi kelompok."],
], "13", TIDAK, 17.5)
slides["s03"] = page(
    "ASESMEN FORUM ANAK · APKL 2/3", "ANALISIS APKL",
    f'<div class="cols" style="grid-template-columns:1fr 1fr 1fr;margin-top:6px">'
    f'<div><div class="cap">Tabel APKL 3: M3, dominasi partisipasi dalam musyawarah desa</div>{m3}</div>'
    f'<div><div class="cap">Tabel APKL 4: M4, stagnasi Karang Taruna</div>{m4}</div>'
    f'<div><div class="cap">Tabel APKL 5: M5, keterbatasan sumber daya pengelola peluang baru</div>{m5}</div></div>',
    SRC_JP, "3/10")

# 4. Rekap APKL
slides["s04"] = page(
    "ASESMEN FORUM ANAK · APKL 3/3", "REKAP APKL",
    flow("APKL")
    + table(["Masalah", "A", "P", "K", "L", "Total", "Status"], [
        ["M1, keaktifan Forum Anak", "5", "4", "3", "5", "17", '<span class="pass">Lolos</span>'],
        ["M2, jangkauan lintas dusun", "4", "4", "5", "2", "15", '<span class="fail">Tidak lolos</span>'],
        ["M4, stagnasi Karang Taruna", "4", "4", "4", "3", "15", '<span class="pass">Lolos</span>'],
        ["M3, dominasi dalam musyawarah", "4", "3", "3", "3", "13", '<span class="pass">Lolos</span>'],
        ["M5, sumber daya pengelola peluang baru", "4", "3", "4", "2", "13", '<span class="fail">Tidak lolos</span>'],
    ], fs=31, widths=["40%", "8%", "8%", "8%", "8%", "10%", "18%"], total=False, center_cols=(1, 2, 3, 4, 5))
    + '<div class="key" style="font-size:26px">Kriteria lolos: <b>Kelayakan (L) minimal 3</b>. M2 memiliki skor kekhalayakan tertinggi, tetapi tidak lolos karena cakupannya melampaui kemampuan kelompok. '
      'M2 dan M4 tidak diabaikan: keduanya muncul kembali sebagai penyebab M1 dalam analisis Fishbone.</div>',
    SRC_P, "4/10")

# 5. USG tables
u1 = usg([
    ["Urgency", "4", "Selama forum vakum, sebagian anggota melewati usia 18 tahun tanpa pernah mengalami partisipasi yang bermakna. Kerugiannya bertambah setiap tahun, meskipun tidak bersifat darurat."],
    ["Seriousness", "4", "Hak partisipasi anak belum terpenuhi meskipun desa berstatus Desa Ramah Anak. Kondisi ini berdampak pada kepercayaan diri, kepemimpinan, dan kepedulian sosial anak."],
    ["Growth", "4", "Tanpa regenerasi dan pembinaan, forum berisiko hanya menjadi formalitas. Organisasi kepemudaan yang dapat menjadi pendamping (Karang Taruna) juga stagnan."],
], "12", "<b>Prioritas utama.</b>", 18.5)
u2 = usg([
    ["Urgency", "3", "Stagnasi sudah berlangsung, tetapi tidak menimbulkan kerugian yang mendesak."],
    ["Seriousness", "3", "Kegiatan kepemudaan menurun, tetapi belum menimbulkan masalah sosial berat."],
    ["Growth", "4", "Regenerasi yang terhambat dapat membuat organisasi vakum secara permanen."],
], "10", "<b>Prioritas kedua.</b>", 18.5)
u3 = usg([
    ["Urgency", "3", "Musyawarah masih berjalan dan keputusan tetap dihasilkan."],
    ["Seriousness", "3", "Berpengaruh pada keterwakilan aspirasi, tetapi belum menimbulkan konflik."],
    ["Growth", "2", "Cenderung stabil dan tidak menunjukkan tanda memburuk; perubahannya bergantung pada gaya fasilitasi."],
], "8", "<b>Prioritas ketiga.</b>", 18.5)
slides["s05"] = page(
    "ASESMEN FORUM ANAK · USG 1/2", "ANALISIS USG",
    flow("USG")
    + '<p class="lead">Masalah yang lolos APKL (M1, M3, M4) dinilai dengan skala 1 sampai 5 untuk setiap kriteria (skor maksimal 15).</p>'
    + f'<div class="cols" style="grid-template-columns:1fr 1fr 1fr">'
      f'<div><div class="cap">Tabel USG 1: M1, Forum Anak</div>{u1}</div>'
      f'<div><div class="cap">Tabel USG 2: M4, Karang Taruna</div>{u2}</div>'
      f'<div><div class="cap">Tabel USG 3: M3, dominasi dalam musyawarah</div>{u3}</div></div>',
    SRC_P, "5/10")

# 6. Rekap USG
slides["s06"] = page(
    "ASESMEN FORUM ANAK · USG 2/2", "REKAP USG",
    flow("USG")
    + table(["Peringkat", "Masalah", "U", "S", "G", "Total"], [
        ["1", "M1, Forum Anak", "4", "4", "4", "12"],
        ["2", "M4, Karang Taruna", "3", "3", "4", "10"],
        ["3", "M3, musyawarah", "3", "3", "2", "8"],
    ], fs=38, widths=["14%", "46%", "10%", "10%", "10%", "10%"], total=False, center_cols=(0, 2, 3, 4, 5))
    + '<div class="key" style="font-size:36px"><b>M1 menjadi isu kunci.</b> Kelembagaannya sudah ada, sasarannya terukur, dan pembenahannya dapat menjadi pintu masuk untuk menjangkau dusun lain.</div>',
    SRC_P, "6/10")

# 7. Fishbone diagram
slides["s07"] = page(
    "ASESMEN FORUM ANAK · FISHBONE 1/3", "ANALISIS FISHBONE",
    '<div style="display:flex;gap:28px;align-items:flex-start">'
    '<div style="flex:none;width:380px;display:flex;flex-direction:column;gap:18px">'
    + flow("Fishbone")
    + '<div class="key"><b>Masalah utama (kepala ikan):</b> rendahnya keaktifan Forum Anak Desa Kejapanan.</div>'
      '<div class="note">Kategori penyebab mengikuti pembagian faktor tingkat mikro dan meso serta faktor kontekstual (Pambudi, 2026).</div></div>'
      '<img src="fishbone-forum-anak.svg" style="width:1300px;height:auto;border:2px solid var(--line);border-radius:14px" alt="Diagram fishbone"></div>',
    SRC_P, "7/10")

# 8. Fishbone table
slides["s08"] = page(
    "ASESMEN FORUM ANAK · FISHBONE 2/3", "PENYEBAB PER KATEGORI",
    table(["Kategori", "Penyebab", "Keterkaitan"], [
        ["<b>Individu</b>", "Motivasi anak rendah; waktu tersita kegiatan sekolah; manfaat forum tidak dirasakan", "Sebagian besar merupakan akibat dari kategori lain, terutama organisasi dan relasi kuasa"],
        ["<b>Organisasi</b>", "Kegiatan tidak rutin; program kurang sesuai minat anak; tidak ada kegiatan unggulan; tidak ada regenerasi", "Kegiatan yang tidak rutin merupakan gejala dari lemahnya tata kelola"],
        ["<b>Relasi kuasa</b>", "Anak tidak dilibatkan dalam keputusan; kegiatan bergantung pada orang dewasa; aspirasi anak tidak ditanggapi", "Ketergantungan pada orang dewasa diperberat oleh stagnasi Karang Taruna (M4)"],
        ["<b>Norma sosial</b>", "Anak dipandang sebagai objek kegiatan; prestasi akademik lebih diutamakan", "Mendasari relasi kuasa yang tidak memberi anak peran"],
        ["<b>Struktur peluang</b>", "Ruang kumpul anak minim; kegiatan terpusat di wilayah tertentu; akses antardusun sulit", "Bagian dari masalah jangkauan lintas dusun (M2)"],
        ["<b>Tata kelola</b>", "SK tanpa pembinaan; tidak ada data dan evaluasi; anggaran belum jelas", "Forum tercatat secara formal, termasuk dalam status Desa Ramah Anak, tetapi tidak dikelola secara berkelanjutan"],
    ], fs=27, widths=["18%", "44%", "38%"], total=False),
    "Kategori Individu, Organisasi, dan Relasi kuasa merupakan faktor tingkat mikro dan meso; Norma sosial, Struktur peluang, dan Tata kelola merupakan faktor kontekstual (Pambudi, 2026).", "8/10")

# 9. Penjelasan deskriptif
layer = lambda n, t, d: (f'<div style="display:grid;grid-template-columns:64px 1fr;gap:18px;align-items:start">'
                         f'<div style="width:64px;height:64px;border-radius:50%;background:var(--yellow);color:var(--navy);font-family:\'League Spartan\';font-weight:800;font-size:32px;display:grid;place-items:center">{n}</div>'
                         f'<div><div class="cap" style="font-size:26px;margin-bottom:4px">{t}</div><p class="lead" style="font-size:23px">{d}</p></div></div>')
slides["s09"] = page(
    "ASESMEN FORUM ANAK · FISHBONE 3/3", "PENJELASAN DESKRIPTIF",
    '<p class="lead" style="font-size:24px">Penyebab yang tampak pada tingkat individu, seperti motivasi rendah dan manfaat yang tidak terasa, lebih tepat dibaca sebagai <b>gejala</b>. Penelusurannya mengarah ke tiga lapisan.</p>'
    + layer("1", "Tata kelola", "Kegiatan tidak rutin karena forum berhenti pada SK. Setelah pembentukan, tidak ada pembinaan, anggaran yang jelas, data anggota, maupun evaluasi. Pemberitaan mencatat Forum Anak Desa dan status Desa Ramah Anak sebagai capaian desa (Jatimsatunews, 2025), sedangkan temuan lapangan menunjukkan bahwa forum belum berfungsi.")
    + layer("2", "Relasi kuasa dan norma sosial", "Program kurang sesuai minat dan manfaatnya tidak terasa karena anak tidak dilibatkan dalam menentukan kegiatan, dan aspirasinya tidak ditanggapi. Pola ini berakar pada norma yang memandang anak sebagai objek kegiatan dan lebih mengutamakan prestasi akademik.")
    + layer("3", "Lingkungan pendukung", "Tidak ada pihak yang mengisi kekosongan tersebut. Karang Taruna sebagai organisasi kepemudaan juga stagnan (M4), sedangkan kegiatan desa terpusat dan akses antardusun sulit (M2). Pak Eki juga menyebut bahwa akhir pekan sudah dipenuhi agenda RT/RW dan kegiatan gabungan tingkat desa sulit mengumpulkan semua wilayah. Akibatnya, forum sulit menjangkau anak di dusun lain.")
    + '<div class="key" style="font-size:26px"><b>Akar masalah utama:</b> Forum Anak berdiri secara formal tanpa sistem pembinaan dan pengelolaan yang berkelanjutan, dan tanpa ruang yang memberi anak peran nyata dalam menentukan kegiatan serta keputusan.</div>',
    SRC_JP, "9/10")

# 10. Potensi + kesimpulan
pot = [
    "Dukungan pemerintah desa dan status Desa Ramah Anak, yang memberi dasar formal untuk menghidupkan kembali forum.",
    "SDN Kejapanan V sebagai pendamping dan jalur menjangkau anak.",
    "Forum Anak dan Lingkungan yang memiliki perwakilan di setiap dusun, sehingga dapat menjadi jalur untuk mengatasi kegiatan yang terpusat.",
    "Perpustakaan desa (Jatimsatunews, 2025) sebagai tempat kegiatan yang sudah tersedia.",
    "Tokoh agama dan tokoh pemuda.",
    "Ragam potensi UMKM (batik, keset, Kampung Pia) sebagai materi kegiatan Forum Anak.",
    "Karang Taruna sebagai mitra jangka panjang apabila organisasi ini ikut dibenahi.",
]
li = "".join(f'<li style="margin:0 0 10px 0">{x}</li>' for x in pot)
slides["s10"] = page(
    "ASESMEN FORUM ANAK", "POTENSI &amp; KESIMPULAN",
    '<div class="cols" style="grid-template-columns:1fr 1fr;gap:40px">'
    f'<div><div class="cap" style="font-size:28px">Potensi pendukung penyelesaian masalah</div><ul style="padding-left:24px;font-size:24px;line-height:1.4;color:#2b3d53">{li}</ul></div>'
    '<div style="display:flex;flex-direction:column;gap:18px"><div class="cap" style="font-size:28px;margin:0">Kesimpulan hasil asesmen</div>'
    '<div class="key" style="font-size:25px">MAP menghasilkan lima masalah. APKL menyaring M2 dan M5 karena berada di luar kelayakan kelompok. USG menetapkan M1, rendahnya keaktifan Forum Anak, sebagai isu kunci. '
    'Fishbone menunjukkan bahwa akar masalahnya bukan kurangnya minat anak, melainkan forum yang berdiri secara formal tanpa sistem pembinaan dan tanpa ruang partisipasi bermakna bagi anak. '
    '<b>Rencana intervensi perlu menyasar tata kelola forum dan peran anak dalam pengambilan keputusan, bukan sekadar menambah kegiatan.</b></div>'
    '<div class="note" style="font-size:16px"><b>Referensi</b><br>Jatimsatunews. (2025, 15 September). <i>Kejapanan-Gempol jadi desa ke-20 dinilai Lomba Kampung Pancasila: Harmoni warga, UMKM unggulan, hingga nol stunting</i>. https://jatimsatunews.com/2025/09/kejapanan-gempol-desa-ke-20-dinilai.html<br>'
    'Pambudi, K. S. (2026). <i>Asesmen dan analisis urgensi masalah</i> [PowerPoint slides].</div></div></div>',
    "Disiapkan oleh Kelompok 1, Universitas Negeri Malang.", "10/10")

for name, html in slides.items():
    (OUT / f"{name}.html").write_text(html, encoding="utf-8")
print("wrote", len(slides), "slides")
