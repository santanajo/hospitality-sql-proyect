import sqlite3

conexion = sqlite3.connect("hospitality_coffee.db")
cursor = conexion.cursor()

cursor.execute("DELETE FROM sales")

conexion.commit() 
print("Tabla sales limpiada correctamente")

conexion.close()