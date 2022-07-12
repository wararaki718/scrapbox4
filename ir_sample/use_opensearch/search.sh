#!/bin/bash

curl -XGET --insecure -u 'admin:admin' 'https://localhost:9200/my-first-index/_doc/1' | jq
