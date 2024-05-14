import json
from dataclasses import dataclass
from typing import Any, List, Set
from typing import Dict

__all__ = [
    "DataCatalog",
    "classify_with_object_type"
]


@dataclass
class Table:
    id: str = None
    collectionId: str = None
    name: str = None
    qualifiedName: str = None
    displayText: str = None
    contact: List["Contact"] = None
    term: List["Term"] = None
    classification: List[str] = None
    endorsement: List[str] = None
    isIndexed: bool = None
    objectType: str = None
    entityType: str = None
    assetType: List[str] = None
    updateBy: str = None
    updateTime: int = None
    createBy: str = None
    createTime: int = None

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}

    def json_dumps(self, **kwargs) -> str:
        return json.dumps(self.as_dict(), **kwargs)


@dataclass
class Contact:
    contactType: str
    id: str


@dataclass
class Term:
    name: str
    guid: str
    glossaryName: str


@dataclass
class DataCatalog:
    key: str
    created_at: int
    data: Dict[str, Any]

    @property
    def tables(self) -> List[Table]:
        return [
            Table(**{k: v for k, v in obj.items() if not k.startswith("@")})
            for obj in self.data["value"] if obj["objectType"] == "Tables"
        ]


def classify_with_object_type(data: DataCatalog) -> List[DataCatalog]:
    object_types: Set = set()
    for obj in data.data["value"]:
        if "objectType" in obj:
            object_types.add(obj["objectType"])

    catalogs: Dict[str, DataCatalog] = {
        object_type: DataCatalog(key=f"{data.key}_{object_type.replace(" ", "_")}", created_at=data.created_at,
                                 data={"value": []})
        for object_type in object_types
    }

    for obj in data.data["value"]:
        if "objectType" in obj:
            catalogs[obj["objectType"]].data["value"].append(obj)

    return list(catalogs.values())
