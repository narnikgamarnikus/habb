from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MapsConfig(AppConfig):
    name = 'habb.maps'
    verbose_name = _('Карта')
    plural_name = _('Карты')

    def ready(self):
        pass
