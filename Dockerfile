FROM tiangolo/meinheld-gunicorn-flask:python3.7-alpine3.8
WORKDIR /app
ADD ./app/ /app/
RUN apk --update add bash nano gcc python3-dev musl-dev libffi-dev build-base openssh libressl-dev
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
ENV FLASK_APP=main.py
ENV FLASK_ENV=production
COPY ./migrate.sh migrate.sh
RUN chmod u+x ./migrate.sh
RUN ./migrate.sh
COPY ./test.sh test.sh
RUN chmod u+x ./test.sh
RUN ./test.sh