# purview-snapshot
*purview-snapshot* is a example backup application for Microsoft Purview DataCatalog.

Microsoft Purview DataCatalog is a data catalog management tool that forms a part of Microsoft's data governance solution. It is useful for various cases, however, it currently lacks a backup function. There is also the risk that a misconfigured scan could override or remove existing metadata, resulting in a permanent loss of maintained metadata.
This example application allows us to dump all table metadata into a local JSON file and restore everything from a JSON snapshot.

## Pre-Requirements
* Create a service principal for this app and assign the appropriate roles as shown below.
  * https://learn.microsoft.com/en-us/purview/tutorial-using-python-sdk

TL;DR -> just check [Makefile](https://github.com/piroyoung/purview-snapshot/blob/main/Makefile)

## Environment Variable
```shell
  export CLIENT_ID=xxxxxx-xxxxxx-xxxxxxxxx
  export CLIENT_SECRET=setyoursecret
  export TENANT_ID=xxxx-xxxxxxx-xxxxxxxxx
  export PURVIEW_ENDPOINT=https://<account>.purview.azure.com/
  export HOST_VOLUME=/your/local/path/to/save/snapshot
```

## Dump to `example.json`
```shell
docker run -it --rm \
    -e CLIENT_ID=$(CLIENT_ID) \
    -e CLIENT_SECRET=$(CLIENT_SECRET) \
    -e TENANT_ID=$(TENANT_ID) \
    -e PURVIEW_ENDPOINT=$(PURVIEW_ENDPOINT) \
    --name pvsnapshot \
    -v $(HOST_VOLUME):/local/pvsnapshot/snapshots/ \
    ghcr.io/piroyoung/purview-snapshot:latest dump example
```

## Restore from `example.json`
```shell
docker run -it --rm \
    -e CLIENT_ID=$(CLIENT_ID) \
    -e CLIENT_SECRET=$(CLIENT_SECRET) \
    -e TENANT_ID=$(TENANT_ID) \
    -e PURVIEW_ENDPOINT=$(PURVIEW_ENDPOINT) \
    --name pvsnapshot \
    -v $(HOST_VOLUME):/local/pvsnapshot/snapshots/ \
    ghcr.io/piroyoung/purview-snapshot:latest restore example
```
