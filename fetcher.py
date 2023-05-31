import pyodbc

class Fetcher():
    def __init__(self, executedCursor: pyodbc.Cursor) -> None:
        self.executedCursor = executedCursor
    
    def fetchone(self):
        self.executedCursor.fetchone()
    
    def fetchmany(self, number_records: int):
        self.executedCursor.fetchmany(number_records)
    
    def fetchall(self):
        self.executedCursor.fetchall()