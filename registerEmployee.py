import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rude/1999",
    database="amdocs_projects_db"
)

# preparing a cursor object
cursorObject = database.cursor()

def register():
    # Get employee data from user input
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    address = input("Enter your address: ")
    contact = input("Enter your contact number: ")

    # SQL query for inserting data into the EMPLOYEES table
    sql = "INSERT INTO EMPLOYEES(FIRST_NAME, LAST_NAME, DATE_OF_BIRTH, ADDRESS, CONTACT) \
    VALUES(%s, %s, %s, %s, %s)"
    val = (fname, lname, dob, address, contact)

    # execute the query and commit changes
    cursorObject.execute(sql,val)
    database.commit()

    if cursorObject.rowcount:
        # retrieving the employee id of the newly inserted employee
        employee_id = cursorObject.lastrowid
        password = employee_id * 10 + 5

        # Updating the EMPLOYEES table with the generated password
        password_update_query = "UPDATE EMPLOYEES SET PASSWORD = %s WHERE ID = %s"
        cursorObject.execute(password_update_query, (password, employee_id))
        database.commit()

        print(f"Hi {fname} {lname}. You are registered successfully!")
        print(f"Your employee ID is {employee_id}, and your password is {password}")
    else:
        print("Registration failed! Please try again.")
    # return f"{cursorObject.rowcount} records inserted."
    return ""

# register()
