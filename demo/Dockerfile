# base python image
FROM python:3.10-alpine

# set project directory on VM
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# make sure to use latest pip
RUN pip install --upgrade pip

# install python dependencies
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

# copy remaining project files to VM
COPY . /app

# expose VM port to host machine
EXPOSE 8000

# start Django app on port 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]