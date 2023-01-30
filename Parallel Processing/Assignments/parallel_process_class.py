import pandas as pd
import math
from concurrent.futures import ProcessPoolExecutor

class Process:

    def __init__(self, df):
        self.df=pd.read_csv(df)


    def make_chunks(self, num_chunks):
        num_rows = self.df.shape[0]
        chunk_size = math.ceil(num_rows / num_chunks)
        chunks = []
        for i in range(0, num_rows, chunk_size):
            chunk = self.df[i:i + chunk_size]
            chunks.append(chunk)
        return chunks


    def count_industry(self,df,industry):
        industry_list = {}
        for all_industries in df[industry].unique():
            industry_list[all_industries] = self.df['Industry'].str.count(all_industries).sum()

        return industry_list


def main():
    my_process=Process("TopRichestInWorld.csv")
    worth=my_process.df["Industry"].unique()
    rp_chunks = my_process.make_chunks(4)
    with ProcessPoolExecutor() as exe:
        processes = [exe.submit(my_process.count_industry, chunk, worth) for chunk in rp_chunks]

    results = [process.result() for process in processes]

    merged_results = {}
    for result in results:
        merged_results = {k: merged_results.get(k, 0) + result.get(k, 0) \
        for k in set(merged_results) | set(result)}
    print(merged_results)

if __name__ == '__main__':
    main()    