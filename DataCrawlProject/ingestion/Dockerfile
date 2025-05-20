FROM python:3.10-slim

WORKDIR /app

COPY ./ingestion /app/ingestion

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "ingestion/ingest.py"]
