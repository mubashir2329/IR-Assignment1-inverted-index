import linecache
import sys
from builtins import print

from task1_functions import *

pattern_split = re.compile('[\\W]')
pattern = re.compile('[a-zA-z]')

try:
    f = open("F:\\6th Semester Assignments\\termids.txt", mode="r", encoding="utf8")
except:
    print("Error while opening file")

t_list = []
for line in f:
    words = pattern_split.split(line)
    t_list.append(words[1])

term = sys.argv[2]
stemmed_term = stem_word(term)
try:
    index = t_list.index(stemmed_term)
except ValueError:
    print("Value Error")

line = linecache.getline("F:\\6th Semester Assignments\\term_index.txt", index+1)
line = pattern_split.split(line)
print("Listing for term: " + stemmed_term)
print("TERMID: " + str(line[0]))
print("Number of documents containing term: " + str(line[2]))
print("Term frequency in corpus: " + str(line[1]))

