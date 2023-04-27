# Importing NLP libraries for pre-processing and morphological analysis
import nltk 
from nltk import sent_tokenize, word_tokenize 
import pymorphy2
import spacy

#Importing Pandas library for data analysis
import pandas as pd

# Opening file with examples from oral corpora 
with open ("Corpora sentences.txt", "r") as file_of_corpora_examples:
    file_of_corpora_examples = file_of_corpora_examples.read()

# Pre-processing proper. The former step is dividing text into separate sentences. The latter one is dividing into tokens
sentences = nltk.sent_tokenize(file_of_corpora_examples)
sentences_in_string = "".join(map(str,(sentences)))
tokens = nltk.word_tokenize(sentences_in_string)
tokens_in_string = "".join(map(str,(tokens)))

#Lemmatization function
morph = pymorphy2.MorphAnalyzer()
def Lemmatizer(sentences_in_string):
    tokens = word_tokenize(sentences_in_string)
    lemmas = list()
    for token in tokens_in_string:
        p = morph.parse(token)[0]
        lemmas.append(p.normal_form)
    return lemmas

#Part-of-speech tagging
nlp = spacy.load("ru_core_news_md")
document = nlp(tokens_in_string)
upos = []
for token in document:
    upos.append(token.pos_)

#Morphological analysis, finding grammatical feats
feats = morph.parse(tokens_in_string)

#Creating a dataframe and filling it
data = [feats]
df = pd.DataFrame(data)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
print (df)
'''
#Printing all results together
print (tokens)
print ("\n".join(Lemmatizer(sentences)))
print ("\n".join(upos))
print (feats) 
'''