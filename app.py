import random
from flask import Flask, request, render_template #request is not used, can be removed
import redis

app = Flask(__name__)

# The redis instance - Commetns on the code should exist only if they add value (In this case, they do not since they are self-explanatory)
r = redis.Redis(host='redis', port=6379, db=0, decode_responses=True) # Use meaningful names for variables, r can be redis_client

@app.route('/')
def show_main_page():
    return render_template("index.html")

@app.route('/roll', methods=['GET'])
def roll_die():
    roll = random.randint(1, 6)
    r.lpush("rolls-history", roll)
    return render_template("roll.html", result=roll) # add blank line before return statement for better readability

@app.route('/history')
def show_history():
    history = r.lrange('rolls-history',0,-1)
    return render_template('history.html', history=history) # add blank line before return statement for better readability


if __name__ == '__main__':
    port = int(os.environ.get("FLASK_PORT", 5000))  # fallback to 5000 if not set - FLASK_PORT is not a good name, use something like APP_PORT
    app.run(debug=True,host="0.0.0.0", port=port)
