import json
import logging
from abc import ABCMeta
from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List, Any, Dict

from azure.core.exceptions import ResourceNotFoundError
from azure.purview.datamap import DataMapClient
from azure.purview.datamap.models import QueryResult, AtlasEntitiesWithExtInfo

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

    def has(self, key: str) -> bool:
        try:
            self.c.entity.get_by_ids(guid=[key])
            return True
        except ResourceNotFoundError:
            return False

    def get(self) -> DataCatalog:
        result: QueryResult = self.c.discovery.query(body={"keywords": "*"})
        table_ids: List[str] = [entity["id"] for entity in result.value if entity["objectType"] == "Tables"]
        response: AtlasEntitiesWithExtInfo = self.c.entity.get_by_ids(guid=table_ids)

        return DataCatalog(
            key=datetime.now().strftime("%Y%m%d%H%M%S"),
            created_at=int(datetime.now().timestamp()),
            body=response
        )

    # https://raw.githubusercontent.com/Azure/azure-sdk-for-python/main/sdk/purview/azure-purview-datamap/azure/purview/datamap/operations/_operations.py
    def put(self, data: DataCatalog):
        # self.c.entity.batch_create_or_update(body=data.body)
        for body in data.bodies:
            if self.has(body.entity.guid):
                _logger.info(f"Updating entity: {body.entity.attributes['name']}")
                self.c.entity.create_or_update(body=body)

            else:
                _logger.info(f"Creating entity: {body.entity.attributes['name']}")
                del body.entity.guid
                del body.entity.created_by
                del body.entity.create_time
                del body.entity.updated_by
                del body.entity.update_time
                del body.entity.version
                del body.entity.last_modified_t_s
                self.c.entity.create_or_update(body=body)


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
                body=AtlasEntitiesWithExtInfo(
                    entities=obj["body"]["entities"],
                    referred_entities=obj["body"]["referredEntities"]
                )
            )
            return dc

    def put(self, data: DataCatalog):
        with open(f"{self.dir}/{data.key}.json", "w") as f:
            d: str = json.dumps(
                {
                    "key": data.key,
                    "created_at": data.created_at,
                    "body": data.body.as_dict()
                },
                indent=4,
                ensure_ascii=False,
                sort_keys=True,
                default=str
            )
            f.write(d)

    def list(self) -> List[str]:
        pass
