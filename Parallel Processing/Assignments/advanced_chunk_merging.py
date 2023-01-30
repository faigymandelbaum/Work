import math
import pandas as pd
from multiprocessing import Pool
import functools

df = pd.read_csv('chatgpt.csv')
column = df['reply_count']

def make_chunks(df, num_chunks):
    num_rows = df.shape[0]
    chunk_size = math.ceil(num_rows / num_chunks)
    chunks = [(df[i:i + chunk_size]) for i in range(0, num_rows, chunk_size)]
    return chunks

def count_replies(df):
    list_of_nums = []
    for num in column.unique():
        list_of_nums.append(num)
    return list_of_nums

def map_reduce(df, num_processes, mapper, reducer):
    chunks = make_chunks(df, num_processes)
    with Pool(num_processes) as pool:
        chunk_results = pool.map(mapper, chunks)
    return functools.reduce(reducer, chunk_results)

def reducer(freq_chunk1, freq_chunk2):
    freq_chunk1.append(freq_chunk2)
    return freq_chunk1

def main():

    date_freq = map_reduce(df, 5, count_replies, reducer)
    print (date_freq)

if __name__ == '__main__':
    main()

"Matzchik matchil"