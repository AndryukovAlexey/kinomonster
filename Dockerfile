FROM python:3.8

WORKDIR /usr/src/kinomonster

COPY . /usr/src/kinomonster/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
