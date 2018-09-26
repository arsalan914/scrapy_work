FROM python:3.6.4

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip

RUN pip install scrapy

RUN mkdir app

COPY . app

