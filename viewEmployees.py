import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rude/1999",
    database="amdocs_projects_db"
)

# preparing a cursor object
cursorObject = database.cursor()

def viewAllEmployees():
    # SQL query to read data from the EMPLOYEES table
    query = "SELECT * FROM EMPLOYEES"
    cursorObject.execute(query)

    result = cursorObject.fetchall()

    for row in result:
        # Formatting the date to 'dd-mm-yyyy'
        formatted_dob = row[3].strftime("%d-%m-%y")
        print((row[0], row[1], row[2], formatted_dob, row[4], row[5]))

    totalEmployees = len(result)
    return f"Total no. of employees: {totalEmployees}"

# totalEmployees = viewAllEmployees()
# print(totalEmployees)