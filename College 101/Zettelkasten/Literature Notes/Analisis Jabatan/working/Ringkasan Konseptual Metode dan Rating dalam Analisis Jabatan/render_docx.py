#!/usr/bin/python3

from html import escape
from pathlib import Path
import re


ROOT = Path("/home/suji/document/Zettelkasten")
SOURCE = ROOT / "College 101/Zettelkasten/Literature Notes/Analisis Jabatan/Ringkasan Konseptual Metode dan Rating dalam Analisis Jabatan.md"
HTML = ROOT / "College 101/Zettelkasten/Literature Notes/Analisis Jabatan/working/Ringkasan Konseptual Metode dan Rating dalam Analisis Jabatan/ringkasan konseptual.html"


def inline(text: str) -> str:
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return text


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
    if line.startswith("## "):
        css_class = ' class="new-page"' if line.startswith("## 4. ") else ""
        body.append(f"<h2{css_class}>{inline(line[3:])}</h2>")
        i += 1
        continue
    if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[| :\-]+\|$", lines[i + 1]):
        rows = []
        header = [cell.strip() for cell in line.strip("|").split("|")]
        rows.append("<tr>" + "".join(f"<th>{inline(cell)}</th>" for cell in header) + "</tr>")
        i += 2
        while i < len(lines) and lines[i].startswith("|"):
            cells = [cell.strip() for cell in lines[i].strip("|").split("|")]
            rows.append("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in cells) + "</tr>")
            i += 1
        body.append("<table>" + "".join(rows) + "</table>")
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
    paragraph = [line]
    i += 1
    while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||- |\d+\. )", lines[i]):
        paragraph.append(lines[i])
        i += 1
    body.append(f"<p>{inline(' '.join(paragraph))}</p>")

document = f"""<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<style>
@page {{ size: A4; margin: 1.45cm 1.65cm 1.45cm 1.65cm; }}
body {{ font-family: Arial, sans-serif; font-size: 9.5pt; line-height: 1.04; color: #000; }}
h1 {{ font-size: 13pt; text-align: center; margin: 0 0 5pt; }}
h2 {{ font-size: 10.5pt; margin: 5pt 0 2pt; page-break-after: avoid; }}
.new-page {{ page-break-before: always; }}
p {{ text-align: justify; margin: 0 0 3pt; }}
table {{ border-collapse: collapse; width: 100%; margin: 0 0 4pt; font-size: 9pt; }}
th, td {{ border: 0.5pt solid #000; padding: 1.5pt 3pt; text-align: left; }}
ul, ol {{ margin: 0 0 3pt 16pt; padding-left: 8pt; }}
li {{ text-align: justify; margin: 0 0 1.5pt; }}
</style>
</head>
<body>{''.join(body)}</body>
</html>
"""
HTML.write_text(document, encoding="utf-8")
