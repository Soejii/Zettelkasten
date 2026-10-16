"""Build the bottom-up fishbone for Forum Anak Desa Kejapanan as SVG."""
import sys
from xml.sax.saxutils import escape

W, H = 1720, 860
SPINE_Y = 430
FONT = "Inter, Arial, sans-serif"
GREY = "#6b7280"
INK = "#1f2937"

# (label, root?, top?, label_cx, causes)
BONES = [
    ("Dibentuk untuk status", True, True, 420, [
        "Dicatat sebagai capaian Desa Ramah Anak",
        "Berhenti pada penerbitan SK",
    ]),
    ("Tanpa pembinaan dan pengelolaan", True, True, 1000, [
        "Pendampingan belum terencana",
        "Anggaran belum jelas",
        "Tanpa data anggota dan evaluasi",
        "Regenerasi pengurus tidak berjalan",
    ]),
    ("Anak tidak memegang kendali", True, False, 480, [
        "Anak tidak dilibatkan menentukan kegiatan",
        "Bergantung pada inisiatif orang dewasa",
        "Aspirasi anak tidak ditanggapi",
        "Anak dipandang sebagai objek kegiatan",
    ]),
    ("Lingkungan desa belum menopang", False, False, 1060, [
        "Kegiatan desa terpusat di wilayah tertentu (M2)",
        "Akses antardusun dinilai cukup jauh",
        "Ruang kumpul anak minim",
        "Karang Taruna stagnan, forum tanpa mitra (M4)",
    ]),
]

out = []
a = out.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
a(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
a(f'<text x="40" y="40" font-family="{FONT}" font-size="22" font-weight="700" fill="{INK}">'
  'Penyebab Forum Anak Desa Kejapanan belum pernah menjalankan program</text>')

# spine and head
spine_end = 1420
a(f'<line x1="60" y1="{SPINE_Y}" x2="{spine_end}" y2="{SPINE_Y}" stroke="{GREY}" stroke-width="3"/>')
a(f'<path d="M{spine_end-10} {SPINE_Y-7} L{spine_end+2} {SPINE_Y} L{spine_end-10} {SPINE_Y+7} Z" fill="{GREY}"/>')
a(f'<rect x="{spine_end+8}" y="{SPINE_Y-52}" width="270" height="104" rx="12" fill="#f3f4f6" stroke="{GREY}" stroke-width="2"/>')
for i, line in enumerate(["Forum Anak belum", "pernah menjalankan", "program"]):
    a(f'<text x="{spine_end+143}" y="{SPINE_Y-16+i*26}" text-anchor="middle" font-family="{FONT}" '
      f'font-size="19" font-weight="700" fill="{INK}">{escape(line)}</text>')

for label, root, top, cx, causes in BONES:
    y0 = 112 if top else H - 104
    x1, y1 = cx + 160, SPINE_Y
    stroke = "#c2410c" if root else "#3b6fc4"
    fill = "#fdecdf" if root else "#e8f0fb"
    bw = 330
    by = y0 - 44 if top else y0 + 4
    a(f'<rect x="{cx-bw/2}" y="{by}" width="{bw}" height="40" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="{2.5 if root else 2}"/>')
    a(f'<text x="{cx}" y="{by+26}" text-anchor="middle" font-family="{FONT}" font-size="17" font-weight="700" fill="{INK}">{escape(label)}</text>')
    a(f'<line x1="{cx}" y1="{y0 if top else y0+4}" x2="{x1}" y2="{y1}" stroke="{stroke}" stroke-width="2.4"/>')
    n = len(causes)
    for k, cause in enumerate(causes):
        t = 0.16 + k * (0.72 / max(n - 1, 1))
        bx = cx + (x1 - cx) * t
        byy = (y0 if top else y0 + 4) + (y1 - (y0 if top else y0 + 4)) * t
        a(f'<line x1="{bx-14}" y1="{byy}" x2="{bx}" y2="{byy}" stroke="{stroke}" stroke-width="1.6"/>')
        a(f'<text x="{bx-20}" y="{byy+5}" text-anchor="end" font-family="{FONT}" font-size="15" fill="{INK}">{escape(cause)}</text>')

# legend
ly = H - 26
a(f'<rect x="40" y="{ly-14}" width="22" height="16" rx="3" fill="#fdecdf" stroke="#c2410c" stroke-width="2"/>')
a(f'<text x="70" y="{ly}" font-family="{FONT}" font-size="15" fill="{INK}">Kategori akar masalah</text>')
a(f'<rect x="280" y="{ly-14}" width="22" height="16" rx="3" fill="#e8f0fb" stroke="#3b6fc4" stroke-width="2"/>')
a(f'<text x="310" y="{ly}" font-family="{FONT}" font-size="15" fill="{INK}">Kategori penyerta</text>')
a(f'<text x="480" y="{ly}" font-family="{FONT}" font-size="15" fill="{INK}">(M2), (M4) : masalah lain hasil MAP yang berhubungan timbal balik dengan Forum Anak</text>')
a('</svg>')

with open(sys.argv[1], "w", encoding="utf-8") as f:
    f.write("\n".join(out))
