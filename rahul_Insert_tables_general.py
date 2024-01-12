from julian_Helperfunction import create_connection, initialize_variable_from_console
from julian_SQL_function import insert_table
import constant
def get_insert_info():

    while True:

        print("in which table would you like to insert?")
        index = input("Press 1 for overview, Press 2 for exercises, Press 3 for bonus, Press 4 for bonus_tasks ")
        if int(index) == 1:
            return constant.OVERVIEW_COLUMNS, constant.OVERVIEW_INSERT_SQL
        elif int(index) == 2:
            return constant.EXERCISES_COLUMNS, constant.EXERCISES_INSERT_SQL
        elif int(index) == 3:
            return constant.BONUS_GENERAL_COLUMNS, constant.BONUS_GENERAL_INSERT_SQL
        elif int(index) == 4:
            return constant.BONUS_TASKS_COLUMNS, constant.BONUS_TASKS_INSERT_SQL
        print("Number didnt match a table! try again LOL")


def get_foreign_key(conn, foreign_key_name):
    if foreign_key_name == 'foreign_key_bonus_id':
        conn.execute("SELECT")
        conn.fetchall()
        pass
    if foreign_key_name == 'foreign_key_bonus_subject':
        pass
    if foreign_key_name == 'foreign_key_exercise_subject':
        pass

def insert_into_table(conn, columns, insertion_query):
    row_data = []
    for item in columns:
        column_name = item[0]
        column_type = item[1]
        message = ''

        if len(item) >= 3:
            message = item[2]
        #if len(item) == 4 and item[4][0:11] == 'foreign_key':
            #variable = "make function to get the correct subject / bonus_id some function get_foreign_key_data(conn, which_id: str)"
            #row_data.append(variable)
            #continue

        variable = initialize_variable_from_console(column_name, column_type, message=message)
        row_data.append(variable)

    row_data = tuple(row_data)
    print("The following information is being saved in the database:", row_data)
    
    with conn:
       insert_table(conn, row_data, insertion_query)
       print("Done Saving.")


#def insert_into_bonus_task(conn, columns, insertion_query):
#    row_data = []
#    for item in columns: