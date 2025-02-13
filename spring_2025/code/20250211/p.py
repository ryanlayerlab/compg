import utils
import sw

fa_file = 'chr22.fa.gz'

#this is toooo big
k = 10

# Load the reference genome
genome = utils.read_fasta(fa_file)

kmers = utils.get_kmers(genome[0][1], k)

H = {}

for i, kmer in enumerate(kmers):
    if kmer not in H:
        H[kmer] = []
    H[kmer].append(i)

#def sim_reads(seq, read_length, num_reads, error_rate):

l = 100

R = utils.sim_reads(genome[0][1], l, 10, 0.1)

for r in R:
    r_kmers = utils.get_kmers(r, k)
    alignments = []
    for i, r_kmer in enumerate(r_kmers):
        if r_kmer in H:
            for p in H[r_kmer]:
                prefix = genome[0][1][p-i:p]
                suffix = genome[0][1][p:p+l-i]
                ref_seq = prefix + suffix
                # get number of matching character in ref_seq and r
                hits = len([1 for i in range(l) if ref_seq[i] == r[i]])
                if hits < 95:
                    continue
                sw_score = sw.sw(ref_seq, r, -1, -1, 1)[0]
                alignments.append((p-i, sw_score))
    # get the alignment with the max score
    try:
        max_alignment = sorted(alignments, key=lambda x: x[1], reverse=True)[0]
        print('max_alignment:', max_alignment)
        print(r)
        print(genome[0][1][max_alignment[0]:max_alignment[0]+l])
    except:
        print('no alignment found')



            #print('found:', r_kmer, H[r_kmer])
        #def sw(A, B, gap, miss, match):
#sizes = []

#for kmer in H:
#    sizes.append(len(H[kmer]))
#
#
#import matplotlib.pyplot as plt
#
#height = 5
#width = 10
#fig, ax = plt.subplots(figsize=(width, height))
#ax.hist(sizes, bins=100, color='blue', alpha=0.7)
## make the y scale log
#ax.set_yscale('log')
## set x min and max
#
#import numpy as np
#
#print('mean:', np.mean(sizes))
#print('median:', np.median(sizes))
#
#plt.tight_layout()
#plt.savefig('hist.png')
#
#
#


