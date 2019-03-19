from pymongo import MongoClient
from pprint import pprint
import pymongo as p

c = MongoClient()
d = c['lab7']
r = d['res']
s = d['st']

r.create_index([('name',p.TEXT)])
s.create_index([('loc',p.GEOSPHERE)])

n1_1 = r.find({'name':{'$regex':'Kimchi'}},{'name':1,'zipcode':1,'address.street':1,'_id':0})
n1_1_1 = r.find({'$text':{'$search':'Kimchi'}})
pprint(list(n1_1_1))

n1_2 = list(r.find({'$text':{'$search':'Nolbu'}}))
for i in n1_2:
    a = i['address']
    print(a)
    r = s.find({'loc':{
        '$near':{
            '$geometry':{
                'type':'Point','coordinates':a['coord']
                },'$maxDistance':150
                }
                }
                }
                )
    pprint(list(r))



n2_1=[{'$match':{'cuisine':'Korean'}},
{'$group':{'_id':'$borough','count':{'$sum':1}}}]

r = d['res']
pprint(list(r.aggregate(n2_1)))


from bson.son import SON

n2_1=[
    {'$match':{'cuisine':'Korean'}},
    {'$unwind':'$grades'},
    {'$group':{'_id':{'borough' : '$borough','grade':'$grades.grade'},'count':{'$sum':1}}},
    {'$sort':SON([('count',-1)])},
    {'$limit':5}
]
pprint(list(r.aggregate(n2_1)))

db = c['lab6']
a = db['air']
s = db['sta']
a.create_index([('name',p.TEXT)])
califonia = s.find_one({'code':'CA'})
n3_1 = [
    {'$match':{'$text':{'$search':'intl'}}},
    {'$match':{'loc':{'$geoWithin':{'$geometry':califonia['loc']}}}},
    {'$project':SON([('name',1),('type',1),('code',1),('_id',0)])},
    {'$sort':SON([('name',1),('code',-1)])}
]
pprint(list(a.aggregate(n3_1)))

r = d['res']
r.create_index([('address',p.GEO2D)])
r.create_index([('cuisine',p.TEXT)])
a = d['air']

airports = a.find({'type':'International'})
for a in airports:
    n3_2 =[
        {'$geoNear':{
            'near':a['loc'],
            'distanceField':'address.coord',        
            'query':{'cuisine':'Korean'},
            'maxDistance':2000
            
        }}
    ]
    pprint(list(r.aggregate(n3_2)))