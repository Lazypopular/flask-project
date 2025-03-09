import sqlite3

conn = sqlite3.connect("maps.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM maps")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()