#!/usr/bin/env bash

echo 'Installing requirements...'
pip install -r ./requirements.txt
echo 'Initializing database...'
flask db init
echo 'Running migrations...'
flask db migrate -m 'database init'
echo 'Updating database...'
flask db upgrade
echo 'Done with the database.'

echo 'Running tests...'
pytest -vvv tests.py
echo "Perfect."
