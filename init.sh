#!/usr/bin/env bash

sudo rm -Rf app/.pytest_cache app/__pycache__ app/views/__pycache__ app/helpers/__pycache__

app="safer"
docker build -t ${app} .
docker run -d -p 56733:80 \
  --name=${app} \
  -v $PWD:/app ${app}