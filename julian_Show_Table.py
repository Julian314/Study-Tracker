from sqlite3 import Error
import sqlite3
from julian_Helperfunction import create_connection
import pandas as pd

def show_table(conn):
    table = input("which table would you like to see ")

    with conn:
        try:
            print(pd.read_sql_query("SELECT * FROM " + table + ";", conn))
        except Error as e:
            print(e)

