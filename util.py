from fileLoader import indexCorpus
from document import buildInvertedIndex
import re
from Algorithms.stemmer_algo import PorterStemmer

def merge_or(wordList, index):
    commonDocument = set()

    for word in wordList:
        if word in index:
            wordIndex = index[word][1:]
            for doc, _ in wordIndex:
                commonDocument.add(doc)

    return commonDocument


def merge_and(wordList, index):
    common_document = merge_or(wordList, index)

    for word in wordList:
        doc_presence = merge_or(word, index)

        common_document = common_document.intersection(doc_presence)

    return common_document


def make_query(query, index):
    query = re.sub("[{}()`\-.,;/'_0-9 \\n]+", '', query.lower()).split(' ')
    p = PorterStemmer()
    words = []

    for word in query:
        words.append(p.stem(word, 0, len(word) - 1))

    return merge_and(words, index)
