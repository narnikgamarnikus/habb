from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.TeamListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(?P<name>[\w.@+-]+)/~redirect/$',
        view=views.TeamRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<name>[\w.@+-]+)/$',
        view=views.TeamDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<name>[\w.@+-]+)/~update/$',
        view=views.TeamUpdateView.as_view(),
        name='update'
    ),
]
