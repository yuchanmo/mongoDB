from pymongo import MongoClient
import pymongo
from pprint import pprint


def osm():
    client = MongoClient('ds1.snu.ac.kr', port=27018, username='dsteam2', password='dsteam2', authsource='dsteam2') 
# db = client.dsteam2
# db.list_collection_names()
    db = client.osm 
    return db

# pprint(db.list_collection_names())
# ss = list(db.map.find({'properties.admin':'South Korea'}))
# db.map.find({
#     'properties'
# })


client.close()