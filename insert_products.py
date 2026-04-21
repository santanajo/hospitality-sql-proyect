import sqlite3

conexion = sqlite3.connect("hospitality_coffee.db") 
cursor = conexion.cursor()

products = [ ("Espresso", "Coffee", 3.00),
            ("Americono", "Coffee", 3.50),
            ("Cappuccino", "Coffee", 4.00),
            ("Latte", "Coffee", 4.20),
            ("Flatwhite", "Coffee", 4.00),
            ("Tea", "Tea", 3.00),
              ("Hot Chocolate", "Chocolate", 4.20),
            ("Matcha", "Tea", 4.50)
            ("Cortado", "Coffee", 3.50)
            ("Machiato", "Coffee", 3.50)]

cursor.executemany("""INSERT INTO products (name, category,price) VALUES (?, ?, ?)
                   """, products)

conexion.commit()
print("Productos insertados correctamente")

conexion.close()
            