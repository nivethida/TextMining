# -*- coding: utf-8 -*-
import nltk
import math
corpus = [
        'This is the first document.',
        'This document is the second document.',
        'And this is the third one.',
        'Is this the first document?'
        ]
def findTF(index):
    sent = corpus[index]
    words = nltk.word_tokenize(sent)
    words = [x.lower() for x in words]
    wordLength =len(words)
    wordCount = {}
    result = {}
    for i in words:
        wordCount[i] = wordCount.get(i, 0)+1
    for i in wordCount:
        result[i] = wordCount.get(i)/wordLength
    return result    
print("TF values: ", findTF(0))   


def findIDF(index):
    idfDict = {}
    sent = corpus[index] # each sentence in the corpus
    words = nltk.word_tokenize(sent)
    words = [x.lower() for x in words]
    wordsCount= dict.fromkeys(words , 0) # will contain the count of words occuring in the corpus
    for j in corpus:
        sents = nltk.word_tokenize(j)
        sents = [x.lower() for x in sents]
        for i in words:
            if i in sents:
               wordsCount[i] += 1  
    print(wordsCount)           
    for word in wordsCount:
        idfDict[word] = math.log(len(corpus)/wordsCount[word]) #caculating idf
    return idfDict     
   
def findTFIDF(tf,idf):
    tfidf = {}
    for i,val in tf.items():
        tfidf[i] = val*idf[i]
    return tfidf

print("TFIDF Values: ",findTFIDF(findTF(3),findIDF(3)))  # passing both tf and idf values as arguments
    

