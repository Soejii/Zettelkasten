"""Render a slide spec to an approximate HTML preview (Open Sans stands in for Canva's default font).

Usage: python3 preview.py <slide> <out.html>
"""
import html
import sys

sys.argv, _args = sys.argv[:1], sys.argv[1:]
exec(open(__file__.replace("preview.py", "native_build.py")).read().split('if __name__ == "__main__":')[0])
key, out = _args
sl = SLIDES[key]
parts = ['<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap" rel="stylesheet">'
         '<style>body{margin:0;width:1920px;height:1080px;position:relative;overflow:hidden;background:#fff;font-family:"Open Sans",sans-serif}'
         'div{position:absolute;box-sizing:border-box;white-space:pre-wrap}</style></head><body>']
ti = 0
for op in sl.ops:
    if op["type"] == "insert_shape":
        st = f'left:{op["left"]}px;top:{op["top"]}px;width:{op["width"]}px;height:{op["height"]}px;background:{op["color"]};border-radius:{op.get("corner_rounding", 0)}px;'
        if op.get("stroke_color"):
            st += f'border:{op["stroke_weight"]}px solid {op["stroke_color"]};'
        parts.append(f'<div style="{st}"></div>')
for op in sl.ops:
    if op["type"] == "add_text":
        f = sl.texts[ti]; ti += 1
        rot = f'transform:rotate({op["rotation"]}deg);' if op.get("rotation") else ""
        st = (f'left:{op["left"]}px;top:{op["top"]}px;width:{op["width"]}px;font-size:{f["font_size"]}px;'
              f'font-weight:{700 if f["font_weight"] == "bold" else 400};color:{f["color"]};'
              f'text-align:{ {"start": "left", "end": "right"}.get(f["text_align"], f["text_align"]) };line-height:{f["line_height"]};{rot}')
        parts.append(f'<div style="{st}">{html.escape(op["text"])}</div>')
parts.append("</body></html>")
open(out, "w").write("".join(parts))
