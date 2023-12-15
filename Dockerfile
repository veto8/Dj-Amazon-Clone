# start docker with python
FROM python:3.11.7-slim-bullseye

# setup linux python
ENV PYTHONUNBUFFERED  = 1

# update linux kernal and setup tools
RUN apt-get update && apt-get -y install gcc libpq-dev

# folder project
WORKDIR /app

# copy requirments
COPY requirments.txt /app/requirments.txt

# install requirments
RUN pip install -r /app/requirments.txt

# copy project folder
COPY . /app/