# Sentence Alignment


| Source | Target | Manual | AI | Final |
|---|---|---|---|---|
| `s1`: À l'Assemblée Nationale. | `t1`: To the National Assembly | `s1` - `t1` | `s1` - `t1` | `s1` - `t1` |
| `s2`: 31 décembre 1791 | `t2`: 31 December 1791 | `s2` - `t2` | `s2` - `t2` | `s2` - `t2` |
| `s3`: J'ai chargé le Ministre des affaires étrangères... | `t3`: I have instructed the minister of external affairs... | `s3` - `t3` | `s3` - `t3` | `s3` - `t3` |
| `s4`: Cet office je dois le dire... | `t4`: This service have to say... | `s4` - `t4` | `s4` - `t4` | `s4` - `t4` |
| `s5`: J'avais droit à compter sur les sentiments... | `t5`: I had the right to count... | `s5` - `t5` | `s5` - `t5` | `s5` - `t5` |
| `s6`: je ne peux pas croire encore... j'aime me persuader... | `t6`: I like to persuade myself... | `s6` - `t6` | `s6` - `t6` | `s6` - `t6` |
| `s7`: Dans la réponse que je fais à l'Empereur... | `t7`: So, the response that i made... | `s7` - `t7` | `s7` - `t7` | `s7` - `t7` |
| `s8`: je lui rappelle le soin... | Untranslated | `s8` - none | `s8` - none | `s8` - none |
| `s9`: Enfin je lui renouvelle le vœu... | Untranslated | `s9` - none | `s9` - none | `s9` - none |
| `s10`: mais en même temps je lui déclare... | Untranslated | `s10` - none | `s10` - none | `s10` - none |

## Summary

- **Linked:** `s1`–`s7` each align to `t1`–`t7`.
- **Partial:** `s6` aligns to `t6`, but the English translation omits the opening
  clause beginning “je ne peux pas croire encore.”
- **Untranslated:** `s8`–`s10` have no target sentence and remain unaligned.


In s6, the English translation leaves out Louis XVI’s opening diplomatic phrase (“je ne peux pas croire encore que ses dispositions soient changées”) and begins with “I like to persuade myself...” The automated tool flagged the mismatch, while human editors recognized it as a shortened translation and kept the sentences linked to preserve the context.
