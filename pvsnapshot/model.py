from dataclasses import dataclass

from azure.purview.datamap.models import AtlasEntitiesWithExtInfo

__all__ = [
    "DataCatalog",
]


@dataclass
class DataCatalog:
    key: str
    created_at: int
    data: AtlasEntitiesWithExtInfo



def _remove_nulls(value):
    if isinstance(value, dict):
        return {k: _remove_nulls(v) for k, v in value.items() if v is not None}
    elif isinstance(value, list):
        return [_remove_nulls(item) for item in value if item is not None]
    else:
        return value
