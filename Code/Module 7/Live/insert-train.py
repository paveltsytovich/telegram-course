import config
import psycopg2
from psycopg2 import sql
from contextlib import closing

def insert_station(conn, cursor,value):
        columns = ("title",)
        values = (value,) # преобразование в tuple
        cmd = sql.SQL('INSERT INTO public."stations" ({}) VALUES ({}) RETURNING id').format(\
            sql.SQL(',').join(map(sql.Identifier,columns)),\
            sql.SQL(',').join(map(sql.Literal,values)))              
        cursor.execute(cmd)
        conn.commit()
        return cursor.fetchone()[0]  
def insert_train(conn,cursor,values):
    columns = ("departurestation","arrivalstation","departuretime","arrivaltime")
    cmd = sql.SQL('INSERT INTO public."trains" ({}) VALUES ({}) ').format(\
        sql.SQL(',').join(map(sql.Identifier,columns)), \
        sql.SQL(',').join(map(sql.Literal,values))) 
    cursor.execute(cmd)
    conn.commit()
    
     


with closing(psycopg2.connect(**config.connection_param)) as conn:
    with conn.cursor() as cursor:
        id_source = insert_station(conn,cursor,"Вольный поселок")
        id_destination = insert_station(conn,cursor,"Поселение хоббитов")
        departure_time = "10:00"
        arrival_time =  "12:00"
        schedule = (id_source,id_destination, departure_time,arrival_time)
        insert_train(conn,cursor,schedule)