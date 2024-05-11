from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, Set
from typing import Dict

__all__ = [
    "DataCatalog",
    "classify_with_object_type"
]


@dataclass
class DataCatalog:
    key: str
    created_at: datetime
    data: Dict[str, Any]


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
