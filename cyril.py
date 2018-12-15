from fileLoader import indexCorpus
from document import buildInvertedIndex

from functionsForParser import *

from util import *

from document import *

corpus = indexCorpus("corpus")

index = buildInvertedIndex(corpus)

with open("output.txt", "w+") as file:
    for word, doc in index.items():
        file.write("%s : %s \n" % (word, doc))


ocean_doc = 40;
year_doc = 9;

ocean = "ocean"
year = "year"

print(index)
print("\n");
'''
print("\nscore_document_freq by document ");
#print ("\tOcean: " + str(score_documents_term_frequency(index,ocean_doc, ocean)));
#print ("\tyear: " + str(score_documents_term_frequency(index,year_doc, year)));
#sdtf_ocean = score_documents_term_frequency(indexWords,7, "Ocean");
#sdtf_year = score_documents_term_frequency(indexWords,57, "years.");

print("\nDocument_frequency ");
print ("\tOcean: " + str(document_frequency(index, ocean)));
print ("\tyear: " + str(document_frequency(index, year)));

print("\nInverse document_frequency ");
print ("\tOcean: " + str(inverse_document_frequency(corpus,index, ocean)));
print ("\tyear: " + str(inverse_document_frequency(corpus, index, year)));

print("\ntf_idf");
print ("\tOcean: " + str(tf_idf(corpus,index,ocean_doc, ocean)));
print ("\tyears " + str(tf_idf(corpus, index,year_doc, year)));

print("\nvector_tf_idf");
print ("\tDoc: "+ str(ocean_doc) + str(vector_tf_idf(corpus, index, ocean_doc)));
print ("\tDoc: " + str(year_doc) + str(vector_tf_idf(corpus, index, year_doc)));

print("\nNormalized_vector");

vector_tf_ifd_doc1 = vector_tf_idf(corpus, index, ocean_doc);
vector_tf_ifd_doc2 = vector_tf_idf(corpus, index, year_doc);

print ("\tDoc: " + str(ocean_doc) + str(l2_normalization_vector(vector_tf_ifd_doc1)));
print ("\tDoc: "+ str(year_doc) +  str(l2_normalization_vector(vector_tf_ifd_doc2)));


'''



# COSINE_SIMILARITY:
def cosine_similarity(tf_idf_q,n_v_q, tf_idf_doc, n_v_doc ):
    #l2_norm_doc = l2_normalization_vector(vector_tf_idf(corpus, index, documentID))
    #tf_idf_doc = tf_idf(corpus,index,documentID, query)
    return (  np.dot(tf_idf_q, tf_idf_doc) / (n_v_q * n_v_doc));





'''
print("\nCosine Similarity");
print ("\tDoc "+ str(ocean_doc)  + ": " +str(    cosine_similarity(1,1,  tf_idf(corpus,index,ocean_doc,ocean)  ,  l2_normalization_vector(vector_tf_ifd_doc1)  )));
print ("\tDoc "+ str(ocean_doc)+ ": "   + str(    cosine_similarity(1,1,  tf_idf(corpus,index,year_doc,year)  ,  l2_normalization_vector(vector_tf_ifd_doc2)  )));

'''




'''
#IL NOUS FAUT : 
- un vecteur normalisé de la question =0
- tf_idf de la question =0

Pour chaque document, on compare le cosinus avec : 
- un vecteur normalisé de la longueur du document
- tf_idf du doc


'''



query = "center" #9 FOIS
#query = input("Entrez un mot")
#print(query);

# CHERCHER DANS TOUS LES DOCS
def search_word_in_corpus(corpus, index, query):
    print("Mot recherché: ",query)

    document_finaux  = {}




    if len(query.split(" "))<=1:
        print("un seul mot")
        liste_doc_one_word = index.get(query)
        #print(liste_doc_one_word)
        if liste_doc_one_word != None:
            temps = liste_doc_one_word.copy()
            temps.pop(0)
            for key, values in temps:
                document_finaux[key]= values
        return  document_finaux

    else:

        liste_doc = make_query(query, index)
        print(liste_doc)
        document_finaux.clear()

        query_as_doc = Document()
        query_as_doc.text= query

        query_as_doc.docno=0
        corpus_query = [query_as_doc]
        inv_index_query = buildInvertedIndex(corpus_query)
        print (inv_index_query)



        word_list = []
        query = query.lower()
        query = query.split(' ')
        p = PorterStemmer()
        for word in query:
            word_list.append(p.stem(word, 0, len(word) - 1))


        vector_query_norm = {}
        # ICI ON CALCULE LE VECTEUR DE LA QUERY
        print("avant for query_number. Taille liste_doc: ", str(corpus_query.__len__()))

        for key, values in inv_index_query.items():
            print("word: ", key)

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



        vector_doc_norm ={}
        #DOC = NUMERO DU DOCUMENT
        # ICI ON CALCULE LE VECTEUR DES DOCUMENTS
        print("avant for doc_number. Taille lsite_doc: ", str(liste_doc.__len__()))
        for doc_number in liste_doc:
            v_tf_idf = vector_tf_idf_opti(corpus,index,doc_number)
            n_v_tf_idf = l2_normalization_vector(v_tf_idf)
            vector_doc_norm[doc_number]=n_v_tf_idf

            print(vector_doc_norm)


        '''
        #print(vector_doc_norm)
        #ICI NOUS AVONS UNE LISTE DE VECTEUR DES DOCUMENTS CONTENANT LES MOTS
        print("Avant for vector_doc_norm")
        for key, values in vector_doc_norm.items():
            print("key" ,str(key))
            print(inverse_document_frequency(corpus,index, key))
            print(vector_query_norm[0])
            print(tf_idf(corpus,index,key,query))
            print(values)
            #print("\nKEY: "+ str(key) +"\n\tTF: "+str(term_frequency2(index,key,query)) +"\n\tIDF1 :" + str(tf_idf(corpus,index,key,query))  + " \n\tSimilarity: "+ str(cosine_similarity(1,1,tf_idf(corpus,index,key,query), values) ))
            document_finaux[key]=cosine_similarity(inverse_document_frequency(corpus,index, key), vector_query_norm[0], tf_idf(corpus,index,key,query)  , values)
        '''

        for key, values in vector_doc_norm.items():
            document_finaux[key]=0

        for term in word_list:
            for key, values in vector_doc_norm.items():
                document_finaux[key] = cosine_similarity(inverse_document_frequency(corpus, index, term),
                                                     n_v_query_tf_idf, tf_idf(corpus, index, key, term), values) + document_finaux[key]




    return document_finaux



#print(search_word_in_corpus(corpus, index, query))

