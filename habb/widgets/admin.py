from django.contrib import admin
from .models import Widget, Website, Leed, Competition


admin.site.register(Widget)
admin.site.register(Website)
admin.site.register(Leed)
admin.site.register(Competition)