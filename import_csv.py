import sqlite3
import csv

conn = sqlite3.connect("HOSPITALITY_coffee.db")
cursor = conn.cursor()

with open("Hotel_sales.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
            row = {k.strip(): v.strip() for k, v in row.items()}
            cursor.execute('''
            INSERT INTO sales
            (sale_date, sale_hour, drink_name, milk_type, quantity, revenue, location)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            row["Sale date"],
            row["pSale_hour"],
            row["Drink name"],
            row["Milk type"],
            row["Quantity"],
            row["Revenue"],
            row["Location"]
        ))

conn.commit()
conn.close()
print("Datos importados correctamente")