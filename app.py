from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
import logging

##Logger section:
logging.basicConfig(filename='bmi.log', level=logging.INFO)

app = Flask(__name__)
db = SQLAlchemy(app)

load_dotenv()

## MYSQL AUTH section:
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

class BMI(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    bmi = db.Column(db.Float, nullable=True)


# GOOGLE OAUTH:#################################################
##class User(db.Model, UserMixin):
    #id = db.Column(db.Integer, primary_key=True)
    # Add any additional fields for the User model as needed

# Flask-Login configuration
##login_manager = LoginManager(app)
###login_manager.login_view = 'google.login'

# Configure Google OAuth
##google_bp = make_google_blueprint(client_id=os.environ.get('GOOGLE_CLIENT_ID'),
                                  #client_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),
                                  #redirect_to='google_login',
                                  ##scope=['profile', 'email'])

#app.register_blueprint(google_bp, url_prefix='/google_login')

# Flask-Dance storage setup
#google_bp.backend = SQLAlchemyStorage(OAuthConsumerMixin, db.session, user=User)

@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info("Received POST request")

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
