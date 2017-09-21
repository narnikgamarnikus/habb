from django.apps import AppConfig


class GamersConfig(AppConfig):
    name = 'habb.gamers'
    verbose_name = "Gamers"

    def ready(self):
        pass
