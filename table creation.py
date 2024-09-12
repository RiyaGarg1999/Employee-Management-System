import mysql.connector
    
# establish connection to the database
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rude/1999",
    database="amdocs_projects_db"
)

# preparing a cursor object
cursorObject = database.cursor()

# creating employee table
employeeRecord = """CREATE TABLE EMPLOYEES(
ID INT AUTO_INCREMENT PRIMARY KEY,
FIRST_NAME VARCHAR(45) NOT NULL,
LAST_NAME VARCHAR(45) NOT NULL,
DATE_OF_BIRTH DATE NOT NULL,
ADDRESS VARCHAR(255),
CONTACT VARCHAR(15), 
PASSWORD VARCHAR(20)
)
"""

# table created
cursorObject.execute(employeeRecord)

# Success message
print("Employees table created successfully!")

# disconnecting from server
database.close()


