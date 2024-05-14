from dataclasses import dataclass
from typing import List

from azure.purview.datamap.models import AtlasEntitiesWithExtInfo
from azure.purview.datamap.models import AtlasEntityWithExtInfo


__all__ = [
    "DataCatalog",
]


@dataclass
class DataCatalog:
    key: str
    created_at: int
    body: AtlasEntitiesWithExtInfo


    @property
    def bodies(self) -> List[AtlasEntityWithExtInfo]:
        return [
            AtlasEntityWithExtInfo(
                entity=entity,
                referred_entities=self.body.referred_entities
            )
            for entity in self.body.entities
        ]



def _remove_nulls(value):
    if isinstance(value, dict):
        return {k: _remove_nulls(v) for k, v in value.items() if v is not None}
    elif isinstance(value, list):
        return [_remove_nulls(item) for item in value if item is not None]
    else:
        return value
