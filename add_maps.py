import sqlite3

conn = sqlite3.connect("maps.db")
cursor = conn.cursor()

maps_data = [
    ('Pearl', 'แผนที่ใต้น้ำ สไตล์เมืองอนาคต', 'pearl.jpg'),
    ('Lotus', 'แผนที่ที่มีประตูหมุนสามจุด', 'lotus.jpg'),
    ('Sunset', 'แผนที่ในบรรยากาศเมืองลอสแองเจลิส', 'sunset.jpg'),
    ('Abyss', 'แผนที่ลอยฟ้าที่ไม่มีขอบเขต', 'abyss.jpg')
]


cursor.executemany("INSERT INTO maps (name, description, img) VALUES (?, ?, ?)", maps_data)
conn.commit()
conn.close()