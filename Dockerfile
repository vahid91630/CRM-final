FROM python:3.11-slim

WORKDIR /app

# System dependencies
RUN apt-get update && \
    apt-get install -y gcc libpq-dev build-essential curl libffi-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy only requirements file first
COPY requirements.txt .

# Debug pip install
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt || (echo "❌ Pip install failed" && ls -l && cat requirements.txt && true)

# Now copy rest of project
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
