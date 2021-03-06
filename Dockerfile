FROM python:3.6.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /webapps
WORKDIR /webapps
# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
#RUN pip install -U pip setuptools
COPY requirements.txt /webapps/
COPY .env /webapps/
RUN pip install --upgrade pip
RUN pip install -r /webapps/requirements.txt
ADD . /webapps/
# Django service
EXPOSE 8001
