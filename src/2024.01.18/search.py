import random
import numpy as np
import time
import tracemalloc
import bisect

word_file = 'words'

D = [] # database 
Q = [] # query 

def load_words():
    D = []
    with open(word_file, 'r') as f:
        for line in f:
            D.append(line.strip())
    return D

W = load_words()

def get_word_subset(W, n):
    return random.sample(W, n)

def check_sorted():
    # we dont get sorted subsets
    for i in range(1000):
        c = get_word_subset(W, 1000)
        c_sort = sorted(c)
        if c == c_sort:
            print('Found sorted subset')

def check_repeats():
    # we dont get the same subsets
    r = None
    for i in range(100):
        print(i)
        c = get_word_subset(W, 200000)
        c = sorted(c)
        if r == c :
            print('Found duplicate subset')
        r = c

def linear_search(Q, D):
    hits = 0
    for q in Q:
        for d in D:
            if d == q:
                hits += 1
                break
    return hits

def binary_search(Q, D):
    hits = 0
    D.sort()

    for q in Q:
        i = bisect.bisect_left(D, q)
        if i < len(D) and D[i] == q:
            hits += 1

    return hits


def binary_search_plus(Q, D):
    hits = 0
    Q.sort()
    D.sort()

    for q in Q:
        i = bisect.bisect_left(D, q)
        if i < len(D) and D[i] == q:
            hits += 1

    return hits

d_size = 200000

def run_a_search(f, Q, D):
    return f(Q,D)

for q_size in range(1,10,1):
    all_trials_time_bsp = []
    all_trials_mem_bsp = []
    all_trials_time_bs = []
    all_trials_mem_bs = []
    for trial in range(10):
        Q = get_word_subset(W, q_size)
        D = get_word_subset(W, d_size)

        
        start = time.monotonic_ns()
        r = run_a_search(binary_search_plus, Q, D)

        r = run_a_search(binary_search, Q, D)
        r = run_a_search(binary_search_plus, Q, D)
        r = run_a_search(binary_search_plus, Q, D)

        end = time.monotonic_ns()

        all_trials_time_bsp.append(end-start)

        start = time.monotonic_ns()
        r = run_a_search(binary_search, Q, D)
        end = time.monotonic_ns()
        all_trials_time_bs.append(end-start)


    print(q_size, 
          np.mean(all_trials_time_bs), 
          np.mean(all_trials_time_bsp),
          np.mean(all_trials_time_bs)  - np.mean(all_trials_time_bsp))
    #print(q_size, np.mean(all_trials_mem_ls), np.mean(all_trials_time_bs))
