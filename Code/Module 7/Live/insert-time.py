import config
import psycopg2
from psycopg2 import sql
from contextlib import closing

def insert_into_station(conn, cursor,value):
        columns = ("title",)
        values = (value,) # преобразование в tuple
        cmd = sql.SQL('INSERT INTO public."stations" ({}) VALUES ({}) RETURNING id').format(\
            sql.SQL(',').join(map(sql.Identifier,columns)),\
            sql.SQL(',').join(map(sql.Literal,values)))              
        cursor.execute(cmd)
        conn.commit()
        return cursor.fetchone()[0]  
    


with closing(psycopg2.connect(**config.connection_param)) as conn:
    with conn.cursor() as cursor:
        id_source = insert_into_station(conn,cursor,"Вольный поселок")
        id_destination = insert_into_station(conn,cursor,"Поселение хоббитов")
        print(id_source,id_destination)