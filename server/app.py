#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def printer(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<parameter>')
def counter(parameter):
    numbers_str = ("\n".join(str(number) for number in range(int(parameter))))
    return numbers_str + "\n"

@app.route('/math/<num1>/<operation>/<num2>')
def mather(num1, operation, num2):
    # num1 = int(num1)
    # num2 = int(num2)
    if operation == "+":
        return str(int(num1) + int(num2))
    elif operation == "-":
        return str(int(num1) - int(num2))
    elif operation == "*":
        return str(int(num1) * int(num2))
    elif operation == "div":
        return str(int(num1) / int(num2))
    elif operation == "%":
        return str(int(num1) % int(num2))
    else:
        return "ERROR"
    
