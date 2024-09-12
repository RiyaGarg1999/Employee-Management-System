import mysql.connector
import time
from registerEmployee import register
from loginEmployee import login
from viewEmployees import viewAllEmployees
from viewEmployeeById import viewEmployeeById
from updateEmployee import updateEmployee
from deleteEmployee import deleteEmployee

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rude/1999",
    database="amdocs_projects_db"
)

# preparing a cursor object
cursorObject = database.cursor()

def menu():
    while True:
        print("\n----- Employee Management System -----")
        print("1. Register New Employee")
        print("2. Login")
        print("3. View All Employees")
        print("4. View Employee By ID")
        print("5. Update Employee")
        print("6. Delete Employee")
        print("7. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                print("\n----- REGISTRATION -----")
                register()
                time.sleep(2)  # Pause for 2 seconds after registering
            case '2':
                print("\n----- LOGIN -----")
                login()
                time.sleep(2)
            case '3':
                print("\n----- VIEW EMPLOYEE DATA -----")
                print(viewAllEmployees())
                time.sleep(4)
            case '4':
                print("\n----- VIEW EMPLOYEE DATA BY ID -----")
                viewEmployeeById()
                time.sleep(3)
            case '5':
                print("\n----- UPDATE EMPLOYEE DETAILS -----")
                updateEmployee()
                time.sleep(2)
            case '6':
                print("\n----- DELETE EMPLOYEE DATA-----")
                deleteEmployee()
                time.sleep(2)
            case '7':
                print("\n----- EXIT -----")
                print('Exiting the system. Goodbye!')
                break
            case _:
                print("Invalid choice. Please try again!")
                time.sleep(2)

menu()

# disconnecting from server
database.close()






