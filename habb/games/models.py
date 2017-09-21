from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Game(models.Model):

    group = models.ForeignKey('groups.Group')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('games:detail', kwargs={'pk': self.pk})
