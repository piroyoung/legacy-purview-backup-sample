import json
import logging
from abc import ABCMeta
from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List, Any, Dict

from azure.purview.datamap import DataMapClient
from azure.purview.datamap.models import QueryResult, AtlasEntityWithExtInfo

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
        table_ids: List[str] = [entity["id"] for entity in result.value if entity["objectType"] == "Tables"]
        response: dict = self.c.entity.get_by_ids(guid=table_ids)

        return DataCatalog(
            key=datetime.now().strftime("%Y%m%d%H%M%S"),
            created_at=int(datetime.now().timestamp()),
            entities=[AtlasEntityWithExtInfo(entity=entity) for entity in response["entities"]]
        )

    # https://raw.githubusercontent.com/Azure/azure-sdk-for-python/main/sdk/purview/azure-purview-datamap/azure/purview/datamap/operations/_operations.py
    def put(self, data: DataCatalog):
        for body in data.get_bodies():
            _logger.info(
                f"Creating entity: {json.dumps(body, indent=4, ensure_ascii=False, sort_keys=True, default=str)}")
            self.c.entity.create_or_update(body=json.dumps(body))


@dataclass(frozen=True)
class LocalSnapshotRepository(SnapshotRepository):
    dir: str

    def get(self, key: str) -> DataCatalog:
        with open(f"{self.dir}/{key}.json", "r") as f:
            d: str = f.read()
            obj: Dict[str, Any] = json.loads(d)
            dc: DataCatalog = DataCatalog(
                key=obj["key"],
                created_at=obj["created_at"],
                entities=[AtlasEntityWithExtInfo(**v) for v in obj["data"]]
            )
            _logger.info(type(dc.entities))
            return dc

    def put(self, data: DataCatalog):
        with open(f"{self.dir}/{data.key}.json", "w") as f:
            d: str = json.dumps(
                data.as_dict(),
                indent=4,
                ensure_ascii=False,
                sort_keys=True,
                default=str
            )
            f.write(d)

    def list(self) -> List[str]:
        pass
