from django.conf.urls import url
from habb.widgets import views


urlpatterns = [
    url(
        regex=r'^widget/$',
        view=views.WidgetListView.as_view(),
        name='widget_list'
    ),
    url(
        regex=r'^widget/(?P<token>[^/]+).js/$',
        view=views.WidgetDetailView.as_view(),
        name='widget_detail'
    ),    
    url(
        regex=r'^widget/~create/$',
        view=views.WidgetCreateView.as_view(),
        name='widget_create'
    ),
    url(
        regex=r'^widget/(P<token>[\w.@+-]+)/~update/$',
        view=views.WidgetUpdateView.as_view(),
        name='widget_update'
    ),
    url(
        regex=r'^widget/(?P<token>[^/]+).js/~delete$',
        view=views.WidgetDeleteView.as_view(),
        name='widget_delete'
    ),        
    url(
        regex=r'^widget/(P<token>[\w.@+-]+)/~redirect/$',
        view=views.WidgetRedirectView.as_view(),
        name='widget_redirect'
    ),

    url(
        regex=r'^website/$',
        view=views.WebsiteListView.as_view(),
        name='website_list'
    ),
    url(
        regex=r'^website/(?P<pk>\d+)/$',
        view=views.WebsiteDetailView.as_view(),
        name='website_detail'
    ),    
    url(
        regex=r'^website/~create/$',
        view=views.WebsiteCreateView.as_view(),
        name='website_create'
    ),
    url(
        regex=r'^website/(?P<pk>\d+)/~update/$',
        view=views.WebsiteUpdateView.as_view(),
        name='website_update'
    ),
    url(
        regex=r'^website/(?P<pk>\d+)/~delete$',
        view=views.WebsiteDeleteView.as_view(),
        name='website_delete'
    ),        
    url(
        regex=r'^website/(?P<pk>\d+)/~redirect/$',
        view=views.WebsiteRedirectView.as_view(),
        name='website_redirect'
    ),

    url(
        regex=r'^leed/$',
        view=views.LeedListView.as_view(),
        name='leed_list'
    ),
    url(
        regex=r'^leed/(?P<pk>\d+)/$',
        view=views.LeedDetailView.as_view(),
        name='leed_detail'
    ),        
]