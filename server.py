from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

user_data = []
def is_valid_number(input_string):
    try:
        # Convert the string to a float, which handles both integers and decimals
        float(input_string)
        return True
    except ValueError:
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a_number = request.form['a_number']
        name = request.form['name']
        user_input = request.form['user_input']


        # Validate A number and Calculated Result
        if a_number.lower().startswith('a') and is_valid_number(user_input):
            # Get the current timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            user_data.append({
                'a_number': a_number,
                'name': name,
                'user_input': float(user_input),
                'timestamp': timestamp  # Include the timestamp in user_data
            })

            return redirect(url_for('index'))
        else:
            return "Invalid input. A number must start with 'A' or 'a', and Calculated Result must be a number."

    return render_template('index.html', user_data=user_data)


@app.route('/summary')
def summary():
    return render_template('summary.html', user_data=user_data)

@app.route('/secure-summary')
def secure_summary():
    return render_template('secure_summary.html', user_data=user_data)

@app.route('/secure-clear')
def secure_clear():
    global user_data
    user_data = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
