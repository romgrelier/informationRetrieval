from parser import indexCorpus

corpus = indexCorpus("corpus")
print(len(corpus))
for doc in corpus:
    print(doc.docno)
    