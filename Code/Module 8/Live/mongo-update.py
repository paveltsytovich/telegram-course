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
query = { "author": "Derrick Mwiti" }
new_author = { "$set": { "author": "John David" } }

articles.update_one(query, new_author)

for article in articles.find():
  print(article)