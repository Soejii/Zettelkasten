"""Generate Canva edit-design operations that rebuild slides as native, editable elements.

Usage:
  python3 native_build.py add <slide>              -> JSON ops: delete old elements, add shapes + text
  python3 native_build.py fmt <slide> <id,id,...>  -> JSON ops: format the new text boxes
The ids for `fmt` are the new text element ids, in the order the text boxes were added.
"""
import json
import sys

NAVY, INK, MUTED, YELLOW = "#254671", "#1d2f47", "#5d6f85", "#ffde59"
BODY, LINE, SOFT, WHITE = "#2b3d53", "#e3e8ee", "#f5f7fa", "#ffffff"
PALE = "#dce8f5"

SLIDES = {}


class Slide:
    def __init__(self, page_id, delete=()):
        self.page_id = page_id
        self.delete = list(delete)
        self.ops = []
        self.shapes = []
        self.text_ops = []
        self.texts = []
        self.extra = []  # ops on existing elements (resize, position, format)

    def S(self, x, y, w, h, color, r=0, stroke=None, sw=0):
        op = {"type": "insert_shape", "page_id": self.page_id, "top": y, "left": x, "width": w, "height": h,
              "path": f"M0 0H{w}V{h}H0Z", "view_box_width": w, "view_box_height": h, "color": color}
        if r:
            op["corner_rounding"] = r
        if stroke:
            op["stroke_color"] = stroke
            op["stroke_weight"] = sw or 2
        self.ops.append(op)
        self.shapes.append(op)

    def T(self, x, y, w, text, size, bold=False, color=BODY, align="start", lh=1.3, rot=0):
        op = {"type": "add_text", "page_id": self.page_id, "text": text, "top": y, "left": x, "width": w}
        if rot:
            op["rotation"] = rot
        self.ops.append(op)
        self.text_ops.append(op)
        self.texts.append({"font_size": int(round(size)), "font_weight": "bold" if bold else "normal",
                           "color": color, "text_align": align, "line_height": lh})

    def add_ops(self):
        return [{"type": "delete_element", "locator_id": d} for d in self.delete] + self.extra + self.ops

    def texts_ops(self):
        return [{"type": "delete_element", "locator_id": d} for d in self.delete] + self.extra + self.text_ops

    def shape_ops(self, ids):
        return self.shapes + [{"type": "layer_element", "locator_id": f"{self.page_id}-{i}", "position": "front"} for i in ids]

    def fmt_ops(self, ids):
        assert len(ids) == len(self.texts), f"expected {len(self.texts)} ids, got {len(ids)}"
        return [{"type": "format_text", "locator_id": f"{self.page_id}-{i}", "formatting": f}
                for i, f in zip(ids, self.texts)]


# ---------------------------------------------------------------- slide 13: Dinamika Kekuasaan
s = Slide("PBrtk6hkyZZQ1vgv", ["PBrtk6hkyZZQ1vgv-LBSFKJdBnKhpRMmS"])
s.T(108, 58, 1700, "DINAMIKA KEKUASAAN", 92, True, NAVY, lh=1.0)
s.T(112, 165, 1300, "Kuat di tiap wilayah, sulit bersatu sebagai satu desa", 26, False, MUTED)
# tier 1
s.S(108, 222, 790, 178, NAVY, 18)
s.T(130, 236, 400, "TINGKAT DESA", 20, True, YELLOW)
s.S(130, 270, 316, 66, WHITE, 12)
s.S(560, 270, 316, 66, WHITE, 12)
s.S(458, 288, 92, 30, YELLOW, 15)
s.T(144, 276, 296, "Pak Kades Randi Saputra", 19, True, INK, lh=1.15)
s.T(144, 304, 296, "Kepala desa, relasi eksternal luas", 14, False, MUTED, lh=1.15)
s.T(458, 293, 92, "SETARA", 14, True, NAVY, "center", 1.1)
s.T(574, 276, 296, "Pak Eki", 19, True, INK, lh=1.15)
s.T(574, 304, 296, "Ketua Pokdarwis & penasihat kades", 14, False, MUTED, lh=1.15)
s.T(130, 344, 750, "Didampingi BPD (9 kursi) dan perangkat desa. Belum ada tokoh lain yang cukup kuat menjadi pesaing serius bagi keduanya.", 16, False, PALE, lh=1.35)
s.T(488, 402, 30, "▼", 20, True, NAVY, "center", 1.0)
# tier 2
s.S(108, 428, 790, 136, "#e8eef6", 18)
s.T(130, 442, 400, "TINGKAT DUSUN", 20, True, NAVY)
for i in range(12):
    s.S(130 + i * 62, 476, 54, 28, WHITE, 8, "#9fb4cc", 2)
s.T(130, 514, 750, "Tiap dusun punya kasun dan tokohnya sendiri. Kekuatannya setara; tidak ada satu dusun yang menguasai dusun lain.", 17, False, BODY, lh=1.35)
s.T(488, 568, 30, "▼", 20, True, NAVY, "center", 1.0)
# tier 3
s.S(108, 594, 790, 118, "#f2f5f8", 18)
s.T(130, 608, 400, "TINGKAT RW / RT", 20, True, NAVY)
s.T(130, 642, 750, "27 RW dan 152 RT, masing-masing punya kepentingan sendiri. Tiap RT/RW mampu menjalankan kegiatannya sendiri.", 17, False, BODY, lh=1.35)
# vibe cards
vibe = [("Demokratis", "Pemilihan RW memakai kampanye; warga berani mencalonkan diri."),
        ("Ego wilayah", "Warga lebih peduli lingkungannya sendiri daripada desa secara utuh."),
        ("Jadwal penuh", "Akhir pekan sudah terisi agenda RT/RW masing-masing."),
        ("Sulit disatukan", "Acara gabungan tingkat desa sulit mengumpulkan semua wilayah.")]
for k, (h, b) in enumerate(vibe):
    x, y = 108 + (k % 2) * 406, 732 + (k // 2) * 104
    s.S(x, y, 384, 92, WHITE, 14, LINE, 2)
    s.S(x + 14, y + 16, 10, 60, YELLOW, 5)
    s.T(x + 36, y + 12, 336, h, 17, True, INK, lh=1.2)
    s.T(x + 36, y + 38, 336, b, 15, False, BODY, lh=1.3)
# who's who
s.T(950, 222, 862, "Siapa saja di tiap wilayah?", 30, True, NAVY, lh=1.1)
s.T(950, 262, 862, "Tokoh yang disebut Pak Eki. Pengaruh mereka kuat, tetapi terbatas pada wilayahnya.", 15, False, MUTED)
tiles = [("Warurejo", "Pak Isyanto, kasun\nWahyu, tokoh pemuda\nPelaku usaha Kampung Pia"),
         ("Tabeyan", "Ustaz Ansori & pondok pesantren\nPak Nanang, Pak Anang, Pak Yuda\nArdiyan, perangkat desa"),
         ("Meli'an", "Pak Putut, orang dekat bupati, terkait Koperasi Desa Merah Putih\nPak Anam"),
         ("Penanggungan", "Pak Toni, aktif bersuara di rapat desa\nLokasi kantor desa"),
         ("Kejapanan", "Purnomo, terkait pasar desa & TKD\nMas Ragil, usaha mi lidi & bimbel"),
         ("Bandulan", "Abah Anas\nKetua RW 6 & RW 7 (Bandulan Lor dan Kidul)"),
         ("Arjosari", "Haji Suar dan Makrama\nKasun, RW, dan RT jadi penggerak utama"),
         ("Besuki", "Pak Misdi, Pak Samsoni, Pak Faisal Gufron\nWarga urban, cenderung menghindari konflik"),
         ("Tawangsari", "Pak Habib, tokoh masyarakat\nHabibi, wartawan"),
         ("Pandean", "Pak Yono, pemilik kafe\nSafii"),
         ("Pabean & Ngasem", "Berbagi satu kursi BPD; rincian tokoh belum diperoleh"),
         ("Balun", "Wilayah kecil, sekitar 1.000 warga; rincian tokoh belum diperoleh")]
tw, th = 206, 176
for k, (h, b) in enumerate(tiles):
    x, y = 950 + (k % 4) * (tw + 12), 292 + (k // 4) * (th + 12)
    dim = k >= 10
    s.S(x, y, tw, th, WHITE if dim else SOFT, 14, LINE, 2)
    s.T(x + 12, y + 10, tw - 24, h, 18, True, NAVY, lh=1.15)
    s.T(x + 12, y + 40, tw - 24, b, 13.5, False, "#7a8899" if dim else BODY, lh=1.3)
s.S(950, 858, 862, 76, "#fff8dc", 14)
s.T(966, 866, 830, "Tokoh lain: Wawan (anggota BPD, adik ipar sekdes) · Pak Muzaki (mantan Ketua DPRD) · Pak Luki (mantan ketua RW, ingin mencalonkan diri, tetapi jaringannya belum cukup kuat untuk menyaingi Pak Kades)", 14.5, False, BODY, lh=1.35)
# bar
s.S(108, 952, 1704, 76, NAVY, 16)
s.S(134, 971, 118, 38, YELLOW, 10)
s.T(134, 978, 118, "INTINYA", 20, True, NAVY, "center", 1.1)
s.T(274, 974, 1520, "Tantangan desa ini bukan elite tandingan, melainkan menyatukan dusun, RW, dan RT yang sama kuat dan punya kepentingan masing-masing.", 19, False, WHITE, lh=1.3)
s.T(108, 1040, 1700, "Sumber: wawancara Pak Eki (Ketua Pokdarwis Desa Kejapanan); jumlah RW/RT dari profil desa kelompok dan Jatimsatunews (2025). Nama dan peran tokoh belum diverifikasi silang.", 13, False, "#7a8899")
SLIDES["13"] = s


import os as _os
for _spec in sorted(f for f in _os.listdir(_os.path.dirname(_os.path.abspath(__file__))) if f.startswith("specs_") and f.endswith(".py")):
    exec(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), _spec)).read())


if __name__ == "__main__":
    mode, key = sys.argv[1], sys.argv[2]
    sl = SLIDES[key]
    if mode == "add":
        print(json.dumps(sl.add_ops(), ensure_ascii=False))
    elif mode == "fmt":
        print(json.dumps(sl.fmt_ops(sys.argv[3].split(",")), ensure_ascii=False))
    elif mode == "texts":
        print(json.dumps(sl.texts_ops(), ensure_ascii=False))
    elif mode == "shapes":
        print(json.dumps(sl.shape_ops(sys.argv[3].split(",")), ensure_ascii=False))
    elif mode == "count":
        print(len(sl.ops), "ops,", len(sl.texts), "texts")
