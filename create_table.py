import sqlite3

conn = sqlite3.connect("maps.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS maps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    img TEXT NOT NULL
);
""")

conn.commit()
conn.close()