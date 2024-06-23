# compte/apps.py

from django.apps import AppConfig


class CompteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'compte'

    def ready(self):
        import compte.signals  # Assurez-vous que le chemin est correct pour vos signaux
