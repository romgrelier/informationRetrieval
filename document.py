
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