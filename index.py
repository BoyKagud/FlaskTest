from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/hello-world", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return "Hello %s" % request.form["name"]
    else:
        return "Hello World"
