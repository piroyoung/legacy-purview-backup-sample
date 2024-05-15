import os

__all__ = ["Environments"]


class Environments:
    CLIENT_ID: str = os.getenv("CLIENT_ID")
    CLIENT_SECRET: str = os.getenv("CLIENT_SECRET")
    TENANT_ID: str = os.getenv("TENANT_ID")
    PURVIEW_ENDPOINT: str = os.getenv("PURVIEW_ENDPOINT")

    # PURVIEW_SCAN_ENDPOINT: str = os.getenv("PURVIEW_SCAN_ENDPOINT")

    @staticmethod
    def verify(self):
        assert self.CLIENT_ID, "CLIENT_ID is not set"
        assert self.CLIENT_SECRET, "CLIENT_SECRET is not set"
        assert self.TENANT_ID, "TENANT_ID is not set"
        assert self.PURVIEW_ENDPOINT, "PURVIEW_ENDPOINT is not set"
        # assert self.__PURVIEW_SCAN_ENDPOINT, "PURVIEW_SCAN_ENDPOINT is not set"

    def __str__(self):
        return ""
