# use opensearch

## run

minimum settings

```shell
docker-compose -f docker-compose.min.yml up
```

opensearch + dashboards

```shell
docker-compose up
```

## check

```shell
curl -XGET https://localhost:9200 -u 'admin:admin' --insecure 
```

if you use dashboard, please access to http://localhost:5601

## operations

create

```shell
bash create_index.sh
```

read

```shell
bash search.sh
```

delete

```shell
bash delete.sh
```
