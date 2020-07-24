# -*- coding: utf-8 -*-

corpus = [
        'This is the first document.',
        'This is the second document.',
        'And thisis the third one.',
        'Is this the first document?'
        ]

import nltk
from nltk.corpus import movie_reviews
import random
# step 1 object set
reviews=[(movie_reviews.words(reviewid), clas)
for clas in ['pos','neg']
for reviewid in movie_reviews.fileids(clas)
]

# step 2 feature function
# features <- existence of the top 3000 most common words in all reviews
allwords=[x.lower() for x in movie_reviews.words() if x.isalpha()]
frequency=nltk.FreqDist(allwords)
most_common=[x for x,y in frequency.most_common(3000)]

def feature(text): # the text is a list of words
    res={}
    text=set(text)
    for i in most_common:
        res[i]=i in text
    return res

#step 3 generate the feature set
featureset=[(feature(text),clas) for text, clas in reviews]

# step 4, train/test divide
random.shuffle(featureset)
num_review=len(featureset)
train_count=int(0.9*num_review)
trainingset=featureset[:train_count]
testingset=featureset[train_count:]

# step 5, training and model evaluation
model=nltk.NaiveBayesClassifier.train(trainingset)
print(nltk.classify.accuracy(model,testingset))
model.show_most_informative_features(20)






