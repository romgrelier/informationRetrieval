import os
from document import Document


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
                        line = file.readline().rstrip()
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
            
    return documents


def indexCorpus(folder):
    corpus = []
    
    for file in os.listdir(folder):
        corpus += loadFile("%s/%s" % (folder, file))

    return corpus

