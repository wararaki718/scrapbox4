#!/bin/bash

curl -H "Content-Type: application/x-ndjson" -POST https://localhost:9200/data/_bulk -u 'admin:admin' --insecure --data-binary "@data.jsonln" | jq

echo "DONE"
