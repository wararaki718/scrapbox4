#!/bin/bash

while ! kustomize build example | kubectl apply -f -; do echo "Retrying to apply resources"; sleep 10; done

echo "port-forward: 'kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80'"
echo "access to http://localhost:8080"
echo "id: user@example.con"
echo "pw: 12341234"
echo ""

echo "DONE"