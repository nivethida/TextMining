# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt

text='''WordCloud: one of the simplest visualization technique
which is a type of word frequency visualization.
The size of the word in the image is bigger for more
frequent word and smaller for less frequen t word. This
type of visualization can be of help in initial query
formation. There are some drawbacks like the longer word
may occupy more space giving the impression of the frequent
word than it actually is. It may not help us to compare two
frequent words about their relationship can be misleading
sometimes even if using two words together may make sense.
Frequent words may not be meaningful. For generating word
cloud I am going to use wordcloud package you can install
the package from pip. Below is the code to generate cloud.
'''

from wordcloud import WordCloud
wc = WordCloud(max_font_size=50,max_words=20,background_color='white').generate(text)
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()

from nltk.corpus import inaugural
text = inaugural.raw()

from wordcloud import WordCloud
wc = WordCloud(max_font_size=50,max_words=20,background_color='white').generate(text)
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()




import nltk
from nltk.draw.dispersion import dispersion_plot
from nltk.corpus import stopwords

stopwords = stopwords.words('english')

wordlist = nltk.word_tokenize(text)

topics = ['government','country','states','citizen','power']
dispersion_plot(wordlist,topics)


wordlist = [x.lower() for x in nltk.word_tokenize(text) if x.lower() not in stopwords and x.isalpha()]


freq = nltk.FreqDist(wordlist)
plt.figure(figsize=(12,12))
freq.plot(50)


# lexical diversity 
# text is a list of words
def ld(text):  
    return len(set(text))/len(text)

from nltk.corpus import brown

for i in brown.categories():
    text = brown.words(categories = i)# list of words in the category
    diversity = ld(text)
    print(i,diversity)
    
    






























