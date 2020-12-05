import pymongo
from pymongo import MongoClient
import DemoBot.config as config
import re

def init_nosql():
    print('Check MongoDB collection...', end = '')
    client  = MongoClient(config.mongo_connection)
    db = client['bot']
    articlies = db.articles
    
    if  articlies.count() == 0:
        article =  { "Object" : "Шуховская башня", "Desc": """                     
                    Шу́ховская ба́шня на Оке́ — единственная в мире гиперболоидная многосекционная опора линии
                    электропередачи, выполненная в виде несущей сетчатой оболочки. Высота 128 м. 
                    Расположена примерно в 12 км от города Дзержинск на левом берегу Оки, за посёлком Дачный
                    """,
                    "tags" : ["башня", "ЛЭП"] }
        articlies.insert_one(article)
        article = { "Object" : "Спасская башня", "Desc": """
                   Спа́сская ба́шня (Фро́ловская, Фло́ровская, Фролола́врская, Иерусали́мские воро́та) — 
                   проездная башня Московского Кремля, выходящая на Красную площадь. 
                   Построена в 1491 году архитектором Пьетро Солари
                   """,
                   "tags" : ["башня"]            
        }
        articlies.insert_one(article)
        article = { "Object" :  "Линия электропередачи", "Desc" : """
                    Ли́ния электропереда́чи (ЛЭП) — один из компонентов электрической сети, система энергетического
                    оборудования, предназначенная для передачи электроэнергии посредством электрического тока.
                    Также электрическая линия в составе такой системы, выходящая за пределы электростанции или 
                    подстанции
                   """,
                   "tags" : ["ЛЭП"]}
        articlies.insert_one(article)
        print('collection created!')
    else:
        print('collection exists!')

def search(message):
    result = ''
    keyword = re.split(r'[ ]',message)
    
    client  = MongoClient(config.mongo_connection)
    db = client['bot']
    articlies = db.articles
    rows = articlies.find( {"tags": {"$in" : keyword[1:]}})
    for c in rows:
        result += "{}\nОписание:\n {}\n".format(c['Object'],c['Desc'])
    return result