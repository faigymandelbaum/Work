#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
file_names = os.listdir("wiki")
print (len(file_names))


# In[2]:


with open(os.path.join("wiki", file_names[0])) as f:
    print(f.read())


# ### Adding the MapReduce Framework

# In[3]:


import math
import functools
from multiprocessing import Pool

def make_chunks(data, num_chunks):
    chunk_size = math.ceil(len(data) / num_chunks)
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

def map_reduce(data, num_processes, mapper, reducer):
    chunks = make_chunks(data, num_processes)
    pool = Pool(num_processes)
    chunk_results = pool.map(mapper, chunks)
    return functools.reduce(reducer, chunk_results)

def map_line_count(file_names):
    total = 0
    for fn in file_names:
        with open(os.path.join("wiki", fn)) as f:
            total += len(f.readlines())
    return total
    
def reduce_line_count(count1, count2):
    return count1 + count2

target = "data"
map_reduce(file_names, 8, map_line_count, reduce_line_count)


# In[4]:


def map_grep(file_names):
    results = {}
    for fn in file_names:
        with open(fn) as f:
            lines = [line for line in f.readlines()]
        for line_index, line in enumerate(lines):
            if target in line:
                if fn not in results:
                    results[fn] = []
                results[fn].append(line_index)
    return results

def reduce_grep(lines1, lines2):
    lines1.update(lines2)
    return lines1

def mapreduce_grep(path, num_processes):
    file_names = [os.path.join(path, fn) for fn in os.listdir(path)]
    return map_reduce(file_names, num_processes,  map_grep, reduce_grep)


# In[5]:


target = "data"
data_occurrences = mapreduce_grep("wiki", 8)


# ### Grep Case Insensitive

# In[6]:


def map_grep(file_names):
    results = {}
    for fn in file_names:
        with open(fn) as f:
            lines = [line.lower() for line in f.readlines()]
        for line_index, line in enumerate(lines):
            if target.lower() in line:
                if fn not in results:
                    results[fn] = []
                results[fn].append(line_index)
    return results


# In[7]:


target = "data"
new_data_occurrences = mapreduce_grep("wiki", 8)


# ### Checking the Implementation

# In[8]:


for fn in new_data_occurrences:
    if fn not in data_occurrences:
        print("Found {} new matches on file {}".format(len(new_data_occurrences[fn]), fn))
    elif len(new_data_occurrences[fn]) > len(data_occurrences[fn]):
        print("Found {} new matches on file {}".format(len(new_data_occurrences[fn]) - len(data_occurrences[fn]), fn))


# ### Finding Match Positions on Lines

# In[17]:


def find_match_indexes(line, target):
    results = []
    i = line.find(target, 0)
    while i != -1:
        results.append(i)
        i = line.find(target, i + 1)
    return results


# In[20]:


def map_grep_match_indexes(file_names):
    results = {}
    for fn in file_names:
        with open(fn) as f:
            lines = [line.lower() for line in f.readlines()]
        for line_index, line in enumerate(lines):
            match_indexes = find_match_indexes(line, target.lower())
            if fn not in results:
                results[fn] = []
            results[fn] += [(line_index, match_index) for match_index in match_indexes]
    return results

def mapreduce_grep_match_indexes(path, num_processes):
    file_names = [os.path.join(path, fn) for fn in os.listdir(path)]
    return map_reduce(file_names, num_processes,  map_grep_match_indexes, reduce_grep)

target = "science"
occurrences = mapreduce_grep_match_indexes("wiki", 8)


# ### Displaying the Results

# In[21]:


import csv

# How many character to show before and after the match
context_delta = 30

with open("results.csv", "w") as f:
    writer = csv.writer(f)
    rows = [["File", "Line", "Index", "Context"]]
    for fn in occurrences:
        with open(fn) as f:
            lines = [line.strip() for line in f.readlines()]
        for line, index in occurrences[fn]:
            start = max(index - context_delta, 0)
            end   = index + len(target) + context_delta
            rows.append([fn, line, index, lines[line][start:end]])
    writer.writerows(rows)


# In[22]:


import pandas as pd
pd.read_csv('results.csv')


# In[ ]:




