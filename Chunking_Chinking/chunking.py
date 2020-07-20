# -*- coding: utf-8 -*-

import nltk
text="Part of Speech tagging does exactly what it sounds like, it tags each word in a sentence with the part of speech for that word. This means it labels words as noun, adjective, verb, etc. PoS tagging also covers tenses of the parts of speech."

wordlist = nltk.word_tokenize(text)

pos = nltk.pos_tag(wordlist)
print(pos)

text1 ="""
Initially we were happy with the product especially since we got it a very good price last Amazon Prime Day sale on July 16, 2018. We liked how we can watch and stream shows easily thru various apps like Netflix, Amazon video, Dramafever, Rakuten etc. Very lighrweight tv and just right for our needs. However to our surprise just awhile ago August 22, 2018, while streaming a drama series, the on screen display turned washed out/white screen. Turned on and off the tv several times to see if it will reboot/restart properly. Unfortunately nothing remedied it. Either you get back to that washed out screen or a totally black screen no apps at all. I have just submitted a replacement request thru Amazon customer service so we will see what happens and how fast they will address our complaint.
Just an update, so we ended up being told by Amazon, to contact Best Buy and we did that by email at the same time indicating in the letter we want a replacement. Best Buy replied to us that it is outside of the return period if we want contact Toshiba directly. So, we did just that..with sheer frustration of course being tossed around. Toshiba nicely told me that they will send the techinician and I asked which company handle this techinician is it Toshiba or a third party. Ironically, they are coordinating with who else. The Geek Squad. Oh dear..back to Best Buy then. The Geek Squad guy came on the appointment date, just a few minutes late, but was nice enough. His assessment as discussed with whoever was on the other end of the line came down to an approval for a replacement. So we were asked to bring the tv over to our local Best Buy, gave us the confirmation and work numbers. Even gave us his business card and that of his manager if in case we encounter problems. For some reason it seems it is not common for them to service products sold by Best Buy throught the Amazon website.
So we went to our local Best Buy. The lady was nice enough, and honest enough to say she was not familiar with an Amazon sale of a Best Buy product. So I had to tell her again the long story of how we got the tv etc etc. Finally someone helped her encode the return correctly and we had a store credit for the complete amount we paid for. However when we got the replacement tv, the price in store is slightly higher so we had to shoulder now the difference. Well, we just paid for it. So in short losing the advantage of that Prime deal sale price which did not work at all with a defective product. We do wish these three companies, Amazon, Best Buy and Toshiba iron out the way they handle requests for replacements and returns....seems initially both Amazon and Best Buy did not want to shoulder the return. If we had not insisted on availing the limited manufacturer's warranty, we would just have been left with a useless crap of a tv.
"""

wlist = nltk.word_tokenize(text1)

pos = nltk.pos_tag(wlist)

jj = [x for x,y in pos if y.startswith('JJ') ]

print(jj)

nn = [x for x,y in pos if y.startswith('NN')]

print(nn)

topnouns = nltk.FreqDist(nn).most_common(5)

print(topnouns)

import nltk
sample = 'our team completed the team project, and the team received grant money'

#extracting structure
# some verbs following some nouns

pos = nltk.pos_tag(nltk.word_tokenize(sample))
grammar = 'chunk:{<NN.*><VB.?>+}' #NNS, NNP, NNPS for Vrbs VB,VBD,VBZ,VBG -> ALL FORMS OF NOUN IS INCLUDED
parser = nltk.RegexpParser(grammar)
chunks = parser.parse(pos) #input for parse is list of tuples
print(chunks)
chunks.draw()

# A is a B, A can be a person or a regular noun
sample = 'He is now the president of United states. Before this he was a sucessful buisiness man'
sents = nltk.sent_tokenize(sample)
grammer = 'chunk: {<PRP><VB.?>+<DT>?<JJ.?>*<NN.*>}'#JJ, JJS, JJR
for i in sents:
     pos = nltk.pos_tag(nltk.word_tokenize(i))
     parser = nltk.RegexpParser(grammer)
     chunks = parser.parse(pos) #input for parse is list of tuples
     print(chunks)
     chunks.draw()
     
# important structure JJ + NN
import nltk
text3 ='''By design, a blockchain is resistant to modification of the data.
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
sents = nltk.sent_tokenize(text3)
grammer = 'chunk: {<DT>?<JJ.?><NN.*>}'
for i in sents:
    pos = nltk.pos_tag(nltk.word_tokenize(i))
    parser = nltk.RegexpParser(grammar)
    chunks = parser.parse(pos) #input for parse is list of tuples
    print(chunks)
     
import nltk   
text='''Donald John Trump (born June 14, 1946) is the 45th and
current President of the United States. Before entering politics,
he was a businessman and television personality. 
'''
grammer = 'Chunk:{<PRP><VB.+><DT>?<NN.?>}'
pos = nltk.pos_tag(nltk.word_tokenize(text))
parser = nltk.RegexpParser(grammer)
chunked = parser.parse(pos) #input for parse is list of tuples

for i in chunked.subtrees():
    if i.label() == "Chunk":
        print(i.leaves())
    
from nltk.corpus import inaugural
text = inaugural.words()
pos = nltk.pos_tag(text)


# JJ +NN but the NN will be 'people'
# !!!!!! important always allow DT iin this kind of structures
jjlist = []
parser = nltk.RegexpParser('chunk:{<JJ.?>+<NN.*>}')
chunk = parser.parse(pos)
for i in chunk.subtrees():
    if i.label()=="chunk" and i.leaves()[-1][0]=='people':
        # i.leaves()=[('american', 'JJ),('people', 'NN')]
        #i.leaves()[-1] = ('people','NN')
        jj = [x[0] for x in i.leaves()[:-1]]
        jjlist += jj
        

frequency = nltk.FreqDist(jjlist)   
print(frequency.most_common(10))  

#NN +VB pharase, NN == "people"
text = [x.lower() for x in inaugural.words()]
pos = nltk.pos_tag(text)
parser = nltk.RegexpParser('chunk: {<NN.*><VB.?>+<DT|JJ.?|NN.*>+}')

chunk = parser.parse(pos)
for i in chunk.subtrees():
    if i.label()=="chunk" and i.leaves()[0][0]=='people':
        # i.leaves()=[('american', 'JJ),('people', 'NN')]
        #i.leaves()[-1] = ('people','NN')
        print(' '.join([x for x,y in i.leaves()]))
        
#CHINKING is to delete a particular text structure
#chunking is to grab particular text stttucture        

sample = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),
       ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]
grammar = '''
chunk: {<.*?>+}
}<DT|JJ.?|NN.*>+{
'''
parser = nltk.RegexpParser(grammar)
chunk = parser.parse(sample)
print(chunk)

#named entity chunking

# distinguches btw various proper nouns
#LOCATION -> yosemitte, rewood national park
#GPE -> hayward, california, LA
text='''Bush was born on July 6, 1946, in New Haven, Lilly
Connecticut. After graduating from Yale University in 1968
and Harvard Business School in 1975, he worked in the oil industry.
Bush married Laura Welch in 1977 and unsuccessfully ran for the U.S.
House of Representatives shortly thereafter.
He later co-owned the Texas Rangers baseball team before defeating Ann
Richards in the 1994 Texas gubernatorial election.
Bush was elected President of the United States in 2000
when he defeated Democratic incumbent Vice President Al Gore
after a close and controversial win that involved a stopped recount
in Florida. He became the fourth person to be elected president
while receiving fewer popular votes than his opponent.[3]
Bush is a member of a prominent political family and is the
eldest son of Barbara and George H. W. Bush, the 41st President
of the United States. He is only the second president to assume
the nation's highest office after his father, following the
footsteps of John Adams and his son, John Quincy Adams.[4]
His brother, Jeb Bush, a former Governor of Florida, was a
candidate for the Republican presidential nomination in the
2016 presidential election. His paternal grandfather,
Prescott Bush, was a United States Senator from Connecticut.'''

#get list of 
organization=[]
person=[]
GPE=[]

pos = nltk.pos_tag(nltk.word_tokenize(text))
ne_chunk=nltk.ne_chunk(pos)
print(ne_chunk)

for i in ne_chunk.subtrees():
    if i.label() == 'ORGANIZATION':
        print([x for x,y in i.leaves()])
    elif i.label == 'PERSON':
        person.append(' '.join([x for x,y in i.leaves()]))
    elif i.label == 'GPE':
        GPE.append(' '.join([x for x,y in i.leaves()]))

print(organization)
print(person)
print(GPE)


# !!!!!!!!!! chunk more styles at same time and preference one not for exam

# !!!!!!!!!!!!!evaluvating chunkers not for exam but important concept

# !!!!!!!!  multistage chunking not for exam IOB tagging not for exam but interested take a look 


print([(x,y) for x,y in zip('lil','ily')])


print(([(x,y) for x,y in zip()]))



















































