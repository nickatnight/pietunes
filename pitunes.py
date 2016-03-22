from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
import re

app = Flask(__name__)

@app.route('/')
def home():
    #term = request.args.get('srch-term')
    #if term:
    #    print 'Term is not None'
    #length = len(utils2.music_dir)
    c = map(chr, range(97, 123))

    return render_template('home.html', chars=c)

@app.route('/<title_letter>')
def index(title_letter):
    c = map(chr, range(97, 123))

    es = Elasticsearch()
    query = es.search(index="music", body={"size":80, "query":
                                           {"prefix":{"artist": title_letter}}})
    return render_template('index.html', music=query, chars=c)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5666)
