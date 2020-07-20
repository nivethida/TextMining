# -*- coding: utf-8 -*-

import nltk
import os
import re
jjlist = []
os.chdir('/Users/nivethida/PythonWorkouts/TextMining/Day4/test')
for i in os.listdir('/Users/nivethida/PythonWorkouts/TextMining/Day4/test'):
    with open(i, 'r') as f:       
        contents = f.readlines()
        totallength = len(contents)
        print(contents[2])
        for i in range(9, totallength): # leaving till line 9
            text = contents[i]
            # !!!!! be careful with delimeter with tab or space important
            message = re.split('\t',text)[3]
            pos = nltk.pos_tag(nltk.word_tokenize(message))
            jj = [x for x in pos[:-1] if x[1].startswith('JJ') and pos[pos.index(x)+1][0]] # search for everything untilll second last tuple listem to video to know why
            # x = ('wonderful', 'JJR')
            jjlist+=jj
            
print(jjlist)           


import nltk
import os
import re
jjlist = []
os.chdir('/Users/nivethida/PythonWorkouts/TextMining/Day4/test')

with open('75018.txt', 'r') as f:
    content = f.readline(20)
    print(content)