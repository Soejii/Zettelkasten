"""Measure rendered text heights with headless Chromium (Open Sans stands in for Canva's default font).

measure([(text, width, font_size, bold, line_height), ...]) -> [height_px, ...]
Results are cached in measure_cache.json next to this file.
"""
import hashlib
import html
import json
import os
import re
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "measure_cache.json")
SAFETY = 0.94  # measure slightly narrower than the real box so Canva's wrapping never runs longer


def _key(t, w, fs, b, lh):
    return hashlib.md5(json.dumps([t, w, fs, b, lh]).encode()).hexdigest()


def measure(items):
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    todo = [it for it in items if _key(*it) not in cache]
    if todo:
        divs = "".join(
            f'<div style="width:{w * SAFETY}px;font-size:{fs}px;font-weight:{700 if b else 400};line-height:{lh};'
            f'white-space:pre-wrap;font-family:\'Open Sans\',sans-serif">{html.escape(t)}</div>'
            for t, w, fs, b, lh in todo)
        page = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap" rel="stylesheet"></head>'
                f'<body style="margin:0">{divs}<script>document.fonts.ready.then(()=>{{const h=[...document.querySelectorAll("div")].map(d=>d.getBoundingClientRect().height);'
                'document.body.setAttribute("data-h",JSON.stringify(h));});</script></body></html>')
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, dir=os.environ.get("MEASURE_TMP", HERE)) as f:
            f.write(page)
            path = f.name
        out = subprocess.run(["chromium", "--headless=new", "--disable-gpu", "--virtual-time-budget=6000", "--dump-dom", __import__("pathlib").Path(path).as_uri()],
                             capture_output=True, text=True).stdout
        os.unlink(path)
        hs = json.loads(html.unescape(re.search(r'data-h="([^"]*)"', out).group(1)))
        for it, h in zip(todo, hs):
            cache[_key(*it)] = h
        json.dump(cache, open(CACHE, "w"))
    return [cache[_key(*it)] for it in items]
