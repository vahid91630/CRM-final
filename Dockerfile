# 1. Base image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements first and install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 4. Copy the whole project
COPY . .

# 5. Expose port
EXPOSE 8000

# 6. Start the app (main.py is inside app/)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
