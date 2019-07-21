import os
from os import sys, path

from flask_migrate import Migrate, MigrateCommand, Manager
from flask_sqlalchemy import SQLAlchemy

try:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from .src import create_app
except ImportError:
    from app.src import create_app

app = create_app(os.environ['UPLOAD_FOLDER'], os.environ['DB_FOLDER'])

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mimetype = db.Column(db.String(64), index=True, unique=False)
    path = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self) -> str:
        return self.filepath


if __name__ == "__main__":
    app.run(debug=os.environ['DEBUG'], host='0.0.0.0')
