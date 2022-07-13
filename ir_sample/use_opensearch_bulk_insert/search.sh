#!/bin/bash

curl -H "Content-Type: application/x-ndjson" -POST https://localhost:9200/movies/_search -u 'admin:admin' --insecure | jq

echo "DONE"
