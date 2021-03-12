#script: dfload1.py
import numpy as np
import pandas as pd
from functools import reduce

def get_counts(chunk):
    ch_count = chunk['Position Title'].value_counts()
    return ch_count

def add_counts(prev_count, curr_count):
    return prev_count.add(curr_count,fill_value = 0)


#data = pd.read_csv("city-of-chicago-salaries.csv",)
chunks = pd.read_csv("/home/debdulalm2016/py3dana/data/city-of-chicago-salaries.csv", chunksize=10000)
chunk_counts = map(get_counts, chunks)
total_counts = reduce(add_counts, chunk_counts)
print(total_counts.head(20))
total_counts.sort_values(ascending=False,inplace=True)
print(total_counts.head())

#ch1_positions = ch1['Position Title']
#print(ch1_positions.head())
#print(ch1_positions.value_counts())
#for chunk in chunks:
#    print('no of rows:', len(chunk))

