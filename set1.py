# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords
import string

text = '''
Elon Reeve Musk is a business magnate, investor and engineer. He is the founder, CEO, and 
lead designer of SpaceX; co-founder, CEO, and product architect of Tesla, Inc.; co-founder 
and CEO of Neuralink; and co-founder of PayPal. In December 2016, he was ranked 21st 
on the Forbes list of The World's Most Powerful People. As of August 2018, he has a 
net worth of $20.2 billion and is listed by Forbes as the 46th-richest person in the 
world. Born in Pretoria, South Africa, Musk taught himself computer programming at the age 
of 12. He moved to Canada when he was 17 to attend Queen's University. He transferred to 
the University of Pennsylvania two years later, where he received an economics degree from 
the Wharton School and a degree in physics from the College of Arts and Sciences. He began a 
Ph.D. in applied physics and material sciences at Stanford University in 1995 but dropped out 
after two days to pursue an entrepreneurial career. He subsequently co-founded Zip2, a web 
software company, which was acquired by Compaq for $340 million in 1999. Musk then founded X.com, 
an online bank. It merged with Confinity in 2000 and became PayPal, which was bought by eBay for 
$1.5 billion in October 2002.
'''

punc = string.punctuation
wordlist = nltk.word_tokenize(text)
free_of_punc = [w for w in wordlist if w not in punc]
print("Number of words in the paragraph: ",len(free_of_punc))
dict1 = dict.fromkeys(free_of_punc)
print("Number of unique words in the paragraph: ",len(dict1.keys()))


import nltk
from nltk.corpus import stopwords
import string

text = '''
Elon Reeve Musk is a business magnate, investor and engineer. He is the founder, CEO, and 
lead designer of SpaceX; co-founder, CEO, and product architect of Tesla, Inc.; co-founder 
and CEO of Neuralink; and co-founder of PayPal. In December 2016, he was ranked 21st 
on the Forbes list of The World's Most Powerful People. As of August 2018, he has a 
net worth of $20.2 billion and is listed by Forbes as the 46th-richest person in the 
world. Born in Pretoria, South Africa, Musk taught himself computer programming at the age 
of 12. He moved to Canada when he was 17 to attend Queen's University. He transferred to 
the University of Pennsylvania two years later, where he received an economics degree from 
the Wharton School and a degree in physics from the College of Arts and Sciences. He began a 
Ph.D. in applied physics and material sciences at Stanford University in 1995 but dropped out 
after two days to pursue an entrepreneurial career. He subsequently co-founded Zip2, a web 
software company, which was acquired by Compaq for $340 million in 1999. Musk then founded X.com, 
an online bank. It merged with Confinity in 2000 and became PayPal, which was bought by eBay for 
$1.5 billion in October 2002.
'''

punc = string.punctuation
stopwords = stopwords.words('english')
wordlist = nltk.word_tokenize(text)
free_of_stopwords = [w.lower() for w in wordlist if w.lower() not in stopwords and w.lower() not in punc]
frequency = nltk.FreqDist(free_of_stopwords)

print("Top ten frequent words in the paragraph: ",frequency.most_common(10))


import re
import nltk
words = nltk.corpus.nps_chat.words()


print([w for w in words if re.search('^.*(asion|ation)$', w)])



import re
import nltk
words = nltk.corpus.nps_chat.words()

words = list(dict.fromkeys(words))# remove duplicates
# whats is the expressions for "no", including "no", "No", "nooooo"

print([w for w in words if re.search('^[Nn][Oo]+$', w)])



import re
import nltk
course_info="1.01 CO Computers 2.05 MATH Mathematics 8.8 ENG English"

course_no = re.findall('\d\.\d+', course_info)

course_abb = re.findall('[A-Z]{2,}', course_info)

course_name = re.findall('[A-Z][a-z]+', course_info)

print('course number: ', course_no)
print('course abb: ', course_abb)
print('course name: ', course_name)

import nltk

text='''Trump entered the 2016 presidential race as a Republican and defeated sixteen opponents in the primaries. 
Commentators described his political positions as populist, protectionist, and nationalist. His campaign received 
extensive free media coverage; many of his public statements were controversial or false. Trump was elected president 
in a surprise victory over Democratic nominee Hillary Clinton. He became the oldest and wealthiest person ever to assume 
the presidency, the first without prior military or government service, and the fifth to have won the election while 
losing the popular vote. His election and policies have sparked numerous protests. Many of his comments and actions 
have been perceived as racially charged. '''

grammar = 'chunk:{<VB.?>+<DT|JJ.?|PRP$>+<NN.*>}'
parser = nltk.RegexpParser(grammar)
sents = nltk.sent_tokenize(text)
for i in sents:
    words = nltk.sent_tokenize(i)
    pos = nltk.pos_tag(words)
    chunks = parser.parse(pos)
    print(chunks)
    chunks.draw()
 
       
import re
import nltk
words = nltk.corpus.nps_chat.words()

text='''Trump entered the 2016 presidential race as a Republican and defeated sixteen opponents in the primaries. 
Commentators described his political positions as populist, protectionist, and nationalist. His campaign received 
extensive free media coverage; many of his public statements were controversial or false. Trump was elected president 
in a surprise victory over Democratic nominee Hillary Clinton. He became the oldest and wealthiest person ever to assume 
the presidency, the first without prior military or government service, and the fifth to have won the election while 
losing the popular vote. His election and policies have sparked numerous protests. Many of his comments and actions 
have been perceived as racially charged. '''

pos = nltk.pos_tag(nltk.word_tokenize(text))
grammar = 'chunk:{<VB.?>+<DT|JJ.?|PRP$>+<NN.*>}'
parser = nltk.RegexpParser(grammar)
chunks = parser.parse(pos)
chunks.draw()


for i in chunks.subtrees():
    if i.label() == "chunk":
        i.draw()
        print(i.leaves())


import nltk
import os
import re

output_file = open('details.csv', 'w')
header = 'file_name'+','+'page'+','+'num_view'+','+'title'+','+'author'+'\n'
print(header)
output_file.write(header)

os.chdir('/Users/nivethida/PythonWorkouts/TextMining/Day4/test')

for i in os.listdir('/Users/nivethida/PythonWorkouts/TextMining/Day4/test'):
    with open(i, 'r') as f:
        file_content = f.readlines()
        page = file_content[1].strip('\n')
        num_view = file_content[2].strip('\n')
        title = file_content[3].strip('\n')
        author = file_content[4].strip('\n')
        file_name = i
        inputs = str(file_name)[:-4]+','+str(page)+','+str(num_view)+','+str(title)+','+str(author)+'\n'
        output_file.write(inputs)

output_file.close()
print('done!!!!')   

import nltk
import string
text = '''
Elon Reeve Musk is a business magnate, investor and engineer. He is the founder, CEO, and 
lead designer of SpaceX; co-founder, CEO, and product architect of Tesla, Inc.; co-founder 
and CEO of Neuralink; and co-founder of PayPal. In December 2016, he was ranked 21st 
on the Forbes list of The World's Most Powerful People. As of August 2018, he has a 
net worth of $20.2 billion and is listed by Forbes as the 46th-richest person in the 
world. Born in Pretoria, South Africa, Musk taught himself computer programming at the age 
of 12. He moved to Canada when he was 17 to attend Queen's University. He transferred to 
the University of Pennsylvania two years later, where he received an economics degree from 
the Wharton School and a degree in physics from the College of Arts and Sciences. He began a 
Ph.D. in applied physics and material sciences at Stanford University in 1995 but dropped out 
after two days to pursue an entrepreneurial career. He subsequently co-founded Zip2, a web 
software company, which was acquired by Compaq for $340 million in 1999. Musk then founded X.com, 
an online bank. It merged with Confinity in 2000 and became PayPal, which was bought by eBay for 
$1.5 billion in October 2002.
'''

punc = string.punctuation
wordlist = nltk.word_tokenize(text)
free_of_punc = [w for w in wordlist if w not in punc]
print("Number of words in the paragraph: ",len(free_of_punc))
dict1 = dict.fromkeys(free_of_punc)
print("Number of unique words in the paragraph: ",len(dict1.keys()))


