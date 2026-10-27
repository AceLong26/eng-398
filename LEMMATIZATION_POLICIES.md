# Lemmatization Policies (`LEMMATIZATION_POLICIES.md`)

## 1. Dictionary & Lexical Authority
- **Primary Authority**: *Trésor de la Langue Française informatisé* (TLFi / CNRTL: [https://www.cnrtl.fr/definition/](https://www.cnrtl.fr/definition/)).
- **Historical Reference**: *Dictionnaire de l'Académie française* (4e édition 1762 & 5e édition 1798) to contextualize late 18th-century syntactic patterns, phonetic spellings, and orthographic variants.
- **Tagset Standard**: Universal POS (UPOS) tags and morphological features adhering to the Universal Dependencies (UD) French framework.

---

## 2. Capitalization Policies
- **Proper Names & Honorific Titles**:
  - Proper nouns and specific historical entities retain initial capitalization in their lemma (e.g., surface `Empereur` $\rightarrow$ lemma `Empereur`; `France` $\rightarrow$ lemma `France`).
- **Common Words & Syntactic Sentence-Starters**:
  - All common nouns, verbs, adjectives, and grammatical particles are normalized to standard lowercase dictionary headword forms (e.g., surface `Dans` $\rightarrow$ lemma `dans`; `Ministre` $\rightarrow$ lemma `ministre`).

---

## 3. Contraction & Clitic Division
- **Elisions and Clitics**:
  - All contracted prepositions, pronouns, articles, and negative particles are tokenized onto their own independent rows.
  - Punctuation (including apostrophes attached to elided monosyllables) remains with the clitic surface token to document the original form precisely.
- **Recording Missing Letters**:
  - Elided letters are fully restored in the canonical dictionary lemma:
    - `l'` $\rightarrow$ lemma `le` (DET, masculine singular elided)
    - `j'` / `je` $\rightarrow$ lemma `je` (PRON, 1st person singular)
    - `n'` $\rightarrow$ lemma `ne` (ADV, polarity=neg)
    - `d'` $\rightarrow$ lemma `de` (ADP)
    - `m'` $\rightarrow$ lemma `me` (PRON, 1st person singular object)

---

## 4. Manual Grammar & Lemmatization Table

### Source Passage
- **Source**: King Louis XVI, *Letter to the Assemblée Nationale* (31 December 1791), British Library Zweig MS 169.
- **Location in Transcription**: Paragraph 2, lines 15–16.
- **Diplomatic Text**:
  > *"Dans la reponse que je fais a l'Empereur, je lui repete que je n'ai rien demander que de juste"*
- **Normalized Modern Text**:
  > *"Dans la réponse que je fais à l'Empereur, je lui répète que je n'ai rien demander [demandé] que de juste"*

---

### Annotation Table (20 Consecutive Word Tokens + Punctuation)

| # | Token (Surface) | Normalized Form | Lemma (TLFi) | UPOS | Morphological Features | Notes & Justifications |
|:---|:---|:---|:---|:---|:---|:---|
| **1** | Dans | Dans | **dans** | `ADP` | _ | Standard preposition introducing locative/contextual circumstantial phrase. Capitalized in MS because it begins a paragraph. |
| **2** | la | la | **le** | `DET` | `Definite=Def\|Gender=Fem\|Number=Sing\|PronType=Art` | Definite feminine article determining *réponse*. |
| **3** | reponse | réponse | **réponse** | `NOUN` | `Gender=Fem\|Number=Sing` | Common noun. MS lacks acute accent (*reponse*); verified headword *réponse* in TLFi. |
| **4** | que | que | **que** | `PRON` | `PronType=Rel` | Relative pronoun acting as direct object complement of the verb *fais*. |
| **5** | je | je | **je** | `PRON` | `Number=Sing\|Person=1\|PronType=Prs` | Subject personal pronoun of relative clause verb *fais*. |
| **6** | fais | fais | **faire** | `VERB` | `Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin` | 1st-person singular present indicative of *faire*. |
| **7** | a | à | **à** | `ADP` | _ | Preposition introducing the indirect object. MS omits grave accent (*a*); normalized to *à*. |
| **8** | l' | l' | **le** | `DET` | `Definite=Def\|Gender=Masc\|Number=Sing\|PronType=Art` | Elided definite article before vowel-initial noun. Lemma restored to *le*. |
| **9** | Empereur | Empereur | **Empereur** | `PROPN` | `Gender=Masc\|Number=Sing` | Proper noun / unique royal title. Retains capital in lemma per policy. |
| **—** | , | , | **,** | `PUNCT` | _ | Punctuation token separating circumstantial clause from main clause. |
| **10** | je | je | **je** | `PRON` | `Number=Sing\|Person=1\|PronType=Prs` | Subject pronoun of the principal clause verb *répète*. |
| **11** | lui | lui | **lui** | `PRON` | `Gender=Masc\|Number=Sing\|Person=3\|PronType=Prs` | 3rd-person masculine singular dative clitic personal pronoun (indirect object = the Emperor). |
| **12** | repete | répète | **répéter** | `VERB` | `Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin` | MS omits acute/grave accents (*repete*); normalized to *répète*. Main governing verb. |
| **13** | que | que | **que** | `SCONJ` | _ | Subordinating conjunction introducing the declarative completive clause (*que je n'ai...*). |
| **14** | je | je | **je** | `PRON` | `Number=Sing\|Person=1\|PronType=Prs` | Subject pronoun of subordinate clause. |
| **15** | n' | n' | **ne** | `ADV` | `Polarity=Neg` | Clitic negative particle before vowel. Restored to canonical lemma *ne*. |
| **16** | ai | ai | **avoir** | `AUX` | `Mood=Ind\|Number=Sing\|Person=1\|Tense=Pres\|VerbForm=Fin` | Auxiliary verb *avoir* in compound past tense. |
| **17** | rien | rien | **rien** | `PRON` | `Gender=Masc\|Number=Sing\|PronType=Neg` | Negative indefinite pronoun functioning as direct object complement. |
| **18** | demander | demandé | **demander** | `VERB` | `Tense=Past\|VerbForm=Part` | **Crux**: MS writes infinitive ending *-er* where standard syntax requires the past participle *-é* after auxiliary *ai*. In 18th-c. French hands, homophonic /-e/ variation is frequent. Lemmatized to infinitive headword *demander*. |
| **19** | que | que | **que** | `ADV` | _ | Restrictive adverb (*ne ... rien que* = "nothing except / only"). Syntactically restrictive particle. |
| **20** | de | de | **de** | `ADP` | _ | Preposition introducing the adjectival complement governed by indefinite pronoun *rien* (*rien de juste*). |

---

## 5. Crux & Disputed Readings Log

1. **`demander` vs `demandé` (Token 18)**:
   - *Issue*: The manuscript text clearly reads `"je n'ai rien demander que de juste"`.
   - *Grammatical Analysis*: Following the finite auxiliary `ai` (Token 16), the standard compound past tense (*passé composé*) requires a past participle (*demandé*). Due to homophony in French phonology (both pronounced [dəmɑ̃de]), scribes regularly substituted the infinitive `-er` for the participle `-é`.
   - *Resolution*: Morphologically tagged as past participle functioning in the verb phrase; lemmatized under the canonical infinitive **`demander`**.

2. **Classification of `que` (Tokens 4, 13, 19)**:
   - *Issue*: Three distinct occurrences of the homograph `que` within the same sentence.
   - *Token 4 (`que`)*: Relative pronoun (`PRON`), referring back to antecedent *réponse*.
   - *Token 13 (`que`)*: Subordinating conjunction (`SCONJ`), introducing the subordinate complement clause governed by *répète*.
   - *Token 19 (`que`)*: Restrictive / exceptive marker (`ADV`). In the construction *ne ... rien que*, it functions adverbially to mean "seulement / si ce n'est" (TLFi: *Emploi adverbial restrictif*).

