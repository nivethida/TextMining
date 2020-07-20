# -*- coding: utf-8 -*-
corpus = [
        'This is the first document.',
        'This is the second document.',
        'And thisis the third one.',
        'Is this the first document?'
        ]
#tf term frequency
from sklearn.feature_extraction.text import CountVectorizer
calculator = CountVectorizer()
tf = calculator.fit_transform(corpus)

#dictionary
print(calculator.get_feature_names())

#term frequency
print(tf)
#(0, 8) 0 is the corpus location 1 is locaion of that word in dictionary

#TF-IDF
from  sklearn.feature_extraction.text import TfidfVectorizer
calculator2 = TfidfVectorizer()
tfidf = calculator2.fit_transform(corpus) 
print(tfidf)
print(tfidf[0,5])


























































































