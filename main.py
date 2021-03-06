from flask import Flask
from flask import jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello This is HomePage of Frank Liang with continuous delivery! And it\'s working! '

@app.route('/name/<value>')
def name(value):
    return ("The name you enter in the parameter is " + value)

@app.route('/time/')
def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return(current_time)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
