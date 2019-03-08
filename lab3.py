from pymongo import MongoClient
from pprint import pprint
client = MongoClient()
db = client.lab3
col = db.imdb


pprint(col.find_one({'name':'Lee'}))
col.insert_one({'name' : 'Lee', 'content' : 'Hello I’m Lee', "tags": ["Hello", "Greet"]})
col.update_one({'name':'Lee'},{'$push':{'comments' :{'$each':[{'name' : 'Kim', 'content' : 'Good posts.', 'like' : 0}]}}})
col.update_one({'name':'Lee'},{'$push':{'comments' :{'$each':[{'name' : 'Choi', 'content' : 'How is it going?', 'like' : 1},{'name' : 'David', 'content' : 'I’m David, What’s up?', 'like' : 2},{'name' : 'Kim', 'content' : 'Glad to hear that', 'like' : 3}]}}})
col.update_one({'name':'Lee'},{'$set':{'comments.1.like':2}})
col.update_one({'name':'Lee'},{'$set':{'comments.0.like':5}})
col.update_one({'name':'Lee'},{'$pop':{'comments':1}})
col.update_one({'name':'Lee'},{'$pull':{'comments':{'name' :'Choi'}}})
col.update_one({'name':'Lee'},{'$unset':{'comments':{'name' :'Choi'}}})

col.insert_many([{'name' : 'Kim', 'age' : 21, 'profile' : 'Hello I’m Kim'},{'name' : 'Lee', 'age' : 22 , 'profile' : 'Hello I’m Lee'},{'name' : 'Jung', 'age' : 22 , 'profile' : 'Hello I’m Jung'},{'name' : 'Park', 'age' : 26 , 'profile' : 'Hello I’m Park'}])
col.update_one({'name':'Kim'},{'$set':{'age':24}},upsert=True)
col.update_one({'name':'Koo'},{'$set':{'age':18}},upsert=True)
pprint(list(col.find().sort('_id',-1).limit(5)))


class ImdbCollection():
    client = MongoClient()
    db = client.lab3
    collection = db.imdb

    

def updatedMovieInfo(row):        
    tmp = dict(row)
    res = dict()
    score = tmp['score']
    genre = tmp['genre']
    
    if 'Horror' in genre:
        res['$pull'] ={'genre':'Horror'}        
        score -= 3        
    if 'Sci-Fi' in genre:
        score += 2
    res['$set'] = {'score' : score}        
    flag = 'sucess'
    flag = flag if (score >=0) and (score <=10) else 'low' if score < 0 else 'high'
    return title,res,flag


collection = db.imdb
rows =collection.find()
totalcnt = rows.count()
success_cnt = 0
high_cnt = 0
low_cnt = 0
print('[INFO]Processing...')
for r in rows:
    title,updatequery,flag = updatedMovieInfo(r)
    print(title,updatequery)
    if flag =='success':
        try:
            collection.update_one({'title':title},updatequery)
            success_cnt+=1
        except:
            print('error occured while updating')
    elif flag =='high':
        high_cnt +=1
    else:
        low_cnt +=1
    
print('[INFO] Success(%s/%s)'%(success_cnt,totalcnt))
print('[INFO] Failed because too high score(%s/%s)'%(high_cnt,totalcnt))
print('[INFO] Failed because too low score(%s/%s)'%(low_cnt,totalcnt))





def showMovie(title):
    collection.find_one()