#!/usr/bin/env bash

app="safer"
docker build -t ${app} .
docker run --rm -d -p 56733:80 --name=${app} -v $PWD:/app ${app}