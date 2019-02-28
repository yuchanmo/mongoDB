from pymongo import MongoClient
from abc import ABC,abstractmethod
from datamodel import Movie

class MongoCollection(ABC):
    _client = MongoClient()
    _collection = _client.test
    def __init__(self,collection):
        self._collection = self._client[collection]

    @abstractmethod
    def insert(self,data):
        pass
    
    @abstractmethod
    def delete(self,condition):
        pass

    @abstractmethod
    def update(self,condition,updatecontents):
        pass


class MovieCollection(MongoCollection):    

    @property
    def moviecollection(self):
        return super()._collection

    def insert(self,data):
        try:
            d = dict(data)
            self._MongoCollection__collection.insert_one(d)
            return data.title
        except:
            return 'fail to insert'
    
    def insert_many(self,datas):
        try:
            ds = []
            for d in datas:
                dd = dict(d)
                ds.append(dd)
            
            super()._collection.insert_many(ds)
            return [d.title for d.title in datas]
        except:
            return 'fail to insert'

    def delete(self,condition):
        pass

    def update(self,condition,updatecontents):
        pass
