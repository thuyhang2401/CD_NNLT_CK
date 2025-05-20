FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY crawl_data /app/crawl_data

EXPOSE 8001

CMD ["uvicorn", "crawl_data.crawl_api:app", "--host", "0.0.0.0", "--port", "8001"]
