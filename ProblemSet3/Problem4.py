# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import re
import os

path = '/Users/nivethida/PythonWorkouts/TextMining/ProblemSet3'
os.chdir(path)

def clean(doc):
    lowercase = [i.lower() for i in nltk.word_tokenize(doc) if i.lower() not in stop and i.isalpha()] # convert to lower case
    text1 = " ".join(lowercase)
    text_no_urls = re.sub(r'^https?:\/\/.[\r\n]', '', text1, flags=re.MULTILINE) #Remove all urls using regular expression.
    return text_no_urls

#Get a list of list of words
with open('text.csv','r') as f:
    contents = [clean(x) for x in f.readlines()]

sentiment_score =[]

#Perform Vadar sentiment analysis
for i in contents:
    review = TextBlob(i)        
    analyzer=SentimentIntensityAnalyzer()  # Analyzing the intensity of the bad review
    sent=analyzer.polarity_scores(review)
    sentiment_score.append(sent['compound']) # Compound score is sentiment
    
#To calculate pairwise opinion distance    
print(sentiment_score)



senti_score_len = len(sentiment_score)

abs_differnce = []

for i in sentiment_score[1:]:
    for j in sentiment_score[:-1]:
        abs_differnce.append(abs(i)-abs(j)) #finding the absolute difference
        
pairwise_opinion_distance = sum(abs_differnce)/len(abs_differnce) # diving by the length of pairs

print(pairwise_opinion_distance)
        













