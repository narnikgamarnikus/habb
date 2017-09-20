from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.GameListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<pk>\d+)/~redirect/$',
        view=views.GameRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.GameDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>\d+)/~update/$',
        view=views.GameUpdateView.as_view(),
        name='update'
    ),
]
