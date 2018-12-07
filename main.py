from fileLoader import indexCorpus
from document import buildInvertedIndex

from functionsForParser import *

corpus = indexCorpus("corpus")

indexWords = buildInvertedIndex(corpus)

with open("output.txt", "w+") as file:
    for word, doc in indexWords.items():
        file.write("%s : %s \n" % (word, doc))



#print (words)
#Wefeel : [2, (2188, 1), (2848, 1)]
#Wefeel : [Corpus, (Doc, nbOccurrence)]
#'Ocean': [3, (7, 1), (11, 1), (49, 1)],
#'years.': [2, (34, 1), (57, 2)]

print(indexWords)
print("\n");
print("Ocean a 1 occurence dans 3 documents")
print("years a 3 occurence dans 2 documents")
print("\nTerm_freq by document ");
print ("\tOcean: " + str(score_documents_term_frequency(indexWords,7, "Ocean")));
print ("\tyears: " + str(score_documents_term_frequency(indexWords,57, "years.")));
#sdtf_ocean = score_documents_term_frequency(indexWords,7, "Ocean");
#sdtf_year = score_documents_term_frequency(indexWords,57, "years.");

print("\nDocument_frequency ");
print ("\tOcean: " + str(document_frequency(indexWords, "Ocean")));
print ("\tyears: " + str(document_frequency(indexWords, "years.")));

print("\nInverse document_frequency ");
print ("\tOcean: " + str(inverse_document_frequency(corpus,indexWords, "Ocean")));
print ("\tyears: " + str(inverse_document_frequency(corpus, indexWords, "years.")));

print("\ntf_idf");
print ("\tOcean: " + str(tf_idf(corpus,indexWords,7, "Ocean")));
print ("\tyears: " + str(tf_idf(corpus, indexWords,57, "years.")));

print("\nvector_tf_idf");
#print ("\tOcean: " + str(vector_tf_idf_one_doc(corpus,indexWords,7, "Ocean")));
#print ("\tyears: " + str(vector_tf_idf_one_doc(corpus, indexWords,57, "years.")));

print(vector_tf_idf_one_doc(corpus, 7))