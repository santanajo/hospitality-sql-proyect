import sqlite3

conn = sqlite3.connect("HOSPITALITY_coffee.db")
c = conn.cursor()
c.execute("UPDATE sales SET location = 'Cowboy' WHERE location = ''")
conn.commit()
print("Updated:", c.rowcount)
conn.close()