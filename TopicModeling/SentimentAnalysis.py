# -*- coding: utf-8 -*-
from textblob import TextBlob
#text = 'the final exam is cumulative and optional'
#blob = TextBlob(text)
#print(blob.tags)

text1 = 'the pandemic is the worst I have seen.'
text2 = 'the economy recovery seems fast'

blob1 = TextBlob(text1)
blob2 = TextBlob(text2)

sent1 = blob1.sentiment
sent2 = blob2.sentiment

print(sent1)
print(sent2)

#polarity ranges from -1 (most negative)to 1 (most positive)
#subjectivity is between 0(most objective to 1 (most subjective)
#subjectivity based on opinion
#objective based on facts

#print(blob1.sentiment.polarity)
#print(blob1.sentiment.subjectivity)

import os
path = '/Users/nivethida/PythonWorkouts/TextMining/Day8'
os.chdir(path)
with open('pos.txt','r') as f:
    reviews = [x.strip('\n').lower() for x in f.readlines() ]



def accuracy(cutoff):
    
num_attempt = 0
num_correct = 0

for i in reviews:
blob = TextBlob(i)
if blob.sentiment.subjectivity > 0.8:
num_attempt+=1
if blob.sentiment.polarity >= cutoff:    
num_correct+=1   


with open('neg.txt','r') as f:
reviews = [x.strip('\n').lower() for x in f.readlines()]

num_attempt = 0
num_correct = 0

for i in reviews:
   
blob = TextBlob(i)
if blob.sentiment.subjectivity > 0.8:
num_attempt+=1
if blob.sentiment.polarity < cutoff:    
num_correct+=1       

return num_correct/num_attempt   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    