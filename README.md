# Information Retrieval

## Installation

```
pip install -r requirements.txt
export FLASK_APP=webpage.py
python -m flask run
```

## Usage

After starting the flask app, a webpage will be available on 127.0.0.1:5000 with a text box ready receive your requeses.

At startup, this application will read all the text inside the corpus directory, it is possible to add more files using the same syntax. After reading, a cache file is built as a json file, if you delete this file, you will need to retart the server to rebuild it and if needed reading the files you added.

The text box takes the words you search for inside the corpus, the webpage will display all the texts containing these words with highligh.
