from flask import Flask

app = Flask(__name__)
first_term = 3
second_term = 2

@app.route("/")
def hello():
    return "Hello World. This is a calculator! <br/> " + add(first_term, second_term) + "<br/>" + subtract(first_term, second_term)

def add(first_term, second_term):
    return "The sum operation with " + str(first_term) + " and " + str(second_term) + " is " + str(first_term + second_term)

def subtract(first_term, second_term):
    return "The substract operation with " + str(first_term) + " and " + str(second_term) + " is " + str(first_term - second_term)