#!/bin/bash

! kustomize build example | kubectl delete -f -;

echo "DONE"
