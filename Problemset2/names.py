# -*- coding: utf-8 -*-
import nltk
import random
from nltk.corpus import names

allnames = [(name, 'female') for name in names.words('female.txt')]+[(name, 'male') for name in names.words('male.txt')]
random.shuffle(allnames)

def feature(text):
    return {'last_letter': text[-1], 'second_last_letter': text[-2]}

featureSet = [(feature(text), clas) for text, clas in allnames]

train = featureSet[:500]
test = featureSet[500:1000]

classifier = nltk.NaiveBayesClassifier.train(train)

print(classifier.classify(feature('nivi')))
    
correct_prediction=0 
total_prediction=0 
for i in test:
    total_prediction+=1
    feature=i[0]
    g=i[1]
    if classifier.classify(feature)==g:
        correct_prediction+=1
print('Accuracy: ',correct_prediction/total_prediction)

