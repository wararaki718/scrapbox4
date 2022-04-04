# sample web application

## build web app

open this project by intellij, and push a build button

## run

start db

```shell
docker-compose up
```

start app

- launch a intellij and push a run bottun

## check

insert data

```shell
curl http://localhost:8080/save
```

get data

```shell
curl http://localhost:8080/findall
```

```shell
curl http://localhost:8080/findbyid/1
```
