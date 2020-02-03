# Certbot REST API server

## Overview
This is a Docker container serves as REST API server that gets certificate using Certbot.  
You can easily activate container by using Docker command.

## Requirements
Python 3.5.2+

## Usage
To pull an image and run Docker container from Dockerhub,  
please execute the following from the root directory:  

```
docker pull procube/pdns_certbot_server

docker run -t -d --name=pdns_certbot_server_test \
-e CERTBOT_PDNS_BASE_URL=http://192.168.0.5:61001/api/v1 \
-e CERTBOT_PDNS_API_KEY=test_api_key \
-e CERTBOT_EMAIL=test@procube.jp \
-p 8080:8080 \
procube/pdns_certbot_server:latest \
python3 -m swagger_server
```

Please change environment variable into your own one.  
  
If you want to run containers from github source repository,  please read following.  
  
To run two Docker containers that serve as server and client respectively by `docker-compose`,  
please edit environment variable CERTBOT_PDNS_BASE_URL, CERTBOT_PDNS_API_KEY, and CERTBOT_EMAIL  
in docker-compose.yml at `test` directory.  
After that, please execute the following from the `test` directory:

```
docker-compose build
docker-compose up -d
```

To run the server on a Docker container by 'docker run',  
please execute the following from the root directory:

```
docker build -t pdns_certbot_server_test:latest .

docker run -t -d --name=pdns_certbot_server_test \
-e CERTBOT_PDNS_BASE_URL=http://192.168.0.5:61001/api/v1 \
-e CERTBOT_PDNS_API_KEY=test_api_key \
-e CERTBOT_EMAIL=test@procube.jp \
-p 8080:8080 \
pdns_certbot_server_test:latest \
python3 -m swagger_server
```
  
Please change environment variable into your own one.  
For more detail, read [the manual](pdns-certbot-server.readthedocs.io).
