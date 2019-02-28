from pymongo import MongoClient


client = MongoClient()
client.list_database_names()
db = client.yuchan
db.list_collection_names()
client.list_database_names()

db.create_collection('yuchancollection')
foo = db.foo

foo.insert({'testtest':'kk'})
for c in foo.find():
    print(c)


import datetime

post = {
    'author':'mike',
    'text':'my first blog post',
    'tags':['mongodb','python','pymongo'],
    'date':datetime.datetime.utcnow()
}


from pprint import pprint
result = foo.find_one()
pprint(list(result))
    
import numpy as np

testd = {k:np.random.randint(1,100) for k in range(100)}


foo.insert_one({'age':24,'name':'Jisu'})

manypeople = [
    {
        'age':24,
        'name':'Jisun'
    },
    {
        'age':51,
        'name':'Daeyoung'
    },
    {
        'age':24,
        'name':'Youngin'
    },
]

foo.insert_many(manypeople)

foo.insert_many([
    {'age':24,'name':'Jisu'},
    {'age':51,'location':'Seoul','name':'Jisu'},
    {'age':24,'name':'Youngjin'},
])

foo.update_many({'age':51},{'$set':{'location':'Califonia'}})

res = foo.delete_many({'age':51})



    
def inputMovieInfo():
    title = input('Movie Title : ')
    director = input('Director : ')
    genre = input('Genre : ')
    score = int(input('score : '))
