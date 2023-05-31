import pyodbc

class Connector:
    def __init__(self, driver: str, server: str, database: str, trusted_connection: str = 'Yes') -> pyodbc.Connection:
        self.__driver = driver
        self.__server = server
        self.__database = database
        self.__trusted_connection = trusted_connection
        self.connector = self.createConnector()
    
    @property
    def driver(self):
        return self.__driver
    @driver.setter
    def driver(self, value: str):
        self.__driver = value
    
    @property
    def server(self):
        return self.__server
    @server.setter
    def server(self, value: str):
        self.__server = value
    
    @property
    def database(self):
        return self.__database
    @database.setter
    def database(self, value: str):
        self.__database = value

    @property
    def trusted_connection(self):
        return self.__trusted_connection
    @trusted_connection.setter
    def trusted_connection(self, value: str):
        self.__trusted_connection = value
    
    def createConnector(self):
        self.connector = pyodbc.connect(f'DRIVER={self.__driver};SERVER={self.__server };DATABASE={self.__database };Trusted_connection={self.__trusted_connection}')
        return self.connector  
    
    def createCursor(self):
        self.cnxn_cursor = self.connector.cursor()
        return self.cnxn_cursor
        
    def executeCursor(self, query: str):
        self.cnxn_cursor.execute(query)
        