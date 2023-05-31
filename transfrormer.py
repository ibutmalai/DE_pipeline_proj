from pandas import DataFrame
from fetcher import Fetcher

class Transformer():
    def __init__(self, data: Fetcher) -> None:
        self.data = DataFrame.from_records(data)
    
#aici putem defini mai multe tipuri de transformari
    def cleanNulls(self, data):
        pass
    ``
    def aggregateSum(self, data):
        pass
    
    def aggregateaverage(self, data):
        pass