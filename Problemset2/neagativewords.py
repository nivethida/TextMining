# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import movie_reviews
import random

negativeWords = []
with open('negative_context.txt', 'r') as f:
    for i in f.readlines():
        negativeWords.append(i.strip('\n'))

negativeWords = [i.lower() for i in negativeWords]        
        
print(negativeWords[:10])  
     
objectSet = [(movie_reviews.words(fileid),cat) for cat in movie_reviews.categories() for fileid in movie_reviews.fileids(cat)]
random.shuffle(objectSet)   

def feature(text): 
      words = [i.lower() for i in text]
      words = set(words)
      result = {}
      for i in negativeWords:
          result[i] = i in words
      return result    

featureSet = [(feature(text), clas) for text,clas in objectSet]

print(featureSet[:1])

trainLen = int(0.80*len(featureSet))

train = featureSet[:trainLen]
test = featureSet[trainLen:]

classifier = nltk.NaiveBayesClassifier.train(train)

print("Accuracy: ",nltk.classify.accuracy(classifier,test))
classifier.show_most_informative_features(15)











