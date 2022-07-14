#!/bin/bash

helm repo add opensearch https://opensearch-project.github.io/helm-charts/
helm repo update

echo "check helm repository"

helm search repo opensearch

echo "DONE"
