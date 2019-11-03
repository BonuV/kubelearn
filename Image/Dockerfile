FROM python:3.7-slim

RUN apt update -y \
    && apt-get install curl -y\
    && pip3 install flask

COPY . /app
WORKDIR /app
RUN chown -R 10001:10001 /app/*

USER 10001:10001

CMD ["python3","app.py","running your local app"]