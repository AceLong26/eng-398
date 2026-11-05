
| Mention | Manual Truth (9.1) | Machine Guess (9.2) | Error Diagnosis |
| :--- | :--- | :--- | :--- |
| **`31 xbre 1791`** | `<date when="1791-12-31">` | *[Omission / Unrecognized]* | **OOV Spelling / Abbreviation Failure**: Standard modern SpaCy pipelines lack temporal resolution for 18th-century scribal abbreviations (`xbre` for *décembre*), failing to identify the date span. |
| **`le Ministre des affaires etrangeres`** | `<persName><roleName type="cabinet">` *(Ministre des affaires étrangères)* | `<orgName type="org">` *(Ministre des affaires étrangères)* | **Type Confusion & Boundary Error**: SpaCy confused the official holding the office (*Claude Antoine de Valdec de Lessart*) with the ministry institution (`ORG`), and dropped the preceding determiner boundary inconsistently. |
| **`MM` (`Messieurs`)** | `<persName type="address"><roleName type="honorific">` | `<persName type="per">` | **Boundary / Span Integrity**: SpaCy identified the token as `PER`, but missed the abbreviated honorific address category and failed to associate it with the legislative deputies. |
| **`l'Empereur`** (all occurrences) | `<persName ref="VIAF:74645226"><roleName type="monarch">` *(Leopold II)* | `<persName type="per">` *(includes `l'`)* | **Boundary Error (Clitic Ingestion)**: SpaCy absorbed the elided definite article `l'` into the entity boundary (`l'Empereur`) contrary to TEI token-isolation policies, which require determiners to stay outside the name element. |
| **`ambassadeur de France`** | `<persName><roleName type="diplomat">` with nested `<placeName>` | *[Omission / Partial]* | **Syntactic / Structural Omission**: SpaCy missed the official title entirely, capturing only the prepositional complement `de France` as a location (`LOC`). |
| **`de France`** | `<placeName>` *(France)* | `<placeName type="loc">` *(de France)* | **Boundary Error (Preposition Absorption)**: Preposition `de` was absorbed directly into the place name span rather than scoping strictly over the toponym `France`. |
| **`Vienne`** | `<placeName ref="GeoNames:2761369">` | `<placeName type="loc">` | **True Positive (Exact Match)**: Successfully recognized as a geographic location (`LOC`). |
| **`deux allies`** | `<rs type="group" subtype="alliance">` | *[Omission / False Negative]* | **Complex Nominal / Semantic Phrase Failure**: Statistical NER models trained on modern news data miss indefinite historical diplomatic nominal phrases referring to allied sovereign powers. |
| **`Electeur de Treves`** (lines 12, 16, 23) | `<persName ref="VIAF:10636906"><roleName type="ruler">` with nested `<placeName>` | `<name type="misc">` | **Type Confusion & Inability to Nest**: SpaCy classified the sovereign title as generic `MISC` rather than `PER` (Clemens Wenzeslaus), and flat sequence tagging could not detect the nested city toponym `Trèves`. |
| **`ce prince`** | `<rs type="person" ref="VIAF:10636906">` | *[Omission / False Negative]* | **Anaphora / Co-reference Failure**: Standard NER sequence labelers do not perform co-reference resolution for demonstrative referring expressions. |
| **`la France`** (lines 7, 21) | `<placeName ref="GeoNames:3017382">` | `<placeName type="loc">` *(la France)* | **Boundary Error (Determiner Absorption)**: Absorbed the proclitic article `la` into the `<placeName>` tag rather than isolating the lexical toponym `France`. |
| **`Nation Françoise`** | `<orgName type="collective" ref="VIAF:264091107">` | `<orgName type="org">` *(Nation Française)* | **Category Nuance & Normalization**: Correctly recognized the multi-word entity boundaries, though modern French models rely strictly on the regularized spelling (`Française`) rather than diplomatic historical forms. |
| **`Brabançons`** | `<rs type="group" subtype="nationality">` | `<placeName type="loc">` | **Type Confusion (Demonym vs. Toponym)**: Misclassified a demonym referring to insurgent people of Brabant as a geographic place (`LOC`). |
| **`Pays Bas autrichiens`** | `<placeName type="region" ref="VIAF:127393433">` | `<placeName type="loc">` | **Boundary / Orthographic Variance**: Correctly identified as location, but sensitive to modern hyphenation (`Pays-Bas`) versus unhyphenated manuscript spacing. |
| **`Etats` (`États`)** | Common noun / collective territory | `<name type="misc">` | **False Positive / Capitalization Bias**: Capitalized common noun *ses États* was incorrectly flagged as a named entity (`MISC`) due to 18th-century capitalization conventions misleading modern statistical weights. |

---

## 2. Global Error Diagnostics & Methodological Findings

1. **Boundary Inconsistencies (Clitics & Prepositions)**:
   - Modern French SpaCy models (`fr_core_news_sm`) consistently bundle prepositions and clitic articles (`l'`, `la`, `de`) into the entity span (e.g., `<placeName>la France</placeName>`, `<persName>l'Empereur</persName>`). 
   - TEI philological policy requires keeping function words and articles outside the entity element to preserve strict token and part-of-speech integrity.

2. **18th-Century Orthography and Capitalization**:
   - Modern models heavily prioritize initial capital letters. In manuscript diplomatic prose where nouns like *États* or honorifics are capitalized, SpaCy produces false positives (`<name type="misc">États</name>`).
   - Conversely, scribal abbreviations such as `xbre` (December) and archaic spellings (`Françoise`, `Treves` without grave accent) bypass statistical gazetteers, causing total omission of dates.

3. **Title vs. Person Disambiguation**:
   - Diplomatic titles (*l'Électeur de Trèves*, *le Ministre des affaires étrangères*) are either conflated into organizations (`ORG`), tagged as generic miscellaneous strings (`MISC`), or completely missed.
   - Standard automated models cannot represent hierarchical or nested relationships (such as a `<placeName>` nested within a `<roleName>` inside a `<persName>`).

4. **Co-reference and Referring Strings (`<rs>`)**:
   - Automated sequence taggers only detect overt proper nouns and fail to capture anaphoric referring expressions (*ce prince*, *deux alliés*), which are crucial for historical and diplomatic discourse analysis.

