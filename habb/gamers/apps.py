from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GamersConfig(AppConfig):
    name = 'habb.gamers'
    verbose_name = _('Игрок')

    def ready(self):
        pass
