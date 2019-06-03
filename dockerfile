FROM python:3.7-stretch

RUN mkdir flask_app
RUN python -m pip install poetry

WORKDIR /flask_app

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN python -m poetry install