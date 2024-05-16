import logging

from azure.identity import ClientSecretCredential
from azure.purview.datamap import DataMapClient

from pvsnapshot.env import Arguments
from pvsnapshot.env import Environments
from pvsnapshot.repository import DataMapAPITableEntityRepository
from pvsnapshot.repository import LocalSnapshotRepository
from pvsnapshot.repository import SnapshotRepository
from pvsnapshot.repository import TableEntityRepository
from pvsnapshot.service import DumpService
from pvsnapshot.service import RestoreService

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

    remote: TableEntityRepository = DataMapAPITableEntityRepository(c=client)
    local: SnapshotRepository = LocalSnapshotRepository(dir="snapshots")

    match Arguments.COMMAND:
        case "dump":
            dump: DumpService = DumpService(remote=remote, local=local, key=Arguments.KEY)
            dump.run()

        case "restore":
            restore: RestoreService = RestoreService(remote=remote, local=local, key=Arguments.KEY)
            restore.run()
