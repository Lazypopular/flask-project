import sqlite3

conn = sqlite3.connect("agents.db")
cursor = conn.cursor()

agents = [
    ("Brimstone", "Controller", "สั่งการจากแนวหลัง เพิ่มประสิทธิภาพให้ทีม", "https://via.placeholder.com/300"),
    ("Viper", "Controller", "ใช้สารพิษเพื่อควบคุมสนามรบและทำให้ศัตรูอ่อนแอ", "https://via.placeholder.com/300"),
    ("Cypher", "Sentinel", "ผู้เชี่ยวชาญด้านการสอดแนมและดักจับศัตรู", "https://via.placeholder.com/300"),
    ("Reyna", "Duelist", "ดูดกลืนพลังจากศัตรูที่ล้มลงเพื่อเพิ่มพลังให้ตัวเอง", "https://via.placeholder.com/300"),
    ("Killjoy", "Sentinel", "ใช้เทคโนโลยีและกับดักเพื่อควบคุมพื้นที่", "https://via.placeholder.com/300"),
    ("Breach", "Initiator", "ใช้พลังทำลายสิ่งกีดขวางเพื่อเปิดทางให้ทีม", "https://via.placeholder.com/300"),
    ("Skye", "Initiator", "ใช้พลังจากธรรมชาติสนับสนุนเพื่อนร่วมทีม", "https://via.placeholder.com/300"),
    ("Yoru", "Duelist", "ใช้พลังแห่งมิติในการเคลื่อนที่และหลอกล่อศัตรู", "https://via.placeholder.com/300"),
    ("Astra", "Controller", "ควบคุมสนามรบจากระยะไกลด้วยพลังดวงดาว", "https://via.placeholder.com/300"),
    ("KAY/O", "Initiator", "หุ่นยนต์ทำลายพลังพิเศษของศัตรู", "https://via.placeholder.com/300"),
    ("Chamber", "Sentinel", "นักแม่นปืนที่สามารถใช้ปืนพิเศษและวางกับดัก", "https://via.placeholder.com/300"),
    ("Neon", "Duelist", "นักวิ่งความเร็วสูง ใช้พลังไฟฟ้าโจมตีศัตรู", "https://via.placeholder.com/300"),
    ("Fade", "Initiator", "ใช้พลังแห่งฝันร้ายเพื่อตามล่าศัตรู", "https://via.placeholder.com/300"),
    ("Harbor", "Controller", "ใช้น้ำสร้างโล่และควบคุมพื้นที่", "https://via.placeholder.com/300"),
    ("Gekko", "Initiator", "ใช้สิ่งมีชีวิตพิเศษช่วยต่อสู้และสนับสนุนทีม", "https://via.placeholder.com/300"),
    ("Deadlock", "Sentinel", "ใช้เทคโนโลยีขั้นสูงในการควบคุมพื้นที่และหยุดศัตรู", "https://via.placeholder.com/300"),
    ("Clove", "Controller", "ใช้พลังลวงตาและหมอกควันเพื่อควบคุมสนามรบ แต่สามารถเล่นเป็น Duelist ได้", "https://via.placeholder.com/300"),
    ("Tejo", "Initiator", "ใช้สกิลเพื่อไล่ที่ศัตรูและกดดันพื้นที่ของฝ่ายตรงข้าม", "https://via.placeholder.com/300"),
    ("Vyse", "Sentinel", "วางกับดักและป้องกันพื้นที่ด้วยเทคโนโลยีขั้นสูง", "https://via.placeholder.com/300"),
    ("Waylay", "Duelist", "เข้าไซท์แบบรวดเร็วและดุดันด้วยสกิลที่เน้นการบุกทะลวง", "https://via.placeholder.com/300")
]

cursor.executemany("INSERT INTO agents (name, role, description, img) VALUES (?, ?, ?, ?)", agents)

conn.commit()
conn.close()
