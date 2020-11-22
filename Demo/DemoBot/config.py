# (c) TICSIA
#
# demo bot config file
import os

bot_id = os.environ.get('BOT_ID','1205352313:AAHvh4X2cpF5TJCa2pTXb_YNORFvKyVzjb4')
connection_param={'dbname':'train-schedule','user':'bot','password':'qwerty','host':'127.0.0.1'}
mongo_connection = 'mongodb://localhost:27017'
ws = 'http://cbu.uz/ru/arkhiv-kursov-valyut/json/RUB/'
