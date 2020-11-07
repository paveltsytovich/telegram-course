import psycopg2
from psycopg2 import sql
from contextlib import closing
import config

with closing(psycopg2.connect(**config.connection_param)) as conn:
    with conn.cursor() as cursor:
        columns = ("departuretime","arrivaltime","title")
      
        cmd = sql.SQL('SELECT {} from public."trains" inner join public."stations" on trains.departurestation = stations .id ').format(
            sql.SQL(',').join(map(sql.Identifier,columns)),           
        )
        cursor.execute(cmd)
        recordset = cursor.fetchall()
        for c in recordset:
            print(c[0],c[1],c[2])
            
    