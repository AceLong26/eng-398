#!/usr/bin/env python3
"""Automated Named Entity Recognition (NER) Pipeline for RELS 398 / ENGL 398.
Extracts normalized text from the TEI <body> (<reg>, <corr>, <expan>),
runs SpaCy statistical sequence models (fr_core_news_sm / en_core_web_sm),
and wraps detected entity spans with TEI P5 elements (<persName>, <placeName>,
<orgName>, <name>) carrying resp="#spacy" and type attributes.

Usage:
    python3 spacy_ner.py [input.xml] [output.xml]
"""
import sys
import os
import xml.etree.ElementTree as ET
import spacy

ET.register_namespace("", "http://www.tei-c.org/ns/1.0")
TEI_NS = "http://www.tei-c.org/ns/1.0"

src_file = sys.argv[1] if len(sys.argv) > 1 else "lemmatized_manualai.xml"
out_file = sys.argv[2] if len(sys.argv) > 2 else "ner_baseline.xml"

if not os.path.exists(src_file):
    # fallback to ground_truth_entities_manual.xml
    src_file = "ground_truth_entities_manual.xml"

tree = ET.parse(src_file)
root = tree.getroot()

# 1. Determine Language & Load Model
lang = next((el.get("{http://www.w3.org/XML/1998/namespace}lang") for el in root.iter() if el.get("{http://www.w3.org/XML/1998/namespace}lang")), "fr")
model_name = "fr_core_news_sm" if lang == "fr" else "en_core_web_sm"

try:
    nlp = spacy.load(model_name)
except OSError:
    sys.exit(f"Error: spaCy model '{model_name}' not found. Download it via: python -m spacy download {model_name}")

def get_norm(elem):
    if elem.tag.endswith("choice"):
        for c in elem:
            if c.tag.split("}")[-1] in ("reg", "corr", "expan"):
                return get_norm(c)
        return ""
    return (elem.text or "") + "".join(get_norm(c) + (c.tail or "") for c in elem)

body = root.find(f".//{{{TEI_NS}}}body")
if body is None:
    body = root

# Recursively un-wrap any entity/name elements inside body to start from plain linguistic tokens
def unwrap_entities(node):
    idx = 0
    while idx < len(node):
        child = node[idx]
        tag = child.tag.split("}")[-1]
        if tag in ("persName", "placeName", "orgName", "date", "name", "roleName"):
            unwrap_entities(child)
            sub_elements = list(child)
            if sub_elements:
                if child.text:
                    if idx > 0:
                        prev = node[idx - 1]
                        prev.tail = (prev.tail or "") + child.text
                    else:
                        node.text = (node.text or "") + child.text
                if child.tail:
                    sub_elements[-1].tail = (sub_elements[-1].tail or "") + child.tail
                node[idx:idx+1] = sub_elements
                idx += len(sub_elements)
                continue
            else:
                # empty entity element
                node.remove(child)
                continue
        else:
            unwrap_entities(child)
            idx += 1

unwrap_entities(body)

TAG_MAP = {
    "PER": "persName",
    "PERSON": "persName",
    "LOC": "placeName",
    "GPE": "placeName",
    "ORG": "orgName",
    "MISC": "name"
}

total_entities = 0

for p_num, p in enumerate(body.findall(f".//{{{TEI_NS}}}p")):
    p_norm = " ".join(get_norm(p).split()).replace("' ", "'")
    if not p_norm.strip():
        continue
    
    doc = nlp(p_norm)
    spacy_tokens = [t for t in doc if not t.is_space]
    
    children = list(p)
    token_to_child_idx = []
    for c_idx, c in enumerate(children):
        if c.tag.split("}")[-1] in ("w", "pc"):
            token_to_child_idx.append(c_idx)
    
    if len(spacy_tokens) != len(token_to_child_idx):
        print(f"Warning in P{p_num}: token count mismatch ({len(spacy_tokens)} spaCy vs {len(token_to_child_idx)} XML).")
        continue
    
    spans_to_wrap = []
    for ent in doc.ents:
        total_entities += 1
        t_indices = [i for i, t in enumerate(spacy_tokens) if ent.start <= t.i < ent.end]
        if t_indices:
            start_child = token_to_child_idx[min(t_indices)]
            end_child = token_to_child_idx[max(t_indices)]
            tei_tag = TAG_MAP.get(ent.label_, "name")
            spans_to_wrap.append((start_child, end_child, tei_tag, ent.label_, ent.text))
            print(f"  P{p_num} [{ent.label_} -> <{tei_tag}>] \"{ent.text}\" (tokens {min(t_indices)}..{max(t_indices)})")
    
    for start_c, end_c, tei_tag, label, text in reversed(spans_to_wrap):
        wrapper = ET.Element(f"{{{TEI_NS}}}{tei_tag}", {
            "type": label.lower(),
            "resp": "#spacy"
        })
        to_wrap = children[start_c : end_c + 1]
        wrapper.extend(to_wrap)
        if to_wrap[-1].tail:
            wrapper.tail = to_wrap[-1].tail
            to_wrap[-1].tail = None
        p[start_c : end_c + 1] = [wrapper]
        children = list(p)

header = root.find(f".//{{{TEI_NS}}}teiHeader")
if header is not None:
    titleStmt = header.find(f".//{{{TEI_NS}}}titleStmt")
    if titleStmt is not None:
        resp = ET.SubElement(titleStmt, f"{{{TEI_NS}}}respStmt")
        resp.set("xml:id", "spacy_nlp")
        name = ET.SubElement(resp, f"{{{TEI_NS}}}name")
        name.text = f"spaCy {model_name} (Automated NER Pipeline)"
        r = ET.SubElement(resp, f"{{{TEI_NS}}}resp")
        r.text = "Automated named entity extraction and classification"

os.makedirs(os.path.dirname(os.path.abspath(out_file)), exist_ok=True)
tree.write(out_file, encoding="utf-8", xml_declaration=True)
print(f"✓ Saved automated NER baseline with {total_entities} entities to {out_file}")

