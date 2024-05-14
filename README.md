# Purview Snapshot
https://learn.microsoft.com/en-us/purview/tutorial-using-python-sdk

```shell
export DOCKER_IMAGE=pvsnapshot:local
export HOST_VOLUME=/mnt/data/purview/snapshots
export CLIENT_ID=...
export CLIENT_SECRET=...
export TENANT_ID=...
export PURVIEW_ENDPOINT=https://<account>.purview.azure.com/

docker build -t $(DOCKER_IMAGE) .
docker run -it --rm \
    -e CLIENT_ID=$(CLIENT_ID) \
    -e CLIENT_SECRET=$(CLIENT_SECRET) \
    -e TENANT_ID=$(TENANT_ID) \
    -e PURVIEW_ENDPOINT=$(PURVIEW_ENDPOINT) \
    --name pvsnapshot \
    -v $(HOST_VOLUME):/local/pvsnapshot/snapshots/ \
    $(DOCKER_IMAGE)
```
