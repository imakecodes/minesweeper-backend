FROM python:3.8

ADD . /app
WORKDIR /app

RUN apt-get update && apt-get install -y \
    bash \
    default-libmysqlclient-dev \
    build-essential \
    && pip install --no-cache-dir -r /app/requirements.txt

CMD ["/app/commands/run-prod.sh"]
