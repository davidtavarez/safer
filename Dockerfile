FROM tiangolo/meinheld-gunicorn-flask:python3.7-alpine3.8
RUN apk --update add bash nano gcc python3-dev musl-dev libffi-dev build-base openssh libressl-dev

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

WORKDIR /app
COPY ./app/ /app/
ENV FLASK_APP=main.py FLASK_ENV=production
COPY ./migrate.sh migrate.sh
RUN chmod u+x ./migrate.sh && ./migrate.sh
COPY ./test.sh test.sh
RUN chmod u+x ./test.sh && ./test.sh
