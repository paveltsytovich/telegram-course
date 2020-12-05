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
 

     
def start_command(message,bot):
        result = get_welcome()
        return (result,None)        
             