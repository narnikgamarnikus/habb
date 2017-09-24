from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
import uuid
from model_utils import Choices

@python_2_unicode_compatible
class User(AbstractUser):

    STATUS = Choices(
        ('free', 'free', _('Free')), 
        ('bronze', 'bronze', _('Bronze')),
        ('silver', 'silver', _('Silver')),
        ('gold', 'gold', _('Gold')),
    )

    status = models.CharField(
        choices=STATUS, 
        default=STATUS.free,
        max_length=20
    )

    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    token = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return '{} {}'.format(
        	self.first_name,
        	self.last_name
        	)

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
