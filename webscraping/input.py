from database.database import mariadb_connection
import mysql.connector as mariadb

mariadb_connection = mariadb_connection()
cursor = mariadb_connection.cursor()

def input_table(data_dict, header):
    if data_dict:
        for i in range(len(data_dict['Licitador'])):
            cursor.execute("insert into licitacao (dt_abertura, licitador, modalidade, nr_publicacao, objeto) VALUES ('{}','{}','{}','{}','{}')".format(data_dict[header[0]][i], data_dict[header[1]][i], data_dict[header[2]][i], data_dict[header[3]][i], data_dict[header[4]][i]))
            mariadb_connection.commit()
        return 'Dados inseridos com sucesso'
    else:
        return 'data_dict nulo'
