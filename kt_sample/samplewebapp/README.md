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
curl localhost:8080/demo/add -d name=First -d email=someemail@someemailprovider.com
```

get data

```shell
curl localhost:8080/demo/all
```
