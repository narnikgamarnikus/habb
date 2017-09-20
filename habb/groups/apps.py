from django.apps import AppConfig


class GroupsConfig(AppConfig):
    name = 'habb.groups'
    verbose_name = "Groups"

    def ready(self):
        pass
