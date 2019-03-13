import numpy as np
import csv
from collections import defaultdict
import string


en_dict = defaultdict(int)
jp_dict = defaultdict(int)
i = 0
en_unk=0
en_sum=0
unk=0
jp_unk=0
jp_sum=0

with open ('/afs/inf.ed.ac.uk/user/s18/s1873947/nmt_toolkit/graphs/test_theja.txt', 'r') as f:
    for row in csv.reader(f):
        words = row[0].strip().split()
        for i in range(len(words)):
            keys = words[i]
            en_dict[keys] += 1
print("Word tokens in English data",len(en_dict))
for key,values in en_dict.items():
    en_sum += values
    print("keys=",key,"values=",values)
    if en_unk == 1:
        unk +=1
print("Word types in English data",en_sum)
print("Number of tokens in english to be replaced by <UNK> are:",unk)
print(en_dict)
'''
en_freq_high = {k: en_dict[k] for k in list(sorted(en_dict, key=en_dict.get, reverse=True))[:10]}
print(en_freq_high)

with open ('/afs/inf.ed.ac.uk/user/s18/s1873947/nmt_toolkit/raw_data/train.jp', 'r') as j:
    for line in csv.reader(j):
        words = line[0].split(' ')
        for i in range(len(words)):
            jp_dict[words[i]] += 1
print("Word tokens in Japanese data",len(jp_dict))
unk=0
for jp_unk in jp_dict.values():
    jp_sum += jp_unk
    if jp_unk == 1:
        unk +=1
print("Word types in Japanese data",jp_sum)
print("Number of tokens in Japanese to be replaced by <UNK> are:",unk)
'''
