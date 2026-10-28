#!/usr/bin/env python3
"""Minimalist NLP Tagger (RELS 398 / ENGL 398 — Lesson 8.2)
Reads text from a TEI XML file specified by the user, runs SpaCy,
prints a token table, and exports nlp_baseline.xml for the Slide 13 diff.

Usage:
    python3 tagger_pipeline.py [input.xml]
"""
import sys
import xml.etree.ElementTree as ET
import spacy

# 1. Read text from user-specified XML file (default: ground_truth_manual.xml)
xml_file = sys.argv[1] if len(sys.argv) > 1 else "transcription_normalized.xml"
text = " ".join(ET.parse(xml_file).getroot().itertext())

# 2. Process with SpaCy (fr_core_news_sm for French, en_core_web_sm for English)
nlp = spacy.load("fr_core_news_sm")
doc = nlp(text)

# 3. Print terminal table (Card A)
print(f"{'Token':12} {'Lemma':12} {'UPOS':8} {'MSD':30}")
for t in doc:
    if not t.is_space:
        print(f"{t.text:12} {t.lemma_:12} {t.pos_:8} {str(t.morph):30}")

# 4. Export nlp_baseline.xml for Slide 13 diff
with open("nlp_baseline.xml", "w", encoding="utf-8") as f:
    f.write('<ab xmlns="http://www.tei-c.org/ns/1.0" type="linguistic_layer">\n')
    for t in doc:
        if not t.is_space:
            if t.pos_ == "PUNCT":
                f.write(f'  <pc pos="PUNCT">{t.text}</pc>\n')
            else:
               msd_attr = f' msd="{str(t.morph)}"' if str(t.morph) else ""
               f.write(f'  <w lemma="{t.lemma_}" pos="{t.pos_}"{msd_attr}>{t.text}</w>\n')
    f.write('</ab>\n')

print(f"\n✓ Saved nlp_baseline.xml from {xml_file}")
