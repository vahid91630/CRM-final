FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies required for building some Python packages
RUN apt-get update && \
    apt-get install -y gcc libpq-dev build-essential python3-dev curl && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better Docker caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy full project files
COPY . .

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
