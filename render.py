#!/usr/bin/env python3
import sys
from lxml import etree
xml_file, xsl_file, out_file = sys.argv[1], sys.argv[2], sys.argv[3]
transform = etree.XSLT(etree.parse(xsl_file))
result = transform(etree.parse(xml_file))
with open(out_file,"wb") as f:
    f.write(etree.tostring(result, method="html", encoding="utf-8"))
print("Wrote", out_file)
