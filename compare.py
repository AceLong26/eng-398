import sys
import difflib
from lxml import html

def words(path):
    body = html.parse(path).find("body")
    return body.text_content().split()

old, new = words(sys.argv[1]), words(sys.argv[2])
matcher = difflib.SequenceMatcher(None, old, new, autojunk=False)
for op, i1, i2, j1, j2 in matcher.get_opcodes():
    if op != "equal":
        print(op.upper(), "|", " ".join(old[i1:i2]), "|", " ".join(new[j1:j2]))
print("Words:", len(old), "and", len(new))