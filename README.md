# Safer

Safer is a torifyed dockerized **RESTful API** for storing encrypted files.

## Installation

First, we need **Docker**. Please refer to the official documentation [here](https://docs.docker.com/install/linux/docker-ce/debian/).

After installing Docker, clone this repo and move into the `safer` folder:

```bash
$ git clone https://github.com/davidtavarez/safer.git
$ cd safer
```

Now, we just need to run the bash script called `init.sh` to build the container:

```bash
$ ./init.sh
```
```
Sending build context to Docker daemon  167.9kB
Step 1/9 : FROM tiangolo/meinheld-gunicorn-flask:python3.7-alpine3.8
python3.7-alpine3.8: Pulling from tiangolo/meinheld-gunicorn-flask
...
...
...
============================= test session starts ==============================
platform linux -- Python 3.7.3, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /app
plugins: flask-0.15.0
collecting ... collected 9 items

tests.py::test_get_filename PASSED                                       [ 11%]
tests.py::test_get_random_bad_joke PASSED                                [ 22%]
tests.py::test_generate_key PASSED                                       [ 33%]
tests.py::test_encrypt_decrypt PASSED                                    [ 44%]
tests.py::test_generate_random_string PASSED                             [ 55%]
tests.py::test_encrypt_decrypt_file PASSED                               [ 66%]
tests.py::test_dummy PASSED                                              [ 77%]
tests.py::test_404 PASSED                                                [ 88%]
tests.py::test_upload_download_file PASSED                               [100%]

=========================== 9 passed in 1.29 seconds ===========================
Removing intermediate container b19cce40f456
 ---> ccc6e3a7a567
Successfully built ccc6e3a7a567
Successfully tagged safer:latest
19653093dcf968aa02b8ac15041f945a7a247af2fc93932923f743e05e53a7af
```

Great! we're ready to go!

## Usage

So the server is running on port: `56733`, we can access the server using `http`:

![Bad jokes](https://raw.githubusercontent.com/davidtavarez/safer/master/screenshots/index.png)


### Using cURL

Uploading files:

```bash
$ curl -H 'Expect:' -F "file=@/PATH/TO/FILE.EXT" -F "password=PASSWORD" http://localhost:56733/file/upload
{"id": 1, "key": "QRhtN5X4oGR8GxlLSEL1GJJlZgf64VXyMkx7YIbvVK4="}
```

Downloading files:

```bash
$ curl -H 'Expect:' -F "key=QRhtN5X4oGR8GxlLSEL1GJJlZgf64VXyMkx7YIbvVK4\=" http://127.0.0.1:56733/file/download/1 > FILE.EXT   
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
