from sqlite3 import Error
import sqlite3
from julian_Helperfunction import create_connection, initialize_variable_from_console
import pandas as pd
import constant

#OVERVIEW_COLUMNS = [ 
#                                        ('subject', str),
#                                        ('lecturer', str),
#                                        ('credits', float),
#                                        ('departament', str, 'Ex: D-ITET'),
#                                        ('category', str),
#                                        ('semester', int),
#                                        ('session', str, 'Ex: HS22'),
#                                        ('weight', float),
#                                        ('status', bool, 'Have you finished this course?'),
#                                        ('priority', str, 'Ex: Low'),
#                                        ('target_grade', float),
#                                        ('final_grade', float),
#                                        ('hours_spent', str, 'Format: hh:mm:ss.')
#                                        ]

def input_update_entry(columns, selected_col):
    for item in columns:
        if item[0] == selected_col:
            column_name = item[0]
            column_type = item[1]
            message = ''

            if len(item) >= 3:
                message = item[2]
            if len(item) == 4 and item[4][0:11] == 'foreign_key':
                #variable = "make function to get the correct subject / bonus_id some function get_foreign_key_data(conn, which_id: str)"
                #row_data.append(variable)
                continue

            variable = initialize_variable_from_console(column_name, column_type, message=message)
            return variable

def update_entry(conn, table):
    type_text = ...
    entry_type = ...
    if table == 'overview':
        type_text = 'subject name.'
        entry_type = 'subject'
    else:
        type_text = 'entry ID (leftmost column)'
        entry_type = 'id'

    print(pd.read_sql_query("SELECT * FROM " + table + ";", conn))
    print(f"Which entry (row) would you like to update? Type the {type_text}")
    row = input(f"Type {type_text}: ")
    print(f"Which part of the entry (column) would you like to update?")
    col = input(f"Type the column name: ")
    print("Updating the following entry:")
    print(pd.read_sql_query(f"SELECT * from {table} WHERE {table}.{entry_type} = \"{row}\";", conn))

    # select the column set from the dictionary defined in constant.py
    column_set = constant.COLUMN_SET[table]

    print(f"What should the new value be?")
    new_val = input_update_entry(column_set, col)
    print(new_val)
    query = f"UPDATE {table} SET {col} = \"{new_val}\" WHERE {entry_type} = \"{row}\";"
    print(query)
    conn.execute(query)
    conn.commit()

