from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TeamsConfig(AppConfig):
    name = 'habb.teams'
    verbose_name = _('Команда')
    plural_name = _('Команды')

    def ready(self):
        pass
