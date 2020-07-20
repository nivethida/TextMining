# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()

doc1 = "Sugar is bad to consume. My sister likes to have sugar, but not my father."
doc2 = "My father spends a lot of time driving my sister around to dance practice."
doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
doc4 = "Sometimes I feel pressure to perform well at school, but my father never seems to drive my sister to do better."
doc5 = "Health experts say that Sugar is not good for your lifestyle."

doc = [doc1,doc2,doc3,doc4,doc5]

def clean(doc): #text is a string
    lowercase=[i.lower() for i in nltk.word_tokenize(doc) if i.lower() not in stop and i.isalpha()] # step 2: convert to lower case
    stem=[stemmer.stem(i) for i in lowercase] # step 5: stem the each words
    return stem


cleaned = [clean(x) for x in doc]

#step2 generate the doctionary

#import sys