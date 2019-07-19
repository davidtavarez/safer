#!/usr/bin/env bash

echo 'Installing requirements...'
pip install -r ./requirements.txt
chmod u+x ./migrate.sh && ./migrate.sh
chmod u+x ./test.sh && ./test.sh
