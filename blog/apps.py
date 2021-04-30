from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

class Crispy_Forms(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crispy_forms'
