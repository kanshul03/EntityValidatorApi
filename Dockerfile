# Using official Python runtime as a parent image.
FROM python:3.7


# The enviroment variable ensures that the python output is set straight to the terminal with out buffering it first.
ENV PYTHONUNBUFFERED 1


# creating root directory for the project in the container
RUN mkdir /entity_validator_api_service

# Setting the working directory to /validate_api_service
WORKDIR /entity_validator_api_service/

# Copying the current directory contents into the container at /entity_validator_api_service
ADD . /entity_validator_api_service/

# Installing any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080

RUN python manage.py migrate

# Running API service using wild-card IP.
ENTRYPOINT ["python", "manage.py","runserver","0.0.0.0:8080"]