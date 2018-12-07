from fileLoader import indexCorpus
from document import buildInvertedIndex

corpus = indexCorpus("corpus")

words = buildInvertedIndex(corpus)

with open("output.txt", "w+") as file:
    for word, doc in words.items():
        file.write("%s : %s \n" % (word, doc))
        
