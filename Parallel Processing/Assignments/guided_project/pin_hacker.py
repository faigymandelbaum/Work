from pin_generator import pin
import math
from multiprocessing import Pool
import functools

def make_chunks(data, num_chunks):
    chunk_size = math.ceil(len(data) / num_chunks)
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def create_number_list():
    num_list = [num for num in range(100, 1000000)]
    return num_list

def mapper(num_list):
    target = pin
    for num in num_list:
        if hash(bytes(num)) == target:
            print (num)
            return num

def reducer(chunk1, chunk2):
    chunk1.update(chunk2)
    return chunk1

def main():
    

    opt_pins = create_number_list()
    chunks = make_chunks(opt_pins, 5)

    with Pool(5) as pool:
        chunk_results = pool.map(mapper, chunks)
        return functools.reduce(reducer, chunk_results) 

if  __name__ == '__main__':
    main() 


