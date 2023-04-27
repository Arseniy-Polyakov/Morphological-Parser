#Importing NLTK libraries
import nltk
from nltk import sent_tokenize, word_tokenize

#Importing pandas library for data analytics
import pandas as pd

#Opening primary file
with open ("Corpus sentences.txt", "r") as file:
    file=file.read()

#Pre-processing
sentences = nltk.sent_tokenize(file)
sentences_in_string = "\n".join(map(str,(sentences)))
tokens = nltk.word_tokenize(sentences_in_string)
tokens_in_string = "\n".join(map(str,(tokens)))

#Adding results in pandas dataframe 
Dataframe = pd.DataFrame({"tokens": tokens})
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)

#Sending dataframe to excel file
writer = pd.ExcelWriter("tokenization.xlsx")
Dataframe.to_excel(writer)
writer.save()

