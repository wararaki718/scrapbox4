# stress-test by using locust

## setup

```shell
pip install locust==2.9.0
```

## build

```shell
docker-compose build
```

## launch api

```shell
docker-compose up
```

## test

```shell
locust -f locust_file.py HelloUser WorldUser
```

after locust launched, you access http://0.0.0.0:8089 on your browser.

set parameters
- number of users
- spawn rate
- host (http://localhost:8000)
