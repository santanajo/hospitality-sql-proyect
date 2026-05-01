import sqlite3

c = sqlite3.connect('hospitality_coffee.db')

fixes = [
    ("20026/03/25", "25/03/2026"),
    ("2026'03/29", "29/03/2026"),
    ("2026?03/25", "25/03/2026"),
    ("25/03/2025", "25/03/2026"),
    ("29/03/2029", "29/03/2026"),
]

for wrong, correct in fixes:
    c.execute("UPDATE sales SET sale_date = ? WHERE sale_date = ?", 
              (correct, wrong))
    print(f"Corregido: {wrong} → {correct}")
c.execute("UPDATE sales SET sale_date = '26/03/2026' WHERE sale_date = '26/02/2026'")
print("Corregido: 26/02/2026 - 26/03/2026")
c.commit()
c.close()
print("Listo!")