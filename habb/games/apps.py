from django.apps import AppConfig


class GamesConfig(AppConfig):
    name = 'habb.games'
    verbose_name = "Games"

    def ready(self):
        pass
