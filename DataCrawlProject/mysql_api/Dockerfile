FROM python:3.10-slim

WORKDIR /app

COPY ./mysql_api /app/mysql_api
COPY ./ingestion /app/ingestion

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=""
ENV MYSQL_HOST=mysql_db
ENV MYSQL_PORT=3306
ENV MYSQL_DATABASE=glasses_db

EXPOSE 8000

CMD ["uvicorn", "mysql_api.sql_api:app", "--host", "0.0.0.0", "--port", "8000"]
