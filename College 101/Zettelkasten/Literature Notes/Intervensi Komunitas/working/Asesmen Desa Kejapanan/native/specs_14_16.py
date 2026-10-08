# Slide specs 14-16 (grid, resources, jelajah). Executed inside native_build.py's namespace.

# ---------------------------------------------------------------- slide 14: Power-Interest Grid
s = Slide("PBTg9bwgMDxSbGP0", ["PBTg9bwgMDxSbGP0-LBYQPtjXXDL3p12j"])
cell_bg = [["#fbf3d6", "#f6eec8", "#d9ebd3"], ["#f4f5f2", "#eef1ee", "#e0ecf2"], ["#f1f3f5", "#eaeff4", "#dbe8f6"]]
s.S(296, 213, 744, 634, NAVY, 8)
for r in range(3):
    for c in range(3):
        s.S(300 + c * 246, 217 + r * 210, 242, 206, cell_bg[r][c], 3)
s.T(57, 512, 200, "POWER", 30, True, NAVY, "center", 1.0, rot=-90)
for r, lab in enumerate(["Tinggi", "Menengah", "Rendah"]):
    s.T(170, 307 + r * 210, 116, lab, 17, True, MUTED, "end", 1.2)
for c, lab in enumerate(["Rendah", "Menengah", "Tinggi"]):
    s.T(300 + c * 246, 856, 242, lab, 17, True, MUTED, "center", 1.2)
s.T(300, 884, 740, "INTEREST", 30, True, NAVY, "center", 1.0)
for (r, c) in [(0, 0), (1, 0), (2, 1)]:
    s.T(310 + c * 246, 310 + r * 210, 222, "Tidak teridentifikasi", 15, False, "#9fb0c4", "center", 1.2)
chips = {(0, 1): [("3", "Aktor eksternal")], (0, 2): [("1", "Pak Kades"), ("2", "Pak Eki")],
         (1, 1): [("6", "Tokoh masyarakat"), ("7", "Pesantren Tabeyan")], (1, 2): [("4", "BPD"), ("5", "Kasun, RW, RT")],
         (2, 0): [("10", "Karang Taruna"), ("11", "Forum Anak")], (2, 2): [("8", "UMKM"), ("9", "Perempuan")]}
for (r, c), items in chips.items():
    cx, cy = 300 + c * 246, 217 + r * 210
    ys = [cy + 80] if len(items) == 1 else [cy + 46, cy + 112]
    for (n, lab), y in zip(items, ys):
        key = n in ("1", "2")
        s.S(cx + 10, y, 222, 48, YELLOW if key else WHITE, 24, None if key else "#d5dde7", 2)
        s.T(cx + 26, y + 13, 196, f"{n}   {lab}", 17, True, INK, lh=1.15)
s.T(1080, 211, 760, "Mengapa di posisi ini?", 30, True, NAVY, lh=1.1)
s.T(1080, 250, 760, "Interest = kepentingan untuk terlibat dan mendukung pembangunan desa atau program intervensi.", 15, False, MUTED, lh=1.25)
rows = [("1", "Pak Kades Randi Saputra", "P tinggi · I tinggi", "Kewenangan formal tertinggi, relasi eksternal kuat, dan belum ada pesaing serius."),
        ("2", "Pak Eki, Ketua Pokdarwis & penasihat kades", "P tinggi · I tinggi", "Pengaruhnya setara Pak Kades; selalu bersuara di rapat dan aktif di kegiatan desa."),
        ("3", "Bupati, DPR/DPRD, kejaksaan, BNN, polisi", "P tinggi · I menengah", "Bisa membuka dana dan dukungan, tetapi masuk lewat relasi Pak Kades, bukan urusan harian."),
        ("4", "BPD (9 kursi)", "P menengah · I tinggi", "Ikut mengesahkan aturan dan anggaran desa, tetapi tiap kursi mewakili wilayahnya sendiri."),
        ("5", "Kasun, ketua RW, dan ketua RT", "P menengah · I tinggi", "Paling kuat menggerakkan warga, tetapi hanya di wilayahnya; kepentingannya tinggi untuk wilayah sendiri."),
        ("6", "Tokoh masyarakat, agama, dan pemuda", "P menengah · I menengah", "Dihormati di lingkungannya, tetapi jangkauannya terpecah per kelompok dan wilayah."),
        ("7", "Pondok pesantren Tabeyan", "P menengah · I menengah", "Punya lahan, santri, dan jaringan; kasus TPS menunjukkan warga tetap mampu menekannya."),
        ("8", "UMKM dan kelompok usaha", "P rendah · I tinggi", "Berkepentingan langsung pada program ekonomi, tetapi tidak punya kewenangan formal."),
        ("9", "Perwakilan perempuan", "P rendah · I tinggi", "Saluran partisipasi warga, tetapi tanpa kewenangan formal yang besar."),
        ("10", "Karang Taruna", "P rendah · I rendah", "Ada secara kelembagaan, tetapi stagnan; program kerjanya tidak berjalan."),
        ("11", "Forum Anak & Lingkungan", "P rendah · I rendah", "Terbentuk dengan perwakilan tiap dusun, tetapi belum aktif berkegiatan.")]
for k, (n, name, tag, why) in enumerate(rows):
    y = 290 + k * 57
    key = n in ("1", "2")
    s.S(1080, y - 5, 760, 2, LINE)
    s.S(1080, y + 6, 34, 34, YELLOW if key else NAVY, 17)
    s.T(1080, y + 14, 34, n, 15, True, NAVY if key else WHITE, "center", 1.0)
    s.T(1126, y, 500, name, 16.5, True, INK, lh=1.2)
    s.T(1620, y + 2, 220, tag, 13, True, NAVY, "end", 1.2)
    s.T(1126, y + 24, 714, why, 14, False, BODY, lh=1.25)
s.S(108, 935, 1732, 92, NAVY, 16)
s.S(138, 961, 196, 40, YELLOW, 10)
s.T(138, 970, 196, "TEMUAN KUNCI", 20, True, NAVY, "center", 1.1)
s.T(360, 951, 1460, "Ada dua pusat pengaruh yang setara, Pak Kades dan Pak Eki. Di bawahnya, tiap dusun, RW, dan RT setara dan punya kepentingan sendiri. Program perlu restu keduanya, lalu dijalankan per wilayah.", 18.5, False, WHITE, lh=1.35)
s.T(108, 1043, 1720, "Sumber: wawancara Pak Eki (Ketua Pokdarwis) dan observasi kelompok. Posisi aktor selain Pak Kades dan Pak Eki merupakan penilaian kelompok berdasarkan wawancara.", 13, False, "#7a8899")
SLIDES["14"] = s

# ---------------------------------------------------------------- slide 15: Sumber Daya Desa
s = Slide("PB1vggJH45rCNktR", ["PB1vggJH45rCNktR-LB77BkTb12sf2MHl", "PB1vggJH45rCNktR-LBTYBflyDlkRzpM1", "PB1vggJH45rCNktR-LB21Xy8pgnt40MR4"])
s.extra = [{"type": "resize_element", "locator_id": "PB1vggJH45rCNktR-LBw8fz5Df9SGBs33", "width": 2124, "height": 254},
           {"type": "resize_element", "locator_id": "PB1vggJH45rCNktR-LBsFy6Pgh7ZsztX1", "width": 1500},
           {"type": "position_element", "locator_id": "PB1vggJH45rCNktR-LBsFy6Pgh7ZsztX1", "top": 34, "left": 108}]
s.T(112, 146, 1400, "Apa yang dimiliki Kejapanan, dan bagaimana itu bisa dipakai untuk program", 24, False, PALE)
cards = [("#4f7da6", "#e6eef7", "SDM & ORGANISASI", "Struktur penggerak desa",
          ["Pemdes, perangkat desa, dan BPD (9 kursi)", "Kasun tiap dusun, 27 RW, dan 152 RT", "Pokdarwis dan Koperasi Desa Merah Putih", "Koperasi Wasuka, wadah ±32 pengusaha pia"],
          "jalur resmi izin, koordinasi, dan penyebaran informasi sampai tingkat RT."),
         ("#d4a72c", "#fdf4d8", "JEJARING EKSTERNAL", "Akses dukungan dan pendanaan",
          ["Relasi Pak Kades dengan bupati dan wakil bupati", "DPR/DPRD, kejaksaan, BNN, kepolisian", "Pemkab, BRI, kampus pernah membantu UMKM pia", "Catatan: dana dari pabrik disebut sulit diperoleh"],
          "sumber dana, narasumber, dan legitimasi untuk kegiatan skala desa."),
         ("#55946a", "#e5f2e8", "EKONOMI & UMKM", "Usaha berbasis kampung",
          ["Industri pengolahan jadi mata pencaharian utama", "Kampung Pia, sentra bebek & telur asin, keset, batik, ecobrick", "Pemilik NIB UMKM terbanyak di Kab. Pasuruan", "Rincian per dusun di slide berikutnya"],
          "titik masuk intervensi ekonomi, seperti pelatihan, pemasaran, dan penguatan kelompok usaha."),
         ("#7c6aa8", "#efecf7", "FASILITAS PUBLIK", "Ruang layanan dan kegiatan warga",
          ["Sekolah dari PAUD hingga SMA/SMK", "Posyandu, layanan kesehatan gratis, perpustakaan desa", "14 masjid, 47 musala, dan gereja", "Pasar desa, lapangan sepak bola, gedung sentra pia"],
          "tempat kegiatan yang sudah tersedia, tanpa perlu membangun fasilitas baru."),
         ("#c46f55", "#f9ebe5", "ASET & LOKASI", "Modal fisik dan posisi strategis",
          ["Tanah kas desa (TKD)", "Kantor desa di Dusun Penanggungan", "Di jalur Jl. Raya Malang-Surabaya, dekat tol Gempol-Pandaan", "Sekitar 1 km dari pusat Kecamatan Gempol"],
          "mudah dijangkau warga, pembeli, dan mitra dari luar desa."),
         ("#3c8e9f", "#e2f2f5", "PARTISIPASI WARGA", "Kesediaan warga untuk terlibat",
          ["Kesehatan gratis selalu ramai, bisa sampai siang", "Forum Anak & Lingkungan ada di tiap dusun, tetapi belum aktif", "Festival Kebangsaan Kampung Pancasila tiap Agustus", "Program lingkungan warga: eco enzym, biopori, kompos"],
          "warga mau datang bila manfaatnya jelas; forum yang belum aktif bisa dihidupkan lewat program.")]
for k, (acc, tint, title, sub, bullets, use) in enumerate(cards):
    x, y = 108 + (k % 3) * 578, 230 + (k // 3) * 402
    s.S(x, y, 548, 380, WHITE, 22, "#dfe5ec", 2)
    s.S(x, y, 548, 12, acc, 6)
    s.T(x + 26, y + 30, 500, title, 28, True, INK, lh=1.05)
    s.T(x + 26, y + 66, 500, sub, 15, False, MUTED, lh=1.2)
    s.T(x + 26, y + 100, 500, "\n".join("•  " + b for b in bullets), 17.5, False, BODY, lh=1.45)
    s.S(x + 16, y + 284, 516, 80, tint, 12)
    s.T(x + 30, y + 296, 488, "Untuk program: " + use, 15.5, False, INK, lh=1.3)
s.T(108, 1046, 1700, "Sumber: wawancara Pak Eki (Ketua Pokdarwis); profil desa yang dihimpun kelompok; Jatimsatunews (2025); Mustofah & Sukmana (2025).", 13, False, "#7a8899")
SLIDES["15"] = s

# ---------------------------------------------------------------- slide 16: Jelajah Kampung
s = Slide("PBfgPP5wdbNJwhfh", ["PBfgPP5wdbNJwhfh-LBwdNJK1LNqXvPDV"])
s.T(108, 58, 1700, "JELAJAH KAMPUNG", 92, True, NAVY, lh=1.0)
s.T(112, 165, 1400, "Kalau berkeliling Kejapanan, inilah yang ditemui di tiap dusun", 26, False, MUTED)
s.S(108, 222, 900, 690, NAVY, 24)
s.S(930, 222, 78, 78, YELLOW, 24)
s.T(138, 246, 600, "DUSUN WARUREJO", 19, True, YELLOW, lh=1.1)
s.T(138, 272, 760, "Kampung Pia", 52, True, WHITE, lh=1.0)
s.T(138, 340, 800, 'Hampir tiap rumah membuat pia. Plang "Kampung Pia" menyambut di jalan masuk dusun, tepat di sisi tol Gempol-Pandaan. Usaha ini dirintis Ibu Yana, pendatang yang mengajari tetangganya membuat pia tanpa takut tersaingi. Kini ibu rumah tangga yang dulu menganggur ikut bekerja, dari mencetak adonan sampai melipat kardus.', 18, False, PALE, lh=1.45)
stats = [("155", "home industry pia di Desa Kejapanan"), ("69%", "pekerjanya perempuan; 71% warga desa sendiri"),
         ("191 ton", "pia pada 2024, dari 30 usaha anggota koperasi"), ("Rp15 rb", "per kotak; varian ayam jadi best seller Pia Mami")]
for k, (n, t) in enumerate(stats):
    x = 138 + k * 212
    s.S(x, 498, 200, 122, "#3a5a83", 14)
    s.T(x + 14, 508, 176, n, 34, True, YELLOW, lh=1.0)
    s.T(x + 14, 550, 176, t, 14, False, PALE, lh=1.3)
tl = [("2009", "Usaha pia mulai dirintis"), ("2011", "Paguyuban Kembang Waru; hibah Pemkab Rp70,9 juta"),
      ("2015", "Berdiri Koperasi Waru Sukses Berkarya (Wasuka)"), ("2019", "Gedung sentra oleh-oleh pia senilai Rp1,6 miliar"),
      ("Kini", "±32 anggota aktif; pia dijual sampai luar Jawa Timur")]
s.S(148, 648, 760, 3, "#bfa94f")
for k, (yr, d) in enumerate(tl):
    x = 138 + k * 168
    s.S(x, 639, 22, 22, YELLOW, 11)
    s.T(x, 668, 158, yr, 17, True, WHITE, lh=1.1)
    s.T(x, 692, 158, d, 14, False, "#c9d7e8", lh=1.3)
s.S(138, 790, 840, 104, WHITE, 14)
s.T(156, 802, 806, "Tantangannya: bantuan modal tidak rutin dan hanya untuk sebagian pengusaha, gedung sentra belum berfungsi optimal (suhu ruang, izin bangunan), dan pengusaha berusia di atas 40 tahun kesulitan promosi lewat media sosial.", 16, False, INK, lh=1.35)
mini = [("#c98a1c", "TAWANGSARI", "Bebek & telur asin", "Peternakan bebek/itik menjadi potensi utama. Desa ini punya sentra bebek dan telur asin yang sudah dipasarkan hingga ke luar daerah.", None),
        ("#55946a", "TABEYAN", "Keset & pedagang", "Banyak warganya berdagang, dan ada klaster UMKM keset. Di sini juga berdiri pondok pesantren yang berpengaruh di lingkungannya.", None),
        ("#7c6aa8", "BANDULAN", "Batik & ecobrick", "Rumah Batik Sumolewo dan kegiatan ecobrick dari sampah plastik.", None),
        ("#4f7da6", "KEJAPANAN", "Pasar & usaha warga", "Pasar desa dan tanah kas desa, peternakan ayam, usaha mi lidi, bimbingan belajar, dan kafe.", None)]
for k, (acc, pin, h, p, small) in enumerate(mini):
    x, y = 1036 + (k % 2) * 396, 222 + (k // 2) * 252
    s.S(x, y, 380, 236, "#fafbfc", 18, LINE, 2)
    s.S(x + 18, y + 20, 10, 10, acc, 5)
    s.T(x + 34, y + 15, 320, pin, 14, True, acc, lh=1.1)
    s.T(x + 18, y + 40, 344, h, 28, True, INK, lh=1.05)
    s.T(x + 18, y + 82, 344, p, 16.5, False, BODY, lh=1.4)
    if small:
        s.T(x + 18, y + 168, 344, small, 13.5, False, "#7a8899", lh=1.3)
s.S(1036, 728, 776, 104, "#fff8dc", 16)
s.T(1056, 742, 736, "Di sekelilingnya, pabrik. Industri pengolahan adalah mata pencaharian utama warga, dengan perusahaan seperti PT Japanan Plastik dan PT Bumifood Agro Industri. Namun menurut narasumber, pabrik sulit diajak mendanai kegiatan desa.", 16, False, BODY, lh=1.4)
badges = [("★", "Desa Ramah Anak", "ditetapkan Juli 2025"), ("0", "Zero stunting", "capaian kesehatan desa"),
          ("#1", "NIB UMKM terbanyak", "di Kabupaten Pasuruan"), ("✓", "Kampung Pancasila", "dinilai lomba kabupaten 2025")]
for k, (ic, t, sub) in enumerate(badges):
    x = 108 + k * 430
    s.S(x, 932, 416, 70, "#e8eef6", 14)
    s.S(x + 14, 947, 40, 40, YELLOW, 20)
    s.T(x + 14, 957, 40, ic, 16, True, NAVY, "center", 1.0)
    s.T(x + 68, 942, 336, t, 17, True, NAVY, lh=1.2)
    s.T(x + 68, 966, 336, sub, 15, False, INK, lh=1.2)
s.T(108, 1040, 1700, "Sumber: wawancara Pak Eki; Irawati (2020); Mustofah & Sukmana (2025); Pemerintah Kabupaten Pasuruan (t.t.); Jatimsatunews (2025); profil desa yang dihimpun kelompok.", 13, False, "#7a8899")
SLIDES["16"] = s
