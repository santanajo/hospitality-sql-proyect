import sqlite3
import pandas as pd

df = pd.read_csv('Hotel_sales_clean.csv')

conexion = sqlite3.connect('hospitality_coffee.db')
cursor = conexion.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sales 
        (sale_date, sale_hour, drink_name, milk_type, 
         quantity, revenue, takeaway, syrup, Location)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        row['sale_date'], row['sale_hour'], row['drink_name'],
        row['milk_type'], row['quantity'], row['revenue'],
        row['takeaway'], row['syrup'], row['location']
    ))

conexion.commit()
conexion.close()
print(f"Insertadas {len(df)} filas correctamente")