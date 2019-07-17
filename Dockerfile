FROM tiangolo/meinheld-gunicorn-flask:python3.7-alpine3.8
RUN apk --update add bash nano gcc python3-dev musl-dev libffi-dev build-base openssh libressl-dev

ENV FLASK_APP=main.py FLASK_ENV=production UPLOAD_FOLDER='/tmp/' DEBUG=False

COPY ./requirements.txt /app/requirements.txt
COPY ./*.py /app/
COPY ./*.sh /app/
COPY ./src/ /app/src/
WORKDIR /app/
RUN chmod u+x ./run.sh && ./run.sh