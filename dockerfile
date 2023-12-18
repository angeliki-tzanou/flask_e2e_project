# Using Python as a parent image
FROM python:3.10-slim-buster
# Working directory to my app in app.py
WORKDIR /app
# Copy the contents from the current directory (ex. contents from app.py, Dockerfile, requirements.txt) into the app container
COPY . /app/
# Ensure that needed packages in the requirements.txt file are being installed in this case "flask"
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y default-libmysqlclient-dev python3-dev build-essential
# Specify the port 5000 being used and can be accessed
EXPOSE 5000
# Ensure the app can run container starts running
CMD ["python", "app.py"]

# Docker build command: docker build -t app .
# Docker run command: docker run -d -p 8008:5000 app



##### Description of Part 1 commands: ######
# First we ensure the app runs locally
# Then we run docker build -t __name_of_app__ .
# This will build the docker image and run all the requirements in the txt file
# After the 10 sec that the command has ran successfully and installed and ran all necessary packages
# We can run docker images so we can see the docker image we just built with the name of the app
# After it pops up on the table then we use docker run -p port:port to expose it and run it in the port we would like to
# Then if we run docker -d -p port:port __name_of_flask__ which would give output to the ID of the container the app is running within
# Docker ps is a list of all the docker containers we have running and their container IDs
# To stop the container from running then you run docker stop ___ID of container running__ and it will stop the docker app from running
# To rerun again you run docker run -d -p port:port __name of app__