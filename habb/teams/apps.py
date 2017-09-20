from django.apps import AppConfig


class TeamsConfig(AppConfig):
    name = 'habb.teams'
    verbose_name = "Teams"

    def ready(self):
        pass
