from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

maps_data = {
    "Ascent": {
        "title": "Ascent",
        "image": "images/ascent.jpg",
        "key_points": ["A Main", "B Main", "Mid", "A Heaven", "B Heaven"],
        "attacker_spawn": "โซนกลางล่างของแผนที่",
        "defender_spawn": "โซนบนกลางของแผนที่",
        "spike_sites": ["A Site", "B Site"],
        "shortcuts": "Mid Courtyard สามารถควบคุมได้เพื่อเปลี่ยนทิศทางการโจมตี",
        "strategy": "ควบคุม Mid เพื่อเพิ่มทางเลือกในการโจมตี A หรือ B",
        "danger_spots": ["Market", "Defender Spawn", "A Rafters"],
        "utility_tips": "ใช้ Smoke หรือ Wall ปิด Mid เพื่อช่วยในการบุก",
        "agents": ["Omen", "Killjoy", "Sova", "Jett"],
        "pros": "มีโอกาสใช้กลยุทธ์ที่หลากหลาย, มีจุดให้ใช้ Utility ได้ดี",
        "cons": "ถ้าสูญเสีย Mid จะเสียเปรียบมาก"
    }
}

def get_db():
    conn = sqlite3.connect("agents.db")
    conn.row_factory = sqlite3.Row
    return conn

# def get_agents():
#     conn = sqlite3.connect("agents.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT name, role, description, image FROM agents")  # ตรวจสอบว่าคอลัมน์ถูกต้อง
#     agents = cursor.fetchall()
#     conn.close()
#     return agents

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/agents")
# def agents():
#     agents = get_agents()  # ดึงข้อมูลตัวละคร
#     return render_template("agents.html", agents=agents)  # ส่งไปที่ agents.html
def agents():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM agents")
    agents = cur.fetchall()
    conn.close()
    print("agents data:", agents)
    return render_template('agents.html', agents=agents)

@app.route('/maps')
def maps_page():
    conn = sqlite3.connect('maps.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description, img FROM maps")
    maps = cursor.fetchall()
    conn.close()
    return render_template('maps.html', maps=maps)

# หน้ารายละเอียดของแต่ละแผนที่
# @app.route('/map/<map_name>')
# def map_detail(map_name):
#     conn = sqlite3.connect('maps.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT name, description, img FROM maps WHERE name = ?", (map_name,))
#     map_info = cursor.fetchone()
#     conn.close()

#     if map_info:
#         return render_template('map_detail.html', name=map_info[0], description=map_info[1], image=map_info[2])
#     else:
#         return "Map not found", 404

@app.route("/map/<map_name>")
def map_detail(map_name):
    map_data = maps_data.get(map_name)
    if map_data:
        return render_template("map_detail.html", map=map_data)
    else:
        return "ไม่พบแผนที่", 404

@app.route('/weapons')
def weapons():
    return render_template('weapons.html')

if __name__ == '__main__':
    app.run(debug=True)