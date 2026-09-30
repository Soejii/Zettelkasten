#!/usr/bin/python3
"""Render the group interview guide markdown to HTML, then to .docx via LibreOffice."""

from html import escape
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path("/home/suji/document/Zettelkasten/College 101/Zettelkasten/Literature Notes/Analisis Jabatan")
SOURCE = ROOT / "Panduan Group Interview Kabid Pembinaan Imakris.md"
WORK = ROOT / "working/Panduan Group Interview Kabid Pembinaan"
HTML = WORK / "Panduan_Group_Interview_Kabid_Pembinaan_Imakris.html"
OUT_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else WORK


def inline(text: str) -> str:
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return text


def cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


lines = SOURCE.read_text(encoding="utf-8").splitlines()
body: list[str] = []
i = 0
while i < len(lines):
    line = lines[i]
    if not line.strip():
        i += 1
        continue
    if line.startswith("# "):
        body.append(f"<h1>{inline(line[2:])}</h1>")
        i += 1
        continue
    if line.startswith("### "):
        body.append(f"<h3>{inline(line[4:])}</h3>")
        i += 1
        continue
    if line.startswith("## "):
        cls = ' class="new-page"' if line.startswith("## Lampiran") else ""
        body.append(f"<h2{cls}>{inline(line[3:])}</h2>")
        i += 1
        continue
    if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[| :\-]+\|$", lines[i + 1]):
        rows = ["<tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells(line)) + "</tr>"]
        i += 2
        while i < len(lines) and lines[i].startswith("|"):
            row = cells(lines[i])
            if not row[0] and row[1].startswith("**") and not any(row[2:]):
                rows.append(f'<tr><td class="group" colspan="{len(row)}">{inline(row[1])}</td></tr>')
            else:
                rows.append("<tr>" + "".join(f"<td>{inline(c) or '&nbsp;'}</td>" for c in row) + "</tr>")
            i += 1
        body.append('<table border="1" cellspacing="0" cellpadding="4" width="100%">' + "".join(rows) + "</table>")
        continue
    if line.startswith("- "):
        items = []
        while i < len(lines) and lines[i].startswith("- "):
            items.append(f"<li>{inline(lines[i][2:])}</li>")
            i += 1
        body.append("<ul>" + "".join(items) + "</ul>")
        continue
    if re.match(r"^\d+\. ", line):
        items = []
        while i < len(lines) and re.match(r"^\d+\. ", lines[i]):
            items.append(f"<li>{inline(re.sub(r'^\d+\. ', '', lines[i]))}</li>")
            i += 1
        body.append("<ol>" + "".join(items) + "</ol>")
        continue
    para = [line]
    i += 1
    while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||- |\d+\. )", lines[i]):
        para.append(lines[i])
        i += 1
    body.append(f"<p>{inline(' '.join(para))}</p>")

HTML.write_text(f"""<!doctype html>
<html lang="id"><head><meta charset="utf-8">
<title>Panduan Group Interview Kabid Pembinaan Imakris</title>
<style>
@page {{ size: A4; margin: 2cm; }}
body {{ font-family: 'Times New Roman', serif; font-size: 11pt; line-height: 1.3; }}
h1, h2, h3 {{ font-family: 'Times New Roman', serif; }}
h1 {{ font-size: 14pt; text-align: center; margin: 0 0 12pt; }}
h3 {{ font-size: 11pt; margin: 10pt 0 4pt; }}
h2 {{ font-size: 12pt; margin: 12pt 0 4pt; }}
.new-page {{ page-break-before: always; }}
p {{ text-align: justify; margin: 0 0 6pt; }}
table {{ border-collapse: collapse; width: 100%; margin: 0 0 8pt; font-size: 10pt; }}
th, td {{ border: 0.5pt solid #000; padding: 3pt 4pt; text-align: left; vertical-align: top; }}
th {{ background: #d9d9d9; }}
td.group {{ background: #f2f2f2; }}
li {{ text-align: justify; margin: 0 0 3pt; }}
</style></head><body>{''.join(body)}</body></html>
""", encoding="utf-8")

subprocess.run(["soffice", "-env:UserInstallation=file:///tmp/render-docx-lo-profile", "--headless", "--infilter=HTML (StarWriter)", "--convert-to", "docx:MS Word 2007 XML",
                "--outdir", str(OUT_DIR), str(HTML)], check=True)
