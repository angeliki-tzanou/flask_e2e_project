from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    print("Received POST request")
    bmi = None
    error = None

    if request.method == 'POST':
        print("Form data:", request.form)
        try:
            ## height and weight are inputted in cm and kgs respectively:
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            print("Height:", height, "Weight:", weight)

            if height <= 0 or weight <= 0:
                raise ValueError("Height and weight must be positive numbers.")

            bmi = "{:.2f}".format(weight / ((height / 100) * (height / 100)))

        except ValueError as e:
            error = str(e)

    return render_template('index.html', bmi=bmi, error=error)

if __name__ == '__main__':
    app.run(debug=True)
