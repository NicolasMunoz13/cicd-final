from flask import Flask

app = Flask(__name__)
first_term = 3
second_term = 2

@app.route("/")
def hello():
    return "Hello World. Welcome to the CI/CD app"
