from elasticsearch import Elasticsearch


es = Elasticsearch()

res = es.search(index="music", body={"size":60, "query": {"match_all":{}}})

print res['hits']
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(title)s %(artist)s: %(album)s" % hit["_source"])
