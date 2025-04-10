import pysam
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def most_common_char(char_list):
    if not char_list:
        return None  # or raise an exception if preferred
    count = Counter(char_list)
    return count.most_common(1)[0][0]

# Path to your BAM file
bam_file = "SRR413984.sorted.NC_000001.10.bam"
# Open the BAM file


min_threshold = 50
max_threshold = 200
min_num_chars = 15
min_char_density = 0.75

# 956749

window_size = []

def get_clipped_seq(read):
    clipped_seq = ''
    pos = 0
    for op, length in read.cigartuples:
        if op == 4:  # Soft clip
            clipped_seq += read.query_sequence[pos:pos+length]
            pos += length
        elif op == 0:
            pos += length
    return clipped_seq

def count_matching_chars(char, char_list):
    count = 0
    for c in char_list:
        if c == char:
            count += 1
    return count

def get_consensus(seq_list):
    consensus = {}
    for seq in seq_list:
        for i in range(len(seq)):
            if i not in consensus:
                consensus[i] = []
            consensus[i].append(seq[i])
    S = ''
    for i in sorted(consensus.keys()):
        mcc = most_common_char(consensus[i])
        mcc_count = count_matching_chars(mcc, consensus[i])
        density = count_matching_chars(mcc, consensus[i])/len(consensus[i])
        if mcc_count >= min_num_chars and density >= min_char_density:
            S += mcc
    return S


with pysam.AlignmentFile(bam_file, "rb") as bam:
    start_window = []
    end_window = [] 
    for read in bam:
        if read.cigartuples[0][0] == 4: # 4 is a soft clip
            if len(start_window) == 0:
                start_window.append((read.pos, get_clipped_seq(read)))
            elif read.pos == start_window[0][0]:
                start_window.append((read.pos, get_clipped_seq(read)))
            else:
                if len(start_window) > min_threshold and len(start_window) < max_threshold:
                    print(len(start_window), start_window[0], '+')
                    s_s = get_consensus([s[1][::-1] for s in start_window])
                    s_s = s_s[::-1]
                    print(s_s)
                start_window = [(read.pos, get_clipped_seq(read))]
        elif read.cigartuples[-1][0] == 4: # 4 is a soft clip
            circle_end = read.pos + read.cigartuples[0][1]
            if len(end_window) == 0:
                end_window.append((circle_end, get_clipped_seq(read)))
            elif circle_end == end_window[0][0]:
                end_window.append((circle_end, get_clipped_seq(read)))
            else:
                if len(end_window) > min_threshold and len(end_window) < max_threshold:
                    print(len(end_window), end_window[0], '-')
                    s_e = get_consensus([s[1] for s in end_window])
                    print(s_e)

                end_window = [(circle_end, get_clipped_seq(read))]

