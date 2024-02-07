import tracemalloc
import time
import numpy as np
import random
import argparse
import matplotlib.pyplot as plt

def ns(P, T):
    occurrences = []
    n = len(T)
    m = len(P)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if T[i + j] != P[j]:
                match = False
                break
        if match:
            occurrences.append(i)

    return occurrences



def get_random_string(alphabet, length):
    return ''.join(random.choice(alphabet) for i in range(length))

def get_random_substring(string, length):
    if length > len(string):
        raise ValueError("Length of substring is longer than the string.")

    start_index = random.randint(0, len(string) - length)
    return string[start_index:start_index + length]

def run_test(test_function, T, P):
    start = time.monotonic_ns()
    r = test_function(T, P)
    stop = time.monotonic_ns()

    tracemalloc.start()
    r = test_function(T, P)
    mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return stop - start, mem[1] - mem[0]

def test_harness(test_functions,
                 text_size_range,
                 pattern_size,
                 rounds):

    run_times = [ [] for _ in range(len(test_functions))]
    mem_usages = [ [] for _ in range(len(test_functions))]

    for text_size in text_size_range:

        _run_times = [ [] for _ in range(len(test_functions))]
        _mem_usages = [ [] for _ in range(len(test_functions))]

        for i in range(rounds):
            T = get_random_string(['A', 'C', 'T', 'G'], text_size)
            P = get_random_substring(T, pattern_size)

            for j, test_function in enumerate(test_functions):
                run_time, mem_usage = run_test(test_function, T, P)
                _run_times[j].append(run_time)
                _mem_usages[j].append(mem_usage)

        for j, test_function in enumerate(test_functions):
            run_times[j].append(np.mean(_run_times[j]))
            mem_usages[j].append(np.mean(_mem_usages[j]))

    return run_times, mem_usages


def get_bad_char_table(P):
    import copy

    occurances = {}
    bct = []
    for i in range(len(P)):
        occurances[P[i]] = i
        bct.append(copy.deepcopy(occurances))
    return bct

def bctl(bct, bad_char, idx, len_P):

    if bad_char in bct[idx]: # char in the prefix
        return (idx - bct[idx][bad_char]) + (len_P - idx - 1)

    #else: #totaly new char

 def ns_bc(P, T):
    occurrences = []
    n = len(T)
    m = len(P)

    bct = get_bad_char_table(P)

    shift = 1

    for i in range(n - m + 1):
        match = True
        for j in range(len(P)-1, -1, -1):
            if T[i + j] != P[j]:
                match = False
                break
        if match:
            occurrences.append(i)

    return occurrences

       

if __name__ == '__main__':
    #    012345678901234567890
    #T = 'ACCTGTACCGTCAGGTAACCG'
    #P = 'ACCG'
    #text_size = 20000000
    #pattern_size = 100
    #T = get_random_string(['A', 'C', 'T', 'G'], text_size)
    #P = get_random_substring(T, pattern_size)
    ## 6 and 17
    #r = ns(P,T)
    #print(r)

    
    bct = get_bad_char_table('GCTACTA')

    
    P = 'GCTACTA'

    bad_char = 'C'
    idx = 3
    print( bctl(bct, bad_char, idx, len(P)))

    bad_char = 'C'
    idx = 5
    print( bctl(bct, bad_char, idx, len(P)))

    bad_char = 'G'
    idx = 6
    print( bctl(bct, bad_char, idx, len(P)))


#    text_size_range =  range(100000, 5000000, 100000)
#
#    test_functions = [ns]
#
#    pattern_size = 10000
#    rounds = 5
#    run_times, mem_usages = test_harness(test_functions,
#                                         text_size_range,
#                                         pattern_size,
#                                         rounds)
#    
#    fig, ax = plt.subplots(2, 1)
#    ax[0].plot(text_size_range, run_times[0], label='Naive')
#    ax[0].set_title('Run Time')
#    ax[0].set_xlabel('Text Size')
#    ax[0].set_ylabel('Time (ns)')
#    ax[0].legend()
#    ax[1].plot(text_size_range, mem_usages[0], label='Naive')
#    ax[1].set_title('Memory Usage')
#    ax[1].set_xlabel('Text Size')
#    ax[1].set_ylabel('Memory (bytes)')
#    ax[1].legend()
#    plt.tight_layout()
#    plt.savefig('naive.png')
#
#    print(run_times)
#    print(mem_usages)
#
