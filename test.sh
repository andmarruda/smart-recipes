#!/bin/bash

docker image rm smart-recepie:latest
docker build -t smart-recepie .
docker run --rm \
  -v $(pwd)/src:/app/src \
  -v $(pwd)/.env:/app/.env \
  -p 8080:8080 \
  smart-recepie:latest
