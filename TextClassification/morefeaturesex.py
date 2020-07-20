# -*- coding: utf-8 -*-

#feature: the exsistence of the most common two consecutive letters.
#ly, er, en, es
#step 0: what are the most common two-consecutive letters

from nltk.corpus import names
import nltk
allname = names.words('male.txt')+names.words('female.txt')

#lily li il ly
#abbey ab bb be ey
# lily -> lily[:1] = lil
# lily -> lily[1:] = ily

print([(x,y) for x,y in zip('lily'[:-1],'lily'[1:])])

twoletters = [''.join([x,y]).lower() for name in allname for x,y in zip(name[:-1],name[1:])]

print(twoletters[:100])

twoletterfreq = nltk.FreqDist(twoletters)

#print(twoletterfreq.most_common(100))

common_twoletters = [x for x,y in twoletterfreq.most_common(100)]

print(common_twoletters)

#step 1 object set

objectset = [(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')]

random.shuffle(objectset)

#step 2 feature func
def feature(text):
    text = text.lower()
    res={}
    for i in common_twoletters:
        res[i] = i in text
    res['last_letter'] = text[-1]
    return res    

print(feature('anna'))

#step 3: define the feature set

featureset = [(feature(text), clas) for text , clas in objectset]

print(featureset[:3])


#step 4 testing and trainig divide












































































