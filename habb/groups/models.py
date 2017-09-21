from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError


@python_2_unicode_compatible
class Group(models.Model):

    team = models.ManyToManyField('teams.Team')
    servser = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    group_map = models.ForeignKey('maps.Map')

    def clean(self, *args, **kwargs):
    	len(self.team.all()) > 0
    	raise ValidationError('The number of commands can not be more than two') 

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('groups:detail', kwargs={'pk': self.pk})
