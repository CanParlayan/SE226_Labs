import mysql.connector

database = mysql.connector.connect(host="localhost", user="root", password="")

myCursor = database.cursor()
myCursor.execute("DROP DATABASE IF EXISTS marvel")
myCursor.execute("CREATE DATABASE marvel")
connection = mysql.connector.connect(host="localhost", user="root", password="", database="marvel")

if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected the MySQL Server version", db_Info)
    myCursor = connection.cursor()
    myCursor.execute("SELECT DATABASE();")
    record = myCursor.fetchone()
    print("You're connected to database:", record)

try:
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="marvel")
    myCursor = connection.cursor()
    myCursor.execute("DROP TABLE IF EXISTS Movies")
    query = """CREATE TABLE Movies (
    ID INT NOT NULL,
    MOVIE VARCHAR(255),
    DATE VARCHAR(255),
    MCU_PHASE VARCHAR(255),
    PRIMARY KEY(ID)
    )"""
    result = myCursor.execute(query)
    print("Tables have created successfully.")
    myCursor.execute("SHOW TABLES")

    for table_name in myCursor:
        print(table_name)

except mysql.connector.Error as error:
    print("Failed to create a table: {}".format(error))

finally:
    if connection.is_connected():
        myCursor.close()
        connection.close()
        print("MySQL connection is interrupted.")

try:
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="marvel")
    myCursor = connection.cursor()
    f = open("../../Desktop/Marvel.txt")
    while f:
        x = f.readline()
        if x == "":
            break
        s = x.split()
        mySql_insert_query = """INSERT INTO Movies (ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)"""
        record = (s[0], s[1], s[2], s[3])
        myCursor.execute(mySql_insert_query, record)
        connection.commit()
    print("Record inserted successfully into the table.")
    myCursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into the table {}".format(error))

finally:
    if connection.is_connected():
        myCursor.close()
        connection.close()
        print("MySQL connection is interrupted.")

try:
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="marvel")

    query = "SELECT * FROM Movies"
    myCursor = connection.cursor()
    myCursor.execute(query)
    records = myCursor.fetchall()
    print("Total number of rows in table:", myCursor.rowcount)
    print("Printing each row...")
    for row in records:
        print(row)
except mysql.connector.Error as error:
    print("Error reading data from MySQL table", error)
finally:
    if connection.is_connected():
        connection.close()
        myCursor.close()
        print("MySQL connection is closed.")

try:
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="marvel")

    query = "DELETE FROM Movies WHERE MOVIE = 'TheIncredibleHulk'"
    myCursor = connection.cursor()
    myCursor.execute(query)
    connection.commit()
    print("Record deleted successfully from Movies table.")
except mysql.connector.Error as error:
    print("Error deleting data from MySQL table", error)
finally:
    if connection.is_connected():
        connection.close()
        myCursor.close()
        print("MySQL connection is closed.")

try:
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="marvel")

    query = "SELECT * FROM Movies WHERE MCU_PHASE = 'Phase2'"
    myCursor = connection.cursor()
    myCursor.execute(query)
    records = myCursor.fetchall()
    for row in records:
        print(row)
except mysql.connector.Error as error:
    print("Error reading data from MySQL table", error)
finally:
    if connection.is_connected():
        connection.close()
        myCursor.close()
        print("MySQL connection is closed.")

try:
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="marvel")

    query = "UPDATE Movies SET DATE = 'November3,2017' WHERE MOVIE = 'Thor:Ragnarok'"
    myCursor = connection.cursor()
    myCursor.execute(query)
    connection.commit()
    print("Record updated successfully in Movies table.")
except mysql.connector.Error as error:
    print("Error updating data in MySQL table", error)
finally:
    if connection.is_connected():
        connection.close()
        myCursor.close()
        print("MySQL connection is closed.")
        