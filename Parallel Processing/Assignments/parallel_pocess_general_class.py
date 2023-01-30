import math
import pandas as pd
from concurrent.futures import ProcessPoolExecutor

class Process:

    def __init__(self, df_path, num_chunks, column):
       
        self.df = pd.read_csv(df_path)
        self.column = column
        self.num_chunks = num_chunks
        self.columns = self.df[column].unique()
        self.chunks = []
        self.column_dict = {}

    def make_chunks(self):
        num_rows = self.df.shape[0]
        chunk_size = math.ceil(num_rows / self.num_chunks)    
        self.chunks = []
        for i in range(0, num_rows, chunk_size):
            chunk = self.df[i:i + chunk_size]
            self.chunks.append(chunk)
        return self.chunks

    def count_column_values(self):
        for column_name in self.columns:
            self.column_dict[column_name] = self.df[self.column].str.count(column_name).sum()
        return self.column_dict

    def process(self):  
        self.make_chunks()
        self.count_column_values()
        with ProcessPoolExecutor() as exe:
            processes = [exe.submit(self.count_column_values) for chunk in self.chunks]

        results = [process.result() for process in processes]

        merged_results = {}
        for result in results:
            merged_results = {k: merged_results.get(k, 0) + result.get(k, 0) \
            for k in set(merged_results) | set(result)}
        print(merged_results)

def main():

    my_process=Process("TopRichestInWorld.csv", 8, 'Industry' )
    my_process.process()

if __name__ == '__main__':
    main() 

