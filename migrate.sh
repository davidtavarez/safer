#!/usr/bin/env bash

export FLASK_APP=main.py
export FLASK_ENV=production
rm -Rf migrations
flask db init && flask db migrate -m 'database init' && flask db upgrade