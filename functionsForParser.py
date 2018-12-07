import math;
import numpy as np;


#TERM FREQUENCY:

def term_frequency(word):
    if type(word) == int:
        if word <= 0:
            return 0;
        else:
            return 1 + math.log(word,10);
    else:
        return 0;

def score_documents_term_frequency(documents,document,query):
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


#DOCUMENT FREQUENCY:
def document_frequency(documents, query):
    for key, values in documents.items():
        if key == query:
            return values[0];
    return 0;

def inverse_document_frequency(corpus, indexWords, query):
    '''
    if documents.__len__() == 0:
        return 0;
    '''
    #print("\ttaille document: "  +str(documents.__len__()) );
    return math.log((corpus.__len__()/document_frequency(indexWords,query)), 10)


def tf_idf(corpus,indexWords, numDocument, query):
    for key,values in indexWords.items():
        if key == query:
            temps = values.copy();
            temps.pop(0);
            for docs in temps:
                if docs[0]==numDocument:
                    return term_frequency(docs[1]) * inverse_document_frequency(corpus, indexWords, query);





def print_documents_to_tf_idf_vector(documents):
    compteur =0;
    for document in documents:
        print("DOCUMENT: "+ str(compteur));
        for query in document:
            print( "\t" +query + " | tf_idf: "+  str( tf_idf(documents,document,query) ));
        compteur=compteur+1;
    return  True;


#VECTOR & NORMALISATION:

def vector_tf_idf_one_doc(corpus,document):
    vector = {}
    for word in indexWords:
        vector[word]=tf_idf(documents,document,word);
    return vector;



def l2_normalization_vector(document):
    vector_normalized =0;
    sum = 0;
    for key,values in document.items():
        sum = sum+values;
    vector_normalized = math.sqrt(sum);
    return vector_normalized


#COSINE_SIMILARITY:

def cosine_similarity(arg_query, document,word):
    l2_norm_doc = l2_normalization_vector(vector_tf_idf_one_doc(docs, document));
    l2_norm_query = l2_normalization_vector(vector_tf_idf_one_doc(queries, arg_query));
    tf_idf_doc = tf_idf(docs, document,word)
    tf_idf_query = tf_idf(queries, document,word)

    return (np.dot(tf_idf_query ,tf_idf_doc) / ( l2_norm_query * l2_norm_doc ) ) ;




