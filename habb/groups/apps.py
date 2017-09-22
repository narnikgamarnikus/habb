from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GroupsConfig(AppConfig):
    name = 'habb.groups'
    verbose_name = _('Группа')
    plural_name = _('Группы')

    def ready(self):
        pass
