
| # | Mention | Manual Truth Category | Authority Link (Wikidata / GeoNames) | spaCy Prediction |
|---:|:---|:---|:---|:---|:---|:---|
| 1 | `Assemblée Nationale` | `<orgName>` | [Wikidata: Q876424](https://www.wikidata.org/wiki/Q876424) | `<orgName type="org">` | `<orgName ref="https://www.wikidata.org/wiki/Q876424">` |
| 2 | `31 xbre 1791` | `<date>` | `@when="1791-12-31"` | `<date when="1791-12-31">` | spaCy missed (`xbre`)|
| 3 | `Ministre des affaires etrangeres` | `<persName>` | [Wikidata: Q2976897](https://www.wikidata.org/wiki/Q2976897) | `<orgName type="org">` | `<persName ref="https://www.wikidata.org/wiki/Q2976897">` | spaCy tagged wrongly (ORG) |
| 4 | `MM` (`Messieurs`) | `<persName>` |  (`ref="#person-001"`) | `<persName type="per">` | `<persName ref="#person-001">` | 
| 5 | `Empereur` (lb 4) | `<persName>` | [Wikidata: Q151321](https://www.wikidata.org/wiki/Q151321) | `<persName type="per">l' Empereur` | `<persName ref="https://www.wikidata.org/wiki/Q151321">` | spaCy tagged wrongly (`l'`)|
| 6 | `ambassadeur` (de France) | `<persName>` | [Wikidata: Q3052789](https://www.wikidata.org/wiki/Q3052789) | `<persName ref="https://www.wikidata.org/wiki/Q3052789">` | spaCy missed title|
| 7 | `France` (lb 4) | `<placeName>` | [GeoNames: 3017382](https://www.geonames.org/3017382) | `<placeName type="loc">de France` | `<placeName ref="https://www.wikidata.org/wiki/Q142">` | spaCy tagged wrongly ( `de`);|
| 8 | `Vienne` (lb 5) | `<placeName>` | [GeoNames: 2761369](https://www.geonames.org/2761369) | `<placeName type="loc">` | `<placeName ref="https://www.wikidata.org/wiki/Q1741">` |
| 9 | `Empereur` (lb 6) | `<persName>` | [Wikidata: Q151321](https://www.wikidata.org/wiki/Q151321) | `<persName type="per">l' Empereur` | `<persName ref="https://www.wikidata.org/wiki/Q151321">` | spaCy tagged wrongly (`l'`); |
| 10 | `France` (lb 7) | `<placeName>` | [GeoNames: 3017382](https://www.geonames.org/3017382) | `<placeName type="loc">la France` | `<placeName ref="https://www.wikidata.org/wiki/Q142">` | spaCy tagged wrongly ( `la`);|

---

 `Ministre des affaires etrangeres` misclassified as `ORG` instead of `PER`.
  - 4 Token Boundary Errors: Ingested articles and prepositions `l'Empereur`, `de France`, `la France`
  - *(Plus 2 complete omissions: `31 xbre 1791` and `ambassadeur`)*
  - identified `MM` / Messieurs

---

## 3. Reflection on Automated vs. Human Entity Curation

Comparing automated tagging with manual review shows why eighteenth-century manuscripts are difficult for modern language tools to process. spaCy’s fr_core_news_sm, trained on modern texts, often included extra words in names, such as l’ in l’Empereur and de in de France. This did not match the project’s TEI encoding rules. It also missed old abbreviations such as xbre for December and incorrectly labelled Ministre des affaires étrangères as an organization rather than a title referring to a person.
The AI model was better at using context to identify people. It connected titles to historical figures, including Leopold II, Valdec de Lessart, and the Marquis de Noailles, and provided verified Wikidata identifiers. For collective parliamentary addresses that did not refer to one person, it used the local identifier #person-001.
However, AI results still need careful checking. Models can invent identifiers or replace original spellings with modern ones. Combining AI tagging, automatic TEI checks, and manual review helps preserve both accurate encoding and historical detail.