#!/bin/bash

curl -XPUT --insecure -u 'admin:admin' 'https://localhost:9200/my-first-index' | jq
curl -XPUT --insecure -u 'admin:admin' 'https://localhost:9200/my-first-index/_doc/1' -H 'Content-Type: application/json' -d '{"Description": "To be or not to be, that is the question."}' | jq

echo "insert documents"