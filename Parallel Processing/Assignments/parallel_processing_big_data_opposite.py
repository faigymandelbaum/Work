# The result prints many times and I get an error afterwards , I spent a lot of time on trying to figure out the error, but no results!!!!!!!!!
# Running the function from deepnote that was made in class caused an error as well in vs code.

import math
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
import time

def make_chunks(list, num_chunks):
    len_list = len(list)
    chunk_size = math.ceil(len_list / num_chunks)

    chunks = []
    for i in range(0, len_list, chunk_size):
        chunk = list[i:i + chunk_size]
        chunks.append(chunk)
    
    return chunks

def count_categories(df, categories):
    apps_in_categories = {}
    for category_name in categories:
        apps_in_categories[category_name] = df['Category'].str.count(category_name).sum()

    return apps_in_categories 

def main():

    store_play = pd.read_csv('googleplaystore.csv')
    categories = store_play['Category'].unique()
    sp_chunks = make_chunks(store_play, 4)

    start = time.time()

    processes = []
    with ProcessPoolExecutor() as exe:
        for chunk in sp_chunks:
            processes = [exe.submit(count_categories, chunk, categories) for chunk in sp_chunks]

    results = []
    for process in processes:
        results.append(process.result())

    merged_results = {}

    for result in results:
        for k in set(result):
            merged_results[k] = merged_results.get(k, 0) + result.get(k, 0)

    print(merged_results)

    end = time.time()
    multiprocess_time = end - start
    print ('multiprocess_time: ', multiprocess_time)

if __name__ == '__main__':
        main()

  