import random
import numpy as np
import gzip


def read_fasta(file):
    if file.endswith('.gz'):
        with gzip.open(file, 'rt') as f:
            data = f.read().split('>')
            data = [x for x in data if x != '']
            data = [x.split('\n') for x in data]
            data = [[x[0], ''.join(x[1:]).upper()] for x in data]
        return data
    else:
        with open(file, 'r') as f:
            data = f.read().split('>')
            data = [x for x in data if x != '']
            data = [x.split('\n') for x in data]
            data = [[x[0], ''.join(x[1:]).upper()] for x in data]
        return data

def get_kmers(seq, k):
    return [seq[i:i+k] for i in range(len(seq) - k + 1)]

def sim_reads(seq, read_length, num_reads, error_rate):
    kmers = get_kmers(seq, read_length)
    seed_reads = [random.choice(kmers) for i in range(num_reads)]

    reads = [] 

    for read in seed_reads:
        error_mask = np.random.poisson(error_rate, read_length)
        flips = np.where(error_mask == 1)[0]
        read_array = list(read)
        for flip in flips:
            new_char = random.choice('ACGT')
            read_array[flip] = new_char
        read = ''.join(read_array)
        reads.append(read)

    return reads
