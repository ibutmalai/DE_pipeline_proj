from pandas import DataFrame

class Loader():
    def __init__(self, data: DataFrame) -> None:
        self.data = data
        
    def save_csv(self, path: str):
        self.data.to_csv(path, index=False)
    
    def save_json(self, path:str):
        self.data.to_json(path)
    
    def save_excel(self, path:str):
        pass
