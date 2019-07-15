# coding=utf-8
from app import db


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mimetype = db.Column(db.String(64), index=True, unique=False)
    path = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return self.filepath
