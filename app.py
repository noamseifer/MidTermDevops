import random
from flask import Flask, request, render_template
import redis

app = Flask(__name__)

# The redis instance
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

@app.route('/')
def show_main_page():
    return render_template("index.html")

@app.route('/roll', methods=['GET'])
def roll_die():
    roll = random.randint(1, 6)
    r.lpush("rolls-history", roll)
    return render_template("roll.html", result=roll)

@app.route('/history')
def show_history():
    history = r.lrange('rolls-history',0,-1)
    return render_template('history.html', history=history)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5005)
