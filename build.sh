#! /usr/bin/bash

docker build --tag miapi .
docker tag miapi:latest miapi:v1.0.1