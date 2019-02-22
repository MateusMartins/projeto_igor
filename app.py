import database

cursor = mariadb_connection.cursor()

cursor.execute("SELECT first_name, last_name, age FROM customer")

for first_name, last_name, age in cursor:
    print("First name: {}, Last name: {}, Age: {}").format(first_name,last_name, age)