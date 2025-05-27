# Imatge base
FROM python:3.12-slim

# Variables d'entorn
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directori de treball
WORKDIR /app

# Instal·lem dependències del sistema (ex: libpq per PostgreSQL)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instal·lem les dependències de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiem el codi
COPY . .

# Exposem el port
EXPOSE 8000

# Comanda de producció amb Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
