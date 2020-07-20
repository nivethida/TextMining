# -*- coding: utf-8 -*-

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

text1 = 'the pandemic is the worst i have seen'
text2 = 'the economy recovery is fast.'

sent1 = analyzer.polarity_scores(text1) 
sent2 = analyzer.polarity_scores(text2) 

print(sent1)
print(sent2)

print(sent1['neg'])
print(sent1['compound'])

pos_attempt = 0
pos_correct = 0

neg_attempt = 0
neg_correct = 0


with open('pos.txt','r') as f:
    review=[x.strip('\n').lower() for x in f.readlines()]
    
for i in review:
    sentimentdict = analyzer.polarity_scores(i)
    if sentimentdict['neg'] < 0.1:
        pos_attempt+=1
        if sentimentdict['pos']-sentimentdict['neg']>0:
            pos_correct+=1
            
print(pos_correct/pos_attempt)            























    