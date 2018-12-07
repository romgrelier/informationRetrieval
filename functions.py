import math;
import numpy as np;

doc1 = {};
doc1["bonjour"]=1;
doc1["appelle"]=2;
doc1["michel"]=1;
doc1["et"]=1;
doc1["toi"]=1;
doc1["comment"]=1;
doc1["tu"]=1;
print (doc1);

doc2 = {};
doc2["bonjour"]=1;
doc2["appelle"]=1;
doc2["Alfred"]=1;


print (doc2);

doc3 = [];


docs = [];
docs.append(doc1);
docs.append(doc2);
docs.append(doc3);
print(docs);


query1 = {}
query1["appelle"]=1;
query2 = {}
query2["Alfred"]=2;

queries =[]
queries.append(query1)
queries.append(query2)




#TERM FREQUENCY:

def term_frequency(word):

    if type(word) == int:
        if word <= 0:
            return 0;
        else:
            return 1 + math.log(word,10);
    else:
        return 0;

def score_documents_term_frequency(documents,query):
    sum=0;
    for document in documents:
        for word in document:
            if word == query:
                print(str(query)+ " : "+str(term_frequency(document.get(query))));
                sum+= term_frequency(document.get(query));
    return sum;


print ("\n" + str(score_documents_term_frequency(docs,"appelle")));
print ("\n" + str(score_documents_term_frequency(docs,"bonjour")));
print (score_documents_term_frequency(docs,"Alfred"));



#DOCUMENT FREQUENCY:
def document_frequency(documents, word):
    sum = 0;
    for document in documents:
        if word in document:
            sum=sum+1;
    return sum;

def inverse_document_frequency(documents, word):
    '''
    if documents.__len__() == 0:
        return 0;
    '''
    #print("\ttaille document: "  +str(documents.__len__()) );
    return math.log((documents.__len__()/document_frequency(documents,word)), 10)


def tf_idf(documents, document, word):
    #print("tf: "+  str(term_frequency(document.get(query))));
    #print("idf: "+ str(inverse_document_frequency(documents,query)));
    return term_frequency(document.get(word))  * inverse_document_frequency(documents,word);

print ("\ndocument_frequency: " + str(document_frequency(docs,"appelle")));
print ("document_frequency: " + str(document_frequency(docs,"Alfred")));

print ("\nidf appelle: " + str(inverse_document_frequency(docs,"appelle")));
print ("idf alfred: " + str(inverse_document_frequency(docs,"Alfred")) +"\n");

print ("tf*idf: " + str(tf_idf(docs,doc1,"appelle")) +"\n" );
print ("tf*idf: " + str(tf_idf(docs,doc1,"bonjour"))+"\n");
print ("tf*idf: " + str(tf_idf(docs,doc1,"Alfred"))+"\n");


def print_documents_to_tf_idf_vector(documents):
    compteur =0;
    for document in documents:
        print("DOCUMENT: "+ str(compteur));
        for query in document:
            print( "\t" +query + " | tf_idf: "+  str( tf_idf(documents,document,query) ));
        compteur=compteur+1;
    return  True;


print_documents_to_tf_idf_vector(docs);
#JUSQU'ICI OK


#VECTOR & NORMALISATION:

def vector_tf_idf_one_doc(documents,document):
    vector = {}
    for word in document:
        vector[word]=tf_idf(documents,document,word);
    return vector;


print("\nTF_IDF VECTOR:")
print(vector_tf_idf_one_doc(docs, doc1))


def l2_normalization_vector(document):
    vector_normalized =0;
    sum = 0;
    for key,values in document.items():
        sum = sum+values;
    vector_normalized = math.sqrt(sum);
    return vector_normalized

print("\nNORMALISATION DU DOC 1: ")
print(l2_normalization_vector(vector_tf_idf_one_doc(docs,doc1)))

print("\nNORMALISATION DU DOC 2: ")
print(l2_normalization_vector(vector_tf_idf_one_doc(docs,doc2)))



print("\nNORMALISATION DE LA REQUETE \"ALFRED\": ")
print(l2_normalization_vector(vector_tf_idf_one_doc(queries,query2)))

print("\nNORMALISATION DE LA REQUETE \"APPELLE\": ")
print(l2_normalization_vector(vector_tf_idf_one_doc(queries,query1)))


#COSINE_SIMILARITY:

def cosine_similarity(arg_query, document,word):
    l2_norm_doc = l2_normalization_vector(vector_tf_idf_one_doc(docs, document));
    l2_norm_query = l2_normalization_vector(vector_tf_idf_one_doc(queries, arg_query));
    tf_idf_doc = tf_idf(docs, document,word)
    tf_idf_query = tf_idf(queries, document,word)

    return (np.dot(tf_idf_query ,tf_idf_doc) / ( l2_norm_query * l2_norm_doc ) ) ;


'''
l2_norm_doc1=l2_normalization_vector(vector_tf_idf_one_doc(docs,doc1));
l2_norm_doc2=l2_normalization_vector(vector_tf_idf_one_doc(docs,doc2));

l2_norm_query1=l2_normalization_vector(vector_tf_idf_one_doc(queries,query1));
l2_norm_query2=l2_normalization_vector(vector_tf_idf_one_doc(queries,query2));
'''

# PAS FINI !!!!
print("\nCOSINE SIMILARITY ALFRED DANS DOC ALFRED: ")
print(cosine_similarity(query2,doc2,"Alfred"));
print("\nCOSINE SIMILARITY ALFRED DANS UN DOC QUI N'A PAS ALFRED: ")
print(cosine_similarity(query2,doc1,"Alfred"));

