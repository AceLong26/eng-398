import sys 
import spacy
nlp = spacy.load('fr_core_news_sm')  # or fr_core_news_sm
doc = nlp("Lettre à l'Assemblée Nationale.")

print(f"{'Token':12} {'Lemma':12} {'UPOS':8} {'Deprel':8}")
for token in doc:
    print(f"{token.text:12} {token.lemma_:12} {token.pos_:8} {token.dep_:8}")
