import sqlite3
from sqlite3 import Error
from julian_Helperfunction import create_connection
from julian_SQL_function import create_table

def create_tables(conn):

    sql_create_overview_table = """ CREATE TABLE IF NOT EXISTS overview (
                                        subject text PRIMARY KEY NOT NULL,
                                        lecturer text,
                                        credits float,
                                        departament text,
                                        category text,
                                        semester integer,
                                        session text,
                                        weight float,
                                        status bool,
                                        priority text,
                                        target_grade float,
                                        final_grade float,
                                        hours_spent time
                                    );"""
    sql_create_exercises_table = """ CREATE TABLE IF NOT EXISTS exercises (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    subject text,
                                    number int,
                                    progress int,
                                    completed_for_bonus bool,
                                    time_expenditure time,
                                    corrected bool,
                                    additional_notes text,
                                    FOREIGN KEY (subject) REFERENCES overview(subject)
                                    ON DELETE CASCADE ON UPDATE CASCADE
                                    );"""
    sql_create_bonus_table = """ CREATE TABLE IF NOT EXISTS bonus (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    subject text,
                                    type text,
                                    enabled bool,
                                    progress float,
                                    FOREIGN KEY (subject) REFERENCES overview(subject)
                                    ON DELETE CASCADE ON UPDATE CASCADE
                                    );"""
    sql_create_bonus_tasks_table = """ CREATE TABLE IF NOT EXISTS bonus_tasks (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    bonus_id int,
                                    task text,
                                    progress float,
                                    time_expenditure time,
                                    FOREIGN KEY (bonus_id) REFERENCES bonus(id)
                                    ON DELETE CASCADE ON UPDATE CASCADE
                                    );"""
                            
    #conn = create_connection(database)

    if conn is not None:

        create_table(conn, sql_create_overview_table)
        create_table(conn, sql_create_exercises_table)
        create_table(conn, sql_create_bonus_table)
        create_table(conn,sql_create_bonus_tasks_table)


    else:

        print("Error! cannot create the database connection.")





