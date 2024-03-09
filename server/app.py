#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:num>')
def count(num):
    return '<br>'.join(str(n) for n in range(1, num + 1))

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == 'add' or operation == '+':
        result = num1 + num2
    elif operation == 'sub' or operation == '-':
        result = num1 - num2
    elif operation == 'mul' or operation == '*':
        result = num1 * num2
    elif operation == 'div' or operation == 'div':  # Use 'div' in URL to avoid issues
        result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
    elif operation == 'mod' or operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
