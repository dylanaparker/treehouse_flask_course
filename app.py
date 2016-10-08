from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name="world"):
    return "Hello, {}!".format(name)

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    return str(num1+num2)


app.run(debug=True, port=8000)
