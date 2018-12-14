#! python3

from flask import Flask, render_template,request

from util import indexCorpus, buildInvertedIndex, make_query

from document import Document

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

    documents = make_query(query, index)

    documents_modified = []
    for indexD in documents:
        d = Document()
        d.docno = corpus[indexD].docno
        d.text = corpus[indexD].text.split(' ')
        documents_modified.append(d)
    
    #print(documents_modified[1].text)

    return render_template('index.html', documents=documents_modified, count=len(documents), words=query.split(' '))

if __name__ == '__main__':
    app.run()