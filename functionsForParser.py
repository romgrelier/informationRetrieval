import math;
import numpy as np;
import numbers;


#TERM FREQUENCY:





def term_frequency(word):
    if type(word) == int:
        if word <= 0:
            return 0;
        else:
            return 1 + math.log(word,10);
    else:
        return 0;




def term_frequency2(index,nodoc, query):
    val = 0
    for key, values in index.items():
        if key == query:
            temp = values.copy()
            temp.pop(0)
            for doc in temp:
                if doc[0]==nodoc:
                    val =doc[1]
    if val == 0:
        return 0
    else:
        return 1 + math.log(val,10)





def score_documents_term_frequency_old(documents,document,query):
    sum=0;
    for key,values in documents.items():
        if key == query:
            temps = values.copy();
            temps.pop(0);
            for docs in temps:
                if docs[0]==document:
                    #print(str(query)+ " : "+str(term_frequency(docs[1])));
                    sum+= term_frequency(docs[1]);
    return sum;


def score_documents_term_frequency(index,document,query):
    sum=0;
    for key,values in index.items():
        if key == query:
            temps = values.copy();
            temps.pop(0);
            for docs in temps:
                if docs[0]==document:
                    #print(str(query)+ " : "+str(term_frequency(docs[1])));
                    sum+= term_frequency(docs[1]);
    return sum;


#DOCUMENT FREQUENCY:
def document_frequency(index, query):
    for key, values in index.items():
        if key == query:
            return values[0];
    return 0;

def inverse_document_frequency(corpus, indexWords, query):
    '''
    if documents.__len__() == 0:
        return 0;
    '''
    #print("\ttaille document: "  +str(documents.__len__()) );
    if document_frequency(indexWords,query) !=0:

        return math.log((corpus.__len__()/document_frequency(indexWords,query)), 10)
    else:
        return 0;


def tf_idf(corpus,indexWords, numDocument, query):
    for key,values in indexWords.items():
        if key == query:
            temps = values.copy();
            temps.pop(0);
            for docs in temps:
                if docs[0]==numDocument:
                    #print ("\tTF: " +str(term_frequency(docs[1])))
                    return term_frequency(docs[1]) * inverse_document_frequency(corpus, indexWords, query)
    return 0


def tf_idf2(corpus, index,nodoc, query):
    return term_frequency2(index,nodoc, query) * inverse_document_frequency(corpus, index, query)

def tf_idf_opti(corpus,indexWords, numDocument, query):
    for key,values in indexWords.items():
        if key == query:
            temps = values.copy()
            doc_freq = temps[0]
            #print("Query: ", str(query), " | Key: " , str(key), " | Value: ", str(values),"| Doc freq: " , str(doc_freq))
            temps.pop(0);
            for docs in temps:
                if docs[0]==numDocument:
                    #print ("\tTF: " +str(term_frequency(docs[1])))

                    return term_frequency(docs[1]) *  math.log(   (corpus.__len__() / doc_freq)   , 10)
    return 0




def print_documents_to_tf_idf_vector(documents):
    compteur =0
    for document in documents:
        print("DOCUMENT: "+ str(compteur))
        for query in document:
            print( "\t" +query + " | tf_idf: "+  str( tf_idf(documents,document,query) ))
        compteur=compteur+1
    return  True


#VECTOR & NORMALISATION:

def vector_tf_idf(corpus,index,document):
    vector = []
    for word in corpus[document].text.split():
        #print("dans le tf:" + str(document) + str(tf_idf(corpus,index,document,word)))
        vector.append(tf_idf(corpus,index,document,word))
    return vector


def vector_tf_idf_opti(corpus,index,document):
    vector = []
    for word in corpus[document].text.split():
        liste_docs = index.get(word)
        if liste_docs != None:
            temps = liste_docs.copy()
            doc_freq = temps[0]
            temps.pop(0)
            for docs in temps:
                if docs[0] == document:
                    vector.append( term_frequency(docs[1]) *  math.log(   (corpus.__len__() / doc_freq)   , 10))
    return vector




def l2_normalization_vector(vector):
    vector_normalized =0;
    sum = 0;
    for values in vector:
        if isinstance(values, numbers.Number) :
            sum = sum+values;
    vector_normalized = math.sqrt(sum);
    return vector_normalized




