import sqlite3

conexion = sqlite3.connect("hospitality_coffe.db")
cursor = conexion.cursor()

print("Base de datos creada correctamente")
conexion.close()