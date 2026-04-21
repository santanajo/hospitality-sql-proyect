import sqlite3

conexion = sqlite3.connect("hospitality_coffee.db")
cursor = conexion.cursor()
cursor.execute("SELECT category, COUNT(*) FROM products GROUP BY category")

products = cursor.fetchall()

for product in products:
    print(product)

conexion.close()    