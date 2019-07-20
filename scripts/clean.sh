#!/usr/bin/env bash

docker-compose -f stop;
printf "\n${White}Removing cache...${Color_Off}\n"
rm -Rf ./__pycache__
rm -Rf ./src/__pycache__
printf "${White}Done.${Color_Off}\n"
printf "\n${White}Removing database...${Color_Off}\n"
rm -Rf ./src/safer.db
printf "${White}Done.${Color_Off}\n"
printf "\n${White}Removing migrations...${Color_Off}\n"
rm -Rf ./migrations
printf "${White}Done.${Color_Off}\n"
docker-compose rm -f