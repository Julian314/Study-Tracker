from julian_SQL_function import create_table
from julian_Helperfunction import create_connection
import sqlite3
from sqlite3 import Error
    
def avg_calculator(conn):

    sem = input("Please enter the semester you want the average of, enter 0 if you want all ")

    if int(sem) != 0:
        query = """SELECT SUM(final_grade * weight) / SUM(weight) FROM overview WHERE final_grade > 0 AND semester = """ + sem+""";"""
    else:
        query = """SELECT SUM(final_grade * weight) / SUM(weight) FROM overview WHERE final_grade > 0"""
    try:
        c = conn.cursor()

        average = c.execute(query)

        print(average.fetchone()[0])

        return average

    except Error as e:
        
        print(e)