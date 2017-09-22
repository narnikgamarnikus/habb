from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GamesConfig(AppConfig):
    name = 'habb.games'
    verbose_name = _('Игра')
    plural_name = _('Игры')

    def ready(self):
        pass
