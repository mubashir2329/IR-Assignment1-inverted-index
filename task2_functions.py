from bisect import bisect_left

from pip._vendor.requests import post


def inverted_index_template(terms_list: list) -> list:
    """Accepts list of terms and returns the template for inverted index
    inverted_index[(term_id, term_freq, doc_freq, list[(docId, pos)])]"""
    inverted_index = []
    for i in range(len(terms_list)):
        inverted_index.append((i + 1, 0, 0, []))
    return inverted_index


def delta_encoding(inverted_index: list) -> list:
    """Accepts inverted index list and apply delta encoding to it
    Updates the inverted_index and returns the same inverted_index"""
    for i in range(len(inverted_index)):  # each term
        posting_list = inverted_index[i][3].copy()
        doc_freq = 1
        pre_docId = 0
        current_docId = 0
        docId = 0
        for j in range(inverted_index[i][1]):  # each posting list
            docId = posting_list[j][0]
            if current_docId == 0:  # first document, # no encoding for posting
                current_docId = posting_list[j][0]  # docId (first) occurrence
                pre_docId = current_docId
                posting_list[j] = (current_docId, inverted_index[i][3][j][1])
                # inverted_index[i] = (inverted_index[i][0], inverted_index[i][1], inverted_index[i][2], posting_list)
            elif docId == current_docId:  # same document, encode posting list
                posting_list[j] = (0, inverted_index[i][3][j][1] - inverted_index[i][3][j - 1][1])  # docId will encode
                # to 0, position will be position - pre_position
            elif docId != current_docId:  # encode docId, position will remain same
                posting_list[j] = (docId - current_docId, inverted_index[i][3][j][1])
                current_docId = docId
                doc_freq += 1
        inverted_index[i] = (inverted_index[i][0], inverted_index[i][1], doc_freq, posting_list)
    return inverted_index


def write_term_index(inverted_index: list):
    """Takes inverted index and write it to term_index.txt in default directory"""
    try:
        term_index_txt = open("term_index.txt", mode='x', encoding='utf8')
    except FileExistsError:
        term_index_txt = open("term_index.txt", mode='w', encoding='utf8')
    for i in range(inverted_index.__len__()):
        term_index_txt.write(
            str(inverted_index[i][0]) + " " + str(inverted_index[i][1]) + " " + str(inverted_index[i][2]))
        for p in inverted_index[i][3]:
            term_index_txt.write(" " + str(p[0])+","+str(p[1]))
        term_index_txt.write('\n')


def get_index(my_list: list, word: str) -> int:
    """Accepts list of strings and returns the string index in list
    Performs binary search"""
    i = bisect_left(my_list, word)
    if i != len(my_list) and my_list[i] == word:
        return i
    else:
        return -1

