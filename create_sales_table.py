import sqlite3

conn = sqlite3.connect("HOSPITALITY_coffee.db")
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS sales')
cursor.execute('''CREATE TABLE sales (
               sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
               sale_date TEXT,
               sale_hour TEXT,
               drink_name TEXT,
               milk_type TEXT,
               quantity INTEGER,
               revenue REAL,
               Location TEXT
     )''')

conn.commit()
conn.close()
print("Tabla sales creada correctamente")
          