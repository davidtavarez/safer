#!/usr/bin/env bash

echo 'Initializing database...'
flask db init
echo 'Running migrations...'
flask db migrate -m 'database init'
echo 'Updating database...'
flask db upgrade
echo 'Done with the database.'