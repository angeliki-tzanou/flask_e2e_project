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
  - <img width="350" alt="Locallyapprunning" src="https://github.com/angeliki-tzanou/flask_e2e_project/assets/141374140/2771d911-559d-4c33-b0eb-63b1eefbac8f">

 - With Docker locally:
   - In my terminal I pip installed the necessary packages
   - Then instead of manually doing so, I used ```docker-compose build``` to build me a docker image for my app.
   - Then I used ```docker-compose up``` to start my application within the Docker created container
   - <img width="250" alt="Screenshot 2023-12-17 at 8 12 42 PM" src="https://github.com/angeliki-tzanou/flask_e2e_project/assets/141374140/76507f3d-104e-45dd-9b37-6a9c37dc17ef">

- Deploy app in Cloud:
  - In this step, I ran to a couple of issues while trying to deploy my app through Azure
  - I used the commands in my terminal to deploy my app such as ```curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash``` (to install azure in my environment), used ```az``` to ensure smooth installation of azure, used ```az login --use-device-code``` to authorize my device as a login, used ```az webapp up --resource-group <groupname> --name <app-name> --runtime <PYTHON:3.9> --sku <B1>``` with a resource group I had created in my azure account and wanted to use for this app and then naming the application.
  - I ran into a couple of issues trying to successfully deploy my app since it had some connectivity issues with my sql credentials
  - Thats why you will see throughout my app.py code I have included some ```print``` statements where I would test if my credentials were being successfully pulled from my ```.env``` file, while also keeping track of my log stream tab under my azure webapp application page.
  - By doing so i was able to make the necessary changes in my app.py code, as well as under my named ```bmi2``` web app in azure I navigated under Settings>Configurations and added in my application settings my ```database_url``` and ```sqlalchemy database uri``` and assigned them in the according values I had previously stored in my ```.env``` file which solved the problem:
<img width="600" alt="SuccessfulAzureDeplImage" src="https://github.com/angeliki-tzanou/flask_e2e_project/assets/141374140/5e4190c0-05f0-4f8f-ad73-6e96bce401c9">

- Template of my .env file:
  - MYSQL_USERNAME= my username from MySQL in Azure
  - MYSQL_PASSWORD= my set password
  - MYSQL_HOST= my host provided in this format e.g. host.mysql.database.azure.com
  - MYSQL_PORT= port which for Azure is 3306
  - MYSQL_DATABASE= the db name I created
  - DATABASE_URL= used this format and inputted my credentials where needed       mysql+mysqlconnector://username:pass@host.mysql.database.azure.com:3306/MYSQL_DB
  - SQLALCHEMY_DATABASE_URI= here similarly as well
 
- Success DEMO APP running- AZURE: (all other DEMOS and screenshots are in my ```docs``` folder)
  - [Azure ONLY.mov.zip](https://github.com/angeliki-tzanou/flask_e2e_project/files/13709892/Azure.ONLY.mov.zip)



