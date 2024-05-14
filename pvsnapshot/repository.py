import json
import logging
from abc import ABCMeta
from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List

from azure.purview.datamap import DataMapClient
from azure.purview.datamap.models import QueryResult

from pvsnapshot.model import DataCatalog

__all__ = [
    "RemoteRepository",
    "SnapshotRepository",
    "RestRemoteRepository",
    "LocalSnapshotRepository"
]

_logger: logging.Logger = logging.getLogger(__name__)


class RemoteRepository(metaclass=ABCMeta):
    @abstractmethod
    def get(self) -> DataCatalog:
        pass

    @abstractmethod
    def put(self, data: DataCatalog):
        pass


class SnapshotRepository(metaclass=ABCMeta):
    @abstractmethod
    def get(self, key: str) -> DataCatalog:
        pass

    @abstractmethod
    def put(self, data: DataCatalog):
        pass

    @abstractmethod
    def list(self) -> List[str]:
        pass


@dataclass(frozen=True)
class RestRemoteRepository(RemoteRepository):
    # https://azuresdkdocs.blob.core.windows.net/$web/python/azure-purview-datamap/1.0.0b1/index.html
    c: DataMapClient

    def get(self) -> DataCatalog:
        result: QueryResult = self.c.discovery.query(body={"keywords": "*"})
        # _logger.info(f"Query result: {result}")

        return DataCatalog(
            key=datetime.now().strftime("%Y%m%d%H%M%S"),
            created_at=int(datetime.now().timestamp()),
            data=result.as_dict()
        )

    # https://raw.githubusercontent.com/Azure/azure-sdk-for-python/main/sdk/purview/azure-purview-datamap/azure/purview/datamap/operations/_operations.py
    def put(self, data: DataCatalog):
        for table in data.tables:
            _logger.info(f"{table.json_dumps(indent=4, ensure_ascii=False)}")
            self.c.entity.create_or_update(
                body=table.as_atlas()
            )


@dataclass(frozen=True)
class LocalSnapshotRepository(SnapshotRepository):
    dir: str

    def get(self, key: str) -> DataCatalog:
        with open(f"{self.dir}/{key}.json", "r") as f:
            d: str = f.read()
            return DataCatalog(**json.loads(d))

    def put(self, data: DataCatalog):
        with open(f"{self.dir}/{data.key}.json", "w") as f:
            d: str = json.dumps(
                {
                    "key": data.key,
                    "created_at": str(data.created_at),
                    "data": data.data
                },
                indent=4,
                ensure_ascii=False
            )
            f.write(d)

    def list(self) -> List[str]:
        pass
