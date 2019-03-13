import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import defaultdict


plt.style.use('ggplot')

fig_1 = plt.figure(figsize=(8, 6))
ax_1 = fig_1.add_subplot(111)

en_dict = []
jp_dict = []

with open ('/afs/inf.ed.ac.uk/user/s18/s1873947/nmt_toolkit/graphs/train_en_data.csv', 'r') as f:
    en_len = [int(row[1]) for row in csv.reader(f,delimiter='#')]
    print ("Number of tokens in English",np.sum(en_len))
    for i in range(len(en_len)):
        en_words = [row[0] for row in csv.reader(f,delimiter='#')]
        print(en_words)
        for j in range(len(en_words)):
            en_dict[en_words[j]] += 1


with open ('/afs/inf.ed.ac.uk/user/s18/s1873947/nmt_toolkit/graphs/train_jp_data.csv', 'r') as f:
    jp_len = [int(row[1]) for row in csv.reader(f,delimiter=',')]
    print ("Number of tokens in Japanese",np.sum(jp_len))

#l_8=np.loadtxt('/afs/inf.ed.ac.uk/user/s18/s1873947/nmt_toolkit/graphs/train_en_data.csv', delimiter='#',skiprows=0, usecols=1)
#ax_1.plot(first_column[1:],'b.',label='Sentence lengths - English data')
colors = ['#E69F00', '#56B4E9']
names = ['English sentences','Japanese sentences']
ax_1.hist([en_len,jp_len],bins=100,color=colors,label=names)

#ax_1.set_xticklabels([i+1 for i in len(en_len)],rotation=60)
#ax_1.set_yticklabels(np.arange(0,len(en_len),50))
ax_1.set_xlabel('Sentence Length')
ax_1.set_ylabel('Frequency')

ax_1.legend(loc='upper right')
fig_1.savefig('Exp2_result_train.png')

