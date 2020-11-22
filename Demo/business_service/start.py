# -*- coding: utf-8 _*_
import random
import os

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    ContentType

def get_welcome():
    random.seed()
    with open(os.getcwd()+'\\data\\welcome.txt','r') as w:
        welcomes = [ c for c in w]
    i = random.randint(0,len(welcomes)-1)
    return welcomes[i]
 
def create_kdb():
    kdb_sauron = KeyboardButton('Расписание по станции Сауроновград')
    kdb_trains = KeyboardButton('Расписание от Сауроновград до Мордор')
    kdb_money = KeyboardButton('Курс валюты')
    kdb_search1 = KeyboardButton('Поиск башня ЛЭП')
    kdb_search2 = KeyboardButton('Поиск ЛЭП')
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(kdb_sauron,kdb_trains)
    markup.row(kdb_search1,kdb_search2)
    markup.row(kdb_money)
    return markup    
     
def start_command(message,bot):
        result = get_welcome()
        mark = create_kdb()
        return (result,mark)        
             