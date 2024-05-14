from dataclasses import dataclass
from typing import Any, List, Set, Optional
from typing import Dict

__all__ = [
    "DataCatalog",
    "classify_with_object_type"
]


@dataclass
class Table:
    id: Optional[str]
    collectionId: Optional[str]
    name: Optional[str]
    qualifiedName: Optional[str]
    displayText: Optional[str]
    contact: Optional[List["Contact"]]
    term: Optional[List["Term"]]
    classification: Optional[List[str]]
    endorsement: Optional[List[str]]
    isIndexed: Optional[bool]
    objectType: Optional[str]
    entityType: Optional[str]
    assetType: Optional[List[str]]
    updateBy: Optional[str]
    updateTime: Optional[int]
    createBy: Optional[str]
    createTime: Optional[int]


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
