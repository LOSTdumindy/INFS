from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = 'User'
    verbose_name_plural = 'Users'
    default_auto_config = 'django.db.models.BigAutoField'

    def ready(self):
        import users.signals
