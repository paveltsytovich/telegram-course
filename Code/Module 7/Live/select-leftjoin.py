import psycopg2
from psycopg2 import sql
from contextlib import closing
import config

with closing(psycopg2.connect(**config.connection_param)) as conn:
    with conn.cursor() as cursor:
        columns = ("source.title","destination.title","trains.departuretime","trains.arrivaltime")
    
        cmd = sql.SQL("""
    select source.title ,destination.title , departuretime, arrivaltime from trains 
left join stations as source on source.id = trains.departurestation 
left join stations as destination on destination.id = trains.arrivalstation """)
        cursor.execute(cmd)
        recordset = cursor.fetchall()
        for c in recordset:
            print(c[0],c[1],c[2],c[3])