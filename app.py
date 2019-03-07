import database
import mysql.connector as mariadb
import matplotlib.pyplot
import tkinter

# Define os parametros
mariadb_connection = database.mariadb_connection()
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

