# FLASK / REACT App for Home Values
# originally setup with this: https://www.youtube.com/watch?v=Q2eafQYgglM

from flask import flask
app = Flask(__name__)


@app.route('/time')
def get_current_time():
	return {'time': time.time()}