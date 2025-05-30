# Futurehouse API Wrapper

Ce projet expose une API REST autour du SDK Python `futurehouse-client` afin de la rendre accessible à n8n ou tout autre outil externe via HTTP.

## 🚀 Démarrage

```bash
docker build -t futurehouse-api .
docker run -p 3000:3000 futurehouse-api
```

## 🔐 Sécurité

Les endpoints sont protégés par un header `x-api-key`. Modifiez la valeur dans `main.py` pour sécuriser votre API.

## 📦 Endpoints disponibles

- `GET /projects` – Liste les projets
- `GET /projects/{project_id}` – Récupère un projet

## 🌍 Déploiement Coolify

1. Poussez ce code dans un dépôt Git.
2. Créez une nouvelle **Dockerfile App** sur Coolify.
3. Configurez le domaine et le port (3000 par défaut).
4. Lancez le déploiement.

Votre API sera disponible à `https://api.votredomaine.fr/projects`.

---
