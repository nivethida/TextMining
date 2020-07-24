# -*- coding: utf-8 -*-
import os
path = '/Users/nivethida/PythonWorkouts/TextMining/ProblemSet3'
os.chdir(path)
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk

analyzer = SentimentIntensityAnalyzer()

negWords = []
post = []
ids = 0

with open('negative-words.txt', 'r', encoding = "ISO-8859-1") as f:
    negWords = f.read().splitlines() #list of all neg words
    
def calculateNeg(text):
    allwords = nltk.word_tokenize(text)
    wordCount = 0
    for i in negWords:
        wordCount += text.count(i)
    return wordCount/len(allwords)  #Calculating negative Loughran score
    
results = open('results.txt', 'w+')  

header = 'ID'+','+'Polarity textblob'+','+'neg_vader'+','+'pos_vader'+','+'compound_vader'+','+'Neg_Loughran'+'\n'

results.write(header)


with open('Post.txt', 'r') as f:
        post = f.readlines()  
        post = [i.strip('\n').lower() for i in post] # list of words in post
        for word in post:
            blob = TextBlob(word)
            polarity = blob.sentiment.polarity
            negVader = analyzer.polarity_scores(word)['neg']
            posVader = analyzer.polarity_scores(word)['pos']
            compVader = analyzer.polarity_scores(word)['compound']
            ids += 1
            negLoughran = calculateNeg(word)
            result = str(ids)+','+str(polarity)+','+str(negVader)+','+str(posVader)+','+str(compVader)+','+str(negLoughran)+'\n'
            results.write(result)
            
            
results.close()            
            
            
            
            
            
            
            
            
            