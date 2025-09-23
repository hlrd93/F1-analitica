FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir mlflow psycopg2-binary

CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000"]
