from pymongo import MongoClient
from abc import ABC,abstractmethod
from datamodel import Movie

def MongoCollection(ABC):
    __client = MongoClient()
    __collection = null    
    def __init__(self,collection):
        __collection = __client[collection]

    @abstractmethod
    def insert(self,data):
        pass
    
    @abstractmethod
    def delete(self,condition):
        pass

    @abstractmethod
    def update(self,condition,updatecontents):
        pass


def MovieCollection(MongoCollection):
    
    def insert(self,data):
        try:
            __collection.insert_one(data)
            return data.title
        except:
            return 'fail to insert'
