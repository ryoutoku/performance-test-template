FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get upgrade

WORKDIR /app

COPY Pipfile /app/
COPY Pipfile.lock /app/

RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install --system