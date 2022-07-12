#!/bin/bash

curl -XDELETE --insecure -u 'admin:admin' 'https://localhost:9200/my-first-index/_doc/1' | jq
curl -XDELETE --insecure -u 'admin:admin' 'https://localhost:9200/my-first-index/' | jq

echo "delete indices"
