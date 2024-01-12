from julian_Helperfunction import create_connection, initialize_variable_from_console
from julian_SQL_function import insert_table

def main():

    database = "/home/arbeite/studium_tracker/python-studium-tracker/sampledb_aris.db;foreign keys = true;"

    conn = create_connection(database)
    
    subject = initialize_variable_from_console('subject', str)
    number = initialize_variable_from_console('number', int)
    progress = initialize_variable_from_console('progress', int)
    completed_for_bonus = initialize_variable_from_console('completed_for_bonus', bool)
    time_expenditure = initialize_variable_from_console('time_expenditure', str)
    corrected = initialize_variable_from_console('corrected', bool)
    additional_notes = initialize_variable_from_console('additional_notes', str)

    with conn:

        exercises = (subject, number, progress, completed_for_bonus, time_expenditure, corrected, additional_notes);

        sql = '''INSERT INTO exercises(subject, number, progress, completed_for_bonus, time_expenditure, corrected, 
            additional_notes)
            VALUES(?,?,?,?,?,?,?)'''

        insert_table(conn, exercises, sql)


if __name__ == '__main__':
    main()

