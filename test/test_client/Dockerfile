FROM python:3.6-alpine

WORKDIR /usr/src/app

COPY ./python-client-generated/requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt \
 && pip3 install tox

RUN apk add build-base libffi-dev libressl-dev
RUN pip3 install certbot-pdns
RUN pip3 install pyopenssl

WORKDIR /root/test

COPY . .
