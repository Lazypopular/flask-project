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
     },
    "Bind": {
        "title": "Bind",
        "image": "images/bind.jpg",
        "key_points": ["A Short", "A Bath", "B Long", "B Hookah"],
        "attacker_spawn": "โซนกลางของแผนที่",
        "defender_spawn": "โซนล่างของแผนที่",
        "spike_sites": ["A Site", "B Site"],
        "shortcuts": "มี Teleporter ที่สามารถใช้เปลี่ยนเลนได้เร็ว",
        "strategy": "ใช้ Teleporter อย่างชาญฉลาดเพื่อสร้างจังหวะโจมตี",
        "danger_spots": ["A Heaven", "B Elbow"],
        "utility_tips": "ใช้ Flash หรือ Stun ปิดมุมที่ศัตรูแอบซุ่ม",
        "agents": ["Raze", "Phoenix", "Brimstone", "Viper"],
        "pros": "มี Teleporter ให้ใช้กลยุทธ์ที่ไม่คาดคิด",
        "cons": "เส้นทางแคบ อาจโดน Utility ของศัตรูง่าย"
    },
    "Haven": {
        "title": "Haven",
        "image": "images/haven.jpg",
        "key_points": ["A Site", "B Site", "C Site", "Mid"],
        "attacker_spawn": "โซนกลางของแผนที่",
        "defender_spawn": "โซนที่มีจุดวาง Spike ถึง 3 จุด",
        "spike_sites": ["A Site", "B Site", "C Site"],
        "shortcuts": "ระวังการโจมตีจากหลายทิศทางพร้อมกัน",
        "strategy": "เน้นการควบคุมทั้งสามจุด A, B และ C เพื่อป้องกันได้ดี",
        "danger_spots": ["A Heaven", "C Window"],
        "utility_tips": "ใช้ Smoke หรือ Flash ที่จุดสำคัญเพื่อช่วยในการเคลียร์พื้นที่",
        "agents": ["Cypher", "Brimstone", "Omen", "Sage"],
        "pros": "สามารถวาง Spike ที่หลายจุด",
        "cons": "มีทางโจมตีจากหลายทิศทาง"
    },
    "Split": {
        "title": "Split",
        "image": "images/split.jpg",
        "key_points": ["A Site", "B Site", "Mid", "Ramps"],
        "attacker_spawn": "โซนกลางของแผนที่",
        "defender_spawn": "โซนที่มีการใช้เชือกและพื้นที่แคบ",
        "spike_sites": ["A Site", "B Site"],
        "shortcuts": "ใช้เชือกเพื่อข้ามพื้นที่สูง",
        "strategy": "ควบคุม Mid และ Ramp เพื่อเปิดเส้นทางไปยัง A หรือ B",
        "danger_spots": ["A Heaven", "B Elbow"],
        "utility_tips": "ใช้ Smokes หรือ Stuns ที่ Ramps เพื่อขัดขวางการโจมตี",
        "agents": ["Jett", "Phoenix", "Sage", "Brimstone"],
        "pros": "แผนที่เหมาะกับการใช้เชือกและมุมแคบ",
        "cons": "การโจมตีผ่านกลางอาจถูกตอบโต้ได้ง่าย"
    },
    "Icebox": {
        "title": "Icebox",
        "image": "images/icebox.jpg",
        "key_points": ["A Site", "B Site", "Mid", "Zipline"],
        "attacker_spawn": "โซนที่สูงชันและมีหิมะ",
        "defender_spawn": "พื้นที่ที่มี Zipline และสูง",
        "spike_sites": ["A Site", "B Site"],
        "shortcuts": "ใช้ Zipline เพื่อหลบการโจมตีหรือเพิ่มทางเลือกในการบุก",
        "strategy": "ใช้ Zipline เพื่อเพิ่มความหลากหลายในการโจมตี",
        "danger_spots": ["A Rafters", "B Back"],
        "utility_tips": "ใช้ Smoke เพื่อปิดมุมที่สูงและช่วยเพิ่มความคุ้มครอง",
        "agents": ["Sova", "Jett", "Raze", "Brimstone"],
        "pros": "มีพื้นที่หลากหลายสำหรับกลยุทธ์",
        "cons": "การยิงในพื้นที่แคบอาจทำให้การควบคุมยาก"
    },
    "Breeze": {
        "title": "Breeze",
        "image": "images/breeze.jpg",
        "key_points": ["A Site", "B Site", "Mid", "Long A"],
        "attacker_spawn": "โซนที่กว้างและมีทะเลทราย",
        "defender_spawn": "พื้นที่ที่เปิดโล่ง",
        "spike_sites": ["A Site", "B Site"],
        "shortcuts": "พื้นที่กว้างสามารถทำให้การโจมตีเร็วหรือช้าได้",
        "strategy": "ใช้พื้นที่กว้างในการควบคุมระยะการยิง",
        "danger_spots": ["A Heaven", "B Elbow"],
        "utility_tips": "ใช้ Smokes หรือ Molotovs เพื่อจำกัดการมองเห็น",
        "agents": ["Phoenix", "Sova", "Brimstone", "Jett"],
        "pros": "การโจมตีระยะไกลมีประสิทธิภาพ",
        "cons": "พื้นที่กว้างทำให้การควบคุมยาก"
    },
    "Fracture": {
        "title": "Fracture",
        "image": "images/fracture.jpg",
        "key_points": ["A Site", "B Site", "Mid", "Back Site"],
        "attacker_spawn": "เริ่มแยกกันสองฝั่ง",
        "defender_spawn": "เริ่มจากตำแหน่งที่แยกกัน",
        "spike_sites": ["A Site", "B Site"],
        "shortcuts": "จุดเชื่อมระหว่างสองฝั่งช่วยให้การโจมตียากขึ้น",
        "strategy": "ใช้การแยกตัวเพื่อเพิ่มทางเลือกในการโจมตี",
        "danger_spots": ["A Highground", "B Elbow"],
        "utility_tips": "ใช้ Smokes ปิดการมองเห็นที่ Mid",
        "agents": ["Raze", "Jett", "Brimstone", "Sage"],
        "pros": "สามารถแยกฝั่งและสร้างความยุ่งเหยิงได้",
        "cons": "ต้องระวังการโจมตีจากทั้งสองฝั่ง"
    },
    "Pearl": {
        "title": "Pearl",
        "image": "images/pearl.jpg",
        "key_points": ["A Site", "B Site", "Mid", "City Center"],
        "attacker_spawn": "สไตล์เมืองใต้น้ำ",
        "defender_spawn": "จุดศูนย์กลางของเมืองอนาคต",
        "spike_sites": ["A Site", "B Site"],
        "shortcuts": "การย้ายที่เร็วในเมืองใต้น้ำ",
        "strategy": "ใช้เมืองใต้น้ำเพื่อขัดขวางการเคลื่อนไหว",
        "danger_spots": ["A Heaven", "B Elbow"],
        "utility_tips": "ใช้ Flash หรือ Smoke เพื่อปิดมุมที่ศัตรูซุ่ม",
        "agents": ["Omen", "Viper", "Sova", "Jett"],
        "pros": "พื้นที่หลากหลายและยุทธศาสตร์ได้หลายทาง",
        "cons": "พื้นที่แคบและการโจมตีอาจถูกจำกัด"
    },
    "Lotus": {
        "title": "Lotus",
        "image": "images/lotus.jpg",
        "key_points": ["A Site", "B Site", "C Site", "Middle"],
        "attacker_spawn": "แผนที่มีประตูหมุนสามจุด",
        "defender_spawn": "โซนเริ่มต้นที่ปลอดภัย",
        "spike_sites": ["A Site", "B Site", "C Site"],
        "shortcuts": "เปิดประตูหมุนเพื่อทำให้ทางสะดวกขึ้น",
        "strategy": "ใช้ประตูหมุนให้เป็นประโยชน์ในการโจมตี",
        "danger_spots": ["A Heaven", "C Highground"],
        "utility_tips": "ใช้ Smoke หรือ Molotov เพื่อป้องกันการโจมตี",
        "agents": ["Raze", "Phoenix", "Sage", "Brimstone"],
        "pros": "ความยุ่งเหยิงจากการเปิดประตูหมุนช่วยเพิ่มความแปลกใหม่",
        "cons": "การควบคุมจุดหลายจุดอาจจะยาก"
    },
    "Sunset": {
        "title": "Sunset",
        "image": "images/sunset.jpg",
        "key_points": ["A Site", "B Site", "Mid", "Sunset Overlook"],
        "attacker_spawn": "บรรยากาศเมืองลอสแองเจลิส",
        "defender_spawn": "พื้นที่ในเมืองที่มีแสงสะท้อน",
        "spike_sites": ["A Site", "B Site"],
        "shortcuts": "บรรยากาศที่สามารถใช้ในการเคลื่อนที่อย่างรวดเร็ว",
        "strategy": "ใช้พื้นที่กว้างเพื่อโจมตีจากหลายมุม",
        "danger_spots": ["A Overlook", "B Elbow"],
        "utility_tips": "ใช้ Smoke หรือ Stuns ในพื้นที่ที่เปิดโล่ง",
        "agents": ["Brimstone", "Sage", "Jett", "Phoenix"],
        "pros": "บรรยากาศที่สวยงาม ช่วยให้การเคลื่อนที่ง่าย",
        "cons": "มีมุมที่ยากต่อการป้องกัน"
    },
    "Abyss" : {
        "title": "Abyss",
        "image": "images/abyss.jpg",
        "key_points": ["A Site", "B Site", "Mid", "Highground"],
        "attacker_spawn": "แผนที่ลอยฟ้าที่ไม่มีขอบเขต",
        "defender_spawn": "พื้นที่ที่ลอยฟ้า",
        "spike_sites": ["A Site", "B Site"],
        "shortcuts": "มุมสูงช่วยให้มองเห็นพื้นที่ได้ดี",
        "strategy": "ใช้ความสูงในการโจมตี",
        "danger_spots": ["A Highground", "B Window"],
        "utility_tips": "ใช้ Smokes เพื่อปิดจุดที่มองเห็นได้ดี",
        "agents": ["Sova", "Brimstone", "Phoenix", "Jett"],
        "pros": "การเคลื่อนที่จากมุมสูงช่วยให้โจมตีได้ง่าย",
        "cons": "การควบคุมพื้นที่แคบยาก"
    },
}

def get_db():
    conn = sqlite3.connect("agents.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/agents")
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