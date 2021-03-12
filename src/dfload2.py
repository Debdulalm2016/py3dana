#script: dfload2.py
import numpy as np
import pandas as pd
from functools import reduce

def get_sum(chunk):
    ch_sum = sum(chunk['Employee Annual Salary'].apply(lambda x: float(x[1:])))
    return ch_sum

def add_sum(prev_sum, curr_sum):
    return prev_sum + curr_sum


#data = pd.read_csv("city-of-chicago-salaries.csv",)
chunks = pd.read_csv('/home/debdulalm2016/py3dana/data/city-of-chicago-salaries.csv', chunksize=10000)
chunk_results = map(get_sum, chunks)
#print(list(chunk_results))
total_sum = reduce(add_sum, chunk_results)
print('Total Salary:', total_sum)

