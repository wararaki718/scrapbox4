FROM python:3.8

RUN pip install poetry
COPY . /opt/app

WORKDIR /opt/app
RUN poetry config virtualenvs.create false && poetry install

WORKDIR /opt/app/src
