import string
import random
from django.core import signing
from django.core.signing import BadSignature, SignatureExpired
from django.utils.dateparse import parse_datetime
#from .signals import pixel_data
import logging
import json
from habb.users.models import User


logger = logging.getLogger(__name__)


def decode_token(user_token):
    print(user_token)
    token = None
    try:
        token = signing.loads(
            user_token, max_age=300)    
    except SignatureExpired:
        logger.exception("token expired")
    except BadSignature:
        logger.exception("token invalid")
    if token:
        token = json.loads(token)
        return token['token']


def encode_user_token(user):
    
    user = User.objects.get(pk=user)
    token = user.token

    data = {
        "token": str(token),
        }

    token = signing.dumps(
        json.dumps(data, separators=(',', ':')), compress=True)

    return {
        'token': token
        }
    
