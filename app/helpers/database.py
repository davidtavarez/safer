# coding=utf-8

from app import db
from app.models import File


def save_file(mimetype, file_path):
    file_object = File(mimetype=mimetype, path=file_path)
    db.session.add(file_object)
    db.session.commit()
    return file_object.id
