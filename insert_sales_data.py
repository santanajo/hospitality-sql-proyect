import sqlite3

conexion = sqlite3.connect("hospitality_coffee.db")
cursor = conexion.cursor()

sales_data = [ #------2026-03=12-----
    ("2026-03-12", "Americano", 26, 143.00),
    ("2026-03-12", "Cappuccino", 10, 55.00),
    ("2026-03-12", "Latte", 2, 11.00),
    ("2026-03-12", "Flat White", 16, 88.00),
    ("2026-03-12", "French Press", 2, 8.00),
    ("2026-03-12", "Cortado", 8, 14.00),
    ("2026-03-12", "Tea Selection", 11, 60.50),
    #-----2026-03-20---------
    ("2026-03-20", "Americano", 16, 88.00),
    ("2026-03-20", "Cappuccino", 8, 44.00),
    ("2026-03-20", "Double Espresso", 1, 4.50),
    ("2026-03-20", "Espresso", 4, 14.00),
    ("2026-03-20", "Latte", 5, 27.50),
    ("2026-03-20", "Flat White", 4, 22.00),
    ("2026-03-20", "French Press", 2, 9.00),
    ("2026-03-20", "Iced Latte", 2, 13.00),
    #----2026-03-21-----------
    ("2026-03-21", "Americano", 20,110.00),
    ("2026-03-21", "Cappuccino", 9, 49.50),
    ("2026-03-21", "latte", 6, 33.00),
    ("2026-03-21", "Flat white", 8, 44.00),
    ("2026-03-21", "Tea Selection", 10, 55.00),
]

cursor.executemany("""INSERT INTO sales (sale_date, drink_name, quantity, revenue) 
                   VALUES (?, ?, ?, ?)
                   """, sales_data)

conexion.commit()
print("Ventas insertadas correctamente")

conexion.close()