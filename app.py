from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', result=None)


@app.route('/calculate', methods=['POST'])
def calculate():
    result = None
    try:
        arg1 = int(request.form.get('arg1'))
        arg2 = int(request.form.get('arg2'))
        op = request.form.get('op')

        if op == 'sum':
            result = arg1 + arg2
        elif op == 'sub':
            result = arg1 - arg2
        elif op == 'mul':
            result = arg1 * arg2
        elif op == 'div':
            if arg2 == 0:
                result = "Error: Division by zero"
            else:
                result = arg1 / arg2
        else:
            result = "Invalid operation"
    except ValueError:
        result = "Error: Invalid input"

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
