from django.conf.urls import url
from habb.widgets import views


urlpatterns = [
    url(r'^leeds/$', views.LeedList.as_view()),
   	url(r'^widgets/$', views.WidgetList.as_view()),
]