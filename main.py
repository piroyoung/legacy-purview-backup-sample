import logging
from datetime import datetime

from azure.identity import ClientSecretCredential
from azure.purview.datamap import DataMapClient

from pvsnapshot.env import Environments
from pvsnapshot.repository import LocalSnapshotRepository
from pvsnapshot.repository import RemoteRepository
from pvsnapshot.repository import RestRemoteRepository
from pvsnapshot.repository import SnapshotRepository
from pvsnapshot.service import DumpService, ClassifyDumpService

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    credentials: ClientSecretCredential = ClientSecretCredential(
        client_id=Environments.CLIENT_ID,
        client_secret=Environments.CLIENT_SECRET,
        tenant_id=Environments.TENANT_ID
    )

    client: DataMapClient = DataMapClient(
        endpoint=Environments.PURVIEW_ENDPOINT,
        credential=credentials
    )

    remote: RemoteRepository = RestRemoteRepository(c=client)
    local: SnapshotRepository = LocalSnapshotRepository(dir="snapshots")

    key: str = datetime.now().strftime("%Y%m%d%H%M%S")
    dump: DumpService = DumpService(remote=remote, local=local, key=key)
    classify: ClassifyDumpService = ClassifyDumpService(local=local, key=key)
    dump.run()
    classify.run()
