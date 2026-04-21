import sqlite3
conexion = sqlite3.connect("hospitality_coffee.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM sales")

rows = cursor.fetchall()
for row in rows:
    print(row)

conexion.close()    