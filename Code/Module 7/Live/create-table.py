import config
import psycopg2
from contextlib import closing

with closing(psycopg2.connect(**config.connection_param)) as conn:
    with conn.cursor() as cursor:
        sql_cmd = """CREATE TABLE public.stations (
id bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
title varchar(50) NOT NULL
);"""
 
        cursor.execute(sql_cmd)
        conn.commit()

    