"""Print format + shape + layer ops for a slide, using the text ids from the latest edit response.

Usage: python3 rest.py <slide>
"""
import json
import subprocess
import sys

_KEY = sys.argv[1]
sys.argv = ["x"]
exec(open("native_build.py").read().split('if __name__ == "__main__":')[0])
sl = SLIDES[_KEY]
ids = subprocess.check_output(["python3", "ids.py", sl.page_id], text=True).strip().split(",")
print(json.dumps(sl.fmt_ops(ids) + sl.shape_ops(ids), ensure_ascii=False))
