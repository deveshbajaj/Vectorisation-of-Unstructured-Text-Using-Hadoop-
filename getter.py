#!/usr/bin/env python3
import sys
import re

import zipimport
importer = zipimport.zipimporter('nltk.mod')

nltk = importer.load_module('nltk')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop = set(stopwords.words('english'))


for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
   
    line = re.sub(r'[^\w\s]','',line)
    text = text +line+' '

    word_tokens = word_tokenize(line)
    filtered_sentence = [w for w in word_tokens if not w in stop]
    final = ' '.join(filtered_sentence)
    print(final)



"""
unique_words = list(set(text.split(" ")))
print(len(unique_words))
final = ' '.join(unique_words)
f = open('words.txt','w')
f.write(final)
f.close()
#print(unique_words)
print("done")"""