#!/usr/bin/env bash

echo 'Creating migrations folder...'
flask db init
echo 'Running migrations...'
flask db migrate -m 'database init'
echo 'Updating database...'
flask db upgrade
echo 'Done with the database.'
