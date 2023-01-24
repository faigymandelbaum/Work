# The result prints many times and I get an error afterwards , I spent a lot of time on trying to figure out the error, but no results!!!!!!!!!
# Running the function from deepnote that was made in class caused an error as well in vs code.

import math
import pandas as pd
from concurrent.futures import ProcessPoolExecutor

def create_count_for_column(df_path, column_name):
    dict = {}
    df = pd.read_csv(df_path)
    my_column = df[column_name].unique()
    for c in my_column:
        dict[c] = df[column_name].str.count(c).sum()
    return dict 


def main():

    def make_chunks(df, num_chunks):
        num_rows = df.shape[0]
        chunk_size = math.ceil(num_rows / num_chunks)

        chunks = []
        for i in range(0, num_rows, chunk_size):
            chunk = df[i:i + chunk_size]
            chunks.append(chunk)
        
        return chunks

    def count_categories(df, categories):
        apps_in_categories = {}

        for category_name in categories:
            apps_in_categories[category_name] = df['Category'].str.count(category_name).sum()

        return apps_in_categories

    store_play = pd.read_csv('googleplaystore.csv')
    categories = store_play['Category'].unique()
    sp_chunks = make_chunks((store_play), 4)

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

# Timing both functions
import time
start = time.time()
create_count_for_column('googleplaystore.csv', 'Category')
end = time.time()
sequential_time = end - start

start = time.time()
if __name__ == '__main__':
    main()
end = time.time()
multiprocess_time = end - start

print ('sequential_time :', sequential_time, '\nmultiprocess_time: ', multiprocess_time)
