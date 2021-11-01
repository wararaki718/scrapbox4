# a sample of pipeline based on docker image component

## setup environment

```shell
pip install kfp
```

## build

```shell
docker-compose build
```

```shell
docker push wararaki/hello-sample:latest
```

## compile

```shell
pipeline.py
```

after that, you upload a generated yaml file to Kubeflow pipeline.
