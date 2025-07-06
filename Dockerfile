FROM python:3.11-slim

WORKDIR /app

# Install system dependencies required for building packages
RUN apt-get update && \
    apt-get install -y gcc libpq-dev build-essential libffi-dev libssl-dev curl && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
