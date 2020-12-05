import DemoBot.config as config
import psycopg2
from psycopg2 import sql
from contextlib import closing
from datetime import datetime
from datetime import timedelta
import random
import re

random.seed()

def create_trains(connection,cursor,stations):
    pass # В этой функции выполните SQL запросы для внесения поездов в расписание 
             
        
def create_stations(connection,cursor):
    pass # В этой функции выполните SQL запросы для внесения станций в таблицу

def init():
    pass 
# В этой функции создайте SQL запросы для внесения в базу списка станций и поездов
# Для удобства, вынесите в отдельные функции, определенные выше, вставку данных о станциях
# и о поездах. Перейдайте в параметрах этих функций объект подключения к БД и  курсор
    
def get_stations():
    pass 
# Эта функция должна возвращаться строку, содержащую все доступные станции. 
# Каждая станция должна быть на отдельной строке. Используйте для этого символ '\n'
    
def schedule_by_station(station):
    pass
# Эта функция должна возвращать расписание поездов от указанной станции. 
# Для каждого поезда вы должны указать станцию отправления, станцию назначения,
# время отправления и время прибытия
# Каждый поезд должен быть отделен от другого символом '\n'
            
            
def schedule_from_to_station(from_station, to_station):
    pass
# Эта функция должна возвращать строку, содержащую расписание поездов от станции from_station до станции to_station
# Для каждого поезда вы должны указать станцию отправления, станцию назначения,
# время отправления и время прибытия
# Каждый поезд должен быть отделен от другого символом '\n'


def train_schedule(message):
# Эта функция вызывается ботом для получения расписания
# Не требуется изменять эту функцию, но вы можете это сделать
# по своему желанию
    single_station = r'^Расписание по станции (\w+){1}'
  
    from_to_station = r'^Расписание от (\w+){1} до (\w+){1}'    
    result = re.search(single_station ,message)
    if result:
      return  schedule_by_station(result.group(1))
    result = re.search(from_to_station,message)
    if result:
        return schedule_from_to_station(result.group(1),result.group(2))
    return 'Вы можете получить расписание по следующим станциям:\n' + get_stations()
    