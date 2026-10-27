# Lemmatization Specification & Publication Report

## 1. Authority & Reference Standards
- **Lexical Authority**: French: *Trésor de la Langue Française informatisé* (TLFi / CNRTL: `https://www.cnrtl.fr/definition/`) & *Dictionnaire de l'Académie française* (4e et 5e éditions, 1762/1798).
- **POS Tagset**: Universal Dependencies (UD) POS tagset for French / TEI POS tagging standards (`@pos`, `@lemma`).
- **Source Corpus**: King Louis XVI, *Letter to the Assemblée Nationale* (31 December 1791), British Library Zweig MS 169 (`transcription_normalized.xml`).

---

## 2. Editorial & Grammatical Principles

### Capitalization
- **Proper Nouns / Named Entities**: Lemmas retain initial capitals (e.g., `Empereur` -> `Empereur`, `France` -> `France`).
- **Common Words**: Lemmas are converted to standard lower-case dictionary citation forms (e.g., `Dans` -> `dans`, `Ministre` -> `ministre`).

### Contraction & Clitic Splits
- Elisions and clitics are segmented into discrete syntactic tokens (`<w>` elements):
  - `l'Empereur` -> `l'` (definite article, lemma: `le`) + `Empereur` (proper noun, lemma: `Empereur`).
  - `je n'ai` -> `je` (pronoun, lemma: `je`) + `n'` (adverb/negation, lemma: `ne`) + `ai` (auxiliary verb, lemma: `avoir`).
  - `d'un` / `d'` -> `d'` (preposition, lemma: `de`).
  - `m'a` -> `m'` (pronoun, lemma: `me`) + `a` (auxiliary verb, lemma: `avoir`).

### Part of Speech (POS) & Lemmatization Standards
- **Verbs**: Lemmatized to infinitive form (e.g., `fais` -> `faire`, `répète` -> `répéter`, `ai` -> `avoir`).
- **Nouns**: Lemmatized to masculine singular form unless inherently feminine or plural (e.g., `réponse` -> `réponse`, `affaires` -> `affaire`).
- **Adjectives**: Lemmatized to masculine singular form (e.g., `étrangères` -> `étranger`, `juste` -> `juste`).


## 4. Crux Log & Grammatical Ambiguities

### Crux 1: Token 18 (`demander` vs `demandé`)
- **Reading / Surface Form**: The manuscript writes `demander` following auxiliary `ai` (*"je n'ai rien demander"*).
- **Analysis**: In classical and 18th-century French manuscript sources, the phonetic equivalence of /-e/ often led to spelling variation between the infinitive (`-er`) and masculine singular past participle (`-é`). Syntactically, it functions as a past participle governed by `ai` (*ai demandé* = compound past).
- **Lemmatization Decision**: In both interpretations (infinitive or participle), the lexical head lemma is **`demander`**.

### Crux 2: Token 19 (`que` in restrictive *ne ... rien que*)
- **Analysis**: *Que* functions here in a restrictive/exceptive locution (*ne ... rien que* = "nothing except / nothing other than"). Depending on the syntactic parsing framework, it can be categorized as a restrictive adverb (`ADV`) or a comparative subordinating conjunction (`SCONJ`).
- **Lemmatization Decision**: Lemmatized as **`que`** with grammatical cross-reference to TLFi under section *II. Emploi comparatif ou restrictif*.

### Crux 3: Cliticization and Elision (`l'`, `n'`)
- **Analysis**: Traditional French tokenizers often keep `l'Empereur` as one string. For corpus and dictionary alignment, clitic elisions (`l'`, `n'`, `d'`, `s'`, `j'`) are treated as discrete word elements (`<w>`) with normalized lemmas (`le`, `ne`, `de`, `se`, `je`).

