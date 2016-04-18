from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    c = map(chr, range(97, 123))
    if request.method == 'POST':
        term = request.form['srch_term']
        es = Elasticsearch()
        query = es.search(index="music", body={"size": 80, "query":
                                                {"prefix":{"artist":term}}})
        return render_template('search.html', music=query)

    return render_template('home.html', chars=c)

@app.route('/<title_letter>')
def index(title_letter):
    c = map(chr, range(97, 123))

    es = Elasticsearch()
    query = es.search(index="music", body={"size":80, "query":
                                           {"prefix":{"artist": title_letter}}})
    return render_template('index.html', music=query, chars=c)

@app.route('/search')
def search():
    query = None
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5666)
