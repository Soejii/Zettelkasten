# Forum Anak assessment slides 17-26, native rebuild. Text copied from the report .md.
# Executed inside native_build.py's namespace (Slide, NAVY, ... are defined there).
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from measure import measure as _measure

PASS, FAIL, ZEBRA, TOTAL, BORDER = "#2f7d4f", "#b4532f", "#f5f7fa", "#fff8dc", "#dfe5ec"
FOOT = "#7a8899"


def _h(text, w, fs, bold=False, lh=1.3):
    return _measure([(text, w, fs, bold, lh)])[0]


def header(s, kick, title, num):
    s.T(112, 46, 1500, kick, 20, True, MUTED, lh=1.1)
    s.T(108, 72, 1560, title, 78, True, NAVY, lh=1.0)
    s.S(1700, 90, 112, 42, YELLOW, 10)
    s.T(1700, 99, 112, num, 20, True, NAVY, "center", 1.1)


def flow(s, x, y, active):
    for i, step in enumerate(["MAP", "APKL", "USG", "Fishbone"]):
        w = 44 + len(step) * 12
        on = step == active
        s.S(x, y, w, 40, YELLOW if on else NAVY, 10)
        s.T(x, y + 9, w, step, 18, True, NAVY if on else WHITE, "center", 1.1)
        x += w
        if i < 3:
            s.T(x + 2, y + 8, 26, "→", 18, True, NAVY, "center", 1.1)
            x += 30
    return y + 40


def para(s, x, y, w, text, fs, color=BODY, lh=1.4, bold=False):
    s.T(x, y, w, text, fs, bold, color, lh=lh)
    return y + _h(text, w, fs, bold, lh)


def box(s, x, y, w, text, fs, fill, color, pad=18, lh=1.4, bold=False, bar=None):
    th = _h(text, w - 2 * pad - (10 if bar else 0), fs, bold, lh)
    hgt = th + 2 * pad
    s.S(x, y, w, hgt, fill, 14)
    if bar:
        s.S(x, y, 8, hgt, bar, 4)
    s.T(x + pad + (10 if bar else 0), y + pad, w - 2 * pad - (10 if bar else 0), text, fs, bold, color, lh=lh)
    return y + hgt


def table(s, x, y, cols, head, rows, fs, lh=1.35, center=(), bold_cols=(), last_total=False, colors=None, hfs=None):
    """Draw a table; return bottom y. colors: {(row, col): hex} for status cells."""
    W = sum(cols)
    hfs = hfs or fs
    pad = 10
    hh = max(_h(t, c - 24, hfs, True, 1.2) for t, c in zip(head, cols)) + 2 * pad
    heights = []
    for r in rows:
        heights.append(max(_h(t, c - 24, fs, (ci in bold_cols), lh) for ci, (t, c) in enumerate(zip(r, cols))) + 2 * pad)
    total = hh + sum(heights)
    s.S(x - 2, y - 2, W + 4, total + 4, BORDER, 12)
    s.S(x, y, W, hh, NAVY, 10)
    cx = x
    for ci, (t, c) in enumerate(zip(head, cols)):
        s.T(cx + 12, y + pad, c - 24, t, hfs, True, WHITE, "center" if ci in center else "start", 1.2)
        cx += c
    ry = y + hh
    for ri, (r, rh) in enumerate(zip(rows, heights)):
        is_total = last_total and ri == len(rows) - 1
        fill = TOTAL if is_total else (ZEBRA if ri % 2 else WHITE)
        s.S(x, ry, W, rh, fill, 0)
        cx = x
        for ci, (t, c) in enumerate(zip(r, cols)):
            col = (colors or {}).get((ri, ci), NAVY if ci in center else BODY)
            b = is_total or ci in bold_cols or (colors or {}).get((ri, ci)) is not None
            s.T(cx + 12, ry + pad, c - 24, t, fs, b, col, "center" if ci in center else "start", lh)
            cx += c
        ry += rh
    return ry


def caption(s, x, y, w, text, fs=21):
    return para(s, x, y, w, text, fs, NAVY, 1.15, True) + 8


def foot(s, text):
    s.T(108, 1044, 1704, text, 13, False, FOOT, lh=1.3)


SRC_P = "Sumber: Pambudi, K. S. (2026). Asesmen dan analisis urgensi masalah [PowerPoint slides]."
SRC_JP = "Sumber: wawancara dan observasi Kelompok 1; Jatimsatunews (2025); Pambudi (2026)."
def PRI(t, lvl):
    return f"Dengan total skor {t} dari maksimal 20, isu ini termasuk prioritas {lvl}."

# ---------------------------------------------------------------- 17 Rumusan masalah
s = Slide("PBt8BSWm8Q5qG36L", ["PBt8BSWm8Q5qG36L-LB3tkkmJ38r0TYbN"])
header(s, "ASESMEN FORUM ANAK DESA KEJAPANAN", "RUMUSAN MASALAH HASIL MAP", "1/11")
y = flow(s, 108, 182, "MAP") + 20
y = para(s, 108, y, 1704, "Metode Asesmen Partisipatif (MAP) melalui wawancara dan observasi lapangan menghasilkan lima masalah.", 26) + 22
y = table(s, 108, y, [130, 1574], ["No", "Rumusan masalah"], [
    ["M1", "Rendahnya keaktifan dan keberfungsian Forum Anak sebagai wadah partisipasi anak, meskipun secara kelembagaan sudah terbentuk"],
    ["M2", "Belum meratanya jangkauan partisipasi dan kegiatan lintas dusun, sehingga aktivitas desa terpusat pada wilayah tertentu"],
    ["M3", "Dominasi partisipasi segelintir pihak dalam forum musyawarah desa (partisipasi deliberatif belum merata)"],
    ["M4", "Stagnasi peran Karang Taruna sebagai organisasi kepemudaan desa"],
    ["M5", "Terbatasnya kapasitas sumber daya pengelola dalam mengoptimalkan peluang baru desa (kafe desa, hidroponik, dan lainnya)"]],
    27, center=(0,), bold_cols=(0,)) + 26
box(s, 108, y, 1704, "Catatan: isu relasi pondok pesantren dan warga juga muncul dalam wawancara, tetapi tidak dianalisis karena data pendukungnya belum memadai dan isunya sensitif.", 23, SOFT, BODY, bar=NAVY)
foot(s, "Disiapkan oleh Kelompok 1, Universitas Negeri Malang.")
SLIDES["17"] = s

# ---------------------------------------------------------------- 18 APKL 1/3
s = Slide("PB1KpPwgPWxPrDd0", ["PB1KpPwgPWxPrDd0-LBR02qQyHxWCTT0R"])
header(s, "ASESMEN FORUM ANAK · APKL 1/3", "ANALISIS APKL", "2/11")
y = flow(s, 108, 182, "APKL") + 16
y = para(s, 108, y, 1704, "Setiap indikator dinilai dengan skala 1 sampai 5 (skor maksimal 20). Dalam rangkaian asesmen, APKL berfungsi untuk menyaring masalah (Pambudi, 2026). Hasil APKL kemudian dilanjutkan dengan USG untuk menentukan skala prioritas.", 21) + 18
cols = [104, 76, 660]
apkl_head = ["Indikator", "Skor", "Keterangan"]
yy = caption(s, 108, y, 840, "Tabel APKL 1: M1, rendahnya keaktifan Forum Anak")
table(s, 108, yy, cols, apkl_head, [
    ["A", "5", "Forum Anak sudah terbentuk, tetapi kegiatannya tidak berjalan rutin. Kondisi ini sedang terjadi dan ditemukan melalui wawancara dan observasi. Kesenjangan ini menonjol karena, menurut pernyataan Kepala Desa dalam pemberitaan, Kejapanan berstatus Desa Ramah Anak sejak Juli 2025 (Jatimsatunews, 2025)."],
    ["P", "4", "Forum ada secara struktural, tetapi belum berfungsi sebagai wadah partisipasi dan suara anak. Penyebabnya berlapis (lihat Fishbone), meskipun belum menimbulkan kerugian akut."],
    ["K", "3", "Sasaran langsung adalah sekitar 4.142 anak usia 8 sampai 18 tahun¹, atau sekitar 19% penduduk. Dampaknya nyata bagi kelompok usia ini dan keluarganya, tetapi tidak menyangkut hajat hidup seluruh warga secara langsung."],
    ["L", "5", "Kelembagaan sudah ada dan terdapat pendamping dari pemerintah desa dan sekolah (SDN Kejapanan V). Intervensi sesuai dengan peran mahasiswa psikologi dan tidak perlu membangun dari nol."],
    ["Total", "17", PRI(17, "tinggi")]], 20, lh=1.3, center=(0, 1), last_total=True)
yy = caption(s, 972, y, 840, "Tabel APKL 2: M2, jangkauan partisipasi lintas dusun belum merata")
table(s, 972, yy, cols, apkl_head, [
    ["A", "4", "Pemerintah desa merasakan langsung kesulitan merangkul seluruh dusun, dan kegiatan berputar di wilayah yang sama. Keterangan ini sejalan dengan wawancara Pak Eki tentang ego wilayah dan sulitnya kegiatan gabungan tingkat desa."],
    ["P", "4", "Desa terbagi atas 12 dusun dengan karakter berbeda. Ketimpangan akses kegiatan menyimpang dari prinsip pembangunan inklusif dan penyebabnya bersifat struktural."],
    ["K", "5", "Menyangkut seluruh warga di 12 dusun (sekitar 21.545 jiwa)."],
    ["L", "2", "Penyelesaiannya menuntut koordinasi 12 dusun, 27 RW, dan 152 RT yang masing-masing memiliki agenda sendiri. Hal ini berada di luar kewenangan dan rentang waktu kelompok."],
    ["Total", "15", PRI(15, "sedang-tinggi")]], 20, lh=1.3, center=(0, 1), last_total=True)
foot(s, "¹ Dihitung dari tabel demografi desa: 2.063 laki-laki dan 2.079 perempuan usia 8 sampai 18 tahun. Persentase dihitung terhadap 21.545 jiwa. Sumber: Jatimsatunews (2025); Pambudi (2026); wawancara dan observasi Kelompok 1.")
SLIDES["18"] = s

# ---------------------------------------------------------------- 19 APKL 2/3
s = Slide("PBJ63PvqFhGyPY2z", ["PBJ63PvqFhGyPY2z-LBJtmRDBTQBQJzZf"])
header(s, "ASESMEN FORUM ANAK · APKL 2/3", "ANALISIS APKL", "3/11")
cols = [92, 64, 396]
tbls = [("Tabel APKL 3: M3, dominasi partisipasi dalam musyawarah desa", [
    ["A", "4", "Pada rapat besar bersama Kepala Desa, pendapat hanya disampaikan oleh beberapa orang. Menurut Pak Eki, yang aktif bersuara hanya tiga orang: Pak Eki sendiri, Pak Toni, dan Pak Putut."],
    ["P", "3", "Musyawarah tetap berjalan dan menghasilkan keputusan, tetapi kualitas partisipasi belum ideal. Masalahnya laten dan belum menimbulkan konflik."],
    ["K", "3", "Berdampak pada keterwakilan aspirasi warga, tetapi terbatas pada peserta forum musyawarah."],
    ["L", "3", "Dapat dibantu dengan teknik fasilitasi, seperti diskusi kelompok kecil atau pengumpulan aspirasi tertulis. Namun, penerapannya bergantung pada persetujuan pemimpin rapat karena kelompok tidak memimpin musyawarah."],
    ["Total", "13", PRI(13, "sedang")]], None),
        ("Tabel APKL 4: M4, stagnasi Karang Taruna", [
    ["A", "4", "Karang Taruna kurang aktif dan program kerjanya tidak berjalan, berdasarkan wawancara dan observasi."],
    ["P", "4", "Karang Taruna seharusnya menjadi penggerak kegiatan kepemudaan desa. Pemberitaan menyebut kegiatan seperti bimbingan belajar gratis oleh Karang Taruna (Jatimsatunews, 2025), tetapi temuan lapangan menunjukkan program kerjanya tidak berjalan. Kesenjangan antara citra resmi dan kondisi lapangan ini memperjelas masalahnya."],
    ["K", "4", "Berdampak pada kelompok pemuda dan menghambat regenerasi kepemimpinan desa."],
    ["L", "3", "Pembenahan memerlukan perbaikan struktur dan regenerasi pengurus yang bergantung pada dinamika internal organisasi. Kelompok hanya dapat berperan sebagai fasilitator."],
    ["Total", "15", PRI(15, "sedang-tinggi")]], None),
        ("Tabel APKL 5: M5, keterbatasan sumber daya pengelola peluang baru", [
    ["A", "4", "Peluang seperti kafe desa dan hidroponik sudah ada, tetapi belum terkelola secara optimal."],
    ["P", "3", "Terdapat kesenjangan antara potensi dan kapasitas pengelolaan (SDM, waktu, pendanaan). Masalahnya berupa peluang yang belum tergarap, bukan penyimpangan dari standar yang berlaku."],
    ["K", "4", "Berpotensi meningkatkan ekonomi dan lapangan kerja warga apabila dikelola dengan baik."],
    ["L", "2", "Membutuhkan modal, keahlian teknis, dan jangka waktu panjang di luar kapasitas intervensi kelompok."],
    ["Total", "13", PRI(13, "sedang")]], None)]
for k, (cap, rows, col) in enumerate(tbls):
    x = 108 + k * 576
    yy = caption(s, x, 192, 552, cap, 19)
    table(s, x, max(yy, 246), cols, apkl_head, rows, 18.5, lh=1.3, center=(0, 1), last_total=True, hfs=16)
foot(s, SRC_JP)
SLIDES["19"] = s

# ---------------------------------------------------------------- 20 Rekap APKL
s = Slide("PBW9H6NpjfNR5qTV", ["PBW9H6NpjfNR5qTV-LBvWtDYGv4dZ5dN1"])
header(s, "ASESMEN FORUM ANAK · APKL 3/3", "REKAP APKL", "4/11")
y = flow(s, 108, 182, "APKL") + 26
y = table(s, 108, y, [210, 834, 125, 125, 125, 125, 160], ["Peringkat", "Masalah", "A", "P", "K", "L", "Total"], [
    ["1", "M1, keaktifan Forum Anak", "5", "4", "3", "5", "17"],
    ["2", "M2, jangkauan lintas dusun", "4", "4", "5", "2", "15"],
    ["2", "M4, stagnasi Karang Taruna", "4", "4", "4", "3", "15"],
    ["4", "M3, dominasi dalam musyawarah", "4", "3", "3", "3", "13"],
    ["4", "M5, sumber daya pengelola peluang baru", "4", "3", "4", "2", "13"]],
    38, lh=1.2, center=(0, 2, 3, 4, 5, 6), bold_cols=(6,), hfs=34) + 34
box(s, 108, y, 1704, "M2 memiliki skor kekhalayakan tertinggi, tetapi skor kelayakannya rendah karena cakupannya melampaui kemampuan kelompok. M2 dan M4 juga muncul kembali sebagai penyebab M1 dalam analisis Fishbone.", 30, NAVY, WHITE, pad=28)
foot(s, SRC_P)
SLIDES["20"] = s

# ---------------------------------------------------------------- 21-22 USG tables (five problems) and 22b recap
uhead = ["Kriteria", "Nilai", "Keterangan"]
usg = [("Tabel USG 1: M1, Forum Anak", [
    ["Urgency", "4", "Selama forum vakum, sebagian anggota melewati usia 18 tahun tanpa pernah mengalami partisipasi yang bermakna. Kerugiannya bertambah setiap tahun, meskipun tidak bersifat darurat."],
    ["Seriousness", "4", "Hak partisipasi anak belum terpenuhi meskipun desa berstatus Desa Ramah Anak. Kondisi ini berdampak pada kepercayaan diri, kepemimpinan, dan kepedulian sosial anak."],
    ["Growth", "4", "Tanpa regenerasi dan pembinaan, forum berisiko hanya menjadi formalitas. Organisasi kepemudaan yang dapat menjadi pendamping (Karang Taruna) juga stagnan."],
    ["Total", "12", "Prioritas utama."]]),
       ("Tabel USG 2: M2, jangkauan lintas dusun", [
    ["Urgency", "3", "Pemerataan penting, tetapi pola ini sudah lama berlangsung dan tidak menimbulkan dampak langsung dalam waktu dekat."],
    ["Seriousness", "4", "Menyebabkan ketimpangan akses kegiatan dan menurunkan rasa kepemilikan warga di dusun yang kurang terjangkau."],
    ["Growth", "3", "Kesenjangan antardusun berpotensi melebar, tetapi pola ini bersifat struktural dan cenderung bertahan, bukan memburuk dengan cepat."],
    ["Total", "10", "Prioritas kedua."]]),
       ("Tabel USG 3: M3, dominasi dalam musyawarah", [
    ["Urgency", "3", "Musyawarah masih berjalan dan keputusan tetap dihasilkan."],
    ["Seriousness", "3", "Berpengaruh pada keterwakilan aspirasi, tetapi belum menimbulkan konflik."],
    ["Growth", "2", "Cenderung stabil dan tidak menunjukkan tanda memburuk; perubahannya bergantung pada gaya fasilitasi."],
    ["Total", "8", "Prioritas ketiga."]]),
       ("Tabel USG 4: M4, Karang Taruna", [
    ["Urgency", "3", "Stagnasi sudah berlangsung, tetapi tidak menimbulkan kerugian yang mendesak."],
    ["Seriousness", "3", "Kegiatan kepemudaan menurun, tetapi belum menimbulkan masalah sosial berat."],
    ["Growth", "4", "Regenerasi yang terhambat dapat membuat organisasi vakum secara permanen."],
    ["Total", "10", "Prioritas kedua."]]),
       ("Tabel USG 5: M5, sumber daya pengelola peluang baru", [
    ["Urgency", "3", "Peluang masih dapat dikembangkan secara bertahap, sehingga tidak bersifat darurat."],
    ["Seriousness", "3", "Potensi ekonomi yang tidak terkelola berarti manfaat bagi warga belum diperoleh, tetapi tidak menimbulkan kerugian langsung."],
    ["Growth", "2", "Perkembangannya lambat dan cenderung stagnan, bukan memburuk."],
    ["Total", "8", "Prioritas ketiga."]])]

s = Slide("PBsR0kl7CgQpyGB1", ["PBsR0kl7CgQpyGB1-LBztVSzHKB8XjgmH"])
header(s, "ASESMEN FORUM ANAK · USG 1/3", "ANALISIS USG", "5/11")
y = flow(s, 108, 182, "USG") + 16
y = para(s, 108, y, 1704, "Kelima masalah dinilai dengan skala 1 sampai 5 untuk setiap kriteria (skor maksimal 15).", 21) + 14
for k, (cap, rows) in enumerate(usg[:3]):
    x = 108 + k * 576
    yy = caption(s, x, y, 552, cap, 19)
    table(s, x, yy, [148, 66, 338], uhead, rows, 17, lh=1.3, center=(1,), last_total=True, hfs=15)
foot(s, SRC_P)
SLIDES["21"] = s

s = Slide("PBdkFRq0yJRCvtmV", ["PBdkFRq0yJRCvtmV-LBTZsFS2ZHHqBV4Q"])
header(s, "ASESMEN FORUM ANAK · USG 2/3", "ANALISIS USG", "6/11")
y = flow(s, 108, 182, "USG") + 26
for k, (cap, rows) in enumerate(usg[3:]):
    x = 108 + k * 876
    yy = caption(s, x, y, 828, cap, 21)
    table(s, x, yy, [190, 90, 548], uhead, rows, 23, lh=1.35, center=(1,), last_total=True, hfs=19)
foot(s, SRC_P)
SLIDES["22"] = s

s = Slide("PBsRZHvSxq7dThC6", [])
header(s, "ASESMEN FORUM ANAK · USG 3/3", "REKAP USG", "7/11")
y = flow(s, 108, 182, "USG") + 26
y = table(s, 108, y, [240, 784, 170, 170, 170, 170], ["Peringkat", "Masalah", "U", "S", "G", "Total"], [
    ["1", "M1, Forum Anak", "4", "4", "4", "12"],
    ["2", "M2, jangkauan lintas dusun", "3", "4", "3", "10"],
    ["2", "M4, Karang Taruna", "3", "3", "4", "10"],
    ["4", "M3, musyawarah", "3", "3", "2", "8"],
    ["4", "M5, sumber daya pengelola", "3", "3", "2", "8"]], 38, lh=1.2, center=(0, 2, 3, 4, 5), bold_cols=(5,), hfs=34) + 34
box(s, 108, y, 1704, "Isu dengan skor tertinggi menjadi isu yang dibahas lebih lanjut (Pambudi, 2026), sehingga M1 menjadi isu kunci. Kelembagaannya sudah ada, sasarannya terukur, dan pembenahannya dapat menjadi pintu masuk untuk menjangkau dusun lain.", 30, NAVY, WHITE, pad=28)
foot(s, SRC_P)
SLIDES["22b"] = s

# ---------------------------------------------------------------- 23 Fishbone diagram (diagram stays an image)
s = Slide("PBgYFY4j7g5b0l47", ["PBgYFY4j7g5b0l47-LBLLM2pprwM3z0Vj"])
header(s, "ASESMEN FORUM ANAK · FISHBONE 1/3", "ANALISIS FISHBONE", "8/11")
y = flow(s, 108, 182, "Fishbone") + 24
y = box(s, 108, y, 400, "Masalah utama (kepala ikan): rendahnya keaktifan Forum Anak Desa Kejapanan.", 22, NAVY, WHITE, pad=22) + 18
box(s, 108, y, 400, "Kategori penyebab mengikuti pembagian faktor tingkat mikro dan meso serta faktor kontekstual (Pambudi, 2026).", 18, SOFT, BODY, bar=NAVY)
s.S(538, 236, 1274, 736, WHITE, 14, BORDER, 2)
_img = {"type": "insert_fill", "page_id": s.page_id, "asset_type": "image", "asset_id": "MAHXVidHOnc", "alt_text": "Diagram fishbone rendahnya keaktifan Forum Anak", "top": 248, "left": 550, "width": 1250, "height": 720}
s.ops.append(_img)
s.shapes.append(_img)
foot(s, SRC_P)
SLIDES["23"] = s

# ---------------------------------------------------------------- 24 Penyebab per kategori
s = Slide("PB5LmXQGJ8DcdXL5", ["PB5LmXQGJ8DcdXL5-LB0bSxgvNwGCH4WY"])
header(s, "ASESMEN FORUM ANAK · FISHBONE 2/3", "PENYEBAB PER KATEGORI", "9/11")
table(s, 108, 196, [300, 760, 644], ["Kategori", "Penyebab", "Keterkaitan"], [
    ["Individu", "Motivasi anak rendah; waktu tersita kegiatan sekolah; manfaat forum tidak dirasakan", "Sebagian besar merupakan akibat dari kategori lain, terutama organisasi dan relasi kuasa"],
    ["Organisasi", "Kegiatan tidak rutin; program kurang sesuai minat anak; tidak ada kegiatan unggulan; tidak ada regenerasi", "Kegiatan yang tidak rutin merupakan gejala dari lemahnya tata kelola"],
    ["Relasi kuasa", "Anak tidak dilibatkan dalam keputusan; kegiatan bergantung pada orang dewasa; aspirasi anak tidak ditanggapi", "Ketergantungan pada orang dewasa diperberat oleh stagnasi Karang Taruna (M4)"],
    ["Norma sosial", "Anak dipandang sebagai objek kegiatan; prestasi akademik lebih diutamakan", "Mendasari relasi kuasa yang tidak memberi anak peran"],
    ["Struktur peluang", "Ruang kumpul anak minim; kegiatan terpusat di wilayah tertentu; akses antardusun sulit", "Bagian dari masalah jangkauan lintas dusun (M2)"],
    ["Tata kelola", "SK tanpa pembinaan; tidak ada data dan evaluasi; anggaran belum jelas", "Forum tercatat secara formal, termasuk dalam status Desa Ramah Anak, tetapi tidak dikelola secara berkelanjutan"]],
    25, lh=1.3, bold_cols=(0,))
foot(s, "Kategori Individu, Organisasi, dan Relasi kuasa merupakan faktor tingkat mikro dan meso; Norma sosial, Struktur peluang, dan Tata kelola merupakan faktor kontekstual (Pambudi, 2026).")
SLIDES["24"] = s

# ---------------------------------------------------------------- 25 Penjelasan deskriptif
s = Slide("PBQm6Z0qyrCv9wtk", ["PBQm6Z0qyrCv9wtk-LB49sXGtLbGPLB5v"])
header(s, "ASESMEN FORUM ANAK · FISHBONE 3/3", "PENJELASAN DESKRIPTIF", "10/11")
y = para(s, 108, 190, 1704, "Penyebab yang tampak pada tingkat individu, seperti motivasi rendah dan manfaat yang tidak terasa, lebih tepat dibaca sebagai gejala. Penelusurannya mengarah ke tiga lapisan.", 24) + 22
layers = [("Tata kelola", "Kegiatan tidak rutin karena forum berhenti pada SK. Setelah pembentukan, tidak ada pembinaan, anggaran yang jelas, data anggota, maupun evaluasi. Pemberitaan mencatat Forum Anak Desa dan status Desa Ramah Anak sebagai capaian desa, sedangkan temuan lapangan menunjukkan bahwa forum belum berfungsi."),
          ("Relasi kuasa dan norma sosial", "Program kurang sesuai minat dan manfaatnya tidak terasa karena anak tidak dilibatkan dalam menentukan kegiatan, dan aspirasinya tidak ditanggapi. Pola ini berakar pada norma yang memandang anak sebagai objek kegiatan dan lebih mengutamakan prestasi akademik."),
          ("Lingkungan pendukung", "Tidak ada pihak yang mengisi kekosongan tersebut. Karang Taruna sebagai organisasi kepemudaan juga stagnan (M4), sedangkan kegiatan desa terpusat dan akses antardusun sulit (M2). Pak Eki juga menyebut bahwa akhir pekan sudah dipenuhi agenda RT/RW dan kegiatan gabungan tingkat desa sulit mengumpulkan semua wilayah. Akibatnya, forum sulit menjangkau anak di dusun lain.")]
for n, (t, d) in enumerate(layers, 1):
    s.S(108, y, 60, 60, YELLOW, 30)
    s.T(108, y + 13, 60, str(n), 30, True, NAVY, "center", 1.0)
    s.T(190, y, 1622, t, 26, True, NAVY, lh=1.15)
    y = para(s, 190, y + 36, 1622, d, 22, BODY, 1.4) + 24
box(s, 108, y + 4, 1704, "Akar masalah utama: Forum Anak berdiri secara formal tanpa sistem pembinaan dan pengelolaan yang berkelanjutan, dan tanpa ruang yang memberi anak peran nyata dalam menentukan kegiatan serta keputusan.", 25, NAVY, WHITE, pad=24)
foot(s, SRC_JP)
SLIDES["25"] = s

# ---------------------------------------------------------------- 26 Potensi & kesimpulan
s = Slide("PBJjLV3pWXNSycw6", ["PBJjLV3pWXNSycw6-LBXtmZsbKbmhJJ9K"])
header(s, "ASESMEN FORUM ANAK", "POTENSI & KESIMPULAN", "11/11")
pot = ["Dukungan pemerintah desa dan status Desa Ramah Anak, yang memberi dasar formal untuk menghidupkan kembali forum.",
       "SDN Kejapanan V sebagai pendamping dan jalur menjangkau anak.",
       "Forum Anak dan Lingkungan yang memiliki perwakilan di setiap dusun, sehingga dapat menjadi jalur untuk mengatasi kegiatan yang terpusat.",
       "Perpustakaan desa sebagai tempat kegiatan yang sudah tersedia.",
       "Tokoh agama dan tokoh pemuda.",
       "Ragam potensi UMKM (batik, keset, Kampung Pia) sebagai materi kegiatan Forum Anak.",
       "Karang Taruna sebagai mitra jangka panjang apabila organisasi ini ikut dibenahi."]
s.T(108, 196, 820, "Potensi pendukung penyelesaian masalah", 27, True, NAVY, lh=1.15)
para(s, 108, 246, 820, "\n".join("•  " + p for p in pot), 24, BODY, 1.5)
s.T(992, 196, 820, "Kesimpulan hasil asesmen", 27, True, NAVY, lh=1.15)
y = box(s, 992, 246, 820, "MAP menghasilkan lima masalah. APKL menyaring dan mengurutkan kelima masalah, dengan M1 memperoleh skor tertinggi. USG terhadap kelima masalah menempatkan M1, rendahnya keaktifan Forum Anak, di peringkat pertama sehingga M1 menjadi isu kunci. Fishbone menunjukkan bahwa akar masalahnya bukan kurangnya minat anak, melainkan forum yang berdiri secara formal tanpa sistem pembinaan dan tanpa ruang partisipasi bermakna bagi anak. Rencana intervensi perlu menyasar tata kelola forum dan peran anak dalam pengambilan keputusan, bukan sekadar menambah kegiatan.", 22, NAVY, WHITE, pad=24) + 20
box(s, 992, y, 820, "Referensi\nJatimsatunews. (2025, 15 September). Kejapanan-Gempol jadi desa ke-20 dinilai Lomba Kampung Pancasila: Harmoni warga, UMKM unggulan, hingga nol stunting. https://jatimsatunews.com/2025/09/kejapanan-gempol-desa-ke-20-dinilai.html\nPambudi, K. S. (2026). Asesmen dan analisis urgensi masalah [PowerPoint slides].", 15, SOFT, BODY, bar=NAVY, lh=1.4)
foot(s, "Disiapkan oleh Kelompok 1, Universitas Negeri Malang.")
SLIDES["26"] = s
