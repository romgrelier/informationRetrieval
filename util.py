from fileLoader import indexCorpus
from document import buildInvertedIndex
import re
from Algorithms.stemmer_algo import PorterStemmer

def get_document(word, index):
    documents = set()

    if word in index:
        for doc, _ in index[word][1:]:
            documents.add(doc)

    return documents

def merge_or(wordList, index):
    commonDocument = set()

    for word in wordList:
        commonDocument |= get_document(word, index)

    return commonDocument


def merge_and(wordList, index):
    common_document = get_document(wordList[0], index)

    for word in wordList[1:]:
        common_document &= get_document(word, index)

    return common_document


def make_query_and(query, index):
    query = query.lower()
    query = query.split(' ')

    p = PorterStemmer()
    words = []

    for word in query:
        words.append(p.stem(word, 0, len(word) - 1))

    return merge_and(words, index)

def make_query_or(query, index):
    query = query.lower()
    query = query.split(' ')

    p = PorterStemmer()
    words = []

    for word in query:
        words.append(p.stem(word, 0, len(word) - 1))

    return merge_or(words, index)
