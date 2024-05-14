import logging
from dataclasses import dataclass
from datetime import datetime

from pvsnapshot.model import DataCatalog
from pvsnapshot.repository import RemoteRepository
from pvsnapshot.repository import SnapshotRepository

__all__ = [
    "DumpService",
    "RestoreService",
]

_logger: logging.Logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DumpService:
    remote: RemoteRepository
    local: SnapshotRepository
    key: str

    def run(self) -> None:
        _logger.info("Dumping data from remote to local")
        data: DataCatalog = self.remote.get()
        data.key = self.key
        data.created_at = datetime.now()
        self.local.put(data)
        _logger.info(f"Data dumped to local with key: {self.key}")


@dataclass(frozen=True)
class RestoreService:
    remote: RemoteRepository
    local: SnapshotRepository
    key: str

    def run(self) -> None:
        # take a snapshot of the current data for backup
        _logger.info("Taking a snapshot of the current data")
        backup_key: str = datetime.now().strftime("%Y%m%d%H%M%S")
        current_data: DataCatalog = self.remote.get()
        current_data.key = f"backup_{backup_key}"
        self.local.put(current_data)
        _logger.info(f"Data snapshot taken with key: {current_data.key}")

        # restore the data from the local
        _logger.info("Restoring data from local")
        data: DataCatalog = self.local.get(self.key)
        self.remote.put(data)
        _logger.info(f"Data restored from local with key: {self.key}")
