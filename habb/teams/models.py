from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Team(models.Model):

    gamers = models.ManyToManyField('gamers.Gamer')
    name = models.CharField(max_length=50)


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('teams:detail', kwargs={'name': self.name})
