from django.apps import AppConfig


class LocalusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'localusers'
    
    def ready(self):
        import localusers.signals
