from database.database import mariadb_connection
import mysql.connector as mariadb
import datetime

mariadb_connection = mariadb_connection()
cursor = mariadb_connection.cursor()

def input_table(tempo):
    if tempo:
        cursor.execute("insert into senac (tempo) VALUES ('{}')".format(str(datetime.timedelta(seconds=tempo))))
        mariadb_connection.commit()
        return 'Dados inseridos com sucesso'
    else:
        return 'Tempo inexistente'
