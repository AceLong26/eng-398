import sys
from lxml import etree, html

TEI = {"tei": "http://www.tei-c.org/ns/1.0"}
source = etree.parse(sys.argv[1])
page = html.parse(sys.argv[2])

print("In the TEI body:")
for name in ["choice", "unclear", "gap", "lb"]:
    found = source.xpath("//tei:body//tei:" + name, namespaces=TEI)
    print("  ", name, len(found))

print("In the page:")
for name in ["reg", "expan", "corr", "orig", "abbr", "sic", "unclear", "gap", "lb"]:
    found = [e for e in page.iter("*") if name in e.get("class", "").split()]
    print("  ", name, len(found))
print("   brackets", page.find("body").text_content().count("[…"))