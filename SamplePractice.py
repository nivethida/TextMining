# -*- coding: utf-8 -*-

text="this is our first exam, it is going to be easy."
#Run the following code, we are going to get a ____ with ___ elements.

import nltk
words = nltk.word_tokenize(text)
print(len(words))

text ='''By design, a blockchain is resistant to modification of the data.
It is "an open, distributed ledger that can record transactions
between two parties efficiently".[7]
For use as a distributed ledger, a blockchain is typically managed by a
peer-to-peer network collectively adhering to a protocol for inter-node
communication and validating new blocks. Once recorded, the data in any
given block cannot be altered retroactively without alteration of all
blocks, which requires consensus of the network majority.
Although blockchain records are not unalterable, blockchains is the key for 
secured transactions, and expedited varifications. However,
the Bitcoin payment network is
an unregulated network, which is always criticized for illegal transactions
'''
import nltk
words = nltk.word_tokenize(text)
print(words)
tokens = nltk.FreqDist(words)
most_comm = tokens.most_common(5)
print(most_comm)
most_comm_words = [words[0] for words in most_comm]
print(most_comm_words)


import re
import nltk
text = 'abandoned, abandon, help, abraised, open'
wordlist = nltk.word_tokenize(text)
for w in wordlist:
    if w == re.match('\bab\w+', w):
        print(w)

import re
import nltk
text = 'abandoned, abandon, help, abraised, open'
for i in text:
    res = re.findall(r'\bab\w+', text)
    print(res)

#https://stackoverflow.com/questions/16440267/how-to-find-a-word-that-starts-with-a-specific-character

chat_words = ['aaople', '87483','1313','ada', 'shdewjhf']
p=[w for w in chat_words if re.search('^[0-9]{4,}$', w)!=None]

print(p)


from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
word = ["game","gaming","games","gamed"]
for word in word:
    print(stemmer.stem(word))


text="BAN671 Data Analytics 38 BAN675 Text Mining 35"

result = re.findall('\s[0-9]{2}', text)
print(result)


import nltk
import re
chat_words = nltk.corpus.nps_chat.words()
chat_words = set(w for w in chat_words)
chat_words = ['n','Nono','Noooo','ooooNo']
x = [w for w in chat_words if re.search('^[Nn]+[Nnoo]+$',w)!=None]
print(x)


import nltk
import re
chat_word = "said"
x = re.search('^..[ilj][bcd]',chat_word)
print(x)


def patterns(word):
    x = re.search('^[a-z]{,3}-[a-z]{2,3}$',word)
    return x

print(patterns("co-op"))
print(patterns("e-bay"))
print(patterns("no-no"))
print(patterns("e-mai"))


import nltk
text = "the light was on"
tagged = nltk.pos_tag(nltk.word_tokenize(text))
print(tagged)


'chunk: {<NN.*><VB.?>+}'

import nltk
sentence = "Mark and John are working at Google"
print(nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence))))

import nltk
text = 'We have three job candidates vivsiting. All candidates are competitive.'
print(nltk.word_tokenize(text))
print(set(nltk.word_tokenize(text)))


h = [(x,y) for y in range(5,7) for x in range(1,4)]
print(h)

import re
text="BAN671 Data Analytics 38 BAN675 Text Mining 35"

print(re.findall('[A-Z]{3}[0-9]{3}',text))
print(re.findall('[A-Z0-9]{6}',text))
print(re.findall('([A-Z]|[0-9]){6}',text))
print(re.findall('[A-Z]{3}\d{1,3}',text))























