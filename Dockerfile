# Imatge base amb Python
FROM python:3.12-slim

# Directori de treball dins del contenidor
WORKDIR /app

# Copiem el requirements i instal·lem
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiem tot el projecte
COPY . .

# Exposem el port
EXPOSE 8000

# Comanda per arrencar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
