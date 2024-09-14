import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="amdocs_projects_db"
)

# preparing a cursor object
cursorObject = database.cursor()


def deleteEmployee():
    employee_id = input("Enter the employee id of the record you want to delete: ")

    confirm_status = input("Are you sure you want to delete? (Y/N): ")
    if confirm_status == 'Y' or confirm_status == 'y':
        query = "DELETE FROM EMPLOYEES WHERE ID = %s"
        cursorObject.execute(query,(employee_id,))
        database.commit()
        
        if cursorObject.rowcount:
            print(f"Employee with ID {employee_id} has been deleted successfully!")
        else:
            print(f"No employee found with ID {employee_id}. Please try again!!")

    else:
        print("Cancelling the delete operation. Exiting...")

    return ""

# deleteEmployee()
