import nltk
from nltk.corpus import movie_reviews
import random
# step 1 object set
reviews=[(movie_reviews.words(reviewid), clas)
for clas in ['pos','neg']
for reviewid in movie_reviews.fileids(clas)
]

# step 1.5 get the most common 100 JJs
sample=random.sample(reviews,200)
pos=[nltk.pos_tag(x) for x,y in sample]

jjlist=[]
for i in pos:
    jj=[x[0] for x in i if "JJ" in x[1] and len(x[0])>=3 and x[0].isalpha()]
    jjlist+=jj

frequency=nltk.FreqDist(jjlist)
common_jj=[x for x,y in frequency.most_common(100)]

# step2 feature function
def feature(text):
    res={}
    for i in common_jj:
        res[i]=i in set([x.lower() for x in text])
    return res

#step 3 generate the feature set
featureset=[(feature(text),clas) for text, clas in reviews]
featureset=featureset[:100]
# step 4, train/test divide
random.shuffle(featureset)
num_review=len(featureset)
train_count=int(0.9*num_review)
trainingset=featureset[:train_count]
testingset=featureset[train_count:]

# step 5, training and model evaluation
model=nlt

#No pickle package for exam
