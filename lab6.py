from pymongo import MongoClient
from pprint import pprint
import pymongo
c = MongoClient()
db = c['lab6']
b = db.blog

pprint(b.find_one())
pprint(b.find({'writer':'Kim'}).explain())
pprint(b.find({'writer':'Kim'}).explain()['executionStats'])

b.create_index([('writer',pymongo.ASCENDING)])
b.index_information()

pprint(b.find({'writer':'Kim'}).explain()['executionStats'])

b.create_index([('_id',pymongo.DESCENDING),('writer',pymongo.ASCENDING)])
b.index_information()

b.drop_indexes()
pprint(b.index_information())

m = db.metro
m.create_index([('doc_id',pymongo.ASCENDING)],unique=True)
m.create_index([('intersect',pymongo.ASCENDING)],sparse=True)
m.drop_index('intersect_1')
m.create_index([('intersect_id',pymongo.ASCENDING)],unique=True,sparse=True)
pprint(m.index_information())

pprint(m.find().limit(2).sort([('doc_id',1)]).explain()['executionStats'])
pprint(m.find().limit(2).sort([('doc_id',1)]).hint([('intersect',1)]).explain()['executionStats'])

m.count_documents({})
m.count_documents({},hint='intersect_1')

from pymongo import GEOSPHERE

sta = db['sta']
sta.create_index([('loc',GEOSPHERE)])
pprint(sta.index_information())

sta.drop_index('loc_2dsphere')

res = db['res']
res.create_index([('name',pymongo.TEXT)])
pprint(res.index_information())

pprint(list(res.find({'$text':{'$search':'Kyochon'}},{'borough':1,'name':1,'_id':0})))