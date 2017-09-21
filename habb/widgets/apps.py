from django.apps import AppConfig


class WidgetConfig(AppConfig):
    name = 'habb.widgets'
    verbose_name = "Widget"

    def ready(self):
        pass
