from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.lab4
c = db.people

def print_result(args,c=db.people):    
    res = c.find(*args)
    pprint(list(res))

n1_1 = [{'age':{'$lt':22}}]
print_result(n1_1)

n1_2 = [{'age':{'$gte':22,'$lte':26}}]
print_result(n1_2)

n1_3 = [{'name':'Lee'},{'_id':0,'profile':1}]
print_result(n1_3)

n1_2_1 = [{'name':{'$ne':'Lee'}}]
print_result(n1_2_1)

n1_2_2 = [{'name':{'$in':['Lee','Park']}}]
print_result(n1_2_2)

n1_2_2 = [{'$or':[{'name':'Lee'},{'name':'Park'}]}]
print_result(n1_2_2)

n1_2_3 = [{'$nor':[{'name':'Lee'},{'name':'Park'},{'name':'Lee'}]}]
print_result(n1_2_3)

n1_2_3 = [{'name':{'$nin':['Lee','Park','Lee']}}]
print_result(n1_2_3)



def print_result(args,c=db.people):    
    res = c.find(*args)
    pprint(list(res))

inv = db.inventory
n2_1 = [{'tags':{'$all':['appliance','school','book']}}]
print_result(n2_1,inv)

n2_2 = [{},{'tags':{'$slice':3}}]
print_result(n2_2,inv)

n2_3 = [{},{'tags':{'$slice':[1,3]}}]
print_result(n2_3,inv)

n2_4 = [{'qty':{'$elemMatch':{'color':'brown'}}}]
n2_4_2 = [{'qty.color':'brown'}]
inv.insert_one({'_id': 9999,
  'code': 'abc',
  'qty': {'color': 'brown', 'num': 100, 'size': '6'},         
  'tags': ['appliance', 'school', 'book']})
print_result(n2_4,inv)
print_result(n2_4_2,inv)

st = db.store
print_result([{}],st)

n3_1 = [{'buyer.name':'J.S. Lee'}]
print_result(n3_1,st)

n3_2 = [{'items'}]