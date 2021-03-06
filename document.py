from Algorithms.stemmer_algo import PorterStemmer
import re


class Document:
    def __init__(self):
        self.docno = ""
        self.fileId = ""
        self.first = ""
        self.second = ""
        self.head = ""
        self.dateline = ""
        self.note = ""
        self.byline = ""
        self.unk = ""
        self.text = ""
        self.words = {}

    def setData(self, markup, content):
        if markup == "DOCNO":
            self.docno = content
        elif markup == "FILEID":
            self.fileId = content
        elif markup == "FIRST":
            self.first = content
        elif markup == "SECOND":
            self.search = content
        elif markup == "HEAD":
            self.head = content
        elif markup == "DATELINE":
            self.dateline = content
        elif markup == "TEXT":
            self.text += ' ' + content
        elif markup == "NOTE":
            self.note = content
        elif markup == "BYLINE":
            self.byline = content
        elif markup == "UNK":
            self.unk = content
        else:
            print("%s does not exist" % markup)

    def listWords(self):
        words = set()

        p = PorterStemmer()

        for word in re.sub('[^ A-Za-z]+', '', self.text.lower()).split(' '):
            word = p.stem(word, 0, len(word) - 1)
            words.add(word)

        return words

    def countWords(self):
        p = PorterStemmer()

        text = re.sub('[^ A-Za-z]+', '', self.text.lower()).split(' ')

        for word in text:
            word = p.stem(word, 0, len(word) - 1)

            if word in self.words:
                self.words[word] += 1
            else:
                self.words[word] = 1

        return self.words

    def __str__(self):
        return str(self.docno)


def buildInvertedIndex(corpus):
    """
    { word : [ count corpus, ( document, count ) ] }
    """
    words = {}
    index = 0

    for document in corpus:

        for word, count in document.countWords().items():

            if word in words:
                words[word][0] += 1
                words[word].append((index, count))

            else:
                words[word] = [1]
                words[word].append((index, count))

        index += 1

    # remove stop words
    with open("stopwords.txt", "r") as stopwords:
        word = stopwords.readline().rstrip()
        while word:
            if word in words:
                del words[word]
            word = stopwords.readline().rstrip()

    if '' in words:
        del words['']

    return words
