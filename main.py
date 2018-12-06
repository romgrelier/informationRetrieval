import re
import os


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
            self.text = content
        elif markup == "NOTE":
            self.note = content
        elif markup == "BYLINE":
            self.byline = content
        elif markup == "UNK":
            self.unk = content
        else:
            print(f"{markup} does not exist")

    def countWords(self):
        for word in self.text.split(" "):
            #word = word.lower()
            #word = re.sub("[*/-<>|(){}]", '', word)
            if word in self.words:
                self.words[word] += 1
            else:
                self.words[word] = 1

        return self.words



def loadFile(path):
    markups = ["DOCNO", "FILEID", "FIRST", "BYLINE", "SECOND", "HEAD", "DATELINE", "NOTE", "UNK"]
    documents = []

    with open(path) as file:
        line = file.readline().rstrip()

        while line:

            # New Document
            if line == "<DOC>":
                document = Document()
                line = file.readline().rstrip()
                #print("DOC begin")
                while line != "</DOC>": # until the end of the doc

                    for markup in markups: # scan which markup

                        # single line
                        if line[:len(markup) + 2] == '<' + markup + '>' and line[len(line) - len(markup) - 3:] == "</" + markup + '>':
                            #print(f"\t{markup} added")
                            document.setData(markup, line[len(markup) + 2:len(line) - len(markup) - 3])
                            line = file.readline().rstrip()
                        # multiline
                        elif line[:len(markup) + 2] == '<' + markup + '>':
                            text = line[len(markup) + 2:]
                            while line[len(line) - len(markup) - 3:] != "</" + markup + '>':
                                text += line
                                line = file.readline().rstrip()
                            text += line[len(markup) + 2:len(line) - len(markup) - 3]
                            line = file.readline().rstrip()
                            document.setData(markup, text)


                    # multiline, loop until markup TEXT
                    if line == "<TEXT>" or line[:len("TEXT") + 2] == '<' + "TEXT" + '>':
                        #print("text begin")
                        text = ""
                        while line != "</TEXT>":
                            #print(line)
                            text += line
                            line = file.readline().rstrip()
                        line = file.readline().rstrip()
                        document.setData("TEXT", text)

                    #print(line)

                documents.append(document)
                #print("document added")

            else: # continue until a doc markup
                line = file.readline().rstrip()


def indexCorpus(folder):
    documents = []
    
    for file in os.listdir(folder):
        print(f"{folder}/{file}")
        documents += loadFile(f"{folder}{file}")

    return documents
"""
documents = indexCorpus("corpus/")
print(len(documents))
"""
print(os.listdir("corpus"))