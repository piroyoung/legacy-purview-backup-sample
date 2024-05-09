from datetime import datetime

from pvsnapshot.model import DataCatalog
from pvsnapshot.repository import LocalRepository
from pvsnapshot.repository import RemoteRepository


class DumpService:
    remote: RemoteRepository
    local: LocalRepository
    key: str

    def run(self) -> None:
        data: DataCatalog = self.remote.get()
        data.key = self.key
        data.created_at = datetime.now()
        self.local.put(data)


class RestoreService:
    remote: RemoteRepository
    local: LocalRepository
    key: str

    def run(self, key: str) -> None:
        # take a snapshot of the current data for backup
        data: DataCatalog = self.remote.get()
        data.key = f"{self.key}_backup"
        data.created_at = datetime.now()
        self.local.put(data)

        # restore the data from the local
        data: DataCatalog = self.local.get(key)
        self.remote.put(data)
