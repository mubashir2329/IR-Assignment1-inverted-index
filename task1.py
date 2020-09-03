# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:33:38 2020

@author: muham
"""

import sys
import os
import re
import time
from task1_functions import *

pattern_split = re.compile('[\\W]')
pattern = re.compile('[a-zA-z]')
dir_path = sys.argv[1]  # to be accepted through command line

docId = 0
docIdMapping = []  # index number (index+1) is document id
totalWords = 0
dic = {}

token_pool = []     # token_pool = list(for each document) list of tokens (index will reflect position of token)
currentdoc = []     # save the tokens of current document being iterated
token_position = 1   # value of position/location of token in a file
last_time = time.time()
for file in os.listdir(dir_path):
    with open(dir_path + "\\" + file, "r", encoding="utf8") as fd:
        # token_pool.append(currentdoc)                                     # adding new document
        # token_position = 1                                                # reset position pointer
        for line in fd:
            for word in pattern_split.split(pre_process(line)):  # separate at non-alphanumeric character [^a-zA-Z0-9]
                if not (not word) and pattern.match(word):
                    if not dic.get(word):
                        dic[word] = 1
                    else:
                        dic[word] = dic[word] + 1   # calculating frequency of term
                    totalWords = totalWords + 1
                    # currentdoc.append((word, token_position))                              # adding token
                    # token_position = token_position + 1
        fd.close()  # close the opened file
        currentdoc = []
    docIdMapping.append(file)  # create the docId(index+1) and Doc Name list for docsid.txt
    docId = docId + 1
    print("Document ID: ", docId)
    print("--- %s seconds ---" % (time.time() - last_time))  # print total time elapsed

freq_list = sort_freq_dict(dic)                             # convert dict to list and sort list based on freq of terms
stopwords_list = get_stopwords(freq_list, 30)               # get list of stop words
reduced_list = remove_stopwords_sorted(freq_list, 30)       # remove stop words
terms_list = freq_list_to_terms_list(freq_list)             # get list of terms
stemmed_terms_list = stem_terms_list(terms_list)            # apply stemming
terms_list = remove_duplicates(terms_list)                  # remove duplicates from list of terms

write_docids(docIdMapping)                                  # write docids.txt
write_termids(terms_list)                                   # write termids.txt
print("completed")
print("Total words = ", totalWords)
print("Total Documents = ", docId)



