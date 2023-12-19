# flask_e2e_project
HHA 504- Final Project


## Brief Explanation of App:
- Its a flaskapp that calculates the Body Mass Index (BMI) based on the user-provided height and weight.
- I also included a small conversion calculator on the side, for height and weight, for users that know their measurements based on the imperial metric system and convert them into S.I units required for the calculator to work.
- Lastly the data inputted in the BMI calculator gets stores in a MySQL database.
  
 <img width="500" alt="Screenshot 2023-12-18 at 6 58 53 PM" src="https://github.com/angeliki-tzanou/flask_e2e_project/assets/141374140/a103da03-b8dd-485d-9607-fac41cc85f0b">

## Technologies: 
- Github (Version Control): linked my Google Shell Environment with my GitHub repo
- Flask (Python; Frotend & Backend): created a BMI Flask application
- MySQL (Database via GCP or Azure): connected my app with MySQL db through Azure
- SQLAlchemy (ORM): used as an ORM library to interact with my database
- .ENV (Environment Variables): stored all of my API keys and credentials
- Tailwind (Frontend Styling): used tailwind css for styling
- API Service (Flask Backend): used to create my routes and an endpoint in which my data retrieved from the app are shown in JSON format
- Logger and or Sentry.io (Debugging & Logging): Used logger as a log mechanism to debug and keep track of the activity recorded in my flask app.
- Docker (Containerization): I used docker for containerization to ensure that my app connected with my db, also ran in that isolated environment.
- GCP or Azure (Deployment): Used Azure for deployment
- Authorization (Google OAuth): only one I could not use
    - I was not able to successfully make it work but I have commented out parts of the code in my app.py that I was trying to use for Google OAuth

### Steps to run web service:
- Without Docker locally:
  - Create the flask app code e.g. app.py, templates etc.
  - Create a MySQL database in my case I used Azure
  - In the Google shell environment in my case, I created a .env file storing all the MySQL credentials
  - Then I connected my flaskapp environment with my MySQL database
  - Then in my terminal, I was able to navigate within and create a database to create a "BMI" table where all the data gets stored in from my web application when a user provides them
  - I ensured all packages were imported in my app.py and pip installed as well as included the necessary ones for my app to run in my ```requirements.txt``` file
  - Lastly I confirmed my app runs by using ```python app.py``` command where I clicked the link and it redirected me to my flask application successfully
 <img width="200" alt="Locallyapprunning" src="https://github.com/angeliki-tzanou/flask_e2e_project/assets/141374140/2771d911-559d-4c33-b0eb-63b1eefbac8f">


