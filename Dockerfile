FROM python:3.6

RUN mkdir /golf_backend
WORKDIR /golf_backend

ADD requirements.txt /golf_backend/requirements.txt
RUN pip install --no-cache-dir --src /usr/src -r requirements.txt

ADD . /golf_backend
