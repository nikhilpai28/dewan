import mysql.connector

host = "sql6.freesqldatabase.com"
user = "sql6640892"
password = "STmI1qLAjm"
database = "sql6640892"

try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if connection.is_connected():
        print("Connected to the database")

    sample_data = ('Python','val')

    cursor = connection.cursor()
    insert_query = "INSERT INTO Softwares(SNO,SOFTWARE,LOCATION) VALUES (1,%s,%s)"
    cursor.execute(insert_query, sample_data)
    connection.commit()

    print("Sample data inserted")

    # Perform database operations here

except mysql.connector.Error as e:
    print("Error:", e)