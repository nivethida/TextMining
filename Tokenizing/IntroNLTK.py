
sample_text = '''
Trump was born and raised in Queens, a borough of New York City, and received a bachelor's 
degree in economics from the Wharton School. He took charge of his family's real-estate business 
in 1971, renamed it The Trump Organization, and expanded its operations from Queens and Brooklyn 
into Manhattan. The company built or renovated skyscrapers, hotels, casinos, and golf courses. 
Trump later started various side ventures, mostly by licensing his name. 
He bought the Miss Universe brand of beauty pageants in 1996, and sold it in 2015. 
He produced and hosted The Apprentice, a reality television series, 
from 2003 to 2015. As of 2020, Forbes estimated his net worth to be $2.1 billion
'''

import nltk


# sentence tokenization
print(nltk.sent_tokenize(sample_text))

for i in nltk.sent_tokenize(sample_text):
    print(i, '\n')
    
    
# word tokenization

for i in nltk.sent_tokenize(sample_text):
    wordlist = nltk.word_tokenize(i)
    #print(wordlist)
    #num_words = len(wordlist)
    #print("no of words : ", num_words)
    num_chars = len(i)
    print("no of character: ", num_chars)
    # num_items = len(set(wordlist))
    # print("num of uniques: ", num_items)
    
    #num_items = list(set(wordlist)) # the sequence is rearranged
    #print("num of uniques: ", num_items)
    
    uniquelist = list(dict.fromkeys(wordlist))
    print(uniquelist)
      
    
    
import nltk

sample_text = '''
Trump was born and raised in Queens, a borough of New York City, and received a bachelor's 
degree in economics from the Wharton School. He took charge of his family's real-estate business 
in 1971, renamed it The Trump Organization, and expanded its operations from Queens and Brooklyn 
into Manhattan. The company built or renovated skyscrapers, hotels, casinos, and golf courses. 
Trump later started various side ventures, mostly by licensing his name. 
He bought the Miss Universe brand of beauty pageants in 1996, and sold it in 2015. 
He produced and hosted The Apprentice, a reality television series, 
from 2003 to 2015. As of 2020, Forbes estimated his net worth to be $2.1 billion
'''
# word frequency count

wordlist = nltk.word_tokenize(sample_text)

dict1 = dict.fromkeys(wordlist)

print(dict1)

for i in dict1.keys():
    dict1[i] = wordlist.count(i)
    
print(dict1)

#freqdist
frequency = nltk.FreqDist(wordlist)

#for i in frequency:
   # print(i, "->", frequency[i])


# sort the words from most frequent to least frequent

print(frequency.most_common()) # print a list of tuple [(word, freq)]

print(frequency.most_common(10))

# stop words appreas frequently .. only connects sentance but no meaning how to clean them


from nltk.corpus import stopwords

stopwords = stopwords.words('english')
print(stopwords)

# stopwords are context specific


sample_text = '''
Trump was born and raised in Queens, a borough of New York City, and received a bachelor's 
degree in economics from the Wharton School. He took charge of his family's real-estate business 
in 1971, renamed it The Trump Organization, and expanded its operations from Queens and Brooklyn 
into Manhattan. The company built or renovated skyscrapers, hotels, casinos, and golf courses. 
Trump later started various side ventures, mostly by licensing his name. 
He bought the Miss Universe brand of beauty pageants in 1996, and sold it in 2015. 
He produced and hosted The Apprentice, a reality television series, 
from 2003 to 2015. As of 2020, Forbes estimated his net worth to be $2.1 billion
'''

wordlist = nltk.word_tokenize(sample_text)
free_of_stopwords = [w for w in wordlist if w not in stopwords]
frequency = nltk.FreqDist(free_of_stopwords)

print(frequency.most_common(10))



wordlist = nltk.word_tokenize(sample_text)
free_of_stopwords = [w for w in wordlist if w.lower() not in stopwords]
frequency = nltk.FreqDist(free_of_stopwords)

print(frequency.most_common(10))


from nltk.corpus import stopwords
import string
stopwords = stopwords.words('english')
print(stopwords)
punc = string.punctuation

print(punc)

#punctuation
wordlist = nltk.word_tokenize(sample_text)
free_of_stopwords = [w for w in wordlist if w.lower() not in stopwords and w.lower() not in punc]
frequency = nltk.FreqDist(free_of_stopwords)
print(frequency[0])
print(frequency.most_common(10))

# years are removed
free_of_stopwords = [w.lower() for w in wordlist if w.lower() not in stopwords and w.isalpha()]
frequency = nltk.FreqDist(free_of_stopwords)
print(frequency.most_common(10))

# defining a cleaning function

def clean(text):
    wordlist=nltk.word_tokenize(text)
    result = [w.lower() for w in wordlist if w.lower() not in stopwords and w.isalpha()]
    res = ' '.join(result)
    return res


print(clean(sample_text))


# stemming
from nltk.stem import PorterStemmer
text1 = ["game","games","gamer","gaming"]
text2 = ["learn", "learning", "learned","learner","learns"]
text3 = ["program", "programs", "programer", "programing", "programers"]
alltext = text1+text2+text3
stemmer = PorterStemmer()
print([stemmer.stem(x) for x in text1])
print([stemmer.stem(x) for x in text2])
print([stemmer.stem(x) for x in text3])

from nltk.stem.snowball import SnowballStemmer


stemmer1 = PorterStemmer()
stemmer2 = SnowballStemmer('english')
stemmer3 = nltk.LancasterStemmer()
stemmer4 = nltk.WordNetLemmatizer()

print([stemmer1.stem(x) for x in alltext])
print([stemmer2.stem(x) for x in alltext])
print([stemmer3.stem(x) for x in alltext])
print([stemmer4.lemmatize(x) for x in alltext])


# part of speech tagging

input = 'time flies like a an arrow"

output = [('time', 'NN'), ('flies', 'VBZ'), ('like', 'in'),('an', 'DT'), ('arrow', 'NN')]
print([','.join(i[0] for i in output if i[1] == 'VBZ')])

#NN: table
#NNS: tables
#NNP: Smith, White House
#NNPS: PLURAL OF NNP

#VB: do
#VBZ: does
#VBD: did
#VBG: doing
#VBN: done

#impossible to transitions from one state to another


pos = nltk.pos_tag(wordlist)
print(pos) # output is list of tuple
# dont do stop word removal if you want POS
# usually we want to recognize preposition phase / verb phrase































    