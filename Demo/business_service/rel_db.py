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
    stations = ("Сауроновград","Вольная","Хоббитон","Гворлум","Орки","Рохляндия","Мордор","Эльфийская")
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
    
def get_stations():
    result = ''
    with closing(psycopg2.connect(**config.connection_param)) as conn:
        with conn.cursor() as cursor:    
            cmd = "SELECT title FROM stations"
            cursor.execute(cmd)
            rows = cursor.fetchall()
            for c in rows:
                result += ' - ' + c[0] + '\n'
            return result
    
def schedule_by_station(station):
    result = ''
    with closing(psycopg2.connect(**config.connection_param)) as conn:
        with conn.cursor() as cursor:    
            cmd = sql.SQL("""select source.title, destination.title, departuretime,arrivaltime from trains
            left join stations as source on source.id = trains.departurestation
            left join stations as destination on destination.id = trains.arrivalstation
            where source.title = {} or destination.title = {} """).format(
                sql.Literal(station),
                sql.Literal(station))
            cursor.execute(cmd)
            if cursor.rowcount == 0:
                return "Нет поездов на этой станции"
            rows = cursor.fetchall()
            for c in rows:
                result += "Ст. отправления " + c[0] + ' время отправления ' + c[2].strftime("%H:%M") + ' ст. прибытия ' + c[1] + ' Время прибытия ' + c[3].strftime("%H:%M") + '\n\n'
            return result 
            
            
def schedule_from_to_station(from_station, to_station):
    result = ''
    with closing(psycopg2.connect(**config.connection_param)) as conn:
        with conn.cursor() as cursor:    
            cmd = sql.SQL("""select source.title, destination.title, departuretime,arrivaltime from trains
            left join stations as source on source.id = trains.departurestation
            left join stations as destination on destination.id = trains.arrivalstation
            where source.title = {} and destination.title = {} """).format(
                sql.Literal(from_station),
                sql.Literal(to_station))
            cursor.execute(cmd)
            if cursor.rowcount == 0:
                return "Нет поездов на этой станции"
            rows = cursor.fetchall()
            for c in rows:
                result += "Ст. отправления " + c[0] + ' время отправления ' + c[2].strftime("%H:%M") + ' ст. прибытия ' + c[1] + ' Время прибытия ' + c[3].strftime("%H:%M") + '\n\n'
            return result 

def train_schedule(message):
    single_station = r'^Расписание по станции (\w+){1}'
  
    from_to_station = r'^Расписание от (\w+){1} до (\w+){1}'    
    result = re.search(single_station ,message)
    if result:
      return  schedule_by_station(result.group(1))
    result = re.search(from_to_station,message)
    if result:
        return schedule_from_to_station(result.group(1),result.group(2))
    return 'Вы можете получить расписание по следующим станциям:\n' + get_stations()
    