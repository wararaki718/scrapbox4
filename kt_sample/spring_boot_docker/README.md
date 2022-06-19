# sample spring boot docker

open this project on your intellij.

## create docker image

```shell
./gradlew bootBuildImage --imageName=sample-kt-web:latest
```

## run

```shell
docker-compose up
```

check

```shell
curl http://localhost:8080/
```
