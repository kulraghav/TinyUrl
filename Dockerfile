FROM python:3.6

EXPOSE 5000

ADD . /TinyUrlApp

WORKDIR /TinyUrlApp

RUN pip install -r requirements.txt