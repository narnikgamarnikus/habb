from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Team(models.Model):

    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=50)


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('teams:detail', kwargs={'name': self.name})
