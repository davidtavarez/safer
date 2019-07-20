#!/usr/bin/env bash

printf "\n${White}Finding the .onion URL...${Color_Off}\n"
OUTPUT=$(docker exec -ti saferhiddenservice onions --json | python -c "import sys, json; print json.load(sys.stdin)['safer'][0].split(':')[0]")
URL="http://${OUTPUT}/"
printf "${White}${BCyan}$OUTPUT${Color_Off}\n"