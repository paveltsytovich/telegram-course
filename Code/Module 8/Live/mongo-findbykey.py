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
result = articles.insert_one(article)

document = articles.find_one({'_id':ObjectId(result.inserted_id)})
print(document)
document = articles.find_one({'_id':ObjectId(result.inserted_id)},{ "_id": 0, "author": 1, "about": 1})
print(document)