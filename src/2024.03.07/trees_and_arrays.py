import heapq
import utils
import random
import numpy as np

CHILDREN = 1
SUB = 0

def add_suffix(nodes, suf):
    n = 0
    i = 0
    while i < len(suf):
        b = suf[i]
        x2 = 0
        while True:
            children = nodes[n][CHILDREN]
            if x2 == len(children):
                n2 = len(nodes)
                nodes.append( [suf[i:], []] )
                nodes[n][CHILDREN].append(n2)
                return
            n2 = children[x2]
            if nodes[n2][SUB][0] == b:
                break
            x2 = x2 + 1

        sub2 = nodes[n2][SUB]
        j = 0
        while j < len(sub2):
            if suf[i+j] != sub2[j]:
                n3 = n2
                n2 = len(nodes)
                nodes.append( [sub2[:j], [n3] ] )
                nodes[n3][SUB] = sub2[j:]
                nodes[n][CHILDREN][x2] = n2
                break
            j = j + 1
        i = i + j
        n = n2

def build_suffix_tree(text):
    if text[-1] != "$":
        text += "$"

    nodes = [ ['', []] ]

    for i in range(len(text)):
        add_suffix(nodes, text[i:])

    return nodes

def bfs(nodes, T):
    sa = []
    pq = [['', 0]]
    while pq:
        sub, n = heapq.heappop(pq)
        if len(nodes[n][CHILDREN]) == 0:
            sa.append(len(T) - len(sub) + 1)
        for child in nodes[n][CHILDREN]:
            heapq.heappush(pq, (sub + nodes[child][SUB], child))


        for first_char in nodes[n][CHILDREN]:
            child = nodes[n][CHILDREN][first_char]
            heapq.heappush(pq, (sub + nodes[child][SUB], child))


    return sa

def lcp(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i = i + 1
    return i

def bsearch(sa, q, T):
    T += '$'
    lo = -1
    hi = len(sa)
    mid = -1
    while ( hi - lo > 1):
        mid = int((hi+lo)/2)
        if T[sa[mid]:] < q:
            lo = mid
        else:
            hi = mid

    # hi is the insertion position
    if hi < 0:
        return 0
    elif hi > len(sa):
        return lcp(T[sa[hi - 1]:], q)
    else:
        return max( lcp(T[sa[hi-1]:], q), lcp(T[sa[hi]:], q))

def get_lcp(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i = i + 1
    return i

def bsearch_num_comps(sa, q, T):
    T += '$'
    lo = -1
    hi = len(sa)
    mid = -1
    num_comps = []
    while ( hi - lo > 1):
        mid = int((hi+lo)/2)
        num_comps.append(get_lcp(T[sa[mid]:], q))
        if T[sa[mid]:] < q:
            lo = mid
        else:
            hi = mid
    return np.median(num_comps)

T = utils.read_fasta('chr22.top.fa.gz')[0]
T = T[1]

#open up our_eng_db.txt and store it into T and remove new lines
#T = open('our_eng_db.txt').read()[:100000].replace('\n', '')

nodes = build_suffix_tree(T)
print('have the suffix tree')
sa = bfs(nodes, T)
print('have the suffix array')

# pick a random string of size p from the string T
len_P = 1000
R = []
for len_P in range(100,30000,1000):
#for len_P in range(100,1000,100):
    r = []
    for rounds in range(10):
        P_i = random.randint(0, len(T) - len_P)
        P = T[P_i:P_i+len_P]
        r.append(bsearch_num_comps(sa, P, T))
    R.append(r)

#make box plot and store into box.png
import matplotlib.pyplot as plt
#make the figure wider
plt.figure(figsize=(20, 5))
plt.boxplot(R)
plt.savefig('box.png')



# test if searchin suffix array is slowed down by long common prefixes
# in gentics
# look at a range of query sizes

#
#
#lcp  = bsearch(sa, "a$", T)

#print(lcp)
