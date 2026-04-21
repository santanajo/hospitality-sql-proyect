import sqlite3

conexion = sqlite3.connect("hospitality_coffee.db")
cursor = conexion.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS orders (order_id INTEGER PRIMARY KEY AUTOINCREMENT,
               table_number INTEGER NOT NULL, order_time TEXT NOT NULL)""")

conexion.commit()

print("tabla orders creada correctamente")

conexion.close()