#!/usr/bin/env python3
from operator import itemgetter
from collections import Counter


import sys
import pandas
import re
import numpy

f = open("words.txt",'r')
d = f.readline()
unique_words = list(d.split(" "))
print(type(d),len(d))

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
    print(''.join(row))

    matrix.append(row)

df = pandas.DataFrame(matrix)
df.columns = unique_words

#print(type(df))
df.to_csv("dev_output.csv")
#print("done")"""
    