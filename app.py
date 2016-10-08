from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, world!"


app.run(debug=True, port=8000)
