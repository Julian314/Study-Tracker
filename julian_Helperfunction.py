from sqlite3 import Error
import sqlite3

def __initialize_variable_from_console(variable_name):

    #print(variable_name)

    variable = input(f"{variable_name}: " )
    try:
        variable = int(variable)
        return variable
    
    except ValueError:

        try:

            variable = float(variable)
            return variable

        except:

            if variable == "False" or variable == "FALSE" or variable == "false":
                return False

            if variable == "True" or variable == "TRUE" or variable == "true":
                return True
            return variable

def type_to_text(type):
    if type == str:
        return 'Input should be text based.'
    if type == float:
        return 'Input should be a number with decimal point.'
    if type == int:
        return 'Input should be a number without a decimal point.'
    if type == bool:
        return 'Input should be either True or False.'
    else:
        return 'Input type is unknown: ' + type

def initialize_variable_from_console(sql_column_name, type, message=''):
    
    print(f"Enter {sql_column_name}.", type_to_text(type), message)
    
    variable = __initialize_variable_from_console(sql_column_name)

    while not isinstance(variable, type):
        print(f"\nWrong Type. Enter {sql_column_name}.", type_to_text(type), message) 
        
        variable = __initialize_variable_from_console(sql_column_name)

    return variable

def create_connection(db_file):
    """create a databse connection to a SQLite database """

    conn = None

    try:

        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = ON")
        print("SQLite3 Version", sqlite3.version)

        return conn
    except Error as e:
        print("\nSomething went wrong when trying to connect to the database.")
        print("Error Type:", type(e), "\nError :", e)

    return conn