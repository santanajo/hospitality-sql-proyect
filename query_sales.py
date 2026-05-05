import sqlite3

conn = sqlite3.connect("HOSPITALITY_coffee.db")
cursor = conn.cursor()

# Top selling drinks by quantity
print("=== TOP SELLING DRINKS ===")
cursor.execute("""
    SELECT drink_name, COUNT(*) AS total
    FROM sales
    GROUP BY drink_name
    ORDER BY total DESC
""")
for row in cursor.fetchall():
    print(row)

# Top drinks by revenue
print("\n=== TOP DRINKS BY REVENUE ===")
cursor.execute("""
    SELECT drink_name, SUM(revenue) AS total_revenue
    FROM sales
    GROUP BY drink_name
    ORDER BY total_revenue DESC
""")
for row in cursor.fetchall():
    print(row)

# Sales by location
print("\n=== SALES BY LOCATION ===")
cursor.execute("""
    SELECT location, COUNT(*) AS total_sales
    FROM sales
    GROUP BY location
    ORDER BY total_sales DESC
""")
for row in cursor.fetchall():
    print(row)

# Sales by day
print("\n=== SALES BY DAY ===")
cursor.execute("""
    SELECT sale_date, COUNT(*) AS total
    FROM sales
    GROUP BY sale_date
    ORDER BY sale_date
""")
for row in cursor.fetchall():
    print(row)

# Busiest hours
print("\n=== BUSIEST HOURS ===")
cursor.execute("""
    SELECT SUBSTR(sale_hour, 1, 2) AS hour, COUNT(*) AS total
    FROM sales
    GROUP BY hour
    ORDER BY total DESC
    LIMIT 5
""")
for row in cursor.fetchall():
    print(row)

# Lemuels total revenue
print("\n=== LEMUELS TOTAL REVENUE ===")
cursor.execute("""
    SELECT location, SUM(revenue) AS total_revenue
    FROM sales
    WHERE location = 'Lemuels'
    GROUP BY location
""")
for row in cursor.fetchall():
    print(row)

conn.close()