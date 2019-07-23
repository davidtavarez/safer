#!/usr/bin/env bash

printf "\n${White}Booting up Docker Containers...${Color_Off}\n"
docker-compose up -d
printf "\n${White}Waiting 20 seconds, tor is booting up...${Color_Off}\n"
sleep 20
printf "\n${White}Finding the .onion URL...${Color_Off}\n"
OUTPUT=$(docker exec -ti saferhiddenservice onions --json | python -c "import sys, json; print json.load(sys.stdin)['safer'][0].split(':')[0]")
URL="http://${OUTPUT}/"
printf "${White}${BCyan}$OUTPUT${Color_Off}\n"

printf "\n${White}Adding an ${BCyan}upload${White} function to your ${BCyan}.bash_profile${White} file...${Color_Off}\n"
printf "${Yellow}"
COMMAND="function upload() { printf \"\nUploading file...\n\"; curl --socks5-hostname 127.0.0.1:9050 -H 'Expect:' -F \"file=@\${1}\" -F \"password=\${2}\" http://tx6j66gbja42nvg6sreumixajlwknlpngdysdw6fbkff3pydptwa26id.onion/file/upload; printf \"\nDone.\n\n\"; }"
echo $COMMAND >> ~/.bash_profile
printf "${Color_Off}"
printf "${White}Adding a ${BCyan}download${White} function to your ${BCyan}.bash_profile${White} file...${Color_Off}\n"
printf "${Yellow}"
COMMAND="function download() { printf \"\nDownloading file...\n\"; curl --socks5-hostname 127.0.0.1:9050 -H 'Expect:' -F \"key=\${2}\" http://tx6j66gbja42nvg6sreumixajlwknlpngdysdw6fbkff3pydptwa26id.onion/file/download/\${1} > \${3}; printf \"\n\nDone.\n\"; }"
echo $COMMAND >> ~/.bash_profile
printf "${Color_Off}"
printf "${White}Done. Remember to do:${BCyan} source ~/.bash_profile ${Color_Off}\n\n"

