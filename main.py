from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, Flask"


@app.route("/user/<name>")
def user_message(name):
    return f"Hello, {name}"


if __name__ == '__main__':
    app.run(debug=True)
