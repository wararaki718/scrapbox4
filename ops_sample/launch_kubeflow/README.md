# launch Kubeflow

## launch

```shell
git clone https://github.com/kubeflow/manifests.git -b v1.5.1 --depth 1
```

```shell
cp launch.sh manifests/launch.sh
cd manifests
bash launch.sh
cd ..
```

## destroy

```shell
cp destroy.sh manifests/launch.sh
cd manifests
bash destroy.sh
cd ..
```
