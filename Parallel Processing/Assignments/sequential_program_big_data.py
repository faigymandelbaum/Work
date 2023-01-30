import multiprocessing
import pandas as pd
import time

def create_count_for_column(df_path, column_name):
    dict = {}
    df = pd.read_csv(df_path)
    my_column = df[column_name].unique()
    for c in my_column:
        dict[c] = df[column_name].str.count(c).sum()
    return dict    

print (create_count_for_column('googleplaystore.csv', 'Category'))

start = time.time()
create_count_for_column('googleplaystore.csv', 'Category')
end = time.time()
time1 = end - start
print(time1)





