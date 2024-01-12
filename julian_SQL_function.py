from sqlite3 import Error
import sqlite3
from julian_Helperfunction import create_connection

def insert_table(conn, table, sql):
    
    cur = conn.cursor()

    cur.execute(sql, table)

    conn.commit()

def create_table(conn, create_table_sql):

    """create a table from the create_table_sql statement

    :param conn: Connection object

    :param create_table_sql: a CREATE TABLE statement

    :return: """

    try:
        c = conn.cursor()

        c.execute(create_table_sql)
    except Error as e:
        print(e)