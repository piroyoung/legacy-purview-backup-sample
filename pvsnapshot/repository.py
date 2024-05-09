from abc import ABCMeta, abstractmethod
from typing import List

from pvsnapshot.model import DataCatalog


class DataCatalogRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_remote(self) -> DataCatalog:
        pass

    @abstractmethod
    def put_remote(self, data: DataCatalog):
        pass

    @abstractmethod
    def get_local(self, key: str) -> DataCatalog:
        pass

    @abstractmethod
    def put_local(self, data: DataCatalog):
        pass

    @abstractmethod
    def list_local(self) -> List[str]:
        pass
