# -*- coding: utf-8 -*-
'''
Identifiers:
\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any letter
\W = anything but a letter
. = any character, except for a new line
\b = space around whole words
\. = period. must use backslash, because . normally means any character.

Modifiers:
{1,3} = for digits, u expect 1-3 counts of digits, or "places"
+ = match 1 or more
? = match 0 or 1 repetitions.
* = match 0 or MORE repetitions
$ = matches at the end of string
^ = matches start of a string
| = matches either/or. Example x|y = will match either x or y
[] = range, or "variance"
{x} = expect to see this amount of the preceding code.
{x,y} = expect to see this x-y amounts of the precedng code
'''

import re
text = "100 MAT Math   102 COM Computer 104 ENG English"

#split
result = re.split('\s', text) #returns list
print(result)

#split with one or more spaces
result = re.split('\s+', text) #returns list
print(result)

#findall mostly used method
result = re.findall("\d",text)
print(result)

#['1', '0', '0', '1', '0', '2', '1', '0', '4']

#find out all chunks of text
result = re.findall("\d{3}",text)
print(result)

#['100', '102', '104']

res = re.findall('\d+', text)
print(res)
#['100', '102', '104']

res = re.findall('\d*', text)
print(res)
#['100', '', '', '', '', '', '', '', '', '', '', '', '', '102', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '104', '', '', '', '', '', '', '', '', '', '', '', '', '']

res = re.findall('\d?', text)
print(res)
#['1', '0', '0', '', '', '', '', '', '', '', '', '', '', '', '', '1', '0', '2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1', '0', '4', '', '', '', '', '', '', '', '', '', '', '', '', '']

text = "100 MAT Math   102023 COM Computer 104 ENG English"
res = re.findall('\d{1,5}', text)
print(res)

#['100', '10202', '3', '104']

#extract all single digit and single letters
text = "100 MAT Math   102 COM Computer 104 ENG English"
result = re.findall('\w',text)
print(result)
#['1', '0', '0', 'M', 'A', 'T', 'M', 'a', 't', 'h', '1', '0', '2', '0', '2', '3', 'C', 'O', 'M', 'C', 'o', 'm', 'p', 'u', 't', 'e', 'r', '1', '0', '4', 'E', 'N', 'G', 'E', 'n', 'g', 'l', 'i', 's', 'h']

#extract chunks of all letters and all numbers

result = re.findall('\w+',text)
print(result)

#['100', 'MAT', 'Math', '102023', 'COM', 'Computer', '104', 'ENG', 'English']

result = re.findall('[a-z0-9]+',text)
print(result)

#['100', 'ath', '102023', 'omputer', '104', 'nglish']

result = re.findall('[a-zA-Z0-9]+',text)
print(result)
#[A-Za-z0-9]
#['100', 'MAT', 'Math', '102023', 'COM', 'Computer', '104', 'ENG', 'English']

result = re.findall('[A-z]+',text)
print(result)

#['MAT', 'Math', 'COM', 'Computer', 'ENG', 'English']

#extract course name
result = re.findall('[A-Z][a-z]+', text)
print(result)

#['Math', 'Computer', 'English']

# + modifies ony the symbol immediately before it !!!!!!!!!!!!!!!! important

#extract course with abbrevation
result = re.findall('[A-Z]+', text)
print(result)

#['MAT', 'M', 'COM', 'C', 'ENG', 'E']

result = re.findall('[A-Z]{3}', text)
print(result)

result = re.findall('[A-Z]{2,}', text)
print(result)

result = re.findall('^([A-Z]+)\s$', text)# ???????
print(result)


#['MAT', 'COM', 'ENG']

#CAPTURING
# what is the course abbrevation for the course 100
text = "100 MAT Math   102023 COM Computer 104 ENG English"

result = re.findall('100 [A-Z]+', text)
print(result)

#['100 MAT']

result = re.findall('100 ([A-Z]+)', text)
print(result)

#['MAT']

#to capture everything in between A and B
# version 1: .*, diligent version of everything
#version 2: .*? lazy version

text= 'I took flight UA400 today and flight UA500 today'

# extract the flight taken today !!!!!!!!!!!!!!! important
res = re.findall('flight (.*) today', text)
print(res)
#['UA400 today and flight UA500']

res2 = re.findall('flight (.*?) today', text)
print(res2)
#['UA400', 'UA500']

#GROUPING
text = 'MgMt 100, MkTg 200, AcTg 300'

result = re.findall('([A-Z][a-z])+', text)
print(result)

#['Mt', 'Tg', 'Tg']

result = re.findall('(?:[A-Z][a-z])+', text)
print(result)
#['MgMt', 'MkTg', 'AcTg']



import re
text = 'my phone number is (510)421-3123'
# a literal predecessor ( :\(
res = re.findall('\(\d+\)\d+-\d+', text)[0]
print(res)

# to extract the area code
res = re.findall('\((\d+)\)\d+-\d+', text)
print(res)


ß

# using regular exp gor stemming
import re
def stem(text):
    suffix = re.findall('^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', text)[0]
    print(re.findall('^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', text))
    #suffix = re.findall('^.*[ing|ment|es|ive|tion|ed|ly]$', text)[0]
    return text[:-len(suffix)]

print(stem('management'))

# do something but return stem and suffix at the same time
def stem(text):
    suffix = re.findall('^(.+)([ing|ment|es|ive|tion|ed|ly]$)', text)[0]
    #suffix = re.findall('^.*[ing|ment|es|ive|tion|ed|ly]$', text)[0]
    return text[:-len(suffix)]

print(stem('management'))

def stem(text):
    group = re.findall('^(.+)([ing|ment|es|ive|tion|ed|ly]$)', text)[0]
    #suffix = re.findall('^.*[ing|ment|es|ive|tion|ed|ly]$', text)[0]
    stem,suffix=group
    return (stem,suffix)

print(stem('management'))

# match and search
# match: trys to match the pattern from the very first char in the text
# search trys to match the pattern from anywhere

text = '1010 Math 102 Com 103 Mus'
pattern = '\d{3}\s\w+'
if re.search(pattern, text):
    x = re.search(pattern, text)
    print('found, start from {}, ends at {}'.format(x.start(), x.end()))
else:
    print('not found')    

text = '1010 Math 102 Com 103 Mus'
pattern = '\d{3}\s\w+'
if re.match(pattern, text):
    x = re.search(pattern, text)
    print('found, start from {}, ends at {}'.format(x.start(), x.end()))
else:
    print('not found') 


# remake re.match using re.findall
    
pattern_match='^\d{3}\s\w+' 
pattern_search='\d{3}\s\w+'  
print(re.findall(pattern_match, text)) 
print(re.findall(pattern_search, text)) 


import re
import nltk
chat = nltk.corpus.nps_chat.posts()


#asion’ or ‘ation’

result = re.findall('^.*(asion|ation)$', chat)

print(result)
print(chat[:3])

words = nltk.corpus.nps_chat.words()
print(words[:100])

words = list(dict.fromkeys(words))# remove duplicates
# whats is the expressions for "ah", including "ahhhh", "aHahah" but not Haha

print([w for w in words if re.search('^[Aa][HhAa]+$', w)])

#extract all decimal numbers used in the chat: 0.1,0.12,.12
print([w for w in words if re.search('^\d*\.\d+$', w)])

print([w for w in words if re.search('^\d+(?:\.\d+)?$', w)])

# search for dash connected values daughter-in-law

print([w for w in words if re.search('^[a-zA-Z]+(-\w+)$', w)])

# abbrevations like U.S.A.

print([w for w in words if re.search('^(?:[A-Z]\.)+$', w)])

#currency: $13. $12.5

print([w for w in words if re.search('^\$\d+(?:\.\d+)?$', w)])

#tokenize with re, goal is to remove the punctuation , and . in the result also tonenize with tabs and multiple places

text = '''here are some spaces     , here are some \t\t\t\t\t\t,  here are
some new line symbols \n\n\n
'''

wordlist = re.split('[\s\t\n,\.]+', text)

print(wordlist)

import nltk
wordlist2 = nltk.word_tokenize(text)
print(wordlist2)


























