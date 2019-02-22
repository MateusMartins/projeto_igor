import mysql.connector as mariadb

mariadb_connection = mariadb.connect(
    user='root', 
    password='', 
    database='agro'
    )