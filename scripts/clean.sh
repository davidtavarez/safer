#!/usr/bin/env bash

docker-compose stop;
printf "\n${White}Removing cache...${Color_Off}\n"
rm -Rf ./app/__pycache__
rm -Rf ./app/src/__pycache__
printf "${White}Done.${Color_Off}\n"
printf "\n${White}Removing database...${Color_Off}\n"
rm -Rf ./app/src/safer.db
printf "${White}Done.${Color_Off}\n"
printf "\n${White}Removing migrations...${Color_Off}\n"
rm -Rf ./app/migrations
printf "${White}Done.${Color_Off}\n"
docker-compose rm -f