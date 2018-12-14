#! python3

from flask import Flask, render_template,request

from util import indexCorpus, buildInvertedIndex, make_query

from document import Document

app = Flask(__name__)

corpus = indexCorpus("corpus")
index = buildInvertedIndex(corpus)

with open("output.txt", "w+") as file:
    for word, doc in index.items():
        file.write("%s : %s \n" % (word, doc))

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
    
    print(documents_modified[1].text)

    return render_template('index.html', documents=documents_modified, count=len(documents), words=query.split(' '))

if __name__ == '__main__':
    app.run()