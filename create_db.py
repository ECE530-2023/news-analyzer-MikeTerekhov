import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://terekhovhd:GreighT131@cluster0.g38mbdx.mongodb.net/?retryWrites=true&w=majority")

dbs = cluster.list_database_names()

# making data base
documents = cluster.documents
# creating necessary collections for users, documents, and analysis
user_collection = documents.user_collection
document_collection = documents.document_collection
analysis_collection = documents.analysis_collection


user = {
"name": "NAME",
"email": "EMAIL@BU.EDU",
"password": "PASSWORD"
    }

doc = {
"name": "NAME",
"type": "TYPE",
"owner_id": 123,
"upload_date MM/DD/YEAR": 3072001
    }

analysis = {
    "document_id": 123, 
    "keywords": ["hi", "bye"],
    "language": "LANGUAGE",
    "over_sentiment": "happy",
    }

def add_user(user):
    user_collection.insert_one(user)

def add_doc(doc):
    document_collection.insert_one(doc)

def add_analysis(analysis):
    analysis_collection.insert_one(analysis)

#add_user(user)
#add_doc(doc)
#add_analysis(analysis)

#inserted_id = document_collection[0].inserted_id
#print(inserted_id)

users = user_collection.find({})
for x in users:                
    print(x)
print("----------------")
docs = document_collection.find({})
for x in docs:
    print(x)
print("----------------")
ans = analysis_collection.find({})
for x in ans:
    print(x)
print("----------------")

from bson.objectid import ObjectId
_id = ObjectId("64166089bb48a5eef4f6ae59")
#document_collection.update_one({'_id': _id}, {"$addToSet" : {'document (text)' : ["this", "is", "the", "text", "in", "the", "doc"]}})