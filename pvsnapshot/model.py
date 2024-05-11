from dataclasses import dataclass
from datetime import datetime
from typing import Any
from typing import Dict

__all__ = ["DataCatalog"]


@dataclass
class DataCatalog:
    key: str
    created_at: datetime
    data: Dict[str, Any]
