import mysql.connector

# Establishing the database connection
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rude/1999",
    database="amdocs_projects_db"
)

# preparing a cursor object
cursorObject = database.cursor()

def login():
    employee_id = input("Enter your Employee ID: ")
    password = input("Enter your password: ")

    # query to check if id and password match
    query = "SELECT * FROM EMPLOYEES WHERE ID = %s AND PASSWORD = %s"
    cursorObject.execute(query, (employee_id, password))

    result = cursorObject.fetchone()  

    if result:
        # Assuming result[1] is first name and result[2] is last name
        print(f"Login successful! Welcome {result[1]} {result[2]}.")
    else:
        print("Invalid Employee ID or Password. Please try again!")

    return ""

# login()  
