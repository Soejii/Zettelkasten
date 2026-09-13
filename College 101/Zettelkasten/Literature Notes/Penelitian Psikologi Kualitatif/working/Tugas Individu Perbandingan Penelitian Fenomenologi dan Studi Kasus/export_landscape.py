"""Render the canonical assignment as an A4 landscape PDF in Fafnir."""
from pathlib import Path
import hashlib
import markdown
from bs4 import BeautifulSoup
from weasyprint import HTML

assignment = "Tugas Individu Perbandingan Penelitian Fenomenologi dan Studi Kasus"
course_dir = Path(__file__).resolve().parents[2]
source = course_dir / (assignment + ".md")
output = Path("/home/suji/document/college/penelitian psikologi kualitatif/assignments") / (assignment.lower() + ".pdf")
text = source.read_text()
body = markdown.markdown(text, extensions=["tables"])
soup = BeautifulSoup(body, "html.parser")
for table in soup.find_all("table"):
    columns = len(table.find("tr").find_all(["th", "td"], recursive=False))
    table["class"] = "comparison" if columns == 3 else "identity"
    colgroup = soup.new_tag("colgroup")
    for width in (["14%", "43%", "43%"] if columns == 3 else ["15%", "85%"]):
        col = soup.new_tag("col")
        col["style"] = "width:" + width
        colgroup.append(col)
    table.insert(0, colgroup)
body = str(soup)
css = """
@page { size: A4 landscape; margin: 12mm 13mm 14mm;
  @bottom-right { content: counter(page) " / " counter(pages); font: 9pt serif; color: #555; }
}
body { font-family: "DejaVu Serif", serif; font-size: 9.5pt; line-height: 1.3; color: #111; }
h1 { font-size: 16pt; line-height: 1.2; margin: 0 0 6mm; }
h2 { font-size: 12pt; margin: 5mm 0 2mm; break-after: avoid; }
p { margin: 0 0 3mm; orphans: 3; widows: 3; }
table { width: 100%; border-collapse: collapse; table-layout: fixed; }
thead { display: table-header-group; }
th, td { border: .6pt solid #777; padding: 2mm; vertical-align: top; overflow-wrap: anywhere; }
th { background: #e9edf0; text-align: left; font-weight: bold; }
th:first-child, td:first-child { font-weight: bold; }
table.identity { margin-bottom: 4mm; }
th, td { box-sizing: border-box; }
tr { break-inside: avoid; }
a { color: #174a75; text-decoration: none; overflow-wrap: anywhere; }
"""
html = '<!doctype html><html lang="id"><meta charset="utf-8"><title>' + assignment + '</title><style>' + css + '</style><body>' + body + '</body></html>'
output.parent.mkdir(parents=True, exist_ok=True)
HTML(string=html, base_url=str(course_dir)).write_pdf(output)
print(output)
print("Source SHA-256:", hashlib.sha256(source.read_bytes()).hexdigest())
