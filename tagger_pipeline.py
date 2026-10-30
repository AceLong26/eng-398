#!/usr/bin/env python3
"""Minimalist NLP Tagger (RELS 398 / ENGL 398)
Extracts normalized text from the TEI <body> (<reg>, <corr>, <expan>),
runs SpaCy, and integrates/replaces lemma, pos, and msd attributes on <w> elements.

Usage:
    python3 tagger_pipeline.py [input.xml] [output.xml]
"""
import sys
import xml.etree.ElementTree as ET
import spacy

# 1. Load TEI XML
ET.register_namespace("", "http://www.tei-c.org/ns/1.0")
src_file = sys.argv[1] if len(sys.argv) > 1 else "transcription_normalized.xml"
out_file = sys.argv[2] if len(sys.argv) > 2 else "transcription_linguist.xml"
tree = ET.parse(src_file)
root = tree.getroot()

# 2. Extract normalized text from <body> (selecting reg, corr, expan)
def get_norm(elem):
    if elem.tag.endswith("choice"):
        for c in elem:
            if c.tag.split("}")[-1] in ("reg", "corr", "expan"):
                return get_norm(c)
        return ""
    return (elem.text or "") + "".join(get_norm(c) + (c.tail or "") for c in elem)

body = root.find(".//{http://www.tei-c.org/ns/1.0}body")
body = body if body is not None else root
text = " ".join(get_norm(body).split()).replace("' ", "'")

# 3. Lemmatize with SpaCy
lang = next((el.get("{http://www.w3.org/XML/1998/namespace}lang") for el in root.iter() if el.get("{http://www.w3.org/XML/1998/namespace}lang")), "fr")
nlp = spacy.load("fr_core_news_sm" if lang == "fr" else "en_core_web_sm")
tokens = [t for t in nlp(text) if not t.is_space]

# 4. Integrate / replace attributes on <w> and <pc> elements
w_elements = [el for el in body.iter() if el.tag.split("}")[-1] in ("w", "pc")]
if w_elements:
    for elem, t in zip(w_elements, tokens):
        elem.set("pos", t.pos_)
        if elem.tag.endswith("w"):
            elem.set("lemma", t.lemma_)
            if t.morph:
                elem.set("msd", str(t.morph))
else:
    s = ET.SubElement(ET.SubElement(body, "p"), "s")
    for t in tokens:
        tag = "pc" if t.pos_ == "PUNCT" else "w"
        attrs = {"pos": t.pos_}
        if tag == "w":
            attrs["lemma"] = t.lemma_
            if t.morph:
                attrs["msd"] = str(t.morph)
        ET.SubElement(s, tag, attrs).text = t.text

# 5. Save output
tree.write(out_file, encoding="utf-8", xml_declaration=True)
print(f"✓ Saved {len(tokens)} tokens into {out_file}")
