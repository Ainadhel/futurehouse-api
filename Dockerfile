# Utiliser une image de base avec Python 3.11
FROM python:3.11-slim

# Installer les dépendances système utiles (et curl pour Coolify healthcheck)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Créer le répertoire de travail
WORKDIR /app

# Copier les fichiers requirements (si tu en as un)
COPY requirements.txt .

# Installer les dépendances Python (y compris futurehouse-client)
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers de l'application
COPY . .

# Exposer le port d'écoute
EXPOSE 3000

# Lancer l'app FastAPI avec Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]