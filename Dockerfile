FROM python:3.6-alpine

RUN mkdir -p /usr/src/app \
 && mkdir -p /etc/letsencrypt

WORKDIR /usr/src/app

COPY ./python-flask-server-generated/requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt \
 && pip3 install connexion[swagger-ui] \
 && apk add build-base libffi-dev libressl-dev \
 && pip3 install certbot-pdns \
 && pip3 install pyopenssl \
 && pip3 install tox

COPY ./python-flask-server-generated /usr/src/app

EXPOSE 8080 80 443

VOLUME /etc/letsencrypt /var/lib/letsencrypt
WORKDIR /opt/certbot

# Retrieve certbot code
RUN mkdir -p src \
 && wget -O certbot-1.0.0.tar.gz https://github.com/certbot/certbot/archive/v1.0.0.tar.gz \
 && tar xf certbot-1.0.0.tar.gz \
 && cp certbot-1.0.0/CHANGELOG.md certbot-1.0.0/README.rst src/ \
 && cp certbot-1.0.0/letsencrypt-auto-source/pieces/dependency-requirements.txt . \
 && cp -r certbot-1.0.0/tools tools \
 && cp -r certbot-1.0.0/acme src/acme \
 && cp -r certbot-1.0.0/certbot src/certbot \
 && rm -rf certbot-1.0.0.tar.gz certbot-1.0.0

# Generate constraints file to pin dependency versions
RUN cat dependency-requirements.txt | tools/strip_hashes.py > unhashed_requirements.txt \
 && cat tools/dev_constraints.txt unhashed_requirements.txt | tools/merge_requirements.py > docker_constraints.txt

# Install certbot runtime dependencies
RUN apk add --no-cache --virtual .certbot-deps \
        libffi \
        libssl1.1 \
        openssl \
        ca-certificates \
        binutils

# Install certbot from sources
RUN apk add --no-cache --virtual .build-deps \
        gcc \
        linux-headers \
        openssl-dev \
        musl-dev \
        libffi-dev \
    && pip install -r dependency-requirements.txt \
    && pip install --no-cache-dir --no-deps \
        --editable src/acme \
        --editable src/certbot \
&& apk del .build-deps

WORKDIR /usr/src/app
CMD ["python3", "-m", "swagger_server"]
