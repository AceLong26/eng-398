# Lemmatization Policies

## 1. Dictionary
- **Authority**: *Trésor de la Langue Française informatisé* (TLFi / CNRTL).
- **Tagset**: Universal Dependencies (UPOS).

## 2. Capitalization
- **Proper Nouns**: Keep initial capital (e.g., `Empereur` → `Empereur`).
- **Common Words**: Lowercase dictionary entry (e.g., `Dans` → `dans`).

## 3. Contractions & Missing Letters
- Split elisions and clitics into separate tokens:
  - `l'Empereur` → `l'` (lemma: `le`) + `Empereur` (lemma: `Empereur`)
  - `n'ai` → `n'` (lemma: `ne`) + `ai` (lemma: `avoir`)
  - `d'` → lemma `de`
  - `m'` → lemma `me`
  - `j'` → lemma `je`
- Restore missing/elided letters in the lemma.

## 4. Headword Rules
- **Verbs**: Infinitive (e.g., `fais` → `faire`, `ai` → `avoir`).
- **Nouns & Adjectives**: Singular citation form (masculine singular where applicable).

## 5. Notes on Difficult Choices
- **`demander` vs `demandé`**: 18th-century spelling uses infinitive `-er` for past participle `-é` after auxiliary `ai`. Lemma is `demander`.
- **`que`**: Disambiguated by syntactic function (relative pronoun `que`, subordinating conjunction `que`, or restrictive adverb `que` in *ne... rien que*).
