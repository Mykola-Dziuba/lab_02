from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', display_text=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form.get('expression', '')
    try:
        # Use eval to calculate the result (be cautious with eval in real projects)
        result = eval(expression)
    except Exception:
        result = "Error"
    return render_template('index.html', display_text=f"{expression} = {result}")

if __name__ == '__main__':
    app.run(debug=True)
