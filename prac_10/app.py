from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'
@app.route('/greet')
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

@app.route('/f')
@app.route('/f/<celsius>')
def f(celsius=""):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"{celsius} celsius is {fahrenheit} fahrenheit"

if __name__ == '__main__':
    app.run()