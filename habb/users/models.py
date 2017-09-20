from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    is_captain = models.BooleanField(_('Is he a captain?'), blank=True, default=False)
    phone_number = models.CharField(_('Phone number'), blank=True, max_length=255, null=True)

    def __str__(self):
        return '{} {}'.format(
        	self.first_name,
        	self.last_name
        	)

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
