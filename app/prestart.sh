#!/usr/bin/env bash

if [ ! -d "/app/migrations" ]; then
    echo 'Initializing database...'
    flask db init
fi
echo 'Running migrations...'
flask db migrate -m '.'
echo 'Updating database...'
flask db upgrade
echo 'Done with the database.'
echo 'Starting tests...'
pytest -vvv tests.py
echo 'Done'