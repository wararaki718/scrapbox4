# sample spring data application

## build & run

open this project on your intellij. After that, build and run this project.

After launching the application, you access to http://localhost:8080 on your browser.

## check

show top level service

```shell
curl http://localhost:8080
```

show person records

```shell
curl http://localhost:8080/people
```

add person

```shell
curl -i -H "Content-Type:application/json" -d '{"firstName": "Frodo", "lastName": "Baggins"}' http://localhost:8080/people
```

find by lastname

```shell
curl http://localhost:8080/people/1
```
