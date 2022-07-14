# opensearch deployment on k8s by using helm

## setup

```shell
brew install helm
```

## initialization

install opensearch chart

```shell
bash init.sh
```

## install chart

```shell
bash install.sh
```

check status

```shell
kubectl get pods --namespace default
```

if the dashboard is running, you execute the below shell. if not, wait a minute.

```shell
bash forward.sh
```

## uninstall chart

```shell
bash uninstall.sh
```
