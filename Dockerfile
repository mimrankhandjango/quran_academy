FROM python:3.11-slim

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev curl \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy project files
COPY . /app

# Copy entrypoint script & make executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Environment defaults
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=quran_academy.settings \
    PORT=8000

EXPOSE 8000

# Entrypoint runs migrations + collectstatic
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "quran_academy.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
