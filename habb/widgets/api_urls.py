from django.conf.urls import url
from habb.widgets import views


urlpatterns = [
	url(r'^leeds/$', views.APILeedView.as_view()),
	#url(r'^leeds/(?P<pk>[0-9]+)/$', views.APILeedView.as_view()),
	#url(r'^widgets/$', views.WidgetList.as_view()),
	url(r'^widgets/(?P<pk>[0-9]+)/$', views.APIWidgetView.as_view())
]