import os
import json
import psycopg2


DATOS_CONN_PG = {}


# Cargamos los datos para conectar a cloudsql
with open('resources/datos_tabla_sql.json') as arch:
    DATOS_CONN_PG = json.load(arch)

def genera_cursor():
    conn = psycopg2.connect(**DATOS_CONN_PG)
    cur = conn.cursor()
    return conn, cur