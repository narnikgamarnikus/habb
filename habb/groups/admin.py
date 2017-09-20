from django.contrib import admin
from .models import Group
from habb.teams.models import Team


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):

    list_display = ['teams', 'servser', 'password', 'group_map']
    search_fields = ['teams', 'servser', 'password', 'group_map']

    def teams(self, obj):

        #return '123'
        return ' vs '.join([team.name for team in obj.team.all()])