#The Flask application container will use python:3.10-alpine as the base image
FROM python:3.8-slim

#This command will create the working directory for our Python Flask application Docker image
WORKDIR /code

RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

#RUN apk --no-cache add build-base libffi-dev
#This command will copy the dependencies and libraries in the requirements.txt to the working directory
COPY requirements.txt /code

#This command will install the dependencies in the requirements.txt to the Docker image
RUN pip install -r requirements.txt

#This command will copy the files and source code required to run the application
COPY . .
EXPOSE 5000
#This command will start the Python Flask application Docker container