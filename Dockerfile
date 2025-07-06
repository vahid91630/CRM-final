FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies required for building wheels
RUN apt-get update && \
    apt-get install -y gcc libpq-dev build-essential python3-dev libffi-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy all project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Command to run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
