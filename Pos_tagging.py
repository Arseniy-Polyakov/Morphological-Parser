#Importing libraries for nlp and working with frameworks
import spacy
import nltk 
from nltk import word_tokenize 
import numpy as np
import pandas as pd

#Opening the file
with open ("Corpus sentences.txt", "r") as file:
    file = file.read()

#Pre-processsing proper   
sentences = nltk.sent_tokenize(file)
sentences_in_string = "\n".join(map(str,(sentences)))
tokens = nltk.word_tokenize(sentences_in_string)
tokens_in_string = "\n".join(map(str,(tokens)))

#POS-tagging proper
nlp = spacy.load("ru_core_news_md")
document = nlp(file)
pos_list = []
for token in document:
    pos_list.append(token.pos_)

#Adding output in dataframe 
dataframe = pd.DataFrame({"upos": pos_list})
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)

#Sending dataframe to excel
writer = pd.ExcelWriter("upos.xlsx")
dataframe.to_excel(writer)
writer.save()

