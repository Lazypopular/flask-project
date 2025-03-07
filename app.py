from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

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


@app.route('/weapons')
def weapons():
    return render_template('weapons.html')

if __name__ == '__main__':
    app.run(debug=True)