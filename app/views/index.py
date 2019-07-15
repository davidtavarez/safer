# coding=utf-8

from app import app
from app.helpers.functions import get_random_bad_joke


@app.route("/", methods=['GET'])
def index():
    return app.response_class(
        response=get_random_bad_joke(),
        status=200,
        mimetype='text/plain'
    )
