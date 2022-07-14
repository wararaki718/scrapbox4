#!/bin/bash

helm install sample-search opensearch/opensearch
helm install sample-dashboards opensearch/opensearch-dashboards

echo "DONE"
