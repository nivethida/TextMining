# preparation
# dict.fromkeys
dct=dict.fromkeys(range(10),0) # generate an empty dictionary

import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
from gensim import corpora
import gensim
import re
import os
import statistics
import numpy as np

def clean(doc):
    lowercase=[i.lower() for i in nltk.word_tokenize(doc) if i.lower() not in stop and i.isalpha()] # step 2: convert to lower case
    normalized=[stemmer.stem(i) for i in lowercase] # step 5: stem the each words
    return normalized

path = '/Users/nivethida/PythonWorkouts/TextMining/ProblemSet3'
os.chdir(path)

# get the list of lists of word
with open('text.csv','r') as f:
    contents=[clean(x) for x in f.readlines()]

# get the dictionary
dictionary = corpora.Dictionary(contents)
print(len(dictionary))

# get the bag of word
doc_term_matrix=[dictionary.doc2bow(doc) for doc in contents]

# train the lda model using 10 topics
import gensim
Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(doc_term_matrix, num_topics=10, id2word = dictionary)

print(ldamodel)

# generate the topic distribution for all documents
topic_distribuition_list=[]
for i in range(len(doc_term_matrix)):
    distribution=dict(ldamodel.get_document_topics(doc_term_matrix[i])) # note taht the distribution only show topics with loading, such as {0: 0.10538977, 7: 0.89361304}
    template_dict=dict.fromkeys(range(10),0) # we need to fill the missing toipcs in the distribution (missing because the loading is 0), this is to create a template of empty dictionary with all 0 values
    template_dict.update(distribution)
    topic_distribuition_list.append(template_dict)

print(topic_distribuition_list)

#pairwise topic similarity

def cossimilarity(x,y):
    value1=np.dot(x,y)
    xm=np.sqrt(sum([i**2 for i in x]))
    ym=np.sqrt(sum([i**2 for i in y]))
    value2=xm*ym
    cs=value1/value2
    return cs

cslist=[]
for i in range(len(topic_distribuition_list)-1):
    for j in range(i,len(topic_distribuition_list)): # remember, this is how to iterate pairwise. You can use itertool though.
        disi=list(topic_distribuition_list[i].values()) # the dict.values() returns a dict_values class variable, we need to convert it to list, otherwise we cannot do dot product.
        disj=list(topic_distribuition_list[j].values())
        cslist.append(cossimilarity(disi,disj))
print(cslist)
print(statistics.mean(cslist))








































