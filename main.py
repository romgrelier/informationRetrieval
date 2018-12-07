from fileLoader import indexCorpus
from document import buildInvertedIndex
from query import make_query

corpus = indexCorpus("corpus")

index = buildInvertedIndex(corpus)

with open("output.txt", "w+") as file:
    for word, doc in index.items():
        file.write("%s : %s \n" % (word, doc))


def merge_or(wordList, index):
    commonDocument = set()

    for word in wordList:

        wordIndex = index[word][2:]
        for doc, _ in wordIndex:
            commonDocument.add(doc)

    return commonDocument


def merge_and(wordList, index):
    common_document = merge_or(wordList, index)

    for word in wordList:
        doc_presence = set()

        wordIndex = index[word][2:]
        for doc, _ in wordIndex:
            doc_presence.add(doc)

        common_document = common_document.intersection(doc_presence)

    return common_document



print("MERGE OR\n")
commonDocument = merge_or(["rule", "spent", "revel"], index)

print("MERGE AND\n")
and_document = merge_and(["rule", "spent"], index)

