import os

from flask import Flask

from app.src.views import index, upload_file, download_file


def create_app(upload_folder: str, basedir: str, ) -> Flask:
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = upload_folder
    app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'safer.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.add_url_rule('/', 'index', index, methods=['GET'])
    app.add_url_rule('/file/upload', 'upload', upload_file, methods=['POST'])
    app.add_url_rule('/file/download/<file_id>', 'download', download_file, methods=['POST'])

    @app.errorhandler(404)
    def page_not_found(ex):
        return app.response_class(
            response='Dafuq R u doing here?!',
            status=404,
            mimetype='text/plain'
        )

    return app
