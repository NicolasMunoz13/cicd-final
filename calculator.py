# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World. Welcome to the CI/CD app"
