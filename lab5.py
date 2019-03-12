from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.lab5
st = db.store


def pp(query,collectionname,optional=None):
    res = collectionname.find(*query)
    if optional:
        res = (optional(res))
    pprint(list(res))

n1_1 = [{'buyer.name':'J.S. Lee'}]
pp(n1_1,st)

n1_2 =[{'items':{'$elemMatch':{'name':{'$regex':'iPhone Xs'}}}},{'_id':0,'items':1}]
pp(n1_2,st)
n1_2_2 = [{'items':{'$elemMatch':{'name':'iPhone Xs'}}},{'_id':0,'items':1}]
pp(n1_2_2,st)


n1_3 = [{'items.price':{'$gt':2000}},{'_id':0,'buyer':1}]
pp(n1_3,st)
n1_3_2 = [{'items':{'$elemMatch':{'price':{'$gt':2000}}}},{'_id':0,'buyer':1}]
pp(n1_3_2,st)


n1_4 = [{'items':{
    '$elemMatch':{
        'name' :'Apple Watch Series 4',
        'attribute.carrier':{
            '$exists':False}}}}]
pp(n1_4,st)

n2_1 = [{}]
pp(n2_1,st,lambda x : x.limit(3))

n2_2=[{}]
pp(n2_2,st,lambda x : x.skip(1).limit(2))

n2_3=[{}]
print(st.count_documents({}))

gr = db.grade
pp([],gr)

res = []
for i in range(100):
    t = gr.find({'sid':i})    
    if len(list(t)) !=3:
        gr.insert_one({'sid':i,'score':80,'type':'quiz'})

pprint(list(gr.find({'type':'quiz'}).sort('score',-1).limit(3)))