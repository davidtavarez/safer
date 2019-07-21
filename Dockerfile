FROM tiangolo/meinheld-gunicorn-flask:python3.7-alpine3.8
RUN apk --update add bash nano gcc python3-dev musl-dev libffi-dev build-base openssh libressl-dev

ENV FLASK_APP=main.py FLASK_ENV=production UPLOAD_FOLDER='/tmp/' DEBUG=False DB_FOLDER='/etc/'

COPY ./app/ /app/

RUN pip install -r ./requirements.txt
RUN pwd && ls -lh && flask db init ; flask db migrate -m '.'; flask db upgrade; pytest -vvv tests.py