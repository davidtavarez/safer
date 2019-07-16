# coding=utf-8
import base64
import os

from cryptography.fernet import Fernet
from flask import json
from flask import make_response
from flask import request

from app import app
from app.helpers.database import save_file
from app.helpers.functions import generate_key, create_encrypted_file, decrypt_file, get_filename
from app.models import File


@app.route("/file/upload", methods=['POST'])
def upload_file():
    if 'password' not in request.form:
        return app.response_class(
            response=json.dumps({'message': "missing parameter: `password`"}),
            status=400,
            mimetype='application/json'
        )
    if 'file' not in request.files:
        return app.response_class(
            response=json.dumps({'message': "missing parameter: `file`"}),
            status=400,
            mimetype='application/json'
        )
    try:
        key = generate_key(request.form['password'], os.urandom(16))
        file_sent = request.files['file']
        file_path = create_encrypted_file(file_sent.filename, file_sent.read(), key, app.config['UPLOAD_FOLDER'])
        file_id = save_file(file_sent.mimetype, file_path)
        return app.response_class(
            response=json.dumps({'id': file_id, 'key': key.decode("utf-8")}),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return app.response_class(
            response=json.dumps({'message': "something went wrong, I know what but I'm not a snitch"}),
            status=500,
            mimetype='application/json'
        )


@app.route("/file/download/<file_id>", methods=['POST'])
def download_file(file_id):
    if 'key' not in request.form:
        return app.response_class(
            response=json.dumps({'message': "missing key"}),
            status=400,
            mimetype='application/json'
        )
    try:
        file_object = File.query.filter_by(id=file_id).first()
        headers = {'Content-Disposition': 'attachment; filename={}'.format(get_filename(file_object.path)),
                   'Content-type': file_object.mimetype}
        key = request.form['key'].encode()
        return make_response((decrypt_file(file_object.path, key), headers))
    except Exception as e:
        return app.response_class(
            response=json.dumps({'message': "something went wrong, I know what but I'm not a snitch"}),
            status=500,
            mimetype='application/json'
        )
