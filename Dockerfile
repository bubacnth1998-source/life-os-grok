FROM python:3.12-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt psycopg2-binary gunicorn
COPY backend ./backend
COPY frontend ./frontend
COPY scripts ./scripts
ENV PYTHONPATH=/app/backend
ENV DATABASE_URL=sqlite:////data/lifeos.db
ENV LIFE_OS_MEDIA_PATH=/data/media
ENV LIFE_OS_ENV=production
RUN mkdir -p /data/media
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--app-dir", "backend", "--host", "0.0.0.0", "--port", "8000"]
