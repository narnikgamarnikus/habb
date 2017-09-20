from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.GroupListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<pk>\d+)/~redirect/$',
        view=views.GroupRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.GroupDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>\d+)/~update/$',
        view=views.GroupUpdateView.as_view(),
        name='update'
    ),
]
