Date: 2026-03-16
Time: 00:00
Status: #low
Tags:

# Setiaji et al. (2023) - Using Multilevel Modeling to Evaluate Science Literacy and Technology Course of Indonesian Non-Science Students

---

**No.**

**Year:** 2023

**Authors:** Bayu Setiaji, Purwoko Haryadi Santoso, Khafidh Nur Aziza, Heri Retnawati, Moh Khairudin

**Title:** Using Multilevel Modeling to Evaluate Science Literacy and Technology Course of the Indonesian Non-Science Students

---

### Variabel

**Variabel (Interes Utama):** Science literacy (performa mahasiswa pada mata kuliah literasi sains dan teknologi)

**Other Variable:** Atribut afektif (motivational beliefs), ujian tengah semester (midterm exam), latar belakang SMA (science/non-science), pendidikan ibu, gender, jalur masuk, pendanaan, beasiswa, tempat tinggal, pendidikan ayah, pendapatan orang tua, level departemen, level fakultas

---

### Research Question / Hypothesis

RQ1. Sejauh mana perbedaan rerata performa mahasiswa, ujian tengah semester, dan atribut afektif pada mata kuliah literasi sains bervariasi berdasarkan level departemen, level fakultas, dan variabel demografis?

RQ2. Sejauh mana level departemen dan level fakultas memvariasikan hubungan (dependence) antara performa mahasiswa pada mata kuliah literasi sains, atribut afektif, dan variabel demografis?

---

### Context

**Context:** Pendidikan Tinggi (Higher Education), evaluasi mata kuliah literasi sains dan teknologi (MKU 6217)

**Sub Context:** Science literacy education untuk mahasiswa non-science, kurikulum Merdeka Belajar, multilevel data analysis dalam konteks pendidikan

**Region:** Indonesia, Yogyakarta (Universitas Negeri Yogyakarta / UNY), tahun akademik 2022/2023

---

### Subjek

**Populasi dan Subjek:** Mahasiswa S1 non-science tahun pertama di UNY yang mengambil mata kuliah literasi sains dan teknologi. Berasal dari 4 departemen: Marketing (*n* = 38), Akuntansi (*n* = 39), Bahasa Jawa (*n* = 51), dan Pendidikan Tari (*n* = 50). Dua fakultas: Fakultas Ekonomi (Marketing, Akuntansi) dan Fakultas Bahasa dan Seni (Bahasa Jawa, Tari). Mayoritas perempuan (76%), latar belakang SMA non-science (67%), berasal dari Jawa Tengah (39%), status ekonomi menengah ke bawah.

**Sample Size:** *N* = 160 (dari 178 partisipan awal, 18 dihapus karena data tidak lengkap)

---

### Research Design

**Research Type** *(Quantitative / Qualitative / Mix / Literature Review)*: Quantitative

**Research Design** *(cross-sectional / longitudinal / prospective / retrospective)*: Cross-sectional

**Research Design** *(correlation / comparative / experiment / SEM)*: Comparative dan Correlational (menggunakan ANOVA untuk perbedaan rerata, lalu Multilevel Modeling untuk asosiasi antar variabel)

---

### Measurement

**Instrument, Validity, Reliability:**
- **SLA-D (Demonstrated Scientific Literacy Assessment):** 26 item pilihan ganda, diadaptasi dari Fives et al. (2014). Versi bahasa Indonesia divalidasi melalui content validity oleh 2 ahli dengan pengalaman 10+ tahun di bidang pendidikan literasi sains. Digunakan sebagai proxy performa mahasiswa.
- **SLA-MB (Motivational Beliefs):** 25 item skala Likert 5 poin, terdiri dari 3 konstruk: Value of Science/VOS, what can I Do in Science/DIS, dan what I Belief About Science/BAS (Fives et al., 2014). Reliabilitas: alpha_all = 0.781, alpha_VOS = 0.868, alpha_DIS = 0.786, alpha_BIS = 0.903. Validitas konstruk dikonfirmasi melalui Exploratory Factor Analysis (EFA) yang menghasilkan 3 komponen dengan eigenvalue > 1.
- **Midterm Exam:** 5 item open-ended, dinilai menggunakan rubrik yang dikembangkan oleh dosen pengampu. Face validity dilakukan.
- **Variabel demografis:** 10 variabel dari data registrar institusi (gender, jalur masuk, pendanaan, beasiswa, latar belakang SMA, tempat tinggal, pendidikan ayah/ibu, pendapatan ayah/ibu).

**AR diukur menggunakan nilai / Skala:** SLA-D dan Midterm dikonversi ke skala 100 poin (continuous/interval). SLA-MB menggunakan skala Likert 5 poin (categorical/ordinal). Variabel demografis berskala nominal.

---

### Data Analysis
*(statistic / thematic)*

Statistik:
- **ANOVA** => menguji perbedaan rerata SPerf, Aff, dan MidTerm antar kelas dari setiap departemen, fakultas, dan aspek demografis (RQ1). Hanya variabel dengan perbedaan signifikan (alpha < 0.05) yang dimasukkan ke model multilevel.
- **Intraclass Correlation (ICC)** => mengukur sejauh mana variabel kategorikal (demografis) berkorelasi dengan variabel dependen.
- **Multilevel Modeling** => two-level (student nested in department) dan three-level (student nested in department nested in faculty). Dibangun secara bertahap: null model (Eq. 1-2), model + MidTerm (Eq. 3-4), model + MidTerm + Aff (Eq. 5-6), model + MidTerm + Aff + HS + MEdu (Eq. 7-8). Estimasi menggunakan **REML** (Restricted Maximum Likelihood). Perbandingan model menggunakan **AIC** (Akaike Information Criterion); model terbaik = AIC terendah.
- Software: R, package `lme4` (fungsi `lmer`).

---

### Result

**RQ1 (Perbedaan rerata):**
- Terdapat perbedaan rerata signifikan (*p* < 0.05) pada SPerf dan MidTerm antar departemen dan fakultas. ICC menunjukkan korelasi yang plausible antara departemen/fakultas dengan performa mahasiswa.
- Tidak ada perbedaan rerata signifikan pada atribut afektif (Aff) antar departemen dan fakultas. Namun scatter plot menunjukkan korelasi antara SPerf dan Aff (*r* = 0.41) serta SPerf dan MidTerm (*r* = 0.35), sementara Aff dan MidTerm independen (*r* = 0.01).
- Dari 10 variabel demografis, hanya **high school background** dan **mother education** yang menunjukkan perbedaan signifikan (*p* < 0.05) pada atribut afektif. Variabel demografis lainnya (gender, jalur masuk, pendanaan, beasiswa, tempat tinggal, pendidikan ayah, pendapatan orang tua) tidak signifikan.

**RQ2 (Multilevel modeling):**
- **Two-level (best model = Model 5):** SPerf diprediksi oleh MidTerm (signifikan, *p* < 0.05) dan Aff (signifikan, *p* < 0.05). Intercept tidak signifikan (*p* > 0.05), menunjukkan bahwa dengan memasukkan atribut afektif, perbedaan antar departemen terkontrol. AIC terendah = 1560.00.
- **Three-level (best model = Model 6):** Konsisten dengan Model 5; MidTerm dan Aff signifikan memprediksi SPerf. Intercept tidak signifikan. AIC terendah = 1564.63.
- **Model 7 dan 8** (menambahkan HS dan MEdu): Koefisien high school background dan mother education **tidak signifikan** (*p* > 0.05) => variabel demografis ini tidak dapat disimpulkan sebagai prediktor performa literasi sains.
- Pola diminishing pada variance dan standard deviation dari intercept dan residual terlihat seiring penambahan prediktor, menunjukkan multilevel model lebih presisi dalam estimasi standard error.

---

### Theory Perspective

- **Multilevel Modeling** (Finch et al., 2016) => pendekatan analisis data hierarkis/nested yang memperhitungkan struktur klaster data (siswa nested dalam departemen nested dalam fakultas)
- **Scientific Literacy Assessment** (Fives et al., 2014) => kerangka pengukuran literasi sains mencakup dimensi demonstrated (kognitif) dan motivational beliefs (afektif: VOS, DIS, BAS)
- **Evaluasi pendidikan sains** (Hobson, 2003) => pentingnya evaluasi formatif selama implementasi instruksi literasi sains
- Referensi ke survei internasional **PISA** dan **TIMSS** sebagai konteks kebijakan pendidikan sains Indonesia

---

### Further Research

- Replikasi studi di universitas lain dalam sistem pendidikan Indonesia untuk meningkatkan generalizability
- Studi komparatif antara mahasiswa non-science dan science majors
- Penggunaan **random slope model** (selain random intercept) untuk menangkap variasi prediktor di level yang lebih tinggi
- Eksplorasi lebih lanjut mengenai dampak variabel demografis dengan sampel yang lebih besar dan lebih beragam
- Investigasi definisi dan pengukuran atribut afektif yang lebih robust (karena konstruk afektif bersifat laten dan beragam definisinya)

---

### My Note

Keunikan studi ini terletak pada penggunaan multilevel modeling untuk mengevaluasi mata kuliah literasi sains di konteks mahasiswa non-science Indonesia, sesuatu yang jarang dilakukan di literatur sebelumnya yang lebih banyak menggunakan analisis single-level. Temuan bahwa variabel demografis (termasuk gender) tidak signifikan memprediksi performa literasi sains cukup mengejutkan dan berlawanan dengan literatur PISA/TIMSS sebelumnya (Cheema, 2017; Ustun et al., 2022; You et al., 2021). Namun, keterbatasan utama terletak pada: (1) sampel hanya dari satu universitas (UNY), sehingga generalizability terbatas; (2) jumlah grup di level 2 dan 3 sangat kecil (4 departemen, 2 fakultas), yang dapat mempengaruhi estimasi parameter multilevel; (3) hanya menggunakan random intercept model tanpa random slope. Menarik bahwa atribut afektif berperan signifikan sebagai "pengontrol" perbedaan antar departemen/fakultas, yang menyiratkan bahwa memasukkan aspek afektif dalam asesmen dapat meningkatkan ekuitas penilaian.

# References

Setiaji, B., Santoso, P. H., Aziza, K. N., Retnawati, H., & Khairudin, M. (2023). Using multilevel modeling to evaluate science literacy and technology course of the Indonesian non-science students. *Manuscript*.