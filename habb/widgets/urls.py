from django.conf.urls import url

from habb.widgets import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.WidgetListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^(P<token>[\w.@+-]+)/~redirect/$',
        view=views.WidgetRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<token>[^/]+).js/$',
        view=views.WidgetDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(P<token>[\w.@+-]+)/~update/$',
        view=views.WidgetUpdateView.as_view(),
        name='update'
    ),
]
