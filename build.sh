#! /usr/bin/bash

docker stop miapi
docker rm miapi

docker rmi miapi:latest
docker rmi miapi:v1.0.1

docker build --tag miapi .
docker tag miapi:latest miapi:v1.0.1