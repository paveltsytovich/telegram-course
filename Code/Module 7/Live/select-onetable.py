import config
import psycopg2
from psycopg2 import sql
from contextlib import closing

with closing(psycopg2.connect(**config.connection_param)) as conn:
    with conn.cursor() as cursor:
        columns = ("id","title")
        where = "Поселение хоббитов"
        cmd = sql.SQL('SELECT {} from public."stations" where {}').format(
            sql.SQL(',').join(map(sql.Identifier,columns)),
            sql.SQL('title = {}').format(sql.Literal(where))
        )
        cursor.execute(cmd)
        recordset = cursor.fetchall()
        for c in recordset:
            print(f"id={c[0]} title={c[1]}")