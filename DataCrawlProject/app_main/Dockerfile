FROM python:3.10-slim

WORKDIR /app/front_end

COPY ./front_end /app/front_end

EXPOSE 8080

CMD ["python", "-m", "http.server", "8080", "--bind", "0.0.0.0"]
