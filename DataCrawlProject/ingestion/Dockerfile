FROM python:3.10-slim

WORKDIR /app

COPY ./ingestion /app/ingestion

RUN pip install --no-cache-dir \
    sqlalchemy \
    pymysql \
    requests \
    pandas

ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=""
ENV MYSQL_HOST=localhost
ENV MYSQL_PORT=3306
ENV MYSQL_DATABASE=glasses_db

CMD ["python", "ingestion/ingest.py"]
