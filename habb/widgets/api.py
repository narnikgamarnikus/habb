from tastypie import fields
from .models import Leed, Widget
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication, MultiAuthentication, ApiKeyAuthentication, SessionAuthentication
from tastypie.authorization import DjangoAuthorization
from .authentication import CryptographicApiKeyAuthentication
from tastypie.constants import ALL, ALL_WITH_RELATIONS


class WidgetResource(ModelResource):
	class Meta:
		queryset = Widget.objects.all()
		resource_name = 'widget'
		authorization = DjangoAuthorization()
		authentication = MultiAuthentication(
			BasicAuthentication(),
			#CryptographicApiKeyAuthentication(),
			ApiKeyAuthentication(),
			SessionAuthentication()
			)


class LeedResource(ModelResource):
	
	widget = fields.ForeignKey(WidgetResource, 'widget')
	
	class Meta:
		queryset = Leed.objects.all()
		resource_name = 'leed'
		authorization = DjangoAuthorization()
		authentication = MultiAuthentication(
			BasicAuthentication(), 
			#CryptographicApiKeyAuthentication(),
			ApiKeyAuthentication(),
			SessionAuthentication()
			)
		#filtering = {
		#	'token': ALL,
		#}
