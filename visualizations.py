import sqlite3
import matplotlib.pyplot as plt
import os
os.chdir(r'C:\Users\Enrique Santana\OneDrive\Escritorio\hospitality_sql_project')
conn = sqlite3.connect("HOSPITALITY_coffee.db")
c = conn.cursor()

# Top 10 selling drinks
c.execute("""
    SELECT drink_name, COUNT(*) as total
    FROM sales
    GROUP BY drink_name
    ORDER BY total DESC
    LIMIT 10
""")
results = c.fetchall()

drinks = [row[0] for row in results]
totals = [row[1] for row in results]

plt.figure(figsize=(12, 6))
plt.barh(drinks, totals, color='steelblue')
plt.xlabel('Number of Sales')
plt.title('Top 10 Best Selling Drinks')
plt.tight_layout()
plt.savefig('top_drinks.png')
plt.show()

# Sales by location
c.execute("""
    SELECT location, COUNT(*) as total
    FROM sales
    GROUP BY location
""")
results2 = c.fetchall()

locations = [row[0] for row in results2]
totals2 = [row[1] for row in results2]

plt.figure(figsize=(8, 5))
plt.bar(locations, totals2, color=['coral', 'steelblue', 'green'])
plt.ylabel('Number of Sales')
plt.title('Sales by Location')
plt.tight_layout()
plt.savefig('sales_by_location.png')
plt.show()

print("Charts saved!")
conn.close()