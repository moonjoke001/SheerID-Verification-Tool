FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir httpx Pillow curl_cffi cloudscraper

# Copy tool files
COPY main.py .
COPY stats.json .
COPY ../anti_detect.py .

# Run as non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

ENTRYPOINT ["python", "main.py"]
