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
    tbl_trains = """CREATE TABLE public.trains (
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
    departurestation bigint NULL,
    arrivalstation bigint NULL,
    departuretime time(0) NULL,
    arrivaltime time(0) NULL
    );
        """
    cursor.execute(tbl_trains)
    connection.commit()
    columns = ("departurestation","arrivalstation","departuretime","arrivaltime")
   
    values = (
        (stations[0],stations[6],datetime.now(), datetime.now() + timedelta(minutes=random.randint(10,40))),
        (stations[0],stations[5],datetime.now(), datetime.now() + timedelta(minutes=random.randint(15,45))),
        (stations[4],stations[0],datetime.now(), datetime.now() + timedelta(minutes=random.randint(10,20))),
        (stations[5],stations[3],datetime.now(), datetime.now() + timedelta(minutes=random.randint(15,50))),
        (stations[2],stations[6],datetime.now(), datetime.now() + timedelta(minutes=random.randint(20,40)))
    )
    for value in values:
        cmd = sql.SQL('INSERT INTO public."trains" ({}) VALUES ({})').format(
          sql.SQL(',').join(map(sql.Identifier,columns)),
          sql.SQL(',').join(map(sql.Literal,value))                  
        )  
        cursor.execute(cmd)
    
    connection.commit();     
             
        
def create_stations(connection,cursor):
    tbl_stations = """CREATE TABLE public.stations (
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
    title varchar(50) NOT NULL
    );"""
        
    cursor.execute(tbl_stations)
    connection.commit()
    stations = ("Око Саурона","Вольный поселок","Поселение хоббитов","Обитель гворлума","Орки пост","Разъезд орков","Мордор","Платформа Эльфийская")
    ids = list()
    for station in stations:
         cmd = sql.SQL('INSERT INTO public."stations" (title) VALUES ({}) RETURNING id').format(sql.Literal(station))
         cursor.execute(cmd)
         connection.commit()
         ids.append(cursor.fetchone()[0])
    return ids


def init():
    print('use connection to postgre SQL:')
    print(config.connection_param)
    print('check postgre SQL tables...',end=' ')
    with closing(psycopg2.connect(**config.connection_param)) as conn:
        with conn.cursor() as cursor:
            cursor.execute("select * from information_schema.tables where table_name='stations'")   
            if cursor.rowcount:
                print('table stations exists.',end=' ')
            else:
                stations = create_stations(conn,cursor);
                print('table stations created.',end=' ')
            cursor.execute("select * from information_schema.tables where table_name='trains'") 
            if cursor.rowcount:
                print('table trains exists.',end=' ') 
            else:
                create_trains(conn,cursor,stations)
                print('table stations created...',end= ' ')
    print()
    
def get_stations(connection,cursor):
    cmd = "SELECT title FROM stations"
    cursor.execute(cmd)
    rows = cursor.fetchall()
    return (r[0] for r in rows)
    

def train_schedule(message):
     single_station = r'^Расписание по станции (\w+ \w*){1}'
     all_schedule = r'^Расписание поездов'
     from_to_station = r'Расписание от (\w+ \w*){1} до (\w+ \w*){1}'
     with closing(psycopg2.connect(**config.connection_param)) as conn:
        with conn.cursor() as cursor:
            
            
            
            
            
            stations = get_stations(conn,cursor) 
            regexp_stations = "|".join(stations)
            