from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
import uuid
from model_utils import Choices
from .utils import token_generator
from django.core import signing
import json


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
    token = models.CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(
        	self.first_name,
        	self.last_name
        	)

    def generate_token(self):
        self.token = token_generator()
        self.save()


    def encode_user_token(self):
        data = {
            "token": self.token,
        }

        token = signing.dumps(
            json.dumps(data, separators=(',', ':')), compress=True)

        return token

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
