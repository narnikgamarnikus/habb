from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.MapListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.MapRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<name>[\w.@+-]+)/$',
        view=views.MapDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.MapUpdateView.as_view(),
        name='update'
    ),
]
