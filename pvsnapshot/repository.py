import copy
import json
import logging
from abc import ABCMeta
from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List, Any, Dict

from azure.core.exceptions import ResourceNotFoundError
from azure.purview.datamap import DataMapClient
from azure.purview.datamap.models import AtlasEntitiesWithExtInfo
from azure.purview.datamap.models import AtlasEntity
from azure.purview.datamap.models import QueryResult

from pvsnapshot.model import DataCatalog

__all__ = [
    "TableEntityRepository",
    "SnapshotRepository",
    "DataMapAPITableEntityRepository",
    "LocalSnapshotRepository"
]

_logger: logging.Logger = logging.getLogger(__name__)


class TableEntityRepository(metaclass=ABCMeta):
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
class DataMapAPITableEntityRepository(TableEntityRepository):
    # https://azuresdkdocs.blob.core.windows.net/$web/python/azure-purview-datamap/1.0.0b1/index.html
    c: DataMapClient

    def has(self, key: str) -> bool:
        try:
            self.c.entity.get_by_ids(guid=[key])
            return True
        except ResourceNotFoundError:
            return False

    def get(self) -> DataCatalog:
        request_body: Dict[str, Any] = {
            "keywords": "*",
            "filter": {
                "objectType": "Tables",
            }
        }

        # get all guid of tables
        result: QueryResult = self.c.discovery.query(body=request_body)
        table_ids: List[str] = [entity["id"] for entity in result.value if entity["objectType"] == "Tables"]

        # get all entities of tables
        response: AtlasEntitiesWithExtInfo = self.c.entity.get_by_ids(guid=table_ids)

        return DataCatalog(
            key=datetime.now().strftime("%Y%m%d%H%M%S"),
            created_at=int(datetime.now().timestamp()),
            body=response
        )

    # https://raw.githubusercontent.com/Azure/azure-sdk-for-python/main/sdk/purview/azure-purview-datamap/azure/purview/datamap/operations/_operations.py
    def put(self, data: DataCatalog):
        for body in data.bodies:
            if self.has(body.entities[0].guid):
                _logger.info(f"Updating entity: {body.entities[0].attributes['name']}")
                self.c.entity.batch_create_or_update(body=body)

            else:
                # Example: https://learn.microsoft.com/en-us/purview/create-relationships
                _logger.info(f"Creating entity: {body.entities[0].attributes['name']}")
                request_body: AtlasEntitiesWithExtInfo = AtlasEntitiesWithExtInfo(entities=[], referred_entities={})

                table_entity: AtlasEntity = copy.deepcopy(body.entities[0])

                # reset invalid guid and set a new pseudo guid
                table_entity.guid = -1

                # delete history attributes
                table_entity.created_by = None
                table_entity.create_time = None
                table_entity.updated_by = None
                table_entity.update_time = None
                table_entity.version = None
                table_entity.last_modified_t_s = None

                # reset relationship between table to columns
                table_entity["relationshipAttributes"]["columns"] = []

                # reset relationship between table to dbSchema
                db_schema_guid: str = table_entity["relationshipAttributes"]["dbSchema"]["guid"]
                table_entity["relationshipAttributes"]["dbSchema"] = {"guid": db_schema_guid}

                for i, c in enumerate(body.entities[0].relationship_attributes["columns"]):
                    column_entity: AtlasEntity = copy.deepcopy(body.referred_entities[c["guid"]])

                    # delete history attributes
                    column_entity.created_by = None
                    column_entity.create_time = None
                    column_entity.updated_by = None
                    column_entity.update_time = None
                    column_entity.version = None
                    column_entity.last_modified_t_s = None

                    # remove invalid guid and set a new pseudo guid
                    column_entity.guid = -10 - i

                    # set a relationship table to column
                    table_entity["relationshipAttributes"]["columns"].append({"guid": column_entity.guid})

                    # set a relationship column to table
                    column_entity["relationshipAttributes"]["table"] = {"guid": table_entity.guid}

                    # add a column entity to the request body
                    request_body.entities.append(column_entity)

                # add a table entity to the request body
                request_body.entities.append(table_entity)
                _logger.info(json.dumps(request_body.as_dict(), indent=2, ensure_ascii=False))

                self.c.entity.batch_create_or_update(body=request_body)


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
                indent=2,
                ensure_ascii=False,
                sort_keys=True,
                default=str
            )
            f.write(d)

    def list(self) -> List[str]:
        pass
