from sqlite3 import Error
import sqlite3
from julian_Helperfunction import create_connection
import pandas as pd

def show_ToDo(conn):

    cur = conn.cursor()

    with conn:
        cur.execute("SELECT bonus.subject, bonus_tasks.task, bonus_tasks.progress FROM bonus_tasks JOIN bonus ON bonus_tasks.bonus_id = bonus.id WHERE bonus_tasks.progress < 100 UNION SELECT exercises.subject, exercises.number, exercises.progress FROM exercises WHERE progress < 100;")
        lst = cur.fetchall()
        for elem in lst:
            print(elem)
        #print(cur.fetchall())
        #print(pd.read_sql_query("SELECT bonus_tasks.task, bonus.subject FROM bonus_tasks JOIN bonus ON bonus_tasks.bonus_id = bonus.id WHERE bonus_tasks.progress < 100 UNION SELECT exercises.subject, exercises.number FROM exercises WHERE progress < 100;", conn))