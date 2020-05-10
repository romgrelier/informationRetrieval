import math
import numpy as np
import numbers
from util import *
from document import *


def term_frequency(word):
    if type(word) == int:
        if word <= 0:
            return 0
        else:
            return 1 + math.log(word, 10)
    else:
        return 0


def term_frequency2(index, nodoc, query):
    val = 0
    for key, values in index.items():
        if key == query:
            temp = values.copy()
            temp.pop(0)
            for doc in temp:
                if doc[0] == nodoc:
                    val = doc[1]
    if val == 0:
        return 0
    else:
        return 1 + math.log(val, 10)


def score_documents_term_frequency_old(documents, document, query):
    sum = 0
    for key, values in documents.items():
        if key == query:
            temps = values.copy()
            temps.pop(0)
            for docs in temps:
                if docs[0] == document:
                    #print(str(query)+ " : "+str(term_frequency(docs[1])));
                    sum += term_frequency(docs[1])
    return sum


def score_documents_term_frequency(index, document, query):
    sum = 0
    for key, values in index.items():
        if key == query:
            temps = values.copy()
            temps.pop(0)
            for docs in temps:
                if docs[0] == document:
                    #print(str(query)+ " : "+str(term_frequency(docs[1])));
                    sum += term_frequency(docs[1])
    return sum


# DOCUMENT FREQUENCY:
def document_frequency(index, query):
    liste_docs = index.get(query)
    if liste_docs != None:
        return liste_docs[0]
    return 0


def inverse_document_frequency(corpus, indexWords, query):
    '''
    if documents.__len__() == 0:
        return 0;
    '''
    #print("\ttaille document: "  +str(documents.__len__()) );
    if document_frequency(indexWords, query) != 0:

        return math.log((corpus.__len__()/document_frequency(indexWords, query)), 10)
    else:
        return 0


def tf_idf(corpus, indexWords, numDocument, query):
    for key, values in indexWords.items():
        if key == query:
            temps = values.copy()
            temps.pop(0)
            for docs in temps:
                if docs[0] == numDocument:
                    #print ("\tTF: " +str(term_frequency(docs[1])))
                    return term_frequency(docs[1]) * inverse_document_frequency(corpus, indexWords, query)
    return 0


def tf_idf2(corpus, index, nodoc, query):
    return term_frequency2(index, nodoc, query) * inverse_document_frequency(corpus, index, query)


def tf_idf_opti(corpus, index, numDocument, query):

    liste_docs = index.get(query)
    if liste_docs != None:
        doc_freq = liste_docs[0]
        liste_docs = liste_docs[1:]
        for docs in liste_docs:
            if docs[0] == numDocument:
                return term_frequency(docs[1]) * math.log((corpus.__len__() / doc_freq), 10)
    return 0


def print_documents_to_tf_idf_vector(documents):
    compteur = 0
    for document in documents:
        print("DOCUMENT: " + str(compteur))
        for query in document:
            print("\t" + query + " | tf_idf: " +
                  str(tf_idf(documents, document, query)))
        compteur = compteur+1
    return True


# VECTOR & NORMALISATION:

def vector_tf_idf(corpus, index, document):
    vector = []
    for word in corpus[document].text.split():
        #print("dans le tf:" + str(document) + str(tf_idf(corpus,index,document,word)))
        vector.append(tf_idf(corpus, index, document, word))
    return vector


def vector_tf_idf_opti(corpus, index, document):
    vector = []

    for word in corpus[document].text.split():
        liste_docs = index.get(word)
        if liste_docs != None:
            doc_freq = liste_docs[0]
            liste_docs = liste_docs[1:]
            for docs in liste_docs:
                if docs[0] == document:
                    vector.append(term_frequency(
                        docs[1]) * math.log((corpus.__len__() / doc_freq), 10))

    return vector


def l2_normalization_vector(vector):
    vector_normalized = 0
    sum = 0
    for values in vector:
        if isinstance(values, numbers.Number):
            sum = sum+values
    vector_normalized = math.sqrt(sum)
    return vector_normalized


# COSINE_SIMILARITY:
def cosine_similarity(tf_idf_q, n_v_q, tf_idf_doc, n_v_doc):
    #l2_norm_doc = l2_normalization_vector(vector_tf_idf(corpus, index, documentID))
    #tf_idf_doc = tf_idf(corpus,index,documentID, query)

    if n_v_doc != 0:
        if n_v_q != 0:
            return (np.dot(tf_idf_q, tf_idf_doc) / (n_v_q * n_v_doc))
        else:
            return 0
    else:
        return 0


# CHERCHER DANS TOUS LES DOCS
def search_word_in_corpus(corpus, index, query):
    #print("Mot recherché: ",query)

    document_finaux = {}

    if len(query.split(" ")) <= 1:
        #print("un seul mot")
        p = PorterStemmer()
        query = p.stem(query, 0, len(query) - 1)
        liste_doc_one_word = index.get(query)
        # print(liste_doc_one_word)

        if liste_doc_one_word != None:
            temps = liste_doc_one_word.copy()
            temps.pop(0)
            for key, values in temps:
                document_finaux[key] = values
        return document_finaux

    else:
        # On part du principe que c'est un and
        liste_doc = make_query_and(query, index)
        if "or" in query:
            # print("or")
            liste_doc = make_query_or(query, index)

        #print("dans la suite")
        # print(liste_doc)
        document_finaux.clear()

        query_as_doc = Document()
        query_as_doc.text = query

        query_as_doc.docno = 0
        corpus_query = [query_as_doc]
        inv_index_query = buildInvertedIndex(corpus_query)
        #print (inv_index_query)


        word_list = []
        query = query.lower()
        query = query.split(' ')
        p = PorterStemmer()
        for word in query:
            word_list.append(p.stem(word, 0, len(word) - 1))

        vector_query_norm = {}
        # ICI ON CALCULE LE VECTEUR DE LA QUERY
        #print("avant for query_number. Taille liste_doc: ", str(corpus_query.__len__()))

        for key, values in inv_index_query.items():
            #print("word: ", key)

            #v_query_tf_idf = vector_tf_idf(corpus, index, 0)
            v_query_tf_idf_opti = vector_tf_idf_opti(corpus, index, 0)
            n_v_query_tf_idf = l2_normalization_vector(v_query_tf_idf_opti)
            vector_query_norm[0] = n_v_query_tf_idf

            '''
            print(document_frequency(index, key))
            print(inverse_document_frequency(corpus,index, key))
            print(v_query_tf_idf)
            print(v_query_tf_idf_opti)
            print(vector_query_norm)
            '''
        vector_doc_norm = {}
        # DOC = NUMERO DU DOCUMENT
        # ICI ON CALCULE LE VECTEUR DES DOCUMENTS
        # print("avant vectorisation. Taille liste_doc: ", str(liste_doc.__len__()))
        for doc_number in liste_doc:
            v_tf_idf = vector_tf_idf_opti(corpus, index, doc_number)
            n_v_tf_idf = l2_normalization_vector(v_tf_idf)
            vector_doc_norm[doc_number] = n_v_tf_idf

            # print(vector_doc_norm)

        #print("fin vectorisation")

        for key, values in vector_doc_norm.items():
            document_finaux[key] = 0

        for key, values in vector_doc_norm.items():

            for term in word_list:
                document_finaux[key] = cosine_similarity(inverse_document_frequency(corpus, index, term),
                                                         n_v_query_tf_idf, tf_idf_opti(corpus, index, key, term), values) + document_finaux[key]


    return document_finaux

