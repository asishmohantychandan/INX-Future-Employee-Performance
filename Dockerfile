
FROM python:3.13-slim

WORKDIR /app

# Runtime library required by XGBoost
RUN apt-get update \
    && apt-get install -y --no-install-recommends libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API and trained model
COPY api/ ./api/
COPY models/ ./models/

# FastAPI listens on port 8000
EXPOSE 8000

CMD ["uvicorn", "main:app", "--app-dir", "api", "--host", "0.0.0.0", "--port", "8000"]