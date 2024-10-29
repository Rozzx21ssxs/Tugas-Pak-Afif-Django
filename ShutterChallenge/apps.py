from django.apps import AppConfig


class ShutterchallengeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ShutterChallenge'  # Sesuaikan dengan nama direktori aplikasi Anda
    
    def ready(self):
        import ShutterChallenge.signals
