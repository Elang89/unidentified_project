FROM python:3.7-stretch

RUN mkdir flask_app

WORKDIR /flask_app

COPY requirements-dev.txt requirements-dev.txt
COPY requirements.txt requirements.txt

RUN python -m venv env
RUN source ./env/activate

RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt