::# -*- coding: utf-8 -*-

x = [(i,j) for i in range(5) for j in range (4)]
print(x)

#[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3)]

values = [1,2,3,4]
keys = ['key1', 'key2','key3','key4']

dict1 = {'{}'.format(x):y for x,y in zip(keys,values)}
print(dict1)

#{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}

#step 1, come up with the object set 
#objectset = [(text, class), (text,class)....(text,class)]

#step 2 , come up with the feature function
# def feature(text) -> features as dictionary
# 'times' -> {'first_letter':'t','last_letter':'s'}

#step 3, convert the object set to feature set using feature function
#feature set =  [({dict1}, class), ({dict2},class)....({dictn},class)]

#step4 randomly generate training and testing set 80/20 or 90/10

#step 5, train the model and testing the accuracy


from nltk.corpus import names
import random
print(names.words('male.txt')[:10])
print(names.words('female.txt')[:10])

#step 1, come up with the object set 
male = [(text,'male') for text in names.words('male.txt')]
female = [(text,'female') for text in names.words('female.txt')]

allnames = male+female
random.shuffle(allnames)
print(allnames[:100])# all male names comes first while traing 80% all male names comes first

# step 2, come up with the feature function
def feature(text):
    return {'last_letter':text[-1]}

#step 3, convert the object set to feature set using feature function
featureset = [(feature(text),clas) for text, clas in allnames[:500]]    

print(featureset[:3])

#[({'last_letter': 'n'}, 'male'), ({'last_letter': 'e'}, 'female'), ({'last_letter': 'r'}, 'female')]

#step4 randomly generate training and testing set 80/20 or 90/10
trainingset= featureset[:400] # allnames has only 500, so 400 is 80%
testingset = featureset[400:] # last 100 is testing

#step 5, train the model and testing the accurac
model = nltk.NaiveBayesClassifier.train(trainingset)

print(model.classify(feature('peng'))) #the input to the classify 

#accuracy
num_correct = 0
num_attempt = 0
true_class = []
predicted_class = []

for i in testingset:
    num_attempt+=1
    true_class.append(i[1])
    predicted_class.append(model.classify(i[0]))
    num_correct+=(1 if predicted_class == true_class  else 0)
    
print(num_correct/num_attempt)    
    
print(true_class[:10])
print(predicted_class[:10])
#check the confusion table

import pandas as pd

true=pd.Series(true_class, name='True Gender')
predicted=pd.Series(predicted_class,name = "Predicted Gender")

print(pd.crosstab(true,predicted))

#task: predict if a name is female name ?
#precision and recall and f1_score
#precision is tp/(tp+fp)
#tp: actual is female, predicted as female
#fp: actual male, predicted as female
#fn: actual female, predicted as male
#precision is tp/(tp+fp) -> among all predicted positives 
#recall is tp/(tp+fn) -> among all actual positives, how many are
#f1_score is the average of precision and recall. f1=1/precision+1/recall


import sklearn
true_class = [1 if x=="female" else 0 for x in true_class]
predicted_class=[1 if x=="female" else 0 for x in predicted_class]
print(sklearn.metrics.precision_score(true_class, predicted_class))
print(sklearn.metrics.recall_score(true_class, predicted_class))
print(sklearn.metrics.f1_score(true_class, predicted_class))





























