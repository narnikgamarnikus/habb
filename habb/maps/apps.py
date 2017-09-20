from django.apps import AppConfig


class MapsConfig(AppConfig):
    name = 'habb.maps'
    verbose_name = "Maps"

    def ready(self):
        pass
