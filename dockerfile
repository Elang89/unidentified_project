FROM python:3.7-stretch

RUN mkdir flask_app

WORKDIR /flask_app

COPY . .

RUN python -m venv env
RUN . env/bin/activate

RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

ENV ENV_PORT 5000

ENV FLASK_ENV staging

ENV PG_HOSTNAME localhost
ENV PG_PORT 5432
ENV PG_USER root
ENV PG_PASSWORD password
ENV PG_DATABASE structure_db

RUN alembic upgrade head
