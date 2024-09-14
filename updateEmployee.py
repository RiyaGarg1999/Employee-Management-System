import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="amdocs_projects_db"
)

# preparing a cursor object
cursorObject = database.cursor()

def updateEmployee():
    employee_id = input("Enter the employee id of the record you want to update: ")

    #  get new employee data from user input
    fname = input("Enter the new first name (leave blank if no change:) ")
    lname = input("Enter the new last name (leave blank if no change:) ")
    dob = input("Enter the new date of birth (YYYY-MM-DD, leave blank if no change): ")
    address = input("Enter the new address (leave blank if no change): ")
    contact = input("Enter the new contact number (leave blank if no change): ")
    password = input("Enter the new password (leave blank if no change): ")

    # dynamic sql query based on user input
    set_clause = []
    parameters = []

    if fname:
        set_clause.append("FIRST_NAME = %s")
        parameters.append(fname)
    if lname:
        set_clause.append("LAST_NAME = %s")
        parameters.append(lname)
    if dob:
        set_clause.append("DATE_OF_BIRTH = %s")
        parameters.append(dob)
    if address:
        set_clause.append("ADDRESS = %s")
        parameters.append(address)
    if contact:
        set_clause.append("CONTACT = %s")
        parameters.append(contact)
    if password:
        set_clause.append("PASSWORD = %s")
        parameters.append(password)

    # ensuring there's atleast one column to update
    if not set_clause:
        print("No updates provided. Exiting...")
        return ""

    set_clause_str = ", ".join(set_clause)
    query = f"UPDATE EMPLOYEES SET {set_clause_str} WHERE ID = %s"
    parameters.append(employee_id)

    # execute the query and commit changes
    cursorObject.execute(query,tuple(parameters))
    database.commit()

    if cursorObject.rowcount:
        print(f"Employee with ID {employee_id} has been updated successfully!")
    else:
        print(f"No employee found with ID {employee_id} or no changes were made")

    return ""

# updateEmployee()
