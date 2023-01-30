import math
import pandas as pd
from multiprocessing import Pool
import functools


def make_chunks(data, num_chunks):
    chunk_size = math.ceil(len(data) / num_chunks)
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def count_industries(data):
    people_in_industries = {}

    for industry_name in data['Industry'].unique():
        people_in_industries[industry_name] = data['Industry'].str.count(industry_name).sum()

    return people_in_industries

def reducer(freq_chunk1, freq_chunk2):
    freq_chunk1.update(freq_chunk2)
    return freq_chunk1

def main():
    richest_people = pd.read_csv('TopRichestInWorld.csv')
    chunks = make_chunks(richest_people, 5)

    with Pool(4) as pool:
        chunk_results = pool.map(count_industries, chunks)
        result = functools.reduce(reducer, chunk_results) 

    print (result)    

  

if __name__ == '__main__':
    main()