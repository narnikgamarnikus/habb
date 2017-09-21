from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Gamer(models.Model):

	first_name = models.CharField(_('First Name'), max_length=50, blank=True, default='')
	last_name = models.CharField(_('Last Name'), max_length=50, blank=True, default='')

	is_captain = models.BooleanField(_('Is he a captain?'), blank=True, default=False)
	phone_number = models.CharField(_('Phone number'), blank=True, max_length=255, null=True)

	def __str__(self):
		return '{} {}'.format(
			self.first_name,
			self.last_name
			)

	def get_absolute_url(self):
		return reverse('gamers:detail', kwargs={'pk': self.pk})