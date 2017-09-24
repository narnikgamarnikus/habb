from django.utils import timezone
from django import template
from django.core import signing
#from ..utils import dont_track
import json
from ..models import Widget
from tastypie.models import ApiKey


register = template.Library()


@register.inclusion_tag('widgets/token.html', takes_context=True)
def token(context):
    pass
    
    token = None
    if context.get('object', None):
        token = None
        if context['object'].__class__.__name__ == 'Widget':
            widget = Widget.objects.get(pk=context['object'].id)
            token = widget.user.token
        data = {
            "path": context['request'].get_full_path(),
            "content_type": context['object'].__class__.__name__,
            "content_id": context['object'].id,
            "timestamp": timezone.now().isoformat(), #.strftime('%Y %m %d %H:%M:%S'),
            "token": str(token),
        }

        token = signing.dumps(
            json.dumps(data, separators=(',', ':')), compress=True)

        return {
            'token': token
            }
    