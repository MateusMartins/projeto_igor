import mysql.connector as mariadb

def mariadb_connection():
    mariadb_connection = mariadb.connect(
        user='root', 
        password='',
        database='agro'
    )
    return mariadb_connection
