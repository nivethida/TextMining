import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
from gensim import corpora
import gensim
import re
import os

def clean(doc):
    lowercase = [i.lower() for i in nltk.word_tokenize(doc) if i.lower() not in stop and i.isalpha()] # step 2: convert to lower case
    normalized = [stemmer.stem(i) for i in lowercase] # step 5: stem the each words
    return normalized

#Get a list of list of words
with open('text.csv','r') as f:
    contents = [clean(x) for x in f.readlines()]

#print(contents)
#print(len(contents))
    
#Removing common topics
commonTopics = ['bitcoin', 'btc', 'price', 'market', 'year', 'time', 'think','would','like','go','people','get','see']
    
for content in contents:
    for  item in content:
        for topic in commonTopics :
            if item == topic:
                content.remove(item)    
print(contents)

#Dictionary    
dictionary = corpora.Dictionary(contents)
print(len(dictionary))

#Bag of words
doc_term_matrix=[dictionary.doc2bow(doc) for doc in contents]

#Training Lda model using 20 topics
Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(doc_term_matrix, num_topics=20, id2word = dictionary)
print(ldamodel.print_topics(num_topics=3, num_words=3))

#Generate Topic Distribution list
topic_distribuition_list=[]
for i in range(len(doc_term_matrix)):
    distribution=dict(ldamodel.get_document_topics(doc_term_matrix[i])) # note taht the distribution only show topics with loading, such as {0: 0.10538977, 7: 0.89361304}
    template_dict=dict.fromkeys(range(10),0) # we need to fill the missing toipcs in the distribution (missing because the loading is 0), this is to create a template of empty dictionary with all 0 values
    template_dict.update(distribution)
    topic_distribuition_list.append(template_dict)

#print(topic_distribuition_list)
print(ldamodel.get_document_topics(doc_term_matrix[0])) #Topic distribution of first post 

