#import stemmer as st
from stemmer import PorterStemmer as st
import sys


p = st
if len(sys.argv) > 1:
    for f in sys.argv[1:]:
        infile = open(f, 'r')
        while 1:
            output = ''
            word = ''
            line = infile.readline()
            if line == '':
                break
            for c in line:
                if c.isalpha():
                    word += c.lower()
                else:
                    if word:
                        output += p.stem(word, 0,len(word)-1)
                        word = ''
                    output += c.lower()
            print output,
        infile.close()

print("test")

