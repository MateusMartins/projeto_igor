import sys
sys.path.insert(0, '/home/mateus/Área de Trabalho/trabalho/projeto_igor/')
from database.database import mariadb_connection
import mysql.connector as mariadb
import matplotlib.pyplot

# Define os parametros
mariadb_connection = mariadb_connection()
cursor = mariadb_connection.cursor()
firstname_list = []
age_list = []

# Efetua o select dos dados
cursor.execute("SELECT firstname, age FROM customer")

# Cria as listas com os nomes e a idade
for firstname, age in cursor:
    firstname_list.append(firstname)
    age_list.append(age)

matplotlib.pyplot.plot(firstname_list, age_list)
matplotlib.pyplot.show()
