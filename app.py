import database
import mysql.connector as mariadb

mariadb_connection = database.mariadb_connection()

cursor = mariadb_connection.cursor()

cursor.execute("SELECT firstname, lastname, age FROM customer")

for first_name, last_name, age in cursor:
    print("First name: {}, Last name: {}, Age: {}".format(first_name,last_name, age))
