import string

from nltk.stem.snowball import EnglishStemmer
import re


def sort_freq_dict(freq_dic: dict) -> list:
    """convert dict to list and sort freq_list (descending order)
     Return sorted frequency list"""
    temp = [(freq_dic[key], key) for key in freq_dic]
    temp.sort()
    temp.reverse()
    return temp


def get_stopwords(sorted_freq_list: list, no_of_stopwords: int) -> list:
    """Accepts sorted frequency list (freq, term) and returns the list of stop words(freq, term)"""
    stopwords = sorted_freq_list[:no_of_stopwords]  # slice (get) first n elements sorted_freq_list[:n]
    return stopwords


def remove_stopwords_sorted(sorted_freq_list: list, no_of_stopwords: int) -> list:
    """Remove the stopwords from sorted frequency list (freq, term)
    Updates the sorted_freq_list to new reduced list
    and also returns the same updated sorted_freq_list(freq, term)"""
    del sorted_freq_list[:no_of_stopwords]
    return sorted_freq_list


def remove_stopwords(term_list: list, stopwords_list: list) -> list:
    """Remove stop words from unsorted term_list(terms, freq) (unsorted based on frequency)
    Updates term list and also returns the same updated list (term_list)"""
    for word_tuple in stopwords_list:
        term_list.remove((word_tuple[1], word_tuple[0]))
    return term_list


def freq_list_to_terms_list(freq_list: list) -> list:
    """Accepts freq_list (freq, terms) and returns terms_list(terms, freq)"""
    unzipped = list(zip(*freq_list))
    my_list = list(unzipped[1])
    # my_list.sort()
    return my_list


def stem_terms_list(terms_list: list) -> list:
    """stems the list of terms(terms) using snowball stemmer
    Update the terms_list and also returns same updated list"""
    stemmer = EnglishStemmer()
    for i in range(terms_list.__len__()):
        terms_list[i] = stemmer.stem(terms_list[i])
    return terms_list


def stem_word(word: str) -> str:
    """stems a single word(string)
    Returns the stemmed from of word """
    return EnglishStemmer().stem(word)


def remove_duplicates(terms_list: list) -> list:
    """accepts list and remove duplicate values and returns the new list"""
    return list(dict.fromkeys(terms_list))


def write_docids(docNames: list):
    """Accepts doc names list (docids) and write docId and DocName in default directory
    docId is index+1 of list"""
    try:
        docId_txt = open("docsid.txt", mode='x', encoding='utf8')
    except FileExistsError:
        docId_txt = open("docsid.txt", mode='w', encoding='utf8')
    for i in range(docNames.__len__()):
        docId_txt.write(str(i+1) + "\t" + docNames[i] + '\n')


def write_termids(terms_list: list):
    """Accepts terms_list (names) and writes termsId (index+1) of terms_list and term
    in default directory"""
    try:
        termids_txt = open("termids.txt", mode='x', encoding='utf8')
    except FileExistsError:
        termids_txt = open("termids.txt", mode='w', encoding='utf8')
    for i in range(terms_list.__len__()):
        termids_txt.write(str(i + 1) + "\t" + terms_list[i] + '\n')


def pre_process(text: str) -> str:
    """Accepts a string and apply pre processing steps
    and returns the list"""
    text.lower()                                                # convert string to lower case
    text = re.sub(r'\d+', '', text)                             # remove digits
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)                           # remove punctuations
    return text
