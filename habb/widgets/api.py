from tastypie import fields
from .models import Leed, Widget
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication, MultiAuthentication, ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from .authentication import CryptographicApiKeyAuthentication

class WidgetResource(ModelResource):
	class Meta:
		queryset = Widget.objects.all()
		resource_name = 'widget'
		authorization = DjangoAuthorization()
		authentication = MultiAuthentication(
			#BasicAuthentication(),
			CryptographicApiKeyAuthentication(),
			#ApiKeyAuthentication()
			)


class LeedResource(ModelResource):
	
	widget = fields.ForeignKey(WidgetResource, 'widget')
	
	class Meta:
		queryset = Leed.objects.all()
		resource_name = 'leed'
		authorization = DjangoAuthorization()
		authentication = MultiAuthentication(
			#BasicAuthentication(), 
			CryptographicApiKeyAuthentication(),
			#ApiKeyAuthentication()
			)
