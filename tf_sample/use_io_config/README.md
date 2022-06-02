# sample terraform on the Docker

initialization settings

```shell
terraform init
```

deploy

```shell
terraform apply
```

After launch the application, you access to http://localhost:8000

change variable

```shell
terraform apply -var "container_name=YetAnotherName"
```

check

```shell
docker ps
```

output

```shell
terraform output
```

destroy

```shell
terraform destroy
```
