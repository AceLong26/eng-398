# Sentence Alignment

| # | Source (`alignment_manual_copy.xml`) | Target (`target_translation.xml`) | Manual | AI | Differ? | Kept Decision & Reason |
|:---:|---|---|:---:|:---:|:---:|---|
| **1** | **`s1`**: À l'Assemblée Nationale. | **`t1`**: To the National Assembly | `s1` - `t1` | `s1` - `t1` | No | Keep `s1` - `t1` |
| **2** | **`s2`**: 31 décembre 1791 | **`t2`**: 31 December 1791 | `s2` - `t2` | `s2` - `t2` | No | Keep `s2` - `t2` |
| **3** | **`s3`**: J'ai chargé le Ministre des affaires étrangères... | **`t3`**: I have instructed the minister of external affairs... | `s3` - `t3` | `s3` - `t3` | No | Keep `s3` - `t3` |
| **4** | **`s4`**: Cet office je dois le dire... | **`t4`**: This service have to say... | `s4` - `t4` | `s4` - `t4` | No | Keep `s4` - `t4` |
| **5** | **`s5`**: J'avais droit à compter sur les sentiments... | **`t5`**: I had the right to count... | `s5` - `t5` | `s5` - `t5` | No | Keep `s5` - `t5` |
| **6** | **`s6`**: je ne peux pas croire encore... | **`t6`**: I like to persuade myself... | `s6` - `t6` | `s6` (partial) | **Yes** | Keep `s6` - `t6` (target omits first clause) |
| **7** | **`s7`**: Dans la réponse que je fais à l'Empereur... | **`t7`**: So, the response that i made... | `s7` - `t7` | `s7` - `t7` | No | Keep `s7` - `t7` |
| **8** | **`s8`**: je lui rappelle le soin... | *[Untranslated]* | `s8` - none | `s8` - `t7` | **Yes** | Keep unaligned (translation ends at `t7`) |
| **9** | **`s9`**: Enfin je lui renouvelle le vœu... | *[Untranslated]* | `s9` - none | `s9` - `t7` | **Yes** | Keep unaligned (translation ends at `t7`) |
| **10** | **`s10`**: mais en même temps je lui déclare... | *[Untranslated]* | `s10` - none | `s10` - `t7` | **Yes** | Keep unaligned (translation ends at `t7`) |

---

### Summary
- **Agreed**: 1–5, 7
- **Divergences**:
  - `s6`: Target omits opening clause; kept 1:1.
  - `s8`–`s10`: Untranslated; kept unaligned.

---

### Four-Line Leipzig Gloss (`s4` - `t4`)

1. **Diplomatic Manuscript**:
   > Cet office je dois le dire , m' a cause le plus grand etonnement .
2. **Normalized Transcription**:
   > Cet office je dois le dire , m' a causé le plus grand étonnement .
3. **Morpheme-by-Morpheme Gloss**:
   > `DEM.M.SG` `dispatch.M.SG` `1SG.NOM` `must.PRS.1SG` `3SG.M.ACC` `say.INF` , `1SG.DAT` `have.PRS.3SG` `cause.PSTP` `DEF.M.SG` `SUP` `great.M.SG` `astonishment.M.SG` .
4. **Free Translation**:
   > "This dispatch, I must say, has caused me the greatest astonishment."

---

### Reflection

Aligning early modern diplomatic French with a contemporary English translation exposes fundamental differences between automated machine pairing and human philological curation. Automated sequence models rely heavily on sentence length, lexical frequency, and standard terminal punctuation. When alignment is strictly one-to-one, automated tools perform reliably across declarative units like heading and date designations (`s1`, `s2`) or balanced complex periods (`s3`–`s5`). However, significant divergences emerge when historical texts deviate from rigid parallel structures.

In sentence `s6`, the English translator omitted Louis XVI’s introductory diplomatic hedge (*"je ne peux pas croire encore que ses dispositions soient changées"*), jumping directly to the declarative complement (*"I like to persuade myself..."*). While an automated system struggled with the asymmetric length and flagged a partial alignment defect, human curation recognizes rhetorical condensation and maintains the sentence-level bond to preserve discursive context. 

More crucially, the automated model failed when handling textual truncation. Because the target translation file concludes at sentence `t7`, the AI attempted to force the remaining source sentences (`s8`–`s10`)—detailing the Brabant troop movements, the peace appeal, and the royal ultimatum—into the final available target block. Human oversight correctly recognized that the source document continues beyond the target translation, establishing unaligned null values rather than introducing false linkages. Manual alignment paired with structured standoff markup thus ensures that linguistic omissions and asymmetrical manuscript boundaries are accurately represented without distorting historical translation data.
