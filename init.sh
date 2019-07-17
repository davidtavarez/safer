#!/usr/bin/env bash

echo 'Deleting cache...'
sudo rm -Rf ./migrations/ ./src/safer.db ./.pytest_cache ./__pycache__ src/.pytest_cache src/__pycache__ src/views/__pycache__ src/helpers/__pycache__

app="safer"
docker build -t ${app} .
docker run --rm -d -p 56733:80 --name=${app} -v $PWD:/app ${app}