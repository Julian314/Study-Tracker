import julian_Helperfunction as helper
import julian_Create_Tables as create
from julian_Show_Table import show_table
from julian_Show_ToDo import show_ToDo
import rahul_Insert_tables_general as insert
import rahul_delete_entry as delete
from Average_Calculator import avg_calculator
import update_entry as update

def main():

    database = "sampledb_aris.db"
    conn = helper.create_connection(database)
    create.create_tables(conn)
    var = 1
    while var:
        print("What would you like to do?")
        num1 = input("Press 1 to manipulate data, 2 to show a table, 3 for functions ")
        if int(num1) == 1:
            num2 = input("Press 1 to insert, Press 2 to delete, 3 to update " )
            if int(num2) == 1:
                columns, insertion_query = insert.get_insert_info()
                insert.insert_into_table(conn, columns, insertion_query)
            elif int(num2) == 2:
                table, primary_key = delete.get_delete_info(conn)
                delete.delete_entry(conn, table, primary_key)
            elif int(num2) == 3:
                table = input("which table do you want to update? ")
                update.update_entry(conn, table)
        elif int(num1) == 2:
            show_table(conn)
        elif int(num1) == 3:
            num2 = input("Press 1 to show your todo list, Press 2 to calculate your average grade ")
            if int(num2) == 1:
                show_ToDo(conn)
            elif int(num2):
                avg_calculator(conn)
        var = input("Press 1 if you would like to do something again, else 0 ")
    
    conn.close()

if __name__ == '__main__':
    main()
