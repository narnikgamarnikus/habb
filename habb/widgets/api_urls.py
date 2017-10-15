from django.conf.urls import url
from habb.widgets import views
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^schema/$', schema_view),
	url(r'^leeds/$', views.APILeedListView.as_view()),
	url(r'^leeds/(?P<pk>[0-9]+)/$', views.APILeedDetailView.as_view()),
	#url(r'^widgets/$', views.WidgetList.as_view()),
	url(r'^widgets/(?P<pk>[0-9]+)/$', views.APIWidgetView.as_view())
]