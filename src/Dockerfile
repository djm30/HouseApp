FROM python:3.9.7

RUN apt-get update

RUN apt-get install

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

