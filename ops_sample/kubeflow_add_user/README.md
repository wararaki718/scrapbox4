# add an user to kubeflow

## setup environment

```shell
pip install passlib
```

```shell
git clone https://github.com/kubeflow/manifests.git
```

## change default user

```shell
python hash_generator.py
```

you set the generated hash to static/Passwords parameters. (see: manifests/common/dex/base/config-map.yaml)

```yaml
  staticPasswords:
    - email: <your email address>
      hash: <your generated hash>
      username: <your username>
      userID: <your userid>
```

## add & update an user

create new user

```shell
kubectl create -f profile.yaml
```

update user

```shell
kubectl apply -f profile.yaml
```
