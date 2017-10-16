from collections import Counter
import pandas
import re
import numpy
headlines = [
    "PretzelBros, airbnb for people who like pretzels, raises $2 million",
    "Top 10 reasons why Go is better than whatever language you use.",
    "Why working at apple stole my soul (I still love it though)",
    "80 things I think you should do immediately if you use python.",
    "Show HN: carjack.me -- Uber meets GTA"
]


unique_words = list(set(" ".join(headlines).split(" ")))
#print(unique_words)

def make_matrix(headlines, vocab):
    matrix = []
    for headline in headlines:
        counter = Counter()
        st = re.findall(r'\w+',headline)
        for i in st:
            counter[i] +=1
        

        # Turn the dictionary into a matrix row using the vocab.
        row = [counter.get(w, 0) for w in vocab]
        #print(row)
        matrix.append(row)
    df = pandas.DataFrame(matrix)
    df.columns = unique_words
    return df

x=make_matrix(headlines, unique_words)
print(type(x))
print(x)

x.to_csv("file_path.csv")
print("done")