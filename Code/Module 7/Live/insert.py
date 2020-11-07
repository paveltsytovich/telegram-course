import config
import psycopg2
from psycopg2 import sql
from contextlib import closing

with closing(psycopg2.connect(**config.connection_param)) as conn:
    with conn.cursor() as cursor:
        columns = ("title",)
        values = ("Вольный поселок",)
        cmd = sql.SQL('INSERT INTO public."stations" ({}) VALUES ({}) RETURNING id').format(\
            sql.SQL(',').join(map(sql.Identifier,columns)),\
            sql.SQL(',').join(map(sql.Literal,values)))              
        cursor.execute(cmd)
        conn.commit()
        id = cursor.fetchone()[0]
        print(id)
        