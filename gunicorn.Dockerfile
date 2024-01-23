FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/app

RUN apt-get update

RUN apt-get upgrade

RUN pip install --upgrade pip

COPY ./src .

RUN pip install -r requirements.txt
