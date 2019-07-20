#!/usr/bin/env bash

printf "\n${White}Booting up Docker Containers...${Color_Off}\n"
docker-compose up -d
OUTPUT=$(docker exec -ti saferhiddenservice onions --json | python -c "import sys, json; print json.load(sys.stdin)['safer'][0].split(':')[0]")
URL="http://${OUTPUT}/"

printf "\n${White}Finding the .onion URL...${Color_Off}\n"
printf "${White}${BCyan}$OUTPUT${Color_Off}\n"