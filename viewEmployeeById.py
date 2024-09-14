import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="amdocs_projects_db"
)

# preparing a cursor object
cursorObject = database.cursor()

def viewEmployeeById():

    employee_id = input("Enter your Employee ID: ")
    # SQL query to read data from the EMPLOYEES table based on employee ID
    query = "SELECT * FROM EMPLOYEES WHERE ID = %s"
    cursorObject.execute(query, (employee_id,))

    #  fetch the result
    result = cursorObject.fetchone()

    if result:
        formatted_dob = result[3].strftime("%d-%m-%y")
        # Displaying employee details
        print(f"ID: {result[0]}")
        print(f"First Name: {result[1]}")
        print(f"Last Name: {result[2]}")
        print(f"Date of Birth: {formatted_dob}")
        print(f"Address: {result[4]}")
        print(f"Contact: {result[5]}")
    else:
        print(f"No employee found with ID: {employee_id}")

    return ""

# viewEmployeeById()
