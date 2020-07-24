# -*- coding: utf-8 -*-
from nltk.corpus import brown
import nltk
import random

tagged_sents = brown.tagged_sents(categories='news')
print(tagged_sents[0])

def feature(sentence,word):
    features={
            "suff1":sentence[word][-1:],
            "suff2":sentence[word][-2:],
            "suff3":sentence[word][-3:],
            "prev": "" if word==0 else sentence[word-1],
            "next": "" if word==len(sentence)-1 else sentence[word + 1]
            }
    return features
   

tagged_sents = brown.tagged_sents(categories='news')[:1000]
featuresets = []
for tagged_sent in tagged_sents:
    untagged_sent = nltk.tag.untag(tagged_sent)
    for i, (word, tag) in enumerate(tagged_sent):
        featuresets.append((feature(untagged_sent, i), tag))
print(featuresets[0])        
        
train = featuresets[100:]
test = featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train)
print(nltk.classify.accuracy(classifier, test))






























































