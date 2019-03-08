import mysql.connector as mariadb

def mariadb_connection():
    mariadb_connection = mariadb.connect(
        user='root', 
        password='',
        database='webscraping'
    )
    return mariadb_connection
