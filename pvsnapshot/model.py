from dataclasses import dataclass
from typing import List

from azure.purview.datamap.models import AtlasEntitiesWithExtInfo

__all__ = [
    "DataCatalog",
]


@dataclass
class DataCatalog:
    key: str
    created_at: int
    body: AtlasEntitiesWithExtInfo

    @property
    def bodies(self) -> List[AtlasEntitiesWithExtInfo]:
        return [
            AtlasEntitiesWithExtInfo(
                entities=[entity],
                referred_entities=self.body.referred_entities
            )
            for entity in self.body.entities
        ]

