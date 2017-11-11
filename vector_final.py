#!/usr/bin/env python2
# -*- coding: utf-8 -*- 
from operator import itemgetter
from collections import Counter
import sys
import pandas 
import re


f = open("wordds.txt",'r')
g= f.readline().split(" ")
unique_words = set(list(f))

#print(type(d),len(d))

matrix =[]
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    #print(line)
    counter = Counter()
    st = re.findall(r'\w+',line)
    for i in st:
        counter[i] +=1
    row = [counter.get(w, 0) for w in unique_words]

    try :
        print(row)
    except :
        # count was not a number, so silently
        # ignore/discard this line
        print("NULL")
        continue
    matrix.append(row)

df = pandas.DataFrame(matrix)
df.columns = unique_words

print(type(df))
df.to_csv("part-00000")
print("done")
    