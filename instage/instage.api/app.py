from flask import Flask, render_template, redirect, url_for
import redis

app = Flask(__name__)
r = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_chore/<chore_id>')
def set_chore(chore_id):
    r.set('current_chore', chore_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
