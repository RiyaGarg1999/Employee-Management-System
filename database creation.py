import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd="rude/1999"
)

# preparing a cursor object
cursorObject = database.cursor()

# creating database
cursorObject.execute("CREATE DATABASE amdocs_projects_db")

# Success message
print("Database 'amdocs_projects_db' created successfully!")

