from dataclasses import dataclass
from typing import Any, List
from typing import Dict

from azure.purview.datamap.models import AtlasEntityWithExtInfo

__all__ = [
    "DataCatalog",
]


@dataclass
class DataCatalog:
    key: str
    created_at: int
    entities: List[AtlasEntityWithExtInfo]

    def as_dict(self) -> Dict[str, Any]:
        return {
            "key": self.key,
            "created_at": self.created_at,
            "data": [e.as_dict() for e in self.entities]
        }

    def get_bodies(self) -> List[Dict[str, Any]]:
        return [_remove_nulls(e.as_dict()) for e in self.entities]


def _remove_nulls(value):
    if isinstance(value, dict):
        return {k: _remove_nulls(v) for k, v in value.items() if v is not None}
    elif isinstance(value, list):
        return [_remove_nulls(item) for item in value if item is not None]
    else:
        return value
