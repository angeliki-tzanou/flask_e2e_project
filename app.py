from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_dance.contrib.google import make_google_blueprint, google
import os

app = Flask(__name__)

load_dotenv()

## OAUTH section:
# Set a secret key for session management
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_default_secret_key')

google_bp = make_google_blueprint(
    client_id=os.environ.get('GOOGLE_OAUTH_CLIENT_ID'),
    client_secret=os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET'),
    redirect_to='google_login',
)

app.register_blueprint(google_bp, url_prefix='/google_login')


## MYSQL AUTH section:
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class BMI(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float, nullable=True)

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
            
            new_bmi = BMI(height=height, weight=weight, bmi=bmi)
            #new record inserted of my BMI object from my app
            db.session.add(new_bmi)
            # Saving data in db
            db.session.commit()

        except ValueError as e:
            error = str(e)

    return render_template('index.html', bmi=bmi, error=error)

@app.route('/api/bmi', methods=['GET'])
def get_bmi_data():
    bmi_data = BMI.query.all()
    bmi_list = [{'height': record.height, 'weight': record.weight, 'bmi': record.bmi} for record in bmi_data]
    return jsonify({'bmi_data': bmi_list})

### Google OAuth:
@app.route('/login')
def login():
    return render_template('login.html', google=google)

@app.route('/google_login')
def google_login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get('/plus/v1/people/me')
    assert resp.ok, resp.text
    return 'Logged in as: ' + resp.json()['displayName']

if __name__ == '__main__':
    app.run(debug=True)
