from sqlite3 import Error
import sqlite3
from julian_Helperfunction import create_connection
import pandas as pd

# In case primary_key_data is a bonus_id, we might want to find out the corresponding entry outside like:
# bonus_id = function_to_find_bonus_id('subject')
# delete_entry(conn, bonus_tasks, bonus_id)
# On this note, this function can't detect children (yet), which need to be deleted in a foreign key constraint environment.
# Should we do this in the main logic of the program like the above or inside the function as well?
def get_delete_info(conn):
    while True:
        print("Where do you want to delete a row? ")
        index = input("Press 1 for overview, Press 2 for exercises, Press 3 for bonus, Press 4 for bonus_tasks ")
        if index == "1":
            primary_key_info = input("which subject do you want to delete? ")
            return "overview", primary_key_info
        elif index == "2":
            primary_key_info = input("from which subject do you want to delete a record from? ")
            return "exercises", primary_key_info
        elif index == "3":
            primary_key_info = input("from which subject do you want to delete a record from? ")
            return "bonus",primary_key_info
        elif index == "4":
            primary_key_info = input("from which bonus_id do you want to delete a record from? ")
            return "bonus_tasks",primary_key_info
        print("Number didnt match a table! Try again")

def delete_entry(conn, table, primary_key_data):
    #print(f"conn == {conn}, table == {table}, primary_key_data == {primary_key_data} ")
    key_column = ''
    if table == 'exercises' or table == 'bonus' or table == 'overview':
        key_column = 'subject'
    elif table == 'bonus_tasks':
        key_column = 'bonus_id'
    else:
        print(f"The table ('{table}') for deletion was not correctly specified. Aborting...")
        return
    if table != 'exercises':
        sql = f"DELETE FROM {table} WHERE {key_column} = \"{primary_key_data}\";"

    else:
        exercise_number = input("Which exercise do you want to delete?")
        sql = f"DELETE FROM {table} WHERE {key_column} = \"{primary_key_data}\" AND number = {exercise_number};"
    print(f"This SQL query is going to be executed: '{sql}' ")

    execute_prompt = 'N'
    execute_prompt = str(input(f"Deleting '{primary_key_data}' from '{table}'. Proceed (y/N)?: "))

    #print(f"execute_prompt: '{execute_prompt}' ")
    if execute_prompt != 'y' and execute_prompt != 'Y':
        print("Aborting deletion...")
        return
    conn.execute(sql)
    conn.commit()


#database = "sampledb_aris.db"
#conn = create_connection(database)
#delete_entry(conn, 'overview', 'Communication Networks')
