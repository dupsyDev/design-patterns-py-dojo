from config import Configuration

class MSsqlConnService():

    def __init__(self, config: Configuration):
            self._config = config
    
    def mssql_conn_string(self):
        host = self._config.getConfig("ms_host")
        port = self._config.getConfig("ms_port")
        database = self._config.getConfig("ms_database")
        username = self._config.getConfig("ms_username")
        password = self._config.getConfig("ms_password")

        return f"host={host};port={port};database={database};username={username};password={password}"