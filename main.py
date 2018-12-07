from fileLoader import indexCorpus
from document import buildInvertedIndex

from functionsForParser import *

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


print(and_document)

print(index)
print("\n");
print("Ocean a 1 occurence dans 3 documents")
print("years a 3 occurence dans 2 documents")
print("\nTerm_freq by document ");
print ("\tOcean: " + str(score_documents_term_frequency(index,169, "Ocean")));
print ("\tyears: " + str(score_documents_term_frequency(index,57, "years.")));
#sdtf_ocean = score_documents_term_frequency(indexWords,7, "Ocean");
#sdtf_year = score_documents_term_frequency(indexWords,57, "years.");

print("\nDocument_frequency ");
print ("\tOcean: " + str(document_frequency(index, "Ocean")));
print ("\tyears: " + str(document_frequency(index, "years.")));

print("\nInverse document_frequency ");
print ("\tOcean: " + str(inverse_document_frequency(corpus,index, "Ocean")));
print ("\tyears: " + str(inverse_document_frequency(corpus, index, "years.")));

print("\ntf_idf");
print ("\tOcean: " + str(tf_idf(corpus,index,169, "Ocean")));
print ("\tyears: " + str(tf_idf(corpus, index,57, "years.")));

print("\nvector_tf_idf");
print ("\tDoc 169: " + str(vector_tf_idf(corpus, index, 169)));
#print ("\tDoc X: " + str(vector_tf_idf(corpus, index, 169)));

print("\nNormalized_vector");
vector_tf_ifd_doc_169 = vector_tf_idf(corpus, index, 169);
print ("\tDoc 169: " + str(l2_normalization_vector(vector_tf_ifd_doc_169)));
#print ("\tDoc X: " + str(vector_tf_idf(corpus, index, 169)));

