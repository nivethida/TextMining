# -*- coding: utf-8 -*-
import nltk
import random
from nltk.corpus import names
import os
path = '/Users/nivethida/PythonWorkouts/TextMining/ProblemSet3'
os.chdir(path)
import re


# List of neutral names is taken from git https://github.com/fivethirtyeight/data/blob/master/unisex-names/unisex_names_table.csv
# The data was in the form of txt 

maleNames = names.words('male.txt')
femaleNames = names.words('female.txt')

unisexNames = []

with open('unisexNames.txt','r') as f:
    unisexNames = f.read().splitlines()    
    
maleNames = names.words('male.txt')
femaleNames = names.words('female.txt')

#Checking the length of male and female names before removing unisex names

#print(len(maleNames))
#print(len(femaleNames)) 

maleNames = [name for name in maleNames if name not in unisexNames ]    
femaleNames = [name for name in femaleNames if name not in unisexNames ]                  

#Checking the length of male and female names before removing unisex names   
#print(len(maleNames))
#print(len(femaleNames)) 

#objectset  
    
allnames = [(name, 'female') for name in femaleNames] + [(name, 'male') for name in maleNames] + [(name, 'unisex') for name in unisexNames]
random.shuffle(allnames)

# feature function

def feature(text):
    if re.search('(\w){2}', text):
        return {'consecutive': True, 'last_letter': text[-1], 'second_last_letter': text[-2]}
    else:
        return {'consecutive': False, 'last_letter': text[-1], 'second_last_letter': text[-2]}
        

featureSet = [(feature(text), clas) for text, clas in allnames]

trainLen = int(0.90*len(featureSet))

train = featureSet[:trainLen]
test = featureSet[trainLen:]


classifier = nltk.NaiveBayesClassifier.train(train)

print(classifier.classify(feature('Joey')))
    
correct_prediction=0 
total_prediction=0 
for i in test:
    total_prediction+=1
    feature=i[0]
    g=i[1]
    if classifier.classify(feature)==g:
        correct_prediction+=1
print('Accuracy: ',correct_prediction/total_prediction)











