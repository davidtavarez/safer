# coding=utf-8
import os
from io import BytesIO

import pytest


import json

from app import app
from app.helpers.functions import get_filename, get_random_bad_joke, generate_key, encrypt, decrypt, \
    create_encrypted_file, decrypt_file, generate_random_string


def test_get_filename():
    file_path = "/tmp/file.pdf"
    assert 'file.pdf' == get_filename(file_path)


def test_get_random_bad_joke():
    assert len(get_random_bad_joke()) > 0


def test_generate_key():
    salt = os.urandom(16)
    first = generate_key('password', salt)
    second = generate_key('password', salt)
    assert first == second


def test_encrypt_decrypt():
    salt = os.urandom(16)
    key = generate_key('password', salt)
    plain_string = b'testing'
    encrypted_string = encrypt(data=plain_string, key=key)
    assert plain_string != encrypted_string
    assert decrypt(encrypted_string, key) == plain_string


def test_generate_random_string():
    random_string = generate_random_string(min_char=6, max_char=8)
    assert 6 <= len(random_string) <= 8


def test_encrypt_decrypt_file():
    base_path = '/tmp/'
    content = b'Testing file'
    filename = generate_random_string()
    file_path = '{}{}.txt'.format(base_path, filename)
    with open(file_path, "wb") as f:
        f.write(content)
        f.close()

    assert os.path.exists(file_path)

    salt = os.urandom(16)
    key = generate_key('password', salt)
    with open(file_path, 'rb') as content_file:
        file_content = content_file.read()

    encrypted_file_path = create_encrypted_file(filename, file_content, key, base_path)

    assert os.path.exists(encrypted_file_path)

    decrypted_content = decrypt_file(encrypted_file_path, key)

    assert decrypted_content == content


@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass  # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client


def test_dummy(client):
    response = client.get('/')
    assert response.status_code == 200


def test_404(client):
    response = client.get('/{}'.format(generate_random_string()))
    assert response.status_code == 404


def test_upload_download_file(client):
    file_content = b'file content'
    password = 'password'
    data = {'file': (BytesIO(file_content), 'test.txt'), 'password': password}
    response = client.post('/file/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    results = json.loads(response.data)
    assert 'id' in results
    assert 'key' in results
    response = client.post('/file/download/{}'.format(results['id']), data={'key': results['key']})
    assert response.data == file_content
