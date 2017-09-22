from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Game(models.Model):

	group = models.ForeignKey('groups.Group', verbose_name=_('Группа'))
	start_date = models.DateTimeField(verbose_name=_('Дата старта'))
	end_date = models.DateTimeField(verbose_name=_('Дата окончания'))

	def __str__(self):
		return str(self.pk)

	class Meta:
		verbose_name = _('Игра')
		verbose_name_plural = _('Игры')

	def get_absolute_url(self):
		return reverse('games:detail', kwargs={'pk': self.pk})
