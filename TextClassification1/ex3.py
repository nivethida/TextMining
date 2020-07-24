# -*- coding: utf-8 -*-

from nltk.corpus import brown
import nltk
import random
print(brown.tagged_words()[:10])
print(brown.tagged_sents()[:10])
print(brown.categories())
print(brown.tagged_sents(categories='adventure')[:10])

#version 1: no context
suffix = []
for i in brown.words():
    suffix.append(i[-1:])
    suffix.append(i[-2:])
    suffix.append(i[-3:])
frequency = nltk.FreqDist([x for x in suffix if x.isalpha()])
most_Common = [x for x,y in frequency.most_common(100)]  
print(most_Common)  

def feature(text):
    res = {}
    for i in most_Common:
        res[i] = text.endswith(i)
    return(res)    
#print(feature('times')) 

objectset = brown.tagged_words()[:5000]

featureset = [(feature(text),clas) for text,clas in  objectset]
random.shuffle(featureset)
trainingset = featureset[:4500]
testingset = featureset[4500:]

model1 = nltk.NaiveBayesClassifier.train(trainingset)
model2 = nltk.DecisionTreeClassifier.train(trainingset)
print(nltk.classify.accuracy(model1,testingset))
print(nltk.classify.accuracy(model2,testingset))
     
print(model1.classify(feature('table')))   
print(model1.classify(feature('tables'))) 
print(model2.classify(feature('table'))) 
print(model2.classify(feature('tables')))    
    
 














   