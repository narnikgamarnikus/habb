from django.contrib import admin
from .models import Gamer


@admin.register(Gamer)
class GamerAdmin(admin.ModelAdmin):

    list_display = ['first_name', 'last_name', 'is_captain', 'phone_number']
    search_fields = ['first_name', 'last_name', 'is_captain', 'phone_number']