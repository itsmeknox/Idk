FROM python

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/

# Installer les dépendances à partir du fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application dans le conteneur
COPY . /app

# Exécuter l'application avec Gunicorn pour la production
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]