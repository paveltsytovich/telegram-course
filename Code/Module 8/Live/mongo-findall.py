import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['bot']
article = {"author": "Derrick Mwiti",
            "about": "Introduction to MongoDB and Python",
            "tags":
                ["mongodb", "python", "pymongo"]}
articles = db.articles
for article in articles.find():
  print(article)