FROM python:3.8.5-alpine

WORKDIR /usr/src/app


COPY ./Pipfile ./
COPY ./Pipfile.lock ./

RUN apk update  \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && python3.8 -m pip install pip --upgrade \
    && python3.8 -m pip install pipenv

RUN pipenv install

COPY . .
