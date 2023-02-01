import math
from multiprocessing import Pool
from  functools import reduce
from hashlib import sha256

with open('pin.txt', 'r') as f:
   target=f.read()
   

def make_chunks(data, num_chunks):
    chunk_size = math.ceil(len(data) / num_chunks)
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def mapper(num_list):
    for num in num_list:
        if sha256(bytes(num)).hexdigest() == target:
            return num
    return 0         

def reducer(result1, result2):
    if result1 != 0:
        return result1
    else:
        return result2    

def map_reduce(data, num_processes, mapper, reducer):
    with Pool(num_processes) as pool:
        results = pool.map(mapper, make_chunks(data, num_processes))
    return reduce(reducer, results, 0)


def main():
    
    num_list = [num for num in range(1000, 10000)]
    my_pin = map_reduce(num_list, 10, mapper, reducer)
    print (my_pin)


if  __name__ == '__main__':
    main() 