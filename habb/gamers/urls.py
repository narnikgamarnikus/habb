from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.GamerListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<pk>\d+)/~redirect/$',
        view=views.GamerRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.GamerDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>\d+)/~update/$',
        view=views.GamerUpdateView.as_view(),
        name='update'
    ),
]
