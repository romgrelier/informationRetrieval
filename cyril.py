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
#commonDocument = merge_or(["rule", "spent", "revel"], index)

print("MERGE AND\n")
and_document = merge_and(["rule", "spent"], index)


print(and_document)

ocean_doc = 40;
year_doc = 9;

print(index)
print("\n");
print("Ocean a 1 occurence dans 3 documents")
print("years a 3 occurence dans 2 documents")
print("\nTerm_freq by document ");
print ("\tOcean: " + str(score_documents_term_frequency(index,ocean_doc, "ocean")));
print ("\tyears: " + str(score_documents_term_frequency(index,year_doc, "years")));
#sdtf_ocean = score_documents_term_frequency(indexWords,7, "Ocean");
#sdtf_year = score_documents_term_frequency(indexWords,57, "years.");

print("\nDocument_frequency ");
print ("\tOcean: " + str(document_frequency(index, "ocean")));
print ("\tyears: " + str(document_frequency(index, "years")));

print("\nInverse document_frequency ");
print ("\tOcean: " + str(inverse_document_frequency(corpus,index, "ocean")));
print ("\tyears: " + str(inverse_document_frequency(corpus, index, "year")));

print("\ntf_idf");
print ("\tOcean: " + str(tf_idf(corpus,index,ocean_doc, "ocean")));
print ("\tyears: " + str(tf_idf(corpus, index,year_doc, "year")));

print("\nvector_tf_idf");
print ("\tDoc: "+ str(ocean_doc) + str(vector_tf_idf(corpus, index, ocean_doc)));
print ("\tDoc: " + str(year_doc) + str(vector_tf_idf(corpus, index, year_doc)));

print("\nNormalized_vector");
vector_tf_ifd_doc1 = vector_tf_idf(corpus, index, ocean_doc);
vector_tf_ifd_doc2 = vector_tf_idf(corpus, index, year_doc);
print ("\tDoc: " + str(ocean_doc) + str(l2_normalization_vector(vector_tf_ifd_doc1)));
print ("\tDoc: "+ str(year_doc) +  str(l2_normalization_vector(vector_tf_ifd_doc2)));

print("\nCosine Similarity");

print ("\tDoc: "+ str(ocean_doc)  + str(l2_normalization_vector(vector_tf_ifd_doc1)));
print ("\tDoc: "+ str(year_doc)  + str(l2_normalization_vector(vector_tf_ifd_doc2)));

