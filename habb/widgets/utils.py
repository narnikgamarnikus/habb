import string
import random
from django.core import signing
from django.core.signing import BadSignature, SignatureExpired
from django.utils.dateparse import parse_datetime
#from .signals import pixel_data
import logging
import json
from habb.users.models import User
from habb.widgets.models import Widget


logger = logging.getLogger(__name__)


def decode_token(user_token):
    token = None
    try:
        token = signing.loads(
            user_token)#, max_age=300)
    except SignatureExpired:
        logger.exception("token expired")
    except BadSignature:
        logger.exception("token invalid")
    if token:
        token = json.loads(token)
        return token['token']


def encode_user_token(user_pk):
    
    user = User.objects.get(pk=user_pk)
    token = user.token

    data = {
        "token": str(token),
        }

    token = signing.dumps(
        json.dumps(data, separators=(',', ':')), compress=True)

    return {
        'token': token
        }
    

def encode_widget_token(widget_pk):
    
    #user = User.objects.get(pk=user)
    widget = Widget.objects.get(pk=widget_pk)
    user = widget.website.user

    data = {
        "token": str(user.token),
        #"widget": str(widget.token)
        }

    token = signing.dumps(
        json.dumps(data, separators=(',', ':')), compress=True)

    return {
        'token': token
        }