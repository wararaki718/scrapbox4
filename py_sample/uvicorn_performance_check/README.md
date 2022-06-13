# uvicorn performance check app

## setup locust

```shell
pip install locust==2.9.0
```

## build batch & api

```shell
docker-compose build
```

## create a model

```shell
docker-compose -f docker-compose.yml -f docker-compose.batch.yml up
```

## launch api

```shell
docker-compose -f docker-compose.yml -f docker-compose.api.yml up
```

increase uvicorn workers

```shell
docker-compose -f docker-compose.yml -f docker-compose.api.multi.yml up
```

open http://localhost:8080/docs on your browser.

## stress test

```shell
locust -f locust_file.py IrisUser
```

open http://localhost:8089/ on your browser.
