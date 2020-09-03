import os
import re
import sys
import time
from task2_functions import *
from task1_functions import *

# part 2
t_list = []

pattern_split = re.compile('[\\t,\\n]')
pattern = re.compile('[a-zA-z]')
dir_path = sys.argv[1]  # to be accepted through command line

docId = 0
token_position = 1
f = open("F:\\6th Semester Assignments\\termids.txt", mode="r", encoding="utf8")
for line in f:
    words = pattern_split.split(line)
    t_list.append(words[1])


pattern_split = re.compile('[\\W]')
inverted_index = inverted_index_template(t_list)
last_time = time.time()
file_list = os.listdir(dir_path)
# file_list = file_list[:100]
for file in file_list:
    docId += 1
    with open(dir_path + "\\" + file, "r", encoding="utf8") as fd:
        token_position = 1
        for line in fd:
            for word in pattern_split.split(pre_process(line)):  # separate at any non-alphanumeric character [^a-zA-Z0-9_]
                if not (not word) and pattern.match(word):
                    # asdfasfd
                    word = stem_word(word)
                    try:
                        index = t_list.index(word)
                        # index = get_index(t_list, word)
                        tup = inverted_index[index]
                        tup[3].append((docId, token_position))
                        inverted_index[index] = (index + 1, tup[1] + 1, 0, tup[3])
                    except ValueError:
                        pass
                    token_position += 1
        fd.close()  # close the opened file
    print("Document ID: ", docId)
    print("--- %s seconds ---" % (time.time() - last_time))  # print total time elapsed

inverted_index = delta_encoding(inverted_index)
write_term_index(inverted_index)
end = 0
