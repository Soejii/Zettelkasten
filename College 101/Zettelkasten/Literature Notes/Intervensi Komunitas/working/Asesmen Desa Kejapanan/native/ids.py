"""Print the text element ids (in order) from the latest Canva edit-design response for a page.

Usage: python3 ids.py <page_id>   (reads this session's transcript)
"""
import json
import sys

T = "/home/suji/.claude/projects/-home-suji-document-Zettelkasten/f2fa6f5b-76e1-4df3-b954-10fb3de51baf.jsonl"
page = sys.argv[1]
found = None
for line in open(T):
    if page not in line or "edits_unverified" not in line:
        continue
    rec = json.loads(line)
    content = rec.get("message", {}).get("content", [])
    for c in content if isinstance(content, list) else []:
        if c.get("type") != "tool_result":
            continue
        parts = c["content"] if isinstance(c["content"], list) else [{"type": "text", "text": c["content"]}]
        for p in parts:
            t = p.get("text", "")
            if t.startswith("{") and '"edits_unverified"' in t and f'"id":"{page}"' in t:
                found = t
import glob, os, re
if found is None:
    fs = sorted(glob.glob(os.path.join(T[:-6], "tool-results", "*.json")), key=os.path.getmtime)
    for f in fs:
        t = open(f).read()
        if '"edits_unverified"' in t and f'"id":"{page}"'.replace('"', '\\"') in t:
            found = json.loads(t)[0]["text"]
els = re.findall(r'\{"id":"(LB[A-Za-z0-9]+)","top":[^{}]*?"type":"(text|shape|rect)"', found.split('"edit_operation_results"')[0])
print(",".join(i for i, ty in els if ty == "text"))
