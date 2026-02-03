FROM python:3.9-slim

WORKDIR /app

# Install system library needed by scikit-learn
RUN apt-get update && apt-get install -y --no-install-recommends libgomp1
RUN rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY model.pkl .

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
