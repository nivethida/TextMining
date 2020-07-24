# -*- coding: utf-8 -*-
import nltk

#step 1
semanticData = [('I love this sandwich.', 'pos'),
('This is an amazing place.', 'pos'),
('I feel very good about these beers.', 'pos'),
('This is my best work.', 'pos'),
("What an awful view!", 'neg'),
('I do not like this restaurant!', 'neg'),
('I am tired of this stuff.', 'neg'),
("I can't deal with this", 'neg'),
('He is my sworn enemy!', 'neg'),
('My boss is horrible!', 'neg')]

#step 2 Feature function
def feature(text):
    if text[-1] == '!':
        return {'sentiment' : 'Negative'}
    else:
        return {'sentiment' : 'positive'}
    
featureSet = [(feature(text), clas) for text, clas in semanticData]    
print(featureSet)

#Seperate traina and test data
train = featureSet[:-2]

#train the data
classifier = nltk.NaiveBayesClassifier.train(train)

print("Rating: ",classifier.classify(feature('I hate the product!')))
















     