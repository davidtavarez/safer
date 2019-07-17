#!/usr/bin/env bash

echo 'Installing requirements...'
pip install -r ./requirements.txt
echo 'Running migrate.sh'
chmod u+x ./migrate.sh && ./migrate.sh
echo 'Running test.sh'
chmod u+x ./test.sh && ./test.sh
