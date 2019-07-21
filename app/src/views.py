import os

from flask import json
from flask import make_response, Response
from flask import request

from app.src.functions import get_random_bad_joke, generate_key, create_encrypted_file, decrypt_file, get_filename


def index() -> Response:
    return Response(
        response=get_random_bad_joke(),
        mimetype='text/plain'
    )


def upload_file() -> Response:
    if 'password' not in request.form:
        return Response(
            response=json.dumps({'message': "missing parameter: `password`"}),
            status=400,
            mimetype='application/json'
        )
    if 'file' not in request.files:
        return Response(
            response=json.dumps({'message': "missing parameter: `file`"}),
            status=400,
            mimetype='application/json'
        )
    try:
        key = generate_key(request.form['password'], os.urandom(16))

        file_sent = request.files['file']
        file_path = create_encrypted_file(file_sent.filename, file_sent.read(), key, os.environ['UPLOAD_FOLDER'])

        from app.main import File
        from app.main import db

        file_object = File(mimetype=file_sent.mimetype, path=file_path)
        db.session.add(file_object)
        db.session.commit()
        file_id = file_object.id

        return Response(
            response=json.dumps({'id': file_id, 'key': key.decode("utf-8")}),
            mimetype='application/json'
        )
    except:
        return Response(
            response=json.dumps({'message': "something went wrong, I know what but I'm not a snitch"}),
            status=500,
            mimetype='application/json'
        )


def download_file(file_id: int) -> Response:
    if 'key' not in request.form:
        return Response(
            response=json.dumps({'message': "missing key"}),
            status=400,
            mimetype='application/json'
        )
    try:
        from app.main import File

        file_object = File.query.filter_by(id=file_id).first()
        headers = {'Content-Disposition': 'attachment; filename={}'.format(get_filename(file_object.path))}
        key = request.form['key'].encode()
        return Response(
            response=decrypt_file(file_object.path, key),
            mimetype=file_object.mimetype,
            content_type=file_object.mimetype,
            headers=headers
        )
    except:
        return Response(
            response=json.dumps({'message': "something went wrong, I know what but I'm not a snitch"}),
            status=500,
            mimetype='application/json'
        )
