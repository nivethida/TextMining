# -*- coding: utf-8 -*-
import re
text="101 COM    Computers 205 MAT   Mathematics 89 ENG   English"
text2=""
result = re.split('\d+',text)
print(result)


import re
text='I toke flight UA500 today and flight UA600 today'
x=re.findall('flight (.*?) today', text)
print(x)
y=re.findall('flight (.*) today', text)
print(y)

import re
text="101 COM    Computers 205 MAT   Mathematics 89 ENG   English"

result = re.findall('101//s+([A-Z]+)', text)
print(result)

text1="can can't can' cant cant't"
test1=re.findall("can('t)+",text1) # this time we need to use double quotation.
print(test1)

text1="can can't can' cant  can't"
test1=re.findall("can(?:'t)+",text1)  # when adding ?:, the regular expression only group the patterns inside the parenthesis and apply the modifier
print(test1)
# another example: suppose you want to extract the course names with one capitalized letter plus one lower case letter such as MgMt and MkTg
text2="MgMt 330, ITM 336, MkTg 447"
test2=re.findall("([A-Z][a-z])+",text2)  # this is wrong because the parenthesis here means capturing, It will capture the "Mt" and "Tg"
print(test2)
correct=re.findall("(?:[A-Z][a-z])+",text2) # converting non-capturing, this means many instances of one capitalized letter plus one lower case letter
print(correct)

text3="(510)772-8823 is a phone number"

result = re.findall("\(\d+\)\d+-\d+", text3)
print(result)

result = re.findall("\(\d+\)", text3)
print(result)

test4=re.findall("\((\d+)\)\d+-\d+",text3)  # you may just use a capturing parenthesis inside a pair of literal parenthesis
print(test4)

import nltk
import re
word = 'we are taking text mining class'
vowel=re.findall('[aei]', word)
print(vowel)


import re
def stem4(word):
    suffix=re.findall('^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', word)
    stem, suffix=suffix[0]
    return suffix, stem
print(stem4('processing'))


import re
text = "100 MAT Math   102 COM Computer 104 ENG English"

result = re.findall('\d',text)
print(result)

#['1', '0', '0', '1', '0', '2', '1', '0', '4']
result = re.findall('\d+',text)
print(result)

#['100', '102', '104']
result = re.findall('\d{3}',text)
print(result)

#['100', '102', '104']

result = re.findall('\d*',text)
print(result)

#['100', '', '', '', '', '', '', '', '', '', '', '', '', '102', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '104', '', '', '', '', '', '', '', '', '', '', '', '', '']

result = re.findall('\d?',text)
print(result)
#['1', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '1', '0', '2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1', '0', '4', '', '', '', '', '', '', '', '', '', '', '', '', '']
text = "100 MAT Math   102023 COM Computer 104 ENG English"
result = re.findall('\d{1,3}',text)
print(result)
#['100', '10202', '3', '104']
result = re.findall('\w',text)
print(result)
#['1', '0', '0', 'M', 'A', 'T', 'M', 'a', 't', 'h', '1', '0', '2', '0', '2', '3', 'C', 'O', 'M', 'C', 'o', 'm', 'p', 'u', 't', 'e', 'r', '1', '0', '4', 'E', 'N', 'G', 'E', 'n', 'g', 'l', 'i', 's', 'h']
result = re.findall('\w+',text)
print(result)
#extract chunks of all letters and all numbers
result = re.findall('',text)
print(result)

result = re.findall('^([A-Z]+\s)$', text)# ???????
print(result)
#['100', 'MAT', 'Math', '102023', 'COM', 'Computer', '104', 'ENG', 'English']

#['100', 'ath', '102023', 'omputer', '104', 'nglish']

#[A-Za-z0-9]
#['100', 'MAT', 'Math', '102023', 'COM', 'Computer', '104', 'ENG', 'English']


#['MAT', 'Math', 'COM', 'Computer', 'ENG', 'English']

#extract course name


#['Math', 'Computer', 'English']

# + modifies ony the symbol immediately before it !!!!!!!!!!!!!!!! important

#extract course with abbrevation

#['MAT', 'M', 'COM', 'C', 'ENG', 'E']

#['MAT', 'COM', 'ENG']






import re
text="101 COM    Computers 205 MAT   Mathematics 89 ENG   English"

result = re.findall('.*',text)
print(result)


# get everything
result14=re.findall('.+',text) #get everything, think about why '.*' will always provides an empty element?
print(result14)
# lazy and diligent version of everything.
import re
text='I toke flight UA500 today and flight UA600 today'
x=re.findall('flight (.*?) today', text)
print(x)
y=re.findall('flight (.*) today', text)
print(y) 

text="101 COM    Computers 205 MAT   Mathematics 89 ENG   English"
result16=re.findall('205 MAT(\s+)([A-Z][a-z]+)',text) #get name of the course 205. "205 " matches exactly the 205 and a space, what is inside matches one or more capitalized characters.
print(result16)
result17=re.findall('89 ([A-Z]+)',text)

text1="can can't can' cant"
test1=re.findall("can('t)+",text1) # this time we need to use double quotation.
print(test1) # only the 't is matched and returned

import re
text1="can can't can' cant"
test1=re.findall("can(?:'t)+",text1)  # when adding ?:, the regular expression only group the patterns inside the parenthesis and apply the modifier
print(test1)

text2="MgMt 330, ITM 336, MkTg 447"
test2=re.findall("([A-Z][a-z])+",text2)  # this is wrong because the parenthesis here means capturing, It will capture the "Mt" and "Tg"
print(test2)
correct=re.findall("(?:[A-Z][a-z])+",text2) # converting non-capturing, this means many instances of one capitalized letter plus one lower case letter
print(correct)

import nltk
import re
word = 'we are taking text mining class'
vowel=re.findall('[aeiou]', word)
print(vowel)

import re
def stem2(word):
    suffix=re.findall('^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', word)
    print(suffix)
    lenth=len(suffix[0]) # remember that suffix is a list, suffix[0] is the string we need
    return word[:-lenth]
print(stem2('processing'))

import re
def stem4(word):
    suffix=re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', word)
    print(suffix)
    stem, suffix=suffix[0]
    return suffix, stem
print(stem4('processing'))


import re
import nltk
text='deejected, object, inject, injector, majestic, majestically'
wordlist=nltk.word_tokenize(text)
for w in wordlist:
    if re.search('^...j..t..$',w): #remember, . stands for anything
        print(w)

pattern='\d{1,3}\s[A-Z]+'
text3="1010 COM    Computers 101 MAT   Mathematics" #swith the numbers
print(re.match(pattern,text3)) #After swiching the numbers, it returns a "none", since match function always start from the 1st character.
print(re.search(pattern,text3)) #no problem with search, start counting from the 2nd character.


import re
import nltk
text='abandoned, abandon, help, abraised, open, closed'
print(re.search('ed$',text))

import re
wordlist=['gold','golf','hold','hole']
y=[w for w in wordlist if re.search('^..[ilj][bcd]',w)!=None]
print(y)

import nltk
import re
chat_words=nltk.corpus.nps_chat.words()
chat_words=set(w for w in chat_words)
x=[w for w in chat_words if re.search('^m+i+n+e+$',w)!=None] # search for different writtings of 'mine'
z= [w for w in chat_words if re.search('^[ha]+$', w)!=None] # search for ah or ha
w=[w for w in chat_words if re.search('^[0-9]+\.[0-9]+$', w)!=None] # search for decimal numbers
p=[w for w in chat_words if re.search('^[0-9]{4}$', w)!=None] # search for years
q= [w for w in chat_words if re.search('^[a-z]{,5}-[a-z]{2,3}$', w)!=None]

print(q)

import re
text='U.S.A is united states'
y=re.findall('(?:[A-Z]\.)+[A-Z]',text)
print(y)


text='e-bay is a company'
y=re.findall('\w+',text) # e-bay is seperated
print(y)
y1=re.findall('[a-z]{1,}-[a-z]{1,}',text) # only e-bay is captured
print(y1)
y2=re.findall('\w+(?:-\w+)*',text) # now correct
print(y)


text1 ="""
Initially we were happy with the product especially since we got it a very good price last Amazon Prime Day sale on July 16, 2018. We liked how we can watch and stream shows easily thru various apps like Netflix, Amazon video, Dramafever, Rakuten etc. Very lighrweight tv and just right for our needs. However to our surprise just awhile ago August 22, 2018, while streaming a drama series, the on screen display turned washed out/white screen. Turned on and off the tv several times to see if it will reboot/restart properly. Unfortunately nothing remedied it. Either you get back to that washed out screen or a totally black screen no apps at all. I have just submitted a replacement request thru Amazon customer service so we will see what happens and how fast they will address our complaint.
Just an update, so we ended up being told by Amazon, to contact Best Buy and we did that by email at the same time indicating in the letter we want a replacement. Best Buy replied to us that it is outside of the return period if we want contact Toshiba directly. So, we did just that..with sheer frustration of course being tossed around. Toshiba nicely told me that they will send the techinician and I asked which company handle this techinician is it Toshiba or a third party. Ironically, they are coordinating with who else. The Geek Squad. Oh dear..back to Best Buy then. The Geek Squad guy came on the appointment date, just a few minutes late, but was nice enough. His assessment as discussed with whoever was on the other end of the line came down to an approval for a replacement. So we were asked to bring the tv over to our local Best Buy, gave us the confirmation and work numbers. Even gave us his business card and that of his manager if in case we encounter problems. For some reason it seems it is not common for them to service products sold by Best Buy throught the Amazon website.
So we went to our local Best Buy. The lady was nice enough, and honest enough to say she was not familiar with an Amazon sale of a Best Buy product. So I had to tell her again the long story of how we got the tv etc etc. Finally someone helped her encode the return correctly and we had a store credit for the complete amount we paid for. However when we got the replacement tv, the price in store is slightly higher so we had to shoulder now the difference. Well, we just paid for it. So in short losing the advantage of that Prime deal sale price which did not work at all with a defective product. We do wish these three companies, Amazon, Best Buy and Toshiba iron out the way they handle requests for replacements and returns....seems initially both Amazon and Best Buy did not want to shoulder the return. If we had not insisted on availing the limited manufacturer's warranty, we would just have been left with a useless crap of a tv.
"""

words = nltk.word_tokenize(text1)

pos = nltk.pos_tag(words)

print(pos)

nouns = [x for x,y in pos if y.startswith('NN')]

print(nouns)

verbs = [x for x,y in pos if y.startswith('VB')]

print(nltk.FreqDist(verbs).most_common(5))

import nltk
sample = 'our team completed the team project, and the team received grant money'

pos = nltk.pos_tag(nltk.word_tokenize(sample))

grammar = 'chunk:{<NN.*><VB.?>+}'
parser = nltk.RegexpParser(grammar)
chunks = parser.parse(pos) #input for parse is list of tuples
print(chunks)

# A is a B, A can be a person or a regular noun
sample = 'He is now the president of United states. Before this he was a sucessful buisiness man'
sents = nltk.sent_tokenize(sample)
grammer = 'chunk: {<PRP><VB.?>+<DT>?<JJ.?>+<NN.*>}'
for i in sents:
    pos = nltk.pos_tag(nltk.word_tokenize(i))

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

grammer = 'chunk: {<DT>?<JJ.?>*<NN.*>+}

grammer = 'chunk: {<NN.*><VB.?>+<DT|JJ.?|NN.*>}+'


from sklearn.feature_extraction.text import CountVectorizer
corpus = [
   'This is the first document.',
   'This document is the second document.',
   'And this is the third one.',
   'Is this the first document?',
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names()) # it assigns each word an index. get the list of words with the 1st labelled index 0
print(X)

import re
result1 = re.match(r'TP', ' Tutorials Point TP')

result2 = re.findall(r'TP', 'TP Tutorials Point TP')

result3 = re.search(r'TP', ' Tutorials Point TP')


print(result1)
print(result2)
print(result3)

import re
result = re.search(r'Tutorials', 'TP Tutorials Point TP')
print(result)





















