from flask import Flask
from flask_rq import RQ, job

app = Flask(__name__)
app.config.from_pyfile("config.py")

rq = RQ()

@app.route('/')
@app.route('/index')
def index():

    # job = get_queue().enqueue(stuff)
    print(send_email())
    return "Heloo"

@job
def send_email():
    sum = 0
    for i in range(100000):
        sum += i**i

if __name__ == '__main__':
    app.run()