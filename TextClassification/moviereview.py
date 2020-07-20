# -*- coding: utf-8 -*-
from nltk.corpus import movie_reviews

print(movie_reviews.categories())
print(movie_reviews.fileids('neg'))

print(movie_reviews.words('neg/cv975_11920.txt'))

#step 1, object s
objectset = [(movie_reviews.words(fileid),cat) for cat in movie_reviews.categories()
for fileid in movie_reviews.fileids(cat)
]
