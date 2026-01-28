# 🛒 Projet E-Commerce Microservices

Architecture microservices développée avec **Django**, **FastAPI** et orchestrée par **Docker**.

## 🏗️ Architecture
- **Gateway** (FastAPI) : Point d'entrée unique (Port 8888).
- **Catalog Service** (Django) : Gestion des produits (Port 8001).
- **Order Service** (Django) : Gestion des commandes (Port 8002).

## 🚀 Lancement Rapide
```bash
docker-compose up -d --build
docker-compose exec catalog python manage.py migrate
docker-compose exec order python manage.py migrate
