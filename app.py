from flask import Flask, render_template, request
from logic import generate_truth_table

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        expression = request.form['expression']
        truth_table = generate_truth_table(expression)
        return render_template('index.html', truth_table=truth_table, expression=expression)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
