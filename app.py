from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/agents')
def agents():
    return render_template('agents.html')

@app.route('/weapons')
def weapons():
    return render_template('weapons.html')

if __name__ == '__main__':
    app.run(debug=True)