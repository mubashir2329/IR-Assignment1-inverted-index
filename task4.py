import matplotlib.pyplot as plt
import os
import re
import math

file = open("F:\\6th Semester Assignments\\term_index.txt", mode='r', encoding='utf8')

f = open("F:\\6th Semester Assignments\\termids.txt", mode="r", encoding="utf8")
pattern_split = re.compile('[\\t,\\n]')
t_list = []
for line in f:
    words = pattern_split.split(line)
    t_list.append(words[1])

left = []
term_freq = []
pattern_split = re.compile('[\\W]')

for i in range(100):
    words = pattern_split.split(file.readline())
    term_freq.append((t_list[i], int(words[1]), math.log(int(words[1]), 10)))
    left.append(i + 1)
    i += 1
    print("working: " + str(i))
print("printing graph")
unzipped = list(zip(*term_freq))
# plt.bar(None, unzipped[1], tick_label=unzipped[0])
plt.bar(left, unzipped[1], tick_label=unzipped[0], width=0.8)
plt.xticks(rotation=90)
plt.xticks(fontsize=8)
plt.xlabel('words')
plt.ylabel('frequency')
plt.title('WORD FREQUENCY GRAPH')
plt.show()

plt.bar(left, unzipped[2], tick_label=unzipped[0], width=0.8)
plt.xticks(rotation=90)
plt.xticks(fontsize=8)
plt.xlabel('words')
plt.ylabel('log_frequency')
plt.title('WORD LOG_FREQUENCY GRAPH')
plt.show()

