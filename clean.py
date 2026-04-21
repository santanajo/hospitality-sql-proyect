import sqlite3

conn = sqlite3.connect("HOSPITALITY_coffee.db")
c = conn.cursor()
c.execute("DELETE FROM sales WHERE drink_name = ''")
conn.commit()
print("Filas borradas:", c.rowcount)
conn.close()