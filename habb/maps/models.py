from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Map(models.Model):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(max_length=50, verbose_name=_('Название карты'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Карта')
        verbose_name_plural = _('Карты')

    def get_absolute_url(self):
        return reverse('maps:detail', kwargs={'name': self.name})
