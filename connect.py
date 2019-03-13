from elasticsearch import Elasticsearch
import datetime
import os

try:
  es_host = os.environ["es_host"]
except KeyError:
  es_host = "localhost"

try:
  indices = os.environ["indices"]
except Exception:
  indices = "*"

try:
  repository_name = os.environ["repository_name"]
except Exception:
  repository_name = "backup"

es = Elasticsearch([{"host":str(es_host)}])

snapshot_body = {"type": "fs","settings": {"location": "/usr/share/elasticsearch/backups"}}

snapshot_name='snapshot'+datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
index_body = {
  "indices": str(indices)
}
es.snapshot.create_repository(repository=str(repository_name), body=snapshot_body)
es.snapshot.create(repository=str(repository_name), snapshot=snapshot_name, body=index_body)
print es.snapshot.get(repository = str(repository_name), snapshot = '_all')