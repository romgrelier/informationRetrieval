from fileLoader import indexCorpus
from document import buildInvertedIndex

corpus = indexCorpus("corpus")

words = buildInvertedIndex(corpus)

with open("output.txt", "w+") as file:
    for word, doc in words.items():
        file.write("%s : %s \n" % (word, doc))



#print (words)
        

#Wefeel : [2, (2188, 1), (2848, 1)]
Wefeel : [Corpus, (Doc, nbOccurrence)]

