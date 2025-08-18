# Bookr - Application Django

Application Django pour la gestion de livres avec base de données SQLite.

## Installation

1. Installer les dépendances :
```bash
pip install django
```

2. Appliquer les migrations :
```bash
python manage.py migrate
```

3. Créer un superuser (optionnel) :
```bash
python manage.py createsuperuser
```

## Modèles

- **LivreType** : Types de livres (genre)
- **LivreStatus** : Statuts des livres 
- **Livre** : Livres avec nom, prix et relations

## Utilisation

Lancer le serveur de développement :
```bash
python manage.py runserver
```

Accéder à l'admin Django : http://127.0.0.1:8000/admin/

## Données de test

Exécuter `python verification.py` pour voir les statistiques de la base de données.