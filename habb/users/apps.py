from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'habb.users'
    verbose_name = "Users"

    def ready(self):
    	import habb.users.signals
