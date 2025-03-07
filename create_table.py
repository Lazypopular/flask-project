import sqlite3

conn = sqlite3.connect("agents.db")
cursor = conn.cursor()

# ✅ สร้างตารางใหม่
cursor.execute("""
CREATE TABLE IF NOT EXISTS agents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    description TEXT NOT NULL,
    img TEXT NOT NULL
);
""")

conn.commit()
conn.close()

print("✅ สร้างตาราง agents สำเร็จ!")

