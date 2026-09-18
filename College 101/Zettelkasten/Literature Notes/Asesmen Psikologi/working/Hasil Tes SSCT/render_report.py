#!/usr/bin/env python3

from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "Hasil Tes SSCT.md"
OUTPUT = Path("/tmp/hasil-tes-ssct.html")


def inline(text: str) -> str:
    rendered = html.escape(text, quote=False)
    rendered = rendered.replace("&lt;br&gt;", "<br>")
    rendered = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", rendered)
    rendered = re.sub(r"`(.+?)`", r"<code>\1</code>", rendered)
    rendered = re.sub(r"\*(.+?)\*", r"<em>\1</em>", rendered)
    return rendered


def cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


lines = SOURCE.read_text(encoding="utf-8").splitlines()
body: list[str] = []
index = 0

while index < len(lines):
    line = lines[index]
    if not line:
        index += 1
        continue

    if line.startswith("# "):
        body.append(f"<h1>{inline(line[2:])}</h1>")
        index += 1
        continue
    if line.startswith("## "):
        body.append(f"<h2>{inline(line[3:])}</h2>")
        index += 1
        continue

    if line.startswith("|") and index + 1 < len(lines) and re.fullmatch(
        r"\|[\s|:-]+\|", lines[index + 1]
    ):
        header = cells(line)
        index += 2
        rows: list[list[str]] = []
        while index < len(lines) and lines[index].startswith("|"):
            rows.append(cells(lines[index]))
            index += 1
        body.append('<table border="1" cellspacing="0" cellpadding="6"><thead><tr>')
        body.extend(f"<th>{inline(value)}</th>" for value in header)
        body.append("</tr></thead><tbody>")
        for row in rows:
            body.append("<tr>")
            body.extend(f"<td>{inline(value)}</td>" for value in row)
            body.append("</tr>")
        body.append("</tbody></table>")
        continue

    body.append(f"<p>{inline(line)}</p>")
    index += 1

document = """<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>Hasil Tes SSCT</title>
<style>
@page { size: A4 landscape; margin: 1.3cm; }
body { font-family: Arial, sans-serif; font-size: 10pt; line-height: 1.35; color: #111; }
h1 { text-align: center; font-size: 18pt; margin: 0 0 12pt; }
h2 { font-size: 13pt; margin: 16pt 0 7pt; page-break-after: avoid; }
p { margin: 4pt 0; }
table { width: 100%; border-collapse: collapse; margin: 7pt 0 14pt; }
tr { page-break-inside: avoid; }
th, td { border: 1px solid #333; padding: 6pt; vertical-align: top; }
th { background: #e9edf2; text-align: center; font-weight: bold; }
th:nth-child(1), td:nth-child(1) { width: 17%; }
th:nth-child(2), td:nth-child(2) { width: 42%; }
th:nth-child(3), td:nth-child(3) { width: 41%; }
code { font-family: Arial, sans-serif; background: none; }
</style>
</head>
<body>
""" + "\n".join(body) + "\n</body>\n</html>\n"

OUTPUT.write_text(document, encoding="utf-8")
print(OUTPUT)
