import json
from unittest import TestCase

from pvsnapshot.model import DataCatalog


class TestDataCatalog(TestCase):
    dc_json: str = """
{
    "key": "20240512062232_Tables",
    "created_at": "2024-05-12 06:22:35.910334",
    "data": {
        "value": [
            {
                "objectType": "Tables",
                "updateBy": "77a0ff23-5541-4b36-a0b9-81ef14e60529",
                "contact": [
                    {
                        "contactType": "Owner",
                        "id": "77a0ff23-5541-4b36-a0b9-81ef14e60529"
                    },
                    {
                        "contactType": "Expert",
                        "id": "77a0ff23-5541-4b36-a0b9-81ef14e60529"
                    },
                    {
                        "contactType": "Expert",
                        "id": "f7fdb1cf-555c-46a6-9784-bf0a6694fd2c"
                    }
                ],
                "term": [
                    {
                        "name": "Silver",
                        "guid": "2621bc04-ed01-4ec7-b052-6f8a618b64f2",
                        "glossaryName": "Glossary"
                    },
                    {
                        "name": "CustomerID",
                        "guid": "212a0b72-5515-49ea-9164-aa050817ff0c",
                        "glossaryName": "Glossary"
                    },
                    {
                        "name": "Gold",
                        "guid": "39af82d7-28f8-4ec4-9f08-a36ccdfd48b7",
                        "glossaryName": "Glossary"
                    },
                    {
                        "name": "DimensionTable",
                        "guid": "b2ea3bd3-2841-4d5f-a57d-7eb420b6ddb4",
                        "glossaryName": "Glossary"
                    }
                ],
                "id": "1f4f9d5b-925f-4b43-8874-86f6f6f60000",
                "collectionId": "oh5tij",
                "displayText": "Customers",
                "isIndexed": true,
                "qualifiedName": "mssql://southridge-replica.database.windows.net/CloudSales/dbo/Customers",
                "entityType": "azure_sql_table",
                "updateTime": 1679020506076,
                "classification": [
                    "MICROSOFT.PERSONAL.NAME",
                    "MICROSOFT.PERSONAL.US.PHONE_NUMBER"
                ],
                "assetType": [
                    "Azure SQL Database"
                ],
                "createBy": "ServiceAdmin",
                "createTime": 1673502725977,
                "name": "Customers",
                "@search.score": 38.83327
            },
            {
                "endorsement": [
                    "certified"
                ],
                "objectType": "Tables",
                "updateBy": "77a0ff23-5541-4b36-a0b9-81ef14e60529",
                "contact": [
                    {
                        "contactType": "Owner",
                        "id": "77a0ff23-5541-4b36-a0b9-81ef14e60529"
                    },
                    {
                        "contactType": "Expert",
                        "id": "77a0ff23-5541-4b36-a0b9-81ef14e60529"
                    }
                ],
                "term": [
                    {
                        "name": "機械学習の特徴量前処理済",
                        "guid": "6cfaa858-d110-492c-bea8-7e754732759a",
                        "glossaryName": "システム管理"
                    },
                    {
                        "name": "Gold",
                        "guid": "3ef899ca-43eb-4822-916e-c40a5feefaca",
                        "glossaryName": "システム管理"
                    },
                    {
                        "name": "Gold",
                        "guid": "39af82d7-28f8-4ec4-9f08-a36ccdfd48b7",
                        "glossaryName": "Glossary"
                    }
                ],
                "id": "9063271f-17b6-4a0a-a290-b6f6f6f60000",
                "displayText": "FactOrders",
                "isIndexed": true,
                "qualifiedName": "mssql://example-synapse-01.sql.azuresynapse.net/pool01/dbo/FactOrders",
                "entityType": "azure_synapse_dedicated_sql_table",
                "updateTime": 1715322361711,
                "assetType": [
                    "Azure Synapse Analytics"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1673504154521,
                "name": "FactOrders",
                "@search.score": 37.70958
            },
            {
                "objectType": "Tables",
                "updateBy": "ServiceAdmin",
                "id": "4e543186-9a41-49dd-9048-40f6f6f60000",
                "collectionId": "oh5tij",
                "isIndexed": true,
                "qualifiedName": "mssql://southridge-replica.database.windows.net/CloudSales/dbo/Addresses",
                "entityType": "azure_sql_table",
                "updateTime": 1673502730040,
                "classification": [
                    "MICROSOFT.PERSONAL.PHYSICALADDRESS"
                ],
                "assetType": [
                    "Azure SQL Database"
                ],
                "createBy": "ServiceAdmin",
                "createTime": 1673502726010,
                "name": "Addresses",
                "@search.score": 35.545925,
                "displayText": "Addresses"
            },
            {
                "endorsement": [
                    "certified"
                ],
                "objectType": "Tables",
                "updateBy": "77a0ff23-5541-4b36-a0b9-81ef14e60529",
                "term": [
                    {
                        "name": "Gold",
                        "guid": "39af82d7-28f8-4ec4-9f08-a36ccdfd48b7",
                        "glossaryName": "Glossary"
                    },
                    {
                        "name": "DimensionTable",
                        "guid": "b2ea3bd3-2841-4d5f-a57d-7eb420b6ddb4",
                        "glossaryName": "Glossary"
                    }
                ],
                "id": "73fb7976-1726-4d1c-9e5e-3ff6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://example-synapse-01.sql.azuresynapse.net/pool01/dbo/DimCustomers",
                "entityType": "azure_synapse_dedicated_sql_table",
                "updateTime": 1673509121767,
                "assetType": [
                    "Azure Synapse Analytics"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1673504364984,
                "name": "DimCustomers",
                "@search.score": 35.391773,
                "displayText": "DimCustomers"
            },
            {
                "endorsement": [
                    "certified"
                ],
                "objectType": "Tables",
                "updateBy": "77a0ff23-5541-4b36-a0b9-81ef14e60529",
                "term": [
                    {
                        "name": "Gold",
                        "guid": "39af82d7-28f8-4ec4-9f08-a36ccdfd48b7",
                        "glossaryName": "Glossary"
                    }
                ],
                "id": "ae61c504-5416-43ce-8396-2bf6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://example-synapse-01.sql.azuresynapse.net/pool01/dbo/DimAddresses",
                "entityType": "azure_synapse_dedicated_sql_table",
                "updateTime": 1673505742118,
                "assetType": [
                    "Azure Synapse Analytics"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1673504364984,
                "name": "DimAddresses",
                "@search.score": 34.98631,
                "displayText": "DimAddresses"
            },
            {
                "objectType": "Tables",
                "updateBy": "ServiceAdmin",
                "id": "6d97668f-67e2-42dd-9796-8ef6f6f60000",
                "collectionId": "oh5tij",
                "isIndexed": true,
                "qualifiedName": "mssql://southridge-replica.database.windows.net/CloudSales/dbo/Orders",
                "entityType": "azure_sql_table",
                "updateTime": 1673502729732,
                "assetType": [
                    "Azure SQL Database"
                ],
                "createBy": "ServiceAdmin",
                "createTime": 1673502726029,
                "name": "Orders",
                "@search.score": 34.191772,
                "displayText": "Orders"
            },
            {
                "objectType": "Tables",
                "updateBy": "ServiceAdmin",
                "id": "8a4d26b9-4d34-48ba-ab44-a9f6f6f60000",
                "collectionId": "oh5tij",
                "isIndexed": true,
                "qualifiedName": "mssql://southridge-replica.database.windows.net/CloudSales/dbo/OrderDetails",
                "entityType": "azure_sql_table",
                "updateTime": 1673502729282,
                "assetType": [
                    "Azure SQL Database"
                ],
                "createBy": "ServiceAdmin",
                "createTime": 1673502725929,
                "name": "OrderDetails",
                "@search.score": 34.191772,
                "displayText": "OrderDetails"
            },
            {
                "objectType": "Tables",
                "updateBy": "ServiceAdmin",
                "id": "738324fe-5bce-4897-a4e4-2df6f6f60000",
                "collectionId": "oh5tij",
                "isIndexed": true,
                "qualifiedName": "mssql://southridge-replica.database.windows.net/CloudSales/dbo/Messages",
                "entityType": "azure_sql_table",
                "updateTime": 1673502728829,
                "assetType": [
                    "Azure SQL Database"
                ],
                "createBy": "ServiceAdmin",
                "createTime": 1673502725937,
                "name": "Messages",
                "@search.score": 34.009453,
                "displayText": "Messages"
            },
            {
                "objectType": "Tables",
                "updateBy": "ServiceAdmin",
                "id": "05c59718-a267-4181-a6c3-23f6f6f60000",
                "collectionId": "lxohd4",
                "isIndexed": true,
                "qualifiedName": "mssql://example-synapse-01.sql.azuresynapse.net/pool01/dbo/dummy",
                "entityType": "azure_synapse_dedicated_sql_table",
                "updateTime": 1673503473739,
                "assetType": [
                    "Azure Synapse Analytics"
                ],
                "createBy": "ServiceAdmin",
                "createTime": 1673503473739,
                "name": "dummy",
                "@search.score": 33.498627,
                "displayText": "dummy"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "0adb15dd-c2c1-4ea0-ae12-2ff6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://synapse-link-example-01.database.windows.net/MSSQLSERVER/CloudSales/dbo/Customers",
                "entityType": "mssql_table",
                "updateTime": 1674107302762,
                "assetType": [
                    "SQL Server"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1674107302762,
                "name": "Customers",
                "@search.score": 33.498627,
                "displayText": "Customers"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "0ba1b1c5-b586-4247-bfba-e4f6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://southridge-replica.database.windows.net/CloudSales/Hidden/Customers",
                "entityType": "azure_sql_table",
                "updateTime": 1674107302825,
                "assetType": [
                    "Azure SQL Database"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1674107302825,
                "name": "Customers",
                "@search.score": 33.498627,
                "displayText": "Customers"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "1006ef32-0253-4fbb-8662-65f6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://synapse-link-example-01.database.windows.net/MSSQLSERVER/CloudSales/Hidden/OrderDetails",
                "entityType": "mssql_table",
                "updateTime": 1674107307045,
                "assetType": [
                    "SQL Server"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1674107307045,
                "name": "OrderDetails",
                "@search.score": 33.498627,
                "displayText": "OrderDetails"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "11b99a20-c71f-430c-8a2a-2bf6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://southridge-replica.database.windows.net/CloudSales/Hidden/OrderUpdates",
                "entityType": "azure_sql_table",
                "updateTime": 1674107300374,
                "assetType": [
                    "Azure SQL Database"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1674107300374,
                "name": "OrderUpdates",
                "@search.score": 33.498627,
                "displayText": "OrderUpdates"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "142f76ea-f1a6-4ddd-8fde-edf6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://southridge-replica.database.windows.net/CloudSales/Hidden/AddressUpdates",
                "entityType": "azure_sql_table",
                "updateTime": 1674107303840,
                "assetType": [
                    "Azure SQL Database"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1674107303840,
                "name": "AddressUpdates",
                "@search.score": 33.498627,
                "displayText": "AddressUpdates"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "29773cd2-24a3-4b74-a026-90f6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://southridge-replica.database.windows.net/CloudSales/Hidden/Orders",
                "entityType": "azure_sql_table",
                "updateTime": 1674107304561,
                "assetType": [
                    "Azure SQL Database"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1674107304561,
                "name": "Orders",
                "@search.score": 33.498627,
                "displayText": "Orders"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "3839e539-d4c9-49ca-a1cd-84f6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://synapse-link-example-01.database.windows.net/MSSQLSERVER/CloudSales/Hidden/Orders",
                "entityType": "mssql_table",
                "updateTime": 1674107304561,
                "assetType": [
                    "SQL Server"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1674107304561,
                "name": "Orders",
                "@search.score": 33.498627,
                "displayText": "Orders"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "39bf10c7-e25f-4a62-a601-a5f6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://synapse-link-example-01.database.windows.net/MSSQLSERVER/CloudSales/dbo/OrderDetails",
                "entityType": "mssql_table",
                "updateTime": 1674107311345,
                "assetType": [
                    "SQL Server"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1674107311345,
                "name": "OrderDetails",
                "@search.score": 33.498627,
                "displayText": "OrderDetails"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "49f08b2c-4116-45a5-aaf4-58f6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://synapse-link-example-01.database.windows.net/MSSQLSERVER/CloudSales/dbo/Orders",
                "entityType": "mssql_table",
                "updateTime": 1674107310169,
                "assetType": [
                    "SQL Server"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1674107310169,
                "name": "Orders",
                "@search.score": 33.498627,
                "displayText": "Orders"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "72aaef09-70cb-469d-8174-51f6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://synapse-link-example-01.database.windows.net/MSSQLSERVER/CloudSales/Hidden/Customers",
                "entityType": "mssql_table",
                "updateTime": 1674107302825,
                "assetType": [
                    "SQL Server"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1674107302825,
                "name": "Customers",
                "@search.score": 33.498627,
                "displayText": "Customers"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "81442453-fc2f-4069-9b4e-60f6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://synapse-link-example-01.database.windows.net/MSSQLSERVER/CloudSales/Hidden/AddressUpdates",
                "entityType": "mssql_table",
                "updateTime": 1674107303840,
                "assetType": [
                    "SQL Server"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1674107303840,
                "name": "AddressUpdates",
                "@search.score": 33.498627,
                "displayText": "AddressUpdates"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "88169aae-b283-4b7b-abae-9df6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://synapse-link-example-01.database.windows.net/MSSQLSERVER/CloudSales/dbo/Addresses",
                "entityType": "mssql_table",
                "updateTime": 1674107300377,
                "assetType": [
                    "SQL Server"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1674107300377,
                "name": "Addresses",
                "@search.score": 33.498627,
                "displayText": "Addresses"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "9debbd57-fddf-4005-8863-fef6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://synapse-link-example-01.database.windows.net/MSSQLSERVER/CloudSales/Hidden/OrderUpdates",
                "entityType": "mssql_table",
                "updateTime": 1674107300374,
                "assetType": [
                    "SQL Server"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1674107300374,
                "name": "OrderUpdates",
                "@search.score": 33.498627,
                "displayText": "OrderUpdates"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "ed178313-fa47-4847-904f-38f6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://southridge-replica.database.windows.net/CloudSales/Hidden/OrderDetails",
                "entityType": "azure_sql_table",
                "updateTime": 1674107307045,
                "assetType": [
                    "Azure SQL Database"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1674107307045,
                "name": "OrderDetails",
                "@search.score": 33.498627,
                "displayText": "OrderDetails"
            },
            {
                "objectType": "Tables",
                "updateBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "id": "9ba26d6c-5325-432b-a9fd-87f6f6f60000",
                "isIndexed": true,
                "qualifiedName": "mssql://southridge-replica.database.windows.net/CloudSales/dbo/FactOrders",
                "entityType": "azure_sql_table",
                "updateTime": 1675906413222,
                "assetType": [
                    "Azure SQL Database"
                ],
                "createBy": "a89e5005-1b4a-425a-91b1-39f75797afcd",
                "createTime": 1675906413222,
                "name": "FactOrders",
                "@search.score": 32.298637,
                "displayText": "FactOrders"
            }
        ]
    }
}
    """
    dc: DataCatalog = DataCatalog(**json.loads(dc_json))

    def test_tables(self):
        for table in self.dc.tables:
            assert table.as_dict()
            assert table.json_dumps(indent=4, ensure_ascii=False)
