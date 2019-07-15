# coding=utf-8

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    UPLOAD_FOLDER = '/tmp/'  # This folder should be encrypted
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'safer.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import models
from app.views.index import index
from app.views.file import upload_file, download_file


@app.errorhandler(404)
def page_not_found(ex):
    return app.response_class(
        response='Dafuq R u doing here?!',
        status=404,
        mimetype='text/plain'
    )
