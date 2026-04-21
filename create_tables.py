import sqlite3

conexion = sqlite3.connect("hospitality_coffee.db")
cursor =conexion.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY AUTOINCREMENT, 
               name TEXT NOT NULL, category TEXT MOT MULL, price REAL NOT NULL)""")

conexion.commit()

print("Tabla products creada correctamente")

conexion.close()