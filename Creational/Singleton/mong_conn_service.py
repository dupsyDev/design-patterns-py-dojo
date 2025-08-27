from config import Configuration

class MongoConnService():

    def __init__(self, config: Configuration):
            self._config = config
    
    def mongo_conn_string(self):
        host = self._config.getConfig("mongo_host")
        port = self._config.getConfig("mongo_port")
        database = self._config.getConfig("mongo_database")
        username = self._config.getConfig("mongo_username")
        password = self._config.getConfig("mongo_password")

        return f"host={host};port={port};database={database};username={username};password={password}"