from pymongo import MongoClient
from pprint import pprint

def query(type,scores):
    with  MongoClient() as c:
        db = c.lab5
        gr = db.grade        
        scores = list(map(int,scores))
        if len(scores)==1:
            return list(gr.find({'type':type,'score':scores[0]}))
        else:
            return list(gr.find({'$and':[{'type':type},{'score':{'$gte': scores[0],'$lte': scores[1]}}]}))


while True:
    type,scores = input('search >').split()    
    scores = [scores[1]] if scores[1].find('-')<0 else sorted(scores[1].split('-'))
    res = query(type,scores)
    print('%-10s %-20s'%('sid',type))
    for row in res:
        print('%-10s %-20s'%(row['sid'],row['score']))

