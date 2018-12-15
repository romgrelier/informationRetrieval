#! python3

from flask import Flask, render_template,request

from util import *

from document import Document

from functionsForParser import *

import operator

import json, os

app = Flask(__name__)

corpus = indexCorpus("corpus")

index = []
if os.path.isfile('data.json'):
    print("loading already built inverted index")
    with open('data.json') as f:
        index = json.load(f)
else:
    index = buildInvertedIndex(corpus)
    with open('data.json', 'w') as outfile:
        json.dump(index, outfile)

@app.route('/')
def search(methods=['GET']):
    query = request.args.get('query', '')

    #print(search_word_in_corpus(corpus, index, query))



    documents = search_word_in_corpus(corpus, index, query)


    #documents = make_query(query, index)

    documents_sorted = sorted(documents.items(), key=operator.itemgetter(1), reverse=True)
    print (documents_sorted)

    documents_modified = []
    for indexD in documents_sorted:
        print(indexD)
        d = Document()
        d.docno = corpus[indexD[0]].docno
        d.text = corpus[indexD[0]].text.split(' ')
        documents_modified.append(d)
    
    #print(documents_modified[1].text)

    return render_template('index.html', documents=documents_modified, count=len(documents), words=query.split(' '))

if __name__ == '__main__':
    app.run()