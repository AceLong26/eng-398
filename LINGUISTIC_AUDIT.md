| # | Word | Dictionary lemma | UPOS | spaCy lemma | spaCy UPOS | AI lemma | AI UPOS |
|---:|---|---|---|---|---|---|---|---|
| 1 | `J'` | `je` | `PRON` | `je` | `PRON` | `je` | `PRON` | M 
| 2 | `ai` | `avoir` | `AUX` | `avoir` | `AUX` | `avoir` | `AUX` | M 
| 3 | `chargé` | `charger` | `VERB` | `charger` | `VERB` | `charger` | `VERB` | M 
| 4 | `le` | `le` | `DET` | `le` | `DET` | `le` | `DET` | M 
| 5 | `Ministre` | `ministre` | `NOUN` | `ministre` | `NOUN` | `ministre` | `NOUN` | M 
| 6 | `de` | `de` | `ADP` | `de` | `ADP` | `des` | `ADP` | M
| 7 | `affaires` | `affaire` | `NOUN` | `affaire` | `NOUN` | `affaire` | `NOUN` | M 
| 8 | `étrangères` | `étranger` | `ADJ` | `étranger` | `ADJ` | `étranger` | `ADJ` | M
| 9 | `Messieurs` | `messieurs` | `NOUN` | `monsieur` | `NOUN` | `monsieur` | `NOUN` | M 
| 10 | `de` | `de` | `ADP` | `de` | `ADP` | `de` | `ADP` | M 

The hand-writen anaysis remains correct in addition to spacy and ai rendering are almost the same withing each these set of words. The origanal writing has remained. the only issue that is prevelent in this sample is in line 6 where the AI has over-normalized the phrase 'de' and changed it to 'des' as it does not have prier context from within the sentence. It has been seen that in addition to over-normalization of certain words, Spacy and Ai struggle to understand how to read endings with -oit as it is not something modern french uses.