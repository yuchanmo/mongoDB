from pymongo import MongoClient
from pprint import pprint

client = MongoClient('ds1.snu.ac.kr', port=27018, username='dsteam2', password='dsteam2', authsource='dsteam2') 
osm = client['osm']


metro = osm['metro']
n1_1 = metro.aggregate([
    {'$group':{'_id':{'line_num':'$line_num'},
    'max_station':{'$max':'$ride_pasgr_num'},
    'min_station':{'$min':'$ride_pasgr_num'},
    'avg_station':{'$avg':'$ride_pasgr_num'},
    }}
])
pprint(list(n1_1))

n1_2 = metro.aggregate([
    {'$match':{'use_dt':{'$gte':'20171221','$lte':'20171228'}}},
    {'$group':{'_id':'$use_dt','total_rider_pasgr':{'$sum':'$ride_pasgr_num'}}},
    {'$sort':{'_id':1}}

])

pprint(list(n1_2))