import sqlite3

conn = sqlite3.connect("agents.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM agents")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()