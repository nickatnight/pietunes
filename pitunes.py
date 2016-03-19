from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)

@app.route('/')
def home():
    #term = request.args.get('srch-term')
    #if term:
    #    print 'Term is not None'
    #length = len(utils2.music_dir)
    es = Elasticsearch()
    query = es.search(index="music", body={"size":80, "query": {"match_all":{}}})

    return render_template('home.html', music=query)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5666)
