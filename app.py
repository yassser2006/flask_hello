# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="color:red;">Welcome Nabil MLops.</h1>'

if __name__ == '__main__':
    app.run(host="0.0.0.0")

