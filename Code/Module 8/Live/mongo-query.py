import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient('mongodb://localhost:27017/')
db = client['bot']
article = {"author": "Derrick Mwiti",
            "about": "Introduction to MongoDB and Python",
            "tags":
                ["mongodb", "python", "pymongo"]}
articles = db.articles
result = articles.find({"tags" : {"$in": ["mongodb"]}})
for c in result:
    print(c)
document = articles.find_one({"author" : {"$eq" : "Derrick Mwiti"}})
print(document)