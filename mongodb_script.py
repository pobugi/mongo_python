"""
https://dev-gang.ru/article/integracija-mongodb-s-python-s-ispolzovaniem-pymongo-9hmv4a77cw/
"""

import pymongo
from pymongo.common import RETRY_READS

client = pymongo.MongoClient('localhost', 27017)
db = client['SeriesDB']
series_collection = db['series']


def insert_document(collection, data):
    return collection.insert_one(data).inserted_id

# new_show = {
#     "name": "FRIENDS",
#     "year": 1994
# }
# print(insert_document(series_collection, new_show)) # 5e4465cfdcbbdc68a6df233f


def find_document(collection, elements, multiple=False):

    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    return collection.find_one(elements)

# result = find_document(series_collection, {'name': 'FRIENDS'})
# print(result) # {'_id': ObjectId('5e3031440597a8b07d2f4111'), 'name': 'FRIENDS', 'year': 1994}


def update_document(collection, query_elements, new_values):
    collection.update_one(query_elements, {'$set': new_values})

# new_show = {
#     "name": "FRIENDS",
#     "year": 1995
# }
# id_ = insert_document(series_collection, new_show)
# update_document(series_collection, {'_id': id_}, {'name': 'F.R.I.E.N.D.S'})
# result = find_document(series_collection, {'_id': id_})
# print(result) # {'_id': ObjectId('5e30378e96729abc101e3997'), 'name': 'F.R.I.E.N.D.S', 'year': 1995}


def delete_document(collection, query):
    collection.delete_one(query)

# delete_document(series_collection, {'_id': id_})
# result = find_document(series_collection, {'_id': id_})
# print(result) # None