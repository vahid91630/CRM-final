FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
