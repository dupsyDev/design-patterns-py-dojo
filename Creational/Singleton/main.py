from config import Configuration
from mssql_conn_service import MSsqlConnService
from mong_conn_service import MongoConnService

if __name__ == "__main__":
    config = Configuration()
    
    config.setConfig("ms_host", "10.29.7.1")
    config.setConfig("ms_port", "5432")
    config.setConfig("ms_database", "dev_info")
    config.setConfig("ms_username", "admin_rocks")
    config.setConfig("ms_password", "*jwoWQu129$2")

    config.setConfig("mongo_host", "10.2.0.87")
    config.setConfig("mongo_port", "1234")
    config.setConfig("mongo_database", "dev_docs")
    config.setConfig("mongo_username", "admin_rocks")
    config.setConfig("mongo_password", "oP01@&bXc1")

    mssql_conn = MSsqlConnService(config)
    mongo_conn = MongoConnService(config)

    print(mssql_conn.mssql_conn_string())
    print(mongo_conn.mongo_conn_string())