
from pymongo import MongoClient
from pprint import pprint
client2 = MongoClient('localhost', port=30000) 
db = client2['repl']

col = db['tx_test2']

with client2.start_session() as s:
    s.start_transaction()
    for i in range(5):
        col.insert_one({'_id':1110},session=s)

    s.commit_transaction()




