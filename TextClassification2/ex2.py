# -*- coding: utf-8 -*-

#goal 1: use many other classifiers to do classification
#goal 2:show how to test the value of feature rigorously
import nltk
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
# BernoulliNB works for binary values
# MultinommialNB works with features of discrete values
# for continuos gaussian - default one is used
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.corpus import names
import random
import statistics
from scipy import stats

#object set is [()] list of tuples
allnames = [(name, "male") for name in names.words("male.txt")]+[(name, "female") for name in names.words("female.txt")]

#feature function
def feature1(text):
    return {'last_letter':text[-1]}

#define additional testing feature
def feature2(text):
    return {'last_letter':text[-1], 'first_letter':text[0]}    


featureset1 = [(feature1(name), clas) for name,clas in allnames]
featureset2 = [(feature2(name), clas) for name,clas in allnames]

trainsize = int(0.8*len(featureset1))

#define classifier objects
BNB = SklearnClassifier(BernoulliNB())
MNB = SklearnClassifier(MultinomialNB())
L1 = SklearnClassifier(LogisticRegression(solver='newton-cg'))
L2 = SklearnClassifier(LogisticRegression(solver='liblinear'))
SVC = SklearnClassifier(SVC())
LSVC = SklearnClassifier(LinearSVC())
NuSVC = SklearnClassifier(NuSVC())

#define accuracy

def accuracy(featureset):
    accuracy = []
    for i in range(10):
        print(i)
        random.shuffle(featureset)
        train=featureset[:trainsize]
        test = featureset[trainsize:]
        nltkNB = nltk.NaiveBayesClassifier.train(train)
        nltkDT = nltk.DecisionTreeClassifier.train(train)
        BNB.train(train);MNB.train(train);L1.train(train);L2.train(train)
        SVC.train(train);LSVC.train(train);NuSVC.train(train)
        #we report accuracy using list of tuple
        #each tuple represents each iteration
        #[(acc1,acc2...acc9),(acc1,acc2...acc9),...]
        acc1 = nltk.classify.accuracy(nltkNB,test)
        acc2 = nltk.classify.accuracy(nltkDT,test)
        acc3 = nltk.classify.accuracy(BNB,test)
        acc4 = nltk.classify.accuracy(MNB,test)
        acc5 = nltk.classify.accuracy(L1,test)
        acc6 = nltk.classify.accuracy(L2,test)
        acc7 = nltk.classify.accuracy(SVC,test)
        acc8 = nltk.classify.accuracy(LSVC,test)
        acc9 = nltk.classify.accuracy(NuSVC,test)
        accuracy.append((acc1,acc2,acc3,acc4,acc5,acc6,acc7,acc8,acc9))
    print([statistics.mean(x) for x in accuracy])    
    return accuracy   
       

#print(accuracy(featureset1))        

accuracy_baseline = accuracy(featureset1)
 
accuracy_testing = accuracy(featureset2)

# draww inference on if the added feature statistically improve the prediction

for i in range(9):
    acc_baseline=[x[i] for x in accuracy_baseline]
    acc_testing=[x[i] for x in accuracy_testing]
    ttest = stats.ttest_ind(acc_baseline,acc_testing,equal_var=False)
    print(ttest)





    
    
    
    
    
    
    
    