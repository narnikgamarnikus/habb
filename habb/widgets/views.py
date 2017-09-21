from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Widget


class WidgetDetailView(LoginRequiredMixin, DetailView):
    model = Widget
    #pk_url_kwarg = 'token' 
    slug_field = 'token'
    slug_url_kwarg = 'token'
    template_name = 'widgets/widget_detail.js'
    content_type = 'application/javascript'
    # These next two lines tell the view to index lookups by Gamename


class WidgetRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('widgets:detail',
                       kwargs={'token': self.kwargs['token']})


class WidgetUpdateView(LoginRequiredMixin, UpdateView):

    #fields = ['name', ]

    # we already imported Game in the view code above, remember?
    model = Widget

    # send the Game back to their own page after a successful update
    def get_success_url(self):
        return reverse('widgets:detail',
                       kwargs={'token': self.kwargs['token']})

    def get_object(self):
        # Only get the Game record for the Game making the request
        return Widget.objects.get(token=self.kwargs['token'])


class WidgetListView(LoginRequiredMixin, ListView):
    model = Widget

    def get_queryset(self):
        queryset = super(WidgetListView, self).get_queryset()
        return queryset.filter(user = self.request.user)

