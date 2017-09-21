from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
import uuid


@python_2_unicode_compatible
class Widget(models.Model):

	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
	token = models.UUIDField(default=uuid.uuid4, editable=False)
	date_start = models.DateTimeField(null=True)
	date_end = models.DateTimeField(null=True)

	def __str__(self):
		return '{}'.format(self.token)

	def widget_script(self):
		return ''

	def get_absolute_url(self):
		return reverse('widgets.detail', kwargs={'token': self.token})