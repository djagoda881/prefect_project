FROM ubuntu:latest

RUN apt update
RUN apt install python3-pip -y
RUN apt-get install libpq-dev -y sudo

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt