import DemoBot.config as config
import psycopg2
from psycopg2 import sql
from contextlib import closing


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
   
             
             
        
def create_stations(connection,cursor):
    tbl_stations = """CREATE TABLE public.stations (
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
    title varchar(50) NOT NULL
    );"""
        
    cursor.execute(tbl_stations)
    connection.commit()
    stations = ("Вольный поселок","Поселение хоббитов","Обитель гворлума","Орки-I","Орки-II","Мордор")
    ids = dict()
    for station in stations:
         cmd = sql.SQL('INSERT INTO public."stations" (title) VALUES ({}) RETURNING id').format(sql.Literal(station))
         cursor.execute(cmd)
         connection.commit()
         ids[station] = cursor.fetchone()[0]    
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
    